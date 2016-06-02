import sys
import os
import time

##early version of script

url = “redacted_url”
ending = url.rsplit('/', 1)[-1]
print(ending)
while True:
	os.system("image-scraper redacted url” + ending + " --formats gif jpg jpeg")
	time.sleep(60)
	ending = str(int(ending)+1)
	print(ending)


