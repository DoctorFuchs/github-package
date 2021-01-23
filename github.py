import os

def install(link):
    try:
        os.system("git clone "+str(link))
    
    except:
        print("git is not installed or your link is not avaible")
    
def update(link):
    try:
        os.system("git fetch "+str(link))
    
    except:
        print("git is not installed or your link is not avaible")
