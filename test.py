#!/bin/python

from xgoogle.GeneralSearch import GeneralSearch

#gs=GeneralSearch('cars', 'baidu')
gs=GeneralSearch('cars')
results = gs.get_results()
