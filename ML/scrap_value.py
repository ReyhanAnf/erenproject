# from gettext import find
# import pandas as pd
# from bs4 import BeautifulSoup
# import requests

# df_link = pd.read_csv('ML/data/link_hoax.csv')

# arrTgl = []
# arrJdl = []
# arrKtn = []

# page = 2

# for i in range(len(df_link)):
#     if i != f'https://turnbackhoax.id/page/{page}/'
#         print(f'succes {i}')
#         link = df_link.link[i]
#         get = requests.get(link)
#         bs = BeautifulSoup(get.text, 'html.parser')

#         semi = bs.find('div', id='main-content')
#         judul = semi.find('h1').get_text()

#         tanggal = semi.find('span',class_='entry-meta-date').find('a').get_text()

#         skonten = semi.find_all('p')
#         konten = [x.get_text() for x in skonten]

#         del konten[0:8]
#         del konten[-8:]
        
#         kontenTeks = ''
#         for k in range(len(konten)):
#             kontenTeks += konten[k]
        
#         arrKtn.append(kontenTeks)
#         arrTgl.append(tanggal)
#         arrJdl.append(judul[8:])
#     else:
#         page += 1
        

# df_data = pd.DataFrame({'tanggal':arrTgl,
#                         'judul':arrJdl,
#                         'konten':arrKtn})

# df_data.to_csv('ML/data/data_news_hoax.csv', index=False)


from gettext import find
import pandas as pd
from bs4 import BeautifulSoup
import requests

df_link = pd.read_csv('ML/data/link_hoax.csv')

arrTgl = []
arrJdl = []
arrKtn = []

page = 2

for i in range(20,200):
    print('succes' ,i)
    link = df_link.link[i]
    get = requests.get(link)
    bs = BeautifulSoup(get.text, 'html.parser')
    semi = bs.find('div', id='main-content')
    judul = semi.find('h1').get_text()
    tanggal = semi.find('span',class_='entry-meta-date').find('a').get_text()

    skonten = semi.find_all('p')
    konten = [x.get_text() for x in skonten]
    del konten[0:8]
    del konten[-8:]
        
    kontenTeks = ''
    for k in range(len(konten)):
        kontenTeks += konten[k]
        
    arrKtn.append(kontenTeks)
    arrTgl.append(tanggal)
    arrJdl.append(judul[8:])

        

df_data = pd.DataFrame({'tanggal':arrTgl,
                        'judul':arrJdl,
                        'konten':arrKtn})

df_data.to_csv('ML/data/data_news_hoax.csv', index=False)





