 from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time





#Figure out the number of pages by looking at the URL for the last item in the pagination. e.g. A has 9 pages, S has 11 pages.


def run_scrapper():
    print('running')
    
    pages=9
    for x in range(1, pages+1):
      url = 'https://www.manualslib.com/brand/A.html'
      url += '?page='
      url += str(x)
      print(url)
      time.sleep(5)
      content = requests.get(url).text
      soup = BeautifulSoup(content, 'html.parser')

      regexBrand = re.compile('.*col-xs-3 col-sm-2 col1.*')
      regexCategory = re.compile('.*catel.*')


      brands = soup.findAll('div', {'class': regexBrand})
      brand_list = []
      for b in brands[0:]:
        result = b.text.strip()
        brand_list.append(result)
      print(brand_list)
    
      category = soup.findAll('div',{'class': regexCategory})
      category_list =[]
      for c in category[0:]:
        result2 = c.text.strip()
        category_list.append(result2)


    #mbl = pd.DataFrame({'Brands':brand_list,'Category':category_list})


    #mbl.to_excel("Brands.xlsx",index=False)
    
    print("done")


run_scrapper()
