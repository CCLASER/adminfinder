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
	link = raw_input("Enter Site Name \n(ex : coli.com or www.coli.com ): ")
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
	Space(9); print "#   *** Admin Page Finder ***   #"
	Space(9); print "#    Author : Dalpan  #"
	Space(9); print "#    Email: dalpanid@gmail.com   #"
        Space(9); print "#    Team : Our Struggle Team   #"
	Space(9); print "#####################################"

Credit()
findAdmin()
