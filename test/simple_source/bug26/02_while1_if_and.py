# From 2.6.9 ftplib.py
# Bug was handling if with "and' inside while1
def getmultiline(line):
    if line[3]:
        while 1:
            if line[2] and line[5]:
                break
    return
