#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Site Name \n(ex : example.com or www.example.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(9); print "#####################################"
	Space(9); print "#   +++ Admin Panel Finder v1 +++   #"
	Space(9); print "#         Script by Gord1           #"
	Space(9); print "#    Our Struggle Team              #"
	Space(9); print "#####################################"

  ____    _    _     ____   _    _   _      ___ ____   
 |  _ \  / \  | |   |  _ \ / \  | \ | |    |_ _|  _ \  
 | | | |/ _ \ | |   | |_) / _ \ |  \| |_____| || | | | 
 | |_| / ___ \| |___|  __/ ___ \| |\  |_____| || |_| | 
 |____/_/   \_\_____|_| /_/   \_\_| \_|    |___|____/  
                                                       
=================================================================== 


Credit()
findAdmin()
