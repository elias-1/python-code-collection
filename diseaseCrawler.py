#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import os
import sys
import re


def main():
	# Store the cookies and create an opener that will hold them
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	# opener.open('http://202.201.7.30:8080/cdd/login.do?loginType=1&userName=lzdx&password=123456')

	directory = './output/'
	if not os.path.exists(directory):
   		os.makedirs(directory)
	
        logfile = "./log.txt"
   	search_url = "http://202.201.7.30:8080/cdd/disease/diseaseSearch.do?model=queryDiseaseById&myback=1&id="
	connection_timeout = 5
   	has_content = 0
   	no_content = 0
	ID_range = range(37000,45000)

   	# for i in range(37000,45000):
	for i in ID_range:
		print "Processing ID %d / %d | total: %d remaining" %(i, ID_range[-1], ID_range[-1] - i)
   		url = search_url + str(i)
                file_name = directory + str(i) +".html"
                try:
                    f = opener.open(url,None,connection_timeout)
                    content = f.read()
                    if len(content.splitlines()) == 1 and content.split('\'')[3] == "/cdd/cdd/login.jsp":
                        # renew the login info, the cookies is expired
                        opener.open('http://202.201.7.30:8080/cdd/login.do?loginType=1&userName=lzdx&password=123456')
                        f = opener.open(url,None,connection_timeout)
                        content = f.read()
                    # print content.count('\n')
                    if content.splitlines()[32].strip() != "操作错误":
                        has_content += 1
                        g = open(file_name,'w')
                        g.write(content)
                        g.close()
                    else:
                        no_content += 1
                except Exception, e:
                    error_str = "index: " + str(i) + " | error message: "  + str(e) + "\n";
		    h = open(logfile,'a')
                    h.write(error_str)
                    h.close()
                    # os.system( "echo %s >> ./log.txt" % e)
        print "We obtain %d page with content, out of total %d \n" %(has_content,len(ID_range))
        print "We obtain %d page without content, out of total %d \n" %(no_content, len(ID_range))
   		
if __name__ == '__main__':
	main()
