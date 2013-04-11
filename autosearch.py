#!/bin/python
#-*- encoding: utf8 -*-

### handle options
import sys, getopt

def opt():
    opts, args = getopt.getopt(sys.argv[1:], "k:e:i:n:q:sfc", 
        ["keyword=", "engine=", "internal=", "num=", "ini=", "sort", "filter", "chart"])
    keyword=""
    engine=""
    internal=0
    num=0
    ini=""
    sort=False
    filter=False
    chart=False
    for op, value in opts:
        if op == "-k":
            keyword = value
        elif op == "-e":
            engine = value
        elif op == "-h":
            usage()
            sys.exit()

def usage():
	print """autosearch  -k,--keyword=keyword
                -e,--engine=google, baidu, yahoo...
                -i,--internal=5(minutes)
                -n,--num=500
                -q,--ini=settings file name
                -s,--sort
                -f,--filter
                -c,--chart
                -h,--help"""

### main logic
from xgoogle.GeneralSearch import GeneralSearch

gs=GeneralSearch('汽车', 'baidu')
results = gs.get_results()
print gs._last_search_url
print gs.num_results
print results[0].title
results = gs.get_results()
print gs._last_search_url
print gs.num_results
print results[0].title

gs2=GeneralSearch('汽车')
results = gs2.get_results()
print gs2._last_search_url
print gs2.num_results
print results[0].title
results = gs.get_results()
print gs._last_search_url
print gs.num_results
print results[0].title

