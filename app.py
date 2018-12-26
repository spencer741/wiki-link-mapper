#WikiLinkMapper v1
#Spencer Arnold

import urllib.request

#Entry 
def main():
    #This is about to be so bad.
    parseRaw(sendReq(prompt()))
    

def prompt():
    
    #root page
    return root = input("Please enter root wiki page link: ")
    
    #simplify entry mechanism by abstracting link entry away.
    #this will be more complex than you think.
    #Hence the prompt func.

def sendReq(url):
    
    return str(urllib.request.urlopen(root).read())

def parseRaw(rawBody):
    recognizer = 0
    for charac in rawBody:
        if (charac == 'h' and recognizer == 0) or (charac == 'r' and recognizer == 1) or (charac == 'e' and recognizer == 2) || (charac == 'f' and recognizer == 3):
            recognizer++
            if(recognizer == 4):
                print("Found URL")
        else
            recognizer = 0
        
    
if __name__ == '__main__':
    main()
