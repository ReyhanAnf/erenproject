import pandas as pd
from bs4 import BeautifulSoup
import requests

arrdata = []
    
for i in range(2,430):
    print(f'succes {i}')
    arrdata = list(dict.fromkeys(arrdata))

    link = f'https://turnbackhoax.id/page/{i}/'
    
    get = requests.get(link)
    bs = BeautifulSoup(get.text, 'html.parser')
    artikel = bs.find('div', id='main-content')
    a = artikel.find_all('a')
    
    for j in a:
        k = j.get('href')
        if k == f'https://turnbackhoax.id/page/{i+1}/':
            pass
        elif k == 'https://turnbackhoax.id/page/429/': 
            pass
        elif k == f'https://turnbackhoax.id/page/{i}/': 
            pass
        elif k == 'https://turnbackhoax.id/': 
            pass
        elif k[0:30] == 'https://turnbackhoax.id/author': 
            pass
        elif k[-12:] == '#mh-comments': 
            arrdata.append(k[:-12])
        else:
            arrdata.append(k)
            

df = pd.DataFrame({'link':arrdata})
df.to_csv('ML/data/link_hoax.csv',index=False)