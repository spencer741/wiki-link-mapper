#WikiLinkMapper v1
#Spencer Arnold

import urllib.request

#Entry 
def main():
    #This is about to be so bad.
    
    contents = sendReq(prompt())
    with open("raw.txt" , "w") as raw:
        raw.write(contents)
        
    parseRaw()
    

def prompt():
    
    #root page
    return input("Please enter root wiki page link: ")
    
    #simplify entry mechanism by abstracting link entry away.
    #Hence the prompt func.

def sendReq(root):
    
    return str(urllib.request.urlopen(root).read())

def parseRaw():
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
                                if "wiki" in url:
                                    url += '\n'
                                    bare.write(url)
                        
                    
        
    
if __name__ == '__main__':
    main()
