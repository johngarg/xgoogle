#!/bin/python
#-*- encoding: utf8 -*-

### handle options
import sys, getopt

keyword=""
engine="google"
internal=0
num=0
preference="autosearch.conf"
sort=False
filter=False
chart=False

def opt():
    opts, args = getopt.getopt(sys.argv[1:], "k:e:i:n:p:sfch", 
        ["keyword=", "engine=", "internal=", "num=", "preference=", "sort", "filter", "chart", "help"])
    for op, value in opts:
        if op == "-k" or op == "--keyword":
            keyword = value
        elif op == "-e" or op == "--engine":
            engine = value
        elif op == "-i" or op == "--internal":
            internal = value
        elif op == "-n" or op == "--num":
            num = value
        elif op == "-p" or op == "--preference":
            preference = value
        elif op == "-s" or op == "--sort":
            sort = True
        elif op == "-f" or op == "--filter":
            filter = True
        elif op == "-c" or op == "--chart":
            chart = True
        elif op == "-h" or op == "--help":
            usage()
            sys.exit()
    print keyword
    print engine
    print internal
    print num
    print preference
    print sort
    print filter
    print chart

def usage():
	print """autosearch is an automatically tools used in command line, the usage:"""
	print """autosearch
    -k,--keyword=keyword
    -e,--engine=google, baidu, yahoo...
    -i,--internal=5(minutes)
    -n,--num=500
    -p,--preference=preference file name
    -s,--sort
    -f,--filter
    -c,--chart
    -h,--help"""

try:
	opt()
except Exception, e:
	usage()
	sys.exit()
else:
	pass
finally:
	pass

### main logic
from xgoogle.GeneralSearch import GeneralSearch

gs=GeneralSearch(keyword, 'baidu')
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

gs2=GeneralSearch(keyword)
results = gs2.get_results()
print gs2.page
print gs2._last_search_url
print gs2.num_results
print results[0].title
print 10*'*'
results = gs2.get_results()
print gs2.page
print gs2._last_search_url
print gs2.num_results
print results[0].title
print 10*'*'

