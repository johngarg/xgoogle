# coding: utf-8
"""
Simulate:
    google_dl -s http://www.marquette.edu/maqom/ -f pdf ""
"""
from xgoogle.search import GoogleSearch


def test_name_error_name2codepoint():
    gs = GoogleSearch('site:http://www.marquette.edu/maqom/')
    gs._set_filetype('pdf')
    assert gs.get_results()
