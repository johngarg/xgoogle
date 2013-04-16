#!/bin/python
#-*- encoding: utf8 -*-

### handle options
import sys, getopt, re

KEYWORD=""
ENGINE=[]
INTERNAL=0
NUM=10
PREFERENCE="autosearch.conf"
FORMAT=""
WRITE=""
FILTER=""
CHART=""
SORT=""
VERBOSE=False

ENGINES=['google', 'baidu', 'qihoo', 'maopu', 'tianya', 'weibo', 'tq']

def opt():
    global KEYWORD, ENGINE, INTERNAL, NUM, PREFERENCE, FORMAT, WRITE, FILTER, CHART, SORT, VERBOSE
    global ENGINES

    blank = re.compile('\s')
    opts, args = getopt.getopt(sys.argv[1:], "k:e:i:n:p:o:w:f:c:s:vh", 
        ["keyword=", "engine=", "internal=", "num=", "preference=", "format=", "write=", "filter=", "chart=", "sort=", "verbose", "help"])
    for op, value in opts:
        if op == "-k" or op == "--keyword":
            KEYWORD = value.strip()
        elif op == "-e" or op == "--engine":
            ENGINE = blank.sub('', value).split(',')
            for e in ENGINE:
            	if not e in ENGINES:
            		print "warning: %s is not supported, ignored" % e
            		ENGINE.remove(e)
        elif op == "-i" or op == "--internal":
            INTERNAL = float(value)
        elif op == "-n" or op == "--num":
            NUM = int(value)
        elif op == "-p" or op == "--preference":
            PREFERENCE = value
        elif op == "-o" or op == "--format":
            FORMAT = value
        elif op == "-w" or op == "--write":
            WRITE = value
        elif op == "-f" or op == "--filter":
            FILTER = value
        elif op == "-c" or op == "--chart":
            CHART = value
        elif op == "-s" or op == "--sort":
            SORT = value
        elif op == "-v" or op == "--verbose":
            VERBOSE = True
        elif op == "-h" or op == "--help":
            usage()
        else:
            usage()

def usage():
	print """autosearch is an automatically tools used in command line, the usage:"""
	print """autosearch
    -k,--keyword=keyword ---if have blank,put the keyword in "",like this "cars tree"
    -e,--engine=google,baidu,qihoo,maopu,tianya,weibo,tq ---at least one of these search engines
    -i,--internal=NUMBER ---seconds, default is 0
    -n,--num=NUMBER ---topmost search results, default is 10
    -p,--preference=FILE ---set preference file name, like autosearch.conf
    -o,--format=title,url,desc ---set output formate
    -w,--write=FILE ---set output file, like autosearch.output
    -f,--filter=STRING ---set filter string
    -c,--chart ---got output chart
    -s,--sort ---set sort type
    -v,--verbose ---if set, print the output to screen also
    -h,--help ---this help information""" 

try:
	opt()
except Exception, e:
	print "error: %s" % e
	usage()
	sys.exit()
else:
	pass
finally:
	pass

if KEYWORD=='':
	print "error: no keyword to query, exit!!!"
	usage()
	sys.exit()

if len(ENGINE)==0:
	print "error: must assign at least 1 search engine!!!"
	usage()
	sys.exit()

def try_output(content):
	if VERBOSE:
		print content

### main logic
from xgoogle.GeneralSearch import GeneralSearch
import time
import string

while True:
	for e in ENGINE:
		gs=GeneralSearch(KEYWORD, e)
		results = gs.get_results()
		print gs.num_results

		count=0
		over=False
		while True:
			for r in results:
				count=count+1
				if count>NUM:
					over=True
					break
				if VERBOSE:
					print 30*'+'
					print "results[%d]: " % count
				for k in ['title', 'url', 'desc']:
					if VERBOSE:
						s = "r.%s" % k
						print "%s: %s" % ( k, eval(s) )
				if VERBOSE:
					print 30*'+'
			if over:
				break
			results = gs.get_results()

		del gs

	if INTERNAL:
		print "info: loop search every %d seconds, press CTRL+C to exit." % INTERNAL
		time.sleep(string.atof(INTERNAL))
	else:
		sys.exit()
