#!/usr/bin/python
import sys
import urllib.request
from bs4 import BeautifulSoup
import dbadapter

def main():
    RootUrl, ArticleDepth = prompt()
    
    #initialize db
    dbadapter.createdb() #if not exist capability? Yes.
    dbadapter.buildTables(RootUrl.replace("https://en.wikipedia.org/wiki/", ""))
    #print(RootUrl.replace("https://en.wikipedia.org/wiki/", ""))

    rec(RootUrl.replace("https://en.wikipedia.org/wiki/", ""), RootUrl, int(ArticleDepth))

def getnumchildren(root):
    content = sendReq(root)
    dbadapter.update(root.replace("https://en.wikipedia.org/wiki/", ""), root, 0)
    soup = BeautifulSoup(content)
    lst = []
    for tag in soup.findAll('a', href=True):
        rawURL = tag['href']
        if rawURL.startswith("/wiki/") and ":" not in rawURL:
            lst.append(rawURL)
    return lst

def rec(root,url,depth):
    if depth < 0:
        return
    else:
        urlkey = dbadapter.update(root, url, 0)
        childlist = getnumchildren(url)
        for child in childlist:
            dbadapter.update(root, child, urlkey)
            depth -= 1
            rec(root,child,depth)

def sendReq(requestedurl):
    makeComplete = requestedurl
    if requestedurl.startswith("/wiki/"): # and ":" not in line:
        makeComplete = "https://en.wikipedia.org"
        makeComplete += requestedurl
    return str(urllib.request.urlopen(makeComplete).read())

def prompt():
    #root page
    RootUrl = input("Please enter root wiki page link: ")
    ArticleDepth = input("Please Enter the article depth you would like to acheive: ")

    return RootUrl, ArticleDepth

if __name__ == '__main__':
    main()



