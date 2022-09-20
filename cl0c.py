import subprocess #line:3
import requests #line:4
import time #line:5
import sys #line:6
import os #line:7
from urllib3 .connectionpool import xrange #line:8


def func (O00OOO0000OO0OO0O ,O000O00O00O0OO00O ,arg3 ='arg3',*,arg4 ,**O0OOO00OO0O0O0O00 ):#line:1
    ebaasidj = ('arg1',O00OOO0000OO0OO0O )#line:2
    adjaasd =  ('arg2',O000O00O00O0OO00O )#line:3
    vdhjsfbwe = ('arg3',arg3 )#line:4
    defpl = ('arg4',arg4 )#line:5
    nuke = ('kwargs',O0OOO00OO0O0O0O00 )#line:6
func ('a','b',arg3 ='c',arg4 ='d')#line:8
os .system ('cls')#line:9
os .system ('title craigLog')#line:10
toolbar_width =15 #line:11
sys .stdout .write ("[%s]"%(" "*toolbar_width ))#line:12
sys .stdout .flush ()#line:13
sys .stdout .write ("\b"*(toolbar_width +1 ))#line:14
for i in xrange (toolbar_width ):#line:16
    time .sleep (0.1 )#line:17
    hwid =str (str (subprocess .check_output ('wmic csproduct get uuid')).strip ().replace (r"\r","").split (r"\n")[1 ].strip ())#line:18
    r =requests .get ("https://pastebin.com/CDgXMFDF")#line:19
    sys .stdout .write ("*")#line:20
    sys .stdout .flush ()#line:21
sys .stdout .write ("\n")#line:22
if hwid in r .text :#line:24
    print ("HWID GOOD!")#line:25
    time .sleep (.1 )#line:26
else :#line:27
    print ("Error! HWID Not I Database!")#line:28
    os .system ('pause >NUL')#line:29
