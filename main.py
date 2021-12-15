from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time
import string

#TODO:
#1. Figure out the number of pages by looking at the URL for the last item in the pagination. e.g. A has 9 pages, S has 11 pages. Do this Dynamically, instead of hardcoding it

#2. The Letter D is giving an error on illegal character, something doesn't play nice with excel. Look into it later... 


def run_scrapper(Alphabet, TotalPages):
    print('running')
    mbl = pd.DataFrame()
    filename = "Brands-"+ Alphabet +".xlsx"
   

    brand_list = []
    category_list =[]
    
    for x in range(1, TotalPages+1):
      url = "https://www.manualslib.com/brand/"+Alphabet+".html?page="+str(x)
      print(url)
     
      time.sleep(5)
      content = requests.get(url).text
      soup = BeautifulSoup(content, 'html.parser')

      regexBrand = re.compile('.*col-xs-3 col-sm-2 col1.*')
      regexCategory = re.compile('.*catel.*')


      brands = soup.findAll('div', {'class': regexBrand})
     
      for b in brands[0:]:
        result = b.text.strip()
        brand_list.append(result)
    
      category = soup.findAll('div',{'class': regexCategory})
      
      for c in category[0:]:
        result2 = c.text.strip()
        category_list.append(result2)
      
      
    mbl = pd.DataFrame({'Brands':brand_list,'Category':category_list})
    mbl.to_excel(filename,index=False)
    print("done")

def BrandLoop():
 
 run_scrapper("A",9)
 run_scrapper("B",6)
 run_scrapper("C",7)
# run_scrapper("D",5)
 run_scrapper("E",6)
 run_scrapper("F",4)
 run_scrapper("G",4)
 run_scrapper("H",5)
 run_scrapper("I",4)
 run_scrapper("J",2)
 run_scrapper("K",3)
 run_scrapper("L",4)
 run_scrapper("M",7)
 run_scrapper("N",4)
 run_scrapper("O",3)
 run_scrapper("P",6)
 run_scrapper("Q",1)
 run_scrapper("R",4)
 run_scrapper("S",11)
 run_scrapper("T",6)
 run_scrapper("U",2)
 run_scrapper("V",3)
 run_scrapper("W",3)
 run_scrapper("X",1)
 run_scrapper("Y",1)
 run_scrapper("Z",1)

  #for alphabet in string.ascii_lowercase:
    #call scraper for each letter

BrandLoop()

