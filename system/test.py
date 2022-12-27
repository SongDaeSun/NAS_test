import os
import time

print (time.ctime(max(os.stat(root).st_mtime for root,_,_ in os.walk('/data'))))