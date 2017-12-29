import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#

#url = "http://www.letrot.com/stats/fiche-course/2017-02-02/7500/1/partants/liste#sub_sub_menu_course"

url_directory = "C:/Users/Giuseppe/Documents/Python/files/files_html_recorded_letrot_fr/"
anneeArray = [7,8,9,10,11,12,13,14,15,16,17]
courseArray = [1,2,3,4,5,6,7,8,9]
#courseArray = [1]
#log_but2 = '//*[@id="main"]/div/div[10]/div[1]/div[3]/section/div/div[1]/ul/li[2]'

for mois in range(12,13):
    for jour in range(10,32):
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
                            if  annee < 10: 
                                browser.get('http://www.letrot.com/stats/fiche-course/200{0}-0{1}-0{2}/7500/{3}/partants/liste#sub_sub_menu_course'.format(annee,mois,jour,course))
                            else:
                                browser.get('http://www.letrot.com/stats/fiche-course/20{0}-0{1}-0{2}/7500/{3}/partants/liste#sub_sub_menu_course'.format(annee,mois,jour,course))
                            #element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, log_but2)))
                            #element.click()
                            time.sleep(1) # Let the user actually see something!
                            if  annee < 10: 
                                Html_file= open(url_directory+"letrot_0{0}0{1}200{2}C{3}.html".format(jour,mois,annee,course),"w")
                                Html_file.write(browser.page_source)
                                Html_file.close()
                            else:
                                Html_file= open(url_directory+"letrot_0{0}0{1}20{2}C{3}.html".format(jour,mois,annee,course),"w")
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
                            if  annee < 10: 
                                browser.get('http://www.letrot.com/stats/fiche-course/200{0}-{1}-0{2}/7500/{3}/partants/liste#sub_sub_menu_course'.format(annee,mois,jour,course))
                            else:
                                browser.get('http://www.letrot.com/stats/fiche-course/20{0}-{1}-0{2}/7500/{3}/partants/liste#sub_sub_menu_course'.format(annee,mois,jour,course))
                            #element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, log_but2)))
                            #element.click()
                            
                            time.sleep(1) # Let the user actually see something!

                            if  annee < 10: 
                                Html_file= open(url_directory+"letrot_0{0}{1}200{2}C{3}.html".format(jour,mois,annee,course),"w")
                                Html_file.write(browser.page_source)
                                Html_file.close()
                            else:
                                Html_file= open(url_directory+"letrot_0{0}{1}20{2}C{3}.html".format(jour,mois,annee,course),"w")
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
                            if  annee < 10: 
                                browser.get('http://www.letrot.com/stats/fiche-course/200{0}-0{1}-{2}/7500/{3}/partants/liste#sub_sub_menu_course'.format(annee,mois,jour,course))
                            else:
                                browser.get('http://www.letrot.com/stats/fiche-course/20{0}-0{1}-{2}/7500/{3}/partants/liste#sub_sub_menu_course'.format(annee,mois,jour,course))
                            #element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, log_but2)))
                           # element.click()

                            time.sleep(1) # Let the user actually see something!

                            if  annee < 10: 
                                Html_file= open(url_directory+"letrot_{0}0{1}200{2}C{3}.html".format(jour,mois,annee,course),"w")
                                Html_file.write(browser.page_source)
                                Html_file.close()
                            else:
                                Html_file= open(url_directory+"letrot_{0}0{1}20{2}C{3}.html".format(jour,mois,annee,course),"w")
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
                            if  annee < 10: 
                                browser.get('http://www.letrot.com/stats/fiche-course/200{0}-{1}-{2}/7500/{3}/partants/liste#sub_sub_menu_course'.format(annee,mois,jour,course))
                            else:
                                browser.get('http://www.letrot.com/stats/fiche-course/20{0}-{1}-{2}/7500/{3}/partants/liste#sub_sub_menu_course'.format(annee,mois,jour,course))
                            
                            time.sleep(1) # Let the user actually see something!

                            if  annee < 10: 
                                Html_file= open(url_directory+"letrot_{0}{1}200{2}C{3}.html".format(jour,mois,annee,course),"w")
                                Html_file.write(browser.page_source)
                                Html_file.close()
                            else:
                                Html_file= open(url_directory+"letrot_{0}{1}20{2}C{3}.html".format(jour,mois,annee,course),"w")
                                Html_file.write(browser.page_source)
                                Html_file.close()

                            browser.quit()
                        except:
                            print("file dosn't exist")
                            Html_file.close()
                            browser.quit()


                except:
                    pass
