from flask import Blueprint, request, jsonify,Blueprint
import sqlite3

ticker_bp = Blueprint('ticker', __name__)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.ticker = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, company_name, ticker):
        node = self.root
        for char in company_name.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.ticker = ticker

    def search(self, company_name):
        node = self.root
        for char in company_name.lower():
            if char not in node.children:
                return None
            node = node.children[char]
        return node.ticker if node.ticker else None

DEFAULT_STOCKS = [
    ("Apple", "AAPL"),
    ("Google", "GOOGL"),
    ("Amazon", "AMZN"),
    ("Tesla", "TSLA"),
    ("Microsoft", "MSFT"),
    ("Netflix", "NFLX"),
]

def init_stocks_db():
    conn = sqlite3.connect("stocks.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stocks (
            company_name TEXT NOT NULL,
            ticker TEXT NOT NULL
        )
    """)
    if cursor.execute("SELECT COUNT(*) FROM stocks").fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO stocks (company_name, ticker) VALUES (?, ?)",
            DEFAULT_STOCKS,
        )
    conn.commit()
    conn.close()

def fetch_data_from_db():
    init_stocks_db()
    conn = sqlite3.connect("stocks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT company_name, ticker FROM stocks")
    data = cursor.fetchall()
    conn.close()
    return data

trie = Trie()
for company_name, ticker in fetch_data_from_db():
    trie.insert(company_name, ticker)

@ticker_bp.route('/get_ticker')
def get_ticker():
    company_name = request.args.get('company', '').strip()
    ticker = trie.search(company_name)
    return jsonify({'ticker': ticker if ticker else None})
