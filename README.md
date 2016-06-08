# swapscrape
An automation tool using Selenium and ImageScraper to grab images from a site.  This particular site adds images to arbitrary directories so it's necessary to upload to discover the URL.  Essentially it uploads an image to an image host, grabs the URL, and grabs images from 'nearby' URLs before tearing down the test.

##Required:
  Firefox web browser: https://www.mozilla.org/en-US/firefox/new/
  
  ImageScraper: https://pypi.python.org/pypi/ImageScraper

    pip install ImageScraper

  Selenium WebDriver python bindings: https://pypi.python.org/pypi/selenium

    pip install -U selenium
    

##Running swapscrape.py

There are essentially two parts to scraping this [unnamed] site:

  (1) automating an upload and grabbing the current URL
  
  (2) parsing that URL and grabbing images from URLs 'nearby'
  
Edit swapscrape.py to reflect both the directory of your images and the URL of the image host.
Enjoy contributing AND plundering for random images!



