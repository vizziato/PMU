
import time

from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



dr = webdriver.PhantomJS(executable_path=r'C:\Users\Giuseppe\Documents\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe')
browser = webdriver.Firefox(executable_path=r'C:\Users\Giuseppe\Documents\Python\geckodriver-v0.16.1-win64\geckodriver.exe')
#browser.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_addeventlistener_displaydate")
browser.get("https://www.pmu.fr/turf/01012016/R1/C1")
time.sleep(10) # Let the user actually see something!
#print(browser.find_element_by_xpath('/html/body'))
#print(browser.find_element_by_xpath("/html/body/div[@id ='container']"))         
#print(browser.find_element_by_xpath("//*[@id='iframeResult']//button"))       
print(browser.find_element_by_xpath('//*[@id="main"]/div/div[8]/div[1]/div[3]/section/div/div[1]/ul/li[2]').click() )
#dr.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_addeventlistener_displaydate")

#dr.find_element_by_id("myBtn").click()

#browser = webdriver.Firefox()
#browser.get('https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_button_group_size&stacked=h')
##log_but2 = '//*[@id="main"]/div/div[8]/div[1]/div[3]/section/div/div[1]/ul/li[2]'
#//*[@id="main"]/div/div[8]/div[1]/div[3]/section/div/div[1]/ul/li[2]
#sel = '#main>div>div:nth-child(8)>div.course-particip>div.course-participants-region>section>div>div.participants-nav-region>ul>li.partants.actif.visible.selected'
#sel = 'ul.tabs>li.partants.actif.visible.selected'
#print(browser.find_element_by_xpath(log_but2).click())
#time.sleep(20) # Let the user actually see something!

#print(browser.find_element_by_class_name('container'))

'''
try:
    element = WebDriverWait(browser, 10).until(
        EC.e((By.ID, "myBtn"))
        )
    #element.click()
    browser.execute_script("arguments[0].click();", element)
        #EC.presence_of_element_located((By.CSS_SELECTOR, "button#myBtn"))

    #print('push button')
except:
    print('error')
'''
#finally:
 #   browser.quit()
#time.sleep(5) # Let the user actually see something!


#browser.find_element_by_id('myBtn')
#time.sleep(5) # Let the user actually see something!

#element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul#ulBirthYear a[data-value='2002']")))
#element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#myBtn")))
#element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.tabs li[data-tag='tag:clic:tableauPartants']")))
#element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, log_but2)))

#print('push button')
#print('element.click()',element)
#browser.quit()



'''
import urllib.request

import httplib2

url = 'https://www.pmu.fr'

#h1 = urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)¶'www.python.org')

h1 = urllib.request.urlopen(url)

data = h1.read()

print(type(data))
print(data)
'''

#from urllib.request import urlopen

#url = 'https://github.com'
#url ='https://www.bcv.ch/'
#url = 'https://www.pmu.fr/turf'

#resp = urlopen(url)
#print(resp.read())

'''
import urllib
import urllib.request
import html.parser
import requests
from requests.exceptions import HTTPError
from socket import error as SocketError
from http.cookiejar import CookieJar

try:
    #req=urllib.request.Request(url, None, {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; G518Rco3Yp0uLV40Lcc9hAzC1BOROTJADjicLjOmlr4=) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'})
    req=urllib.request.Request(url, None, {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; G518Rco3Yp0uLV40Lcc9hAzC1BOROTJADjicLjOmlr4=) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept': 'text/html','Accept-Charset': 'utf-8'})
    cj = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    #opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
    response = opener.open(req)
    #resp = urlopen(url)
    raw_response = response.read().decode('utf8', errors='ignore')
    #raw_response = response.read()
    print(raw_response)
    response.close()
    #print(raw_response)
except urllib.request.HTTPError as inst:
    output = format(inst)
    print(output)


'''
'''
import urllib.request
response = urllib.request.urlopen('https://www.pmu.fr/')
html = response.read()

print(html)
'''
'''
import urllib
import urllib.request
import html.parser
import requests
from requests.exceptions import HTTPError
from socket import error as SocketError
from http.cookiejar import CookieJar

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
response = opener.open('http://www.bad.org.uk')
print(response.read())
'''
'''
import requests

url = 'https://www.pmu.fr/turf/28042017/R1/C2/E_QUINTE_PLUS'
r = requests.get(url).text

print(r)



#url = 'https://github.com'
#url ='https://www.bcv.ch/'
#url = 'https://www.pmu.fr/turf'

#url = "https://www.pmu.fr/turf/28042017/R1/C2/E_QUINTE_PLUS"

# use firefox to get page with javascript generated content
#!/usr/bin/env python
from contextlib import closing
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait

# use firefox to get page with javascript generated content
with closing(Firefox()) as browser:
     browser.get(url)
     button = browser.find_element_by_name('button')
     button.click()
     # wait for the page to load
     WebDriverWait(browser, timeout=10).until(
         lambda x: x.find_element_by_id('someId_that_must_be_on_new_page'))
     # store it to string variable
     page_source = browser.page_source
print(page_source)

'''
'''
from selenium import webdriver
from bs4 import BeautifulSoup as bs
driver = webdriver.Firefox()
driver.get("http://www.walmart.com/cp/121828")
source = driver.page_source()
soup = bs(source)
dept_list = soup.find_all("div", class_ = "departments")
'''

from selenium import webdriver


#url = 'https://github.com'
#url ='https://www.bcv.ch/'
#url = 'https://www.pmu.fr/turf'

#url = "https://www.pmu.fr/turf/28042017/R1/C2/E_QUINTE_PLUS"

anneeArray = [16]

#browser = webdriver.Firefox()
#browser.get(url)
#print(browser.page_source)
#Html_file= open("record.html","w")
#Html_file.write(browser.page_source)
#Html_file.close()

'''
for mois in range(1,1):
    for jour in range(1,10):
        for annee in anneeArray:
            print('annee', annee)
            try:
                if jour < 10 and mois < 10:
                    try:

                        browser = webdriver.Firefox()
                        browser.get('https://www.pmu.fr/turf/0{0}0{1}20{2}/R1/C2/E_QUINTE_PLUS'.format(jour,mois,annee))
                        Html_file= open("0{0}0{1}20{2}.html".format(jour,mois,annee),"w")
                        Html_file.write(browser.page_source)
                        Html_file.close()
                        browser.quit()
                            #print(contenu)
                    except:
                        print("file dosn't exist")
                elif jour < 10 and mois >= 10:
                    try:
                        browser = webdriver.Firefox()
                        browser.get('https://www.pmu.fr/turf/0{0}{1}20{2}/R1/C2/E_QUINTE_PLUS'.format(jour,mois,annee))
                        Html_file= open("0{0}{1}20{2}.html".format(jour,mois,annee),"w")
                        Html_file.write(browser.page_source)
                        Html_file.close()
                        browser.quit()
                    except:
                        print("file dosn't exist")
                        
                elif jour >=  10 and mois < 10:
                    try:
                        browser = webdriver.Firefox()
                        browser.get('https://www.pmu.fr/turf/{0}0{1}20{2}/R1/C2/E_QUINTE_PLUS'.format(jour,mois,annee))
                        Html_file= open("0{0}0{1}20{2}.html".format(jour,mois,annee),"w")
                        Html_file.write(browser.page_source)
                        Html_file.close()
                        browser.quit()
                    except:
                        print("file dosn't exist")
                else:
                    try:
                        browser = webdriver.Firefox()
                        browser.get('https://www.pmu.fr/turf/{0}{1}20{2}/R1/C2/E_QUINTE_PLUS'.format(jour,mois,annee))
                        Html_file= open("0{0}0{1}20{2}.html".format(jour,mois,annee),"w")
                        Html_file.write(browser.page_source)
                        Html_file.close()
                        browser.quit()
                    except:
                        print("file dosn't exist")


'''
'''
import time
from selenium import webdriver
import selenium.webdriver.chrome.service as service


user_path = '/home/giuseppe/Documents/Projets/PythonPMU/chromedriver'


driver = webdriver.Chrome(user_path)  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
'''

'''
service = service.Service(user_path)
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
driver.quit()
'''