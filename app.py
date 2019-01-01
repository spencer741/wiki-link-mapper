#WikiLinkMapper v1
#Spencer Arnold

import urllib.request

#Entry 
def main():
    #This is about to be so bad.
    RootUrl, ArticleDepth = prompt()
    contents = sendReq(RootUrl)
    with open("raw.txt" , "w") as raw:
        raw.write(contents)
        
    ParseRawUrls()
    AssembleCompleteUrls()
    

def prompt():
    
    #root page
    RootUrl = input("Please enter root wiki page link: ")
    ArticleDepth = input("Please Enter the article depth you would like to acheive: ")
    return RootUrl, ArticleDepth
    #simplify entry mechanism by abstracting link entry away.
    #Hence the prompt func.

def sendReq(root):
    
    return str(urllib.request.urlopen(root).read())

def ParseRawUrls():
    #make algorithm cleaner. perhaps general. pass in string and loop through each character for matching or something.
    with open("raw.txt", 'r') as raw:
        with open("Bare_Urls.txt" , 'w') as bare:    
            for char in iter(lambda: raw.read(1), ''):
                #print("here")
                if char == 'h':
                    char = raw.read(1)
                    if char == 'r':
                        char = raw.read(1)
                        if char == 'e':
                            char = raw.read(1)
                            if char == 'f':
                                raw.read(2)
                                char = raw.read(1)
                                url = ""
                                #print("Found a URL in Response Data!")
                                while char != '"':
                                    url += char
                                    char = raw.read(1)
                                    #cleans up non wiki related links
                                if url.startswith("/wiki/") and ":" not in url:
                                    isVisited = False
                                    url += '\n'
                                    with open("Visited_Urls.txt", 'r') as visited:
                                        vline = visited.readline()
                                        while vline != '' and isVisited == False:
                                            if url == vline:
                                                isVisited = True
                                            vline = visited.readline()
                                            
                                    if(not isVisited):
                                        with open("Visited_Urls.txt", 'a') as visited:
                                            visited.write(url)
                                            bare.write(url)
                                   
                        
                    
def AssembleCompleteUrls():
    with open("Bare_Urls.txt" , 'r') as bare:
        with open("Complete_Urls.txt", 'a') as complete:
            
            for line in iter(bare.readline, ''):
                
                if line.startswith("/wiki/"): # and ":" not in line:
                    makeComplete = "https://en.wikipedia.org"
                    makeComplete += line
                    complete.write(makeComplete)
                
if __name__ == '__main__':
    main()
