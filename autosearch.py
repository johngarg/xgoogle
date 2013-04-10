#!/bin/python
#-*- encoding: utf8 -*-

### ini handler, must be in GeneralSearch.py
import ConfigParser
import string, os, sys

cf = ConfigParser.ConfigParser()
cf.read("autosearch.conf")

s = cf.sections()
print 'section:', s

o = cf.options("db")
print 'options:', o

v = cf.items("db")
print 'db:', v
 
print '-'*60

db_host = cf.get("db", "db_host")
db_port = cf.getint("db", "db_port")
db_user = cf.get("db", "db_user")
db_pass = cf.get("db", "db_pass")

### handle options
import sys, getopt

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

def usage()
	print "autosearch  -k,--keyword=keyword
                -e,--engine=google, baidu, yahoo...
                -i,--internal=5(minutes)
                -n,--num=500
                -q,--ini=settings file name
                -s,--sort
                -f,--filter
                -c,--chart
                -h,--help"

### main logic
from xgoogle.GeneralSearch import GeneralSearch

gs=GeneralSearch('cars', 'baidu')
#gs=GeneralSearch('cars')
results = gs.get_results()
