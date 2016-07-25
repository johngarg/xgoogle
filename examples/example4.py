#!/usr/bin/python
#
# Justin Vieira (justin@rancorsoft.com)
# http://www.rancorsoft.com  --  Let's Rock Together.
#
# This program does a Google search for "super test results" and returns
# all results.
#

from xgoogle.search import GoogleSearch, SearchError
from threading import Thread
from random import randint
import time

try:
  gs = GoogleSearch("super test results")
  gs.results_per_page = 50
  displayedResults = 0
  results = gs.get_results()
  while displayedResults < gs.num_results:
      for res in results:
        if res.title is not None:
            print res.title.encode('utf8')
        if res.desc is not None:
            print res.desc.encode('utf8')
        if res.url is not None:
            print res.url.encode('utf8')
        displayedResults += gs.results_per_page
        print
      time.sleep(randint(15,60))
      results = gs.get_results()
except SearchError, e:
  print "Search failed: %s" % e

