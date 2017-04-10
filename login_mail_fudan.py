#!/usr/bin/env python                                                            
# -*- coding: utf-8 -*-                                                          
#                                                                                
# Copyright (c) 2016 chaoqiankeji.com, Inc. All Rights Reserved                   
#                                                                                

"""                                                                              
File: login_mail_fudan.py                                                                       
Author: minus(minus@stu.xjtu.edu.cn)                                             
Date: 2017-04-10 20:06
Project: cdr2                                                  
"""

import requests
import json
from lxml import etree

FUDAN_URL = 'https://mail.fudan.edu.cn/coremail/index.jsp'
RECEIVE_URL = 'https://mail.fudan.edu.cn/coremail/XT3/mbox/list.jsp?sid=CAttWzggMTKdRCWynlggXWjcamIYhjBG&fid=1&nav_type=system&inbox=true'
POST_DATA = {
    'action:login':'',
    'domain':'fudan.edu.cn',
    'locale':'zh_CN',
    'nodetect':'false',
    'password':'qw549380211',
    'uid':'15110180025',
    'useSSL':'true'
}


def main():
    r = requests.Session()
    res = r.post(FUDAN_URL, data=POST_DATA)
    html = res.text

    selector=etree.HTML(html)
    url2=selector.xpath('//*[@id="navFid_1"]/@href')#找到收件箱对应的链接
    RECEIVE_URL = 'https://mail.fudan.edu.cn/coremail/XT3/' + url2[0]
    RECEIVE_URL = RECEIVE_URL.replace('list', 'getListDatas')
    print RECEIVE_URL

    # print res.text
    receive = r.post(RECEIVE_URL)
    with open('/home/minus/a.html','wb') as f:
        f.write(receive.text.encode('utf-8'))

if __name__ == '__main__':
    main()
