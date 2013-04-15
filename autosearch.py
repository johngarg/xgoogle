#!/bin/python
#-*- encoding: utf8 -*-

### handle options
import sys, getopt

KEYWORD=""
ENGINE=[]
INTERNAL=0
NUM=0
PREFERENCE="autosearch.conf"
OUTPUT=""
SORT=False
FILTER=False
CHART=False

def opt():
    global KEYWORD, ENGINE, INTERNAL, NUM, PREFERENCE, OUTPUT, SORT, FILTER, CHART

    opts, args = getopt.getopt(sys.argv[1:], "k:e:i:n:p:sfch", 
        ["keyword=", "engine=", "internal=", "num=", "preference=", "sort", "filter", "chart", "help"])
    for op, value in opts:
        if op == "-k" or op == "--keyword":
            KEYWORD = value
        elif op == "-e" or op == "--engine":
            ENGINE = value
        elif op == "-i" or op == "--internal":
            INTERNAL = value
        elif op == "-n" or op == "--num":
            NUM = value
        elif op == "-p" or op == "--preference":
            PREFERENCE = value
        elif op == "-o" or op == "--output":
            OUTPUT = value
        elif op == "-s" or op == "--sort":
            SORT = True
        elif op == "-f" or op == "--filter":
            FILTER = True
        elif op == "-c" or op == "--chart":
            CHART = True
        elif op == "-h" or op == "--help":
            usage()
            sys.exit()

def usage():
	print """autosearch is an automatically tools used in command line, the usage:"""
	print """autosearch
    -k,--keyword=keyword
    -e,--engine=google, baidu, yahoo...
    -i,--internal=5(minutes)
    -n,--num=500
    -p,--preference=preference file name
    -o,--output
    -s,--sort
    -f,--filter
    -c,--chart
    -h,--help"""

try:
	opt()
	print ENGINE
except Exception, e:
	print e
	usage()
	sys.exit()
else:
	pass
finally:
	pass

### main logic
from xgoogle.GeneralSearch import GeneralSearch
import time
import string

if INTERNAL:
	while True:
		gs=GeneralSearch(KEYWORD, 'baidu')
		results = gs.get_results()
		print gs.page
		print gs._last_search_url
		print gs.num_results
		print results[0].title
		print 10*'*'
		results = gs.get_results()
		print gs.page
		print gs._last_search_url
		print gs.num_results
		print results[0].title
		print 10*'*'

#		gs2=GeneralSearch(KEYWORD)
#		results = gs2.get_results()
#		print gs2.page
#		print gs2._last_search_url
#		print gs2.num_results
#		print results[0].title
#		print 10*'*'
#		results = gs2.get_results()
#		print gs2.page
#		print gs2._last_search_url
#		print gs2.num_results
#		print results[0].title
#		print 10*'*'

		time.sleep(string.atof(INTERNAL))