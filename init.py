#!/usr/bin/python
import sys
import urllib.request
from bs4 import BeautifulSoup


def main():
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
    RootUrl, ArticleDepth = prompt()
    content = sendReq(RootUrl)
    with open("raw.txt" , "w") as raw:
        raw.write(content)
    test()

def sendReq(requesteduri):
    
    return str(urllib.request.urlopen(requesteduri).read())

def prompt():
    
    #root page
    RootUrl = input("Please enter root wiki page link: ")
    ArticleDepth = input("Please Enter the article depth you would like to acheive: ")
    return RootUrl, ArticleDepth

def test():
    with open('raw.txt', 'r') as raw:
        data = raw.read()
        soup = BeautifulSoup(data)
        count = 0;
        for tag in soup.findAll('a', href=True):
            rawURL = tag['href']
            if rawURL.startswith("/wiki/") and ":" not in rawURL:
                rawURL.strip("/wiki/")
                print (rawURL);
                count+=1
        print("Urls in page: " , count)

if __name__ == '__main__':
    main()
