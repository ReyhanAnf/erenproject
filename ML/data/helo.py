from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://covid19.go.id/p/hoax-buster'
url2 = 'https://www.erentech.my.id'


coption = Options()
drive = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=coption)
drive.get(url2)

drive.find_element_by_xpath('//*[@id="search-toggler"]/svg').click()


drive.find_element_by_xpath('//*[@id="search-input"]').send_keys('Earphone')
