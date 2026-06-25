"""
WSGI entry point for PythonAnywhere.

Setup on PythonAnywhere:
  1. Clone the repo into your home directory, e.g.
     /home/YOURUSERNAME/Investify-Stock-Market-Website
  2. Web tab → Manual configuration → point WSGI file at this file
  3. Set virtualenv and install: pip install -r requirements.txt
  4. Reload the web app
"""
import os
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

os.chdir(PROJECT_DIR)

from MainApp import app as application  # noqa: E402
