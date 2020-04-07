#!/usr/bin/python
#coding=utf-8
#-*-coding:utf-8 -*-
import codecs
from translate import Translator
import re, sys, os
import json
path = "/home/reeman/Public/ReemanWeb/robot_web_ui"
import sys
reload(sys)
sys.setdefaultencoding('gbk')

# print sys.argv[0]
# cwd = os.getcwd()
# fn = os.path.resolve(os.path.abspath(cwd),sys.argv[1])
# test2 = (cwd + sys.argv[1])
#print test2
# print os.path.dirname(os.path.abspath(__file__))
fn = os.path.join( path + sys.argv[1])
# print os.path.exists (fn)
class MyList(list):
    def __str__(self):
        retval = "["
        for item in self:
            retval += '"'
            retval += item
            retval += '"'
            retval += ","
        retval = retval.rstrip(",")
        retval += "]"
        return retval

#regex = "<\s*Button[^>]*>(.*?)<\s*/\s*Button>$" 
with open(fn, "r") as f:
    text = f.read()
    html_str = re.sub(r'<br>', ' ' , text)
    relt1 = re.findall(r'<Button[^>]*>(.+?)<\s*/\s*Button>', html_str)
    
list(set(relt1))
data = {}
relt = MyList(relt1)
translator= Translator(from_lang="chinese",to_lang="english")
for x in range(len(relt)): 
    translation = translator.translate(relt[x])
   # print translation   
    print relt[x]
    data[relt[x]]= translation
    result = json.dumps(data)
    json_data = json.dumps(relt[x])


with codecs.open("test.json", "w", 'gbk') as f:
    json.dump(json_data.encode('gbk'), f)
    f.write(result)


print sys.stdout.encoding
