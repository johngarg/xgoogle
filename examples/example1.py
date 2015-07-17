#!/usr/bin/python
#
# This program does a Google search for "quick and dirty" and returns
# 50 results.
#

from xgoogle.search import GoogleSearch, SearchError
try:
  gs = GoogleSearch("quick and dirty")
  gs.results_per_page = 50
  results = gs.get_results()
  for res in results:
    if res.title is not None:
        print res.title.encode('utf8')
    if res.desc is not None:
        print res.desc.encode('utf8')
    if res.url is not None:
        print res.url.encode('utf8')
    print
except SearchError, e:
  print "Search failed: %s" % e

