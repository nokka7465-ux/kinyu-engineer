"""Run article generator with new articles data.
Usage: python scripts/run_gen.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_article import main
from new_articles_data import ARTICLES

written = main(ARTICLES)
print(f'Generated {len(written)} articles:')
for f in written:
    print(f'  {f}')
