from pathlib import Path
from pickle import FALSE

path = Path('/var/log/dnf.log')
matchon = "unloaded."

content=path.read_text()
lines = content.splitlines()
count=0
for line in lines:
    count+=1
    for word in line.split():
       #print(word)
        if word == matchon :
           print(lines[count-1])


