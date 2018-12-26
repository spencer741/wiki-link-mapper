#WikiLinkMapper v1
#Spencer Arnold

import urllib.request
import re

#Entry 
def main():
    #This is about to be so bad.
    parseRaw(sendReq(prompt()))
    

def prompt():
    
    #root page
    return input("Please enter root wiki page link: ")
    
    #simplify entry mechanism by abstracting link entry away.
    #this will be more complex than you think.
    #Hence the prompt func.

def sendReq(root):
    
    return str(urllib.request.urlopen(root).read())

def parseRaw(haystack):
    #I suck. Figure out regex
    needle = r"^href\".*\""
    pattern = re.compile(needle)
    print(pattern)
    print(re.findall(pattern, haystack))
        
    
if __name__ == '__main__':
    main()
