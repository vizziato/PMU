import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#url = 'https://github.com'
#url ='https://www.bcv.ch/'
#url = 'https://www.pmu.fr/turf'

#url = "https://www.pmu.fr/turf/28042017/R1/C2/E_QUINTE_PLUS"

url_directory = "C:/Users/Giuseppe/Documents/Python/PythonPMU/files_html_recorded/"
anneeArray = [17]
courseArray = [1,2,3,4,5,6,7,8,9]
#courseArray = [1]
log_but2 = '//*[@id="main"]/div/div[10]/div[1]/div[3]/section/div/div[1]/ul/li[2]'

for mois in range(1,13):
    for jour in range(1,32):
        for annee in anneeArray:
            for course in courseArray:
                print('jour', jour)
                print('mois', mois)
                print('annee', annee)
                print('course', course)       
                try:
                    if jour < 10 and mois < 10:
                        try:

                            browser = webdriver.Firefox(executable_path=r'C:\Users\Giuseppe\Documents\Python\geckodriver-v0.16.1-win64\geckodriver.exe')
                            browser.get('https://www.pmu.fr/turf/0{0}0{1}20{2}/R1/C{3}'.format(jour,mois,annee,course))
                            #log_but2 = '//*[@id="main"]/div/div[8]/div[1]/div[3]/section/div/div[1]/ul/li[2]'
                            #//*[@id="main"]/div/div[8]/div[1]/div[3]/section/div/div[1]/ul/li[2]
                            #sel = '#main>div>div:nth-child(8)>div.course-particip>div.course-participants-region>section>div>div.participants-nav-region>ul>li.partants.actif.visible.selected'
                            #sel = 'ul.tabs>li.partants.actif.visible.selected'
                            #print(browser.find_element_by_xpath(log_but2).click())
                            #print(browser.find_element_by_css_selector(sel).click())
                            #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul#ulBirthYear a[data-value='2002']")))
                            #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.tabs li[data-tag='tag:clic:tableauPartants']")))
                            element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, log_but2)))
                            element.click()
                            time.sleep(1) # Let the user actually see something!

                            Html_file= open(url_directory+"0{0}0{1}20{2}C{3}.html".format(jour,mois,annee,course),"w")
                            Html_file.write(browser.page_source)
                            Html_file.close()


                            browser.quit()
                        except:
                            print("file dosn't exist")
                            Html_file.close()
                            browser.quit()
                    elif jour < 10 and mois >= 10:
                        try:
                            browser = webdriver.Firefox(executable_path=r'C:\Users\Giuseppe\Documents\Python\geckodriver-v0.16.1-win64\geckodriver.exe')
                            browser.get('https://www.pmu.fr/turf/0{0}{1}20{2}/R1/C{3}'.format(jour,mois,annee,course))
                            element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, log_but2)))
                            element.click()
                            
                            time.sleep(1) # Let the user actually see something!

                            Html_file= open(url_directory+"0{0}{1}20{2}C{3}.html".format(jour,mois,annee,course),"w")
                            Html_file.write(browser.page_source)
                            Html_file.close()

                            browser.quit()

                        except:
                            print("file dosn't exist")
                            Html_file.close()
                            browser.quit()                            
                    elif jour >=  10 and mois < 10:
                        try:
                            browser = webdriver.Firefox(executable_path=r'C:\Users\Giuseppe\Documents\Python\geckodriver-v0.16.1-win64\geckodriver.exe')
                            browser.get('https://www.pmu.fr/turf/{0}0{1}20{2}/R1/C{3}'.format(jour,mois,annee,course))

                            element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, log_but2)))
                            element.click()

                            time.sleep(1) # Let the user actually see something!

                            Html_file= open(url_directory+"{0}0{1}20{2}C{3}.html".format(jour,mois,annee,course),"w")
                            Html_file.write(browser.page_source)
                            Html_file.close()

                            browser.quit()
                        except:
                            print("file dosn't exist")
                            Html_file.close()
                            browser.quit()
                    else:
                        try:
                            browser = webdriver.Firefox(executable_path=r'C:\Users\Giuseppe\Documents\Python\geckodriver-v0.16.1-win64\geckodriver.exe')
                            browser.get('https://www.pmu.fr/turf/{0}{1}20{2}/R1/C{3}'.format(jour,mois,annee,course))

                            element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, log_but2)))
                            element.click()
                            
                            time.sleep(1) # Let the user actually see something!

                            Html_file= open(url_directory+"{0}{1}20{2}C{3}.html".format(jour,mois,annee,course),"w")
                            Html_file.write(browser.page_source)
                            Html_file.close()

                            browser.quit()
                        except:
                            print("file dosn't exist")
                            Html_file.close()
                            browser.quit()


                except:
                    pass
