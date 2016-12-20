#!/usr/bin/python
import re
import sys

class xmlInfo:
    def __init__(self):
        self.searchKey = ""
        self.returnType = ""
        self.pageUrl = []

def getListInfo(infos,key1Str):
    outlist = []
    try:
        symbolpre = "<"+key1Str+">"
        symbolend = "</"+key1Str+">"
        tokens = infos.split(symbolpre)
        for token in tokens:
            token = token.strip()
            if symbolend not in token:
                continue
            values = token.split(symbolend)
            value = values[0].strip()
            if value!="":
                outlist.append(value)
    except:
        outlist = []
    return outlist

if __name__=="__main__":
    if len(sys.argv)!=3:
        print "input Error!!!\npython diff.py file1 file2"
        exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    
    file1dic = {}
    fin1 = open(file1,"r")
    while 1:
        line = fin1.readline()
        line = line.strip()
        if not line:
            break
        line = re.sub("<xmldoc>.*?</xmldoc>","",line)
        key = re.sub("^.+<key>(.+?)</key>.+$",r"\1",line)
        value = xmlInfo()
        value.searchKey = re.sub("^.+<searchkey>(.+?)</searchkey>.+$",r"\1",line)
        value.returnType = re.sub("^.+<returntype>(.+?)</returntype>.+$",r"\1",line)
        item_list = getListInfo(line,"item")
        for item in item_list:
            #urls = re.findall('<url><!\[CDATA\[(.*?)\]\]></url>',item)
            urls = re.findall('<url>(.*?)</url>',item)
            if len(urls)>0:
                url = re.sub("^<!\[CDATA\[(.*?)\]\]>$",r'\1',urls[0])
                value.pageUrl.append(url)
            else:
                #urls = re.findall('<business_url><!\[CDATA\[(.*?)\]\]></business_url>',item)
                urls = re.findall('<business_url>(.*?)</business_url>',item)
                if len(urls)>0:
                    url = re.sub("^<!\[CDATA\[(.*?)\]\]>$",r'\1',urls[0])
                    value.pageUrl.append(url)
        #print value.pageUrl
        #print len(value.pageUrl)
        file1dic[key] = value
    fin1.close()

    file2dic = {}
    fin2 = open(file2,"r")
    while 1:
        line = fin2.readline()
        line = line.strip()
        if not line:
            break
        line = re.sub("<xmldoc>.*?</xmldoc>","",line)
        key = re.sub("^.+<key>(.+?)</key>.+$",r"\1",line)
        value = xmlInfo()
        value.searchKey = re.sub("^.+<searchkey>(.+?)</searchkey>.+$",r"\1",line)
        value.returnType = re.sub("^.+<returntype>(.+?)</returntype>.+$",r"\1",line)
        item_list = getListInfo(line,"item")
        for item in item_list:
            #urls = re.findall('<url><!\[CDATA\[(.*?)\]\]></url>',item)
            urls = re.findall('<url>(.*?)</url>',item)
            if len(urls)>0:
                url = re.sub("^<!\[CDATA\[(.*?)\]\]>$",r'\1',urls[0])
                value.pageUrl.append(url)
            else:
                #urls = re.findall('<business_url><!\[CDATA\[(.*?)\]\]></business_url>',item)
                urls = re.findall('<business_url>(.*?)</business_url>',item)
                if len(urls)>0:
                    url = re.sub("^<!\[CDATA\[(.*?)\]\]>$",r'\1',urls[0])
                    value.pageUrl.append(url)
        file2dic[key] = value
    fin2.close()
   
    #diff
    sumNum = 0
    diffskNum = 0
    difftyNum = 0
    diff1stNum = 0
    diff3stNum = 0
    diff5stNum =0
    for key,value1 in file1dic.items():
        if not file2dic.has_key(key):
            continue
        sumNum += 1
        value2 = file2dic[key]
        if value1.searchKey!=value2.searchKey:
            diffskNum += 1
        if value1.returnType!=value2.returnType:
            difftyNum += 1
        for i in range(len(value1.pageUrl)):
            if i>4:
              break
            if i>(len(value2.pageUrl)-1):
                diff5stNum += 1
                if i==0:
                    diff1stNum += 1
                    diff3stNum += 1
                    break
                elif i<3:
                    diff3stNum += 1
                    break
                break
            elif value1.pageUrl[i]!=value2.pageUrl[i]:
                diff5stNum += 1
                if i==0:
                    diff1stNum += 1
                    diff3stNum += 1
                    break
                elif i<3:
                    diff3stNum += 1
                    break
                break

    print "sumNum:%d\tdiffskNum:%d\tdifftyNum:%d\tskRate:%f\ttyRate:%f" % (sumNum,diffskNum,difftyNum,float(diffskNum)/sumNum,float(difftyNum)/sumNum)    
    print "diff1stNum:%d\tdiff3stNum:%d\tdiff5stNum:%d\t1stRate:%f\t3stRate:%f\t5stRate:%f" % (diff1stNum,diff3stNum,diff5stNum,float(diff1stNum)/sumNum,float(diff3stNum)/sumNum,float(diff5stNum)/sumNum)    
 
