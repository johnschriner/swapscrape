# swapscrape
An automation tool using Selenium and ImageScraper to grab images from a site

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



