#WikiLinkMapper v1
#Spencer Arnold

import urllib.request

#Entry 
def main():
    #This is about to be so bad.
    
    contents = sendReq(RootUrl)
    with open("raw.txt" , "w") as raw:
        raw.write(contents)
        
    ParseRawUrls()
    AssembleCompleteUrls()
    



def sendReq(requesteduri):
    
    return str(urllib.request.urlopen(requesteduri).read())

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

#old junk
'''
def recurse(root, url, depth):
    #have a width and a depth. Once the width gets down to zero, decrement depth
    numchildren = getnumchildren(url)
    depth-=1
    if depth == -1:
        return
    else:
        #store parent url in the db. This is so we get a primary key to use as a self-referencing key for all of the children
        key = dbadapter.update(root, url, 0)
        #print("this is key: " + key)
        #send request to parent url to get children
        content = sendReq(url)

        #parse content and store url with key
        soup = BeautifulSoup(content)

        print(depth, " PAGE ---------------------------------")

        for tag in soup.findAll('a', href=True):
            rawURL = tag['href']
            if rawURL.startswith("/wiki/") and ":" not in rawURL:
                dbadapter.update(root, rawURL, key)
                print(rawURL.replace("/wiki/",""))
        key+=1
        print("MADE IT TO BEGINNING OF RECURSE!!!")
        recurse(root, dbadapter.getURL(root, key), depth)

'''