#!/bin/python
## coding=utf-8 ##
#-*- encoding: utf8 -*-

### handle options
import sys, getopt, re, os

KEYWORD=""
ENGINE=[]
INTERNAL=0
NUM=10
PREFERENCE=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'autosearch.conf')
FORMAT=['title', 'url', 'desc']
WRITE="autosearch.output"
FILTER=""
CHART=""
SORT=""
VERBOSE=False

ENGINES=['google', 'baidu', 'qihoo', 'maopu', 'tianya', 'weibo', 'tq']
FORMATS=['title', 'url', 'desc']
DATA=[]

ENCODING = sys.getfilesystemencoding()

def opt():
    global KEYWORD, ENGINE, INTERNAL, NUM, PREFERENCE, FORMAT, WRITE, FILTER, CHART, SORT, VERBOSE
    global ENGINES, FORMATS

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
            		error( "warning: %s is not supported, ignored" % e )
            		ENGINE.remove(e)
            	else:
            		DATA.append([e, []])
        elif op == "-i" or op == "--internal":
            INTERNAL = float(value)
        elif op == "-n" or op == "--num":
            NUM = int(value)
        elif op == "-p" or op == "--preference":
            PREFERENCE = value
        elif op == "-o" or op == "--format":
            FORMAT = blank.sub('', value).split(',')
            for f in FORMAT:
            	if not f in FORMATS:
            		error( "warning: format %s is not supported, ignored" % f )
            		FORMAT.remove(f)
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
            sys.exit()
        else:
            error( "warning: option %s not recognized, ignored" % op )

def usage():
	print """autosearch is an automatically tools used in command line, the usage:"""
	print """autosearch
    -k,--keyword=keyword ---if have blank,put the keyword in "",like this "cars tree"
    -e,--engine=google,baidu,qihoo,maopu,tianya,weibo,tq ---at least one of these search engines
    -i,--internal=NUMBER ---seconds, default is 0
    -n,--num=NUMBER ---topmost search results, default is 10
    -p,--preference=FILE ---set preference file name, default is autosearch.conf
    -o,--format=title,url,desc ---set output formate, default is title,url,desc
    -w,--write=FILE ---set output file, default is autosearch.output
    -f,--filter=STRING ---set filter string
    -c,--chart ---got output chart
    -s,--sort ---set sort type
    -v,--verbose ---if set, print the output to screen also
    -h,--help ---this help information""" 

def error(msg):
	print 50*'*'
	print "*** %s" % msg
	print 50*'*'
	usage()
	sys.exit()

def try_output(content):
	#s = str.format( content )
	if VERBOSE:
		print content
	if WRITE:
		with open(WRITE, 'a+') as f:
			f.write(content.encode('utf-8'))
			f.write("\n")

import cairo
import pycha
import pycha.bar
def try_chart():
	global DATA
	#print DATA

	if CHART=='':
		return

	width, height = (500,400)
	surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
	chart = pycha.bar.VerticalBarChart(surface)
	chart.addDataset( DATA )
	chart.render()
	surface.write_to_png('output.png')

try:
	opt()
except Exception, e:
	error( "error: %s" % e )
	usage()
	sys.exit()
else:
	pass
finally:
	pass

if KEYWORD=='':
	error( "error: no keyword to query, exit!!!" )

if len(ENGINE)==0:
	error( "error: must assign at least 1 search engine!!!" )

if not os.path.exists(PREFERENCE):
	error( "error: preference file %s not exists!!!" % PREFERENCE )

if WRITE:
	with open(WRITE, 'w', ) as f:
		pass

### main logic
from xgoogle.GeneralSearch import GeneralSearch
import time
import string
import time

start_time = 0
while True:
	for e in ENGINE:
		gs=GeneralSearch(KEYWORD.decode(ENCODING), e, PREFERENCE)
		results = gs.get_results()
		print gs.num_results
		#print gs._last_search_url
		
		#s1 = str.format( "%s: %d results of \"" % ( e.upper(), gs.num_results ) )
		#s2 = str.format( "\" --- %s" % ( time.strftime("%Y-%m-%d %X", time.localtime())) )
		#s = s1 + KEYWORD.decode(ENCODING) + s2
		#try_output( s )
		try_output( "%s: %d results of \"%s\" --- %s" % ( e.upper(), gs.num_results, KEYWORD.decode(ENCODING), time.strftime("%Y-%m-%d %X", time.localtime())) )
		try_output( 80*'-' )

		index = ENGINE.index(e)
		if DATA[index][0]==e:
			#DATA[index][1].append([time.strftime("%Y-%m-%d %X", time.localtime()), gs.num_results])
			DATA[index][1].append([start_time, gs.num_results])

		count=0
		over=False
		while True:
			for r in results:
				count=count+1
				if count>NUM:
					over=True
					break
				try_output( "results[%d]: " % count )
				for k in FORMAT:
					s = "r.%s" % k
					c = eval( s )

					try_output( "%s" % c )
				try_output( 80*'+' )
			if count==0 or over:
				break
			results = gs.get_results()

		del gs

	try_chart()

	if INTERNAL:
		print "info: loop search every %d seconds, press CTRL+C to exit." % INTERNAL
		time.sleep(string.atof(INTERNAL))
		start_time += INTERNAL
	else:
		sys.exit()
