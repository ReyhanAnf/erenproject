def Scrap(url):
  import requests
  from bs4 import BeautifulSoup

  rurl = requests.get(url)
  coverpage = rurl.content
  
  soup = BeautifulSoup(coverpage, 'html5lib')
  cp_title = soup.find_all('title')
  cp_p = soup.find_all('p')
  
  cp_title = [cp_title[i].get_text() for i in range(len(cp_title))]
  cp_p = [cp_p[i].get_text() for i in range(len(cp_p))]
  
  result =  {'title': cp_title, 'content': cp_p}
  return result