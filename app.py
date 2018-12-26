#WikiLinkMapper v1
#Spencer Arnold

import urllib.request

#Entry 
def main():
    root = prompt()
    contents = str(urllib.request.urlopen(root).read())
    

def prompt():
    
    #root page
    return root = input("Please enter root wiki page link: ")
    
    #simplify entry mechanism by abstracting link entry away.
    #this will be more complex than you think.
    #Hence the prompt func.

def sendReq(url):
    
    return str(urllib.request.urlopen(root).read())
    
if __name__ == '__main__':
    main()
