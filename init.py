#!/usr/bin/python
import sys
import urllib.request
from bs4 import BeautifulSoup
import dbadapter

def main():
    RootUrl, ArticleDepth, CleanBeforeExecute = prompt()

    dbadapter.createdb() #if not exist capability? Yes.

    rootTopic = RootUrl.replace("https://en.wikipedia.org/wiki/", "")

    if(CleanBeforeExecute == 'Y'):
        dbadapter.deletetable(rootTopic)
    
    dbadapter.buildTables(rootTopic)

    rec(rootTopic, RootUrl.replace("https://en.wikipedia.org", ""), int(ArticleDepth), True)

def getchildren(root):
    content = sendReq(root)
    #head, sep, tail = content.partition('References')
    #create rules to clean wikipedia by stripping out undesirable tags
    #dbadapter.update(root.replace("https://en.wikipedia.org/wiki/", ""), root, 0)
    soup = BeautifulSoup(content, features="html.parser")
    lst = []
    for tag in soup.findAll('a', href=True):
        rawURL = tag['href']
        if rawURL.startswith("/wiki/") and ":" not in rawURL and "disambiguation" not in rawURL:
            lst.append(rawURL)
    return lst

def rec(root,url,depth,first):
    if depth == 0: #base case
        return
    else: #recursive case

        #update parent and obtain key
        urlkey = dbadapter.update(root, url, 0)

        #get number of children for child processing
        childlist = getchildren(url)

        #if there is a duplicate, don't pursue its children... right now we are pursuing
        #them up to the alloted depth...
       
        depth -= 1
        #pre-order traverse. Left to right.
        for child in childlist:
            #print("depth: ",depth)
            dbadapter.update(root, child, urlkey) 
            rec(root,child,depth,first)
            #need to check children duplicates
            #need to add a db flag if the child has been processed as a parent.

def sendReq(requestedurl):
    makeComplete = requestedurl
    if requestedurl.startswith("/wiki/"): # and ":" not in line:
        makeComplete = "https://en.wikipedia.org"
        makeComplete += requestedurl
    return str(urllib.request.urlopen(makeComplete).read())

def prompt():
    #todo: input sanitation
    RootUrl = input("Please enter root wiki page link: ")
    ArticleDepth = input("Please Enter the article depth you would like to acheive: ")
    CleanBeforeExecute = input("Would you like to clean table in question before execution? (Y/N): ")

    return RootUrl, ArticleDepth, CleanBeforeExecute

if __name__ == '__main__':
    main()



