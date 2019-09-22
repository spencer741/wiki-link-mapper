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

    #recurse(RootUrl.replace("https://en.wikipedia.org/wiki/", ""), RootUrl, ArticleDepth)
    

def recurse(root, url, depth):
    if depth == 0:
        return
    else:
        #store parent url in the db. This is so we get a primary key to use as a self-referencing key for all of the children
        key = dbadapter.update(root, url, None)

        #send request to parent url to get children
        content = sendReq(url)

        #parse content and store url with key
        soup = BeautifulSoup(content)
        for tag in soup.findAll('a', href=True):
            rawURL = tag['href']
            if rawURL.startswith("/wiki/") and ":" not in rawURL:
                dbadapter.update(root, rawURL, key)
                print(rawURL.replace("/wiki/",""))
        key+=1
        depth-=1
        recurse(dbadapter.getURL(root, key), depth)

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



