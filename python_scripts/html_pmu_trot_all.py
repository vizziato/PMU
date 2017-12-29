

import re
import codecs
import pandas as jockey
from pandas.io.json import json_normalize

from bs4 import BeautifulSoup


mareponse=[]

for i in range(7,15):
   

    if i < 10:
        with codecs.open('/home/giuseppe/Documents/Projets/PythonPMU/files_html_uploader/0{0}112016.html'.format(i), encoding='utf8', errors='replace') as rd:
            contenu = rd.read()
    else:
        with codecs.open('/home/giuseppe/Documents/Projets/PythonPMU/files_html_uploader/{0}112016.html'.format(i), encoding='utf8', errors='replace') as rd:
            contenu = rd.read()

        
    """
    Parser document .html
    """
    soup = BeautifulSoup(contenu,'lxml')


    """
    Recherche de l'hippodrome et de la date'
    """

    titre =  soup.find("h2", class_="course-title")
    #print(titre)
    hippodrome = titre.b.next_sibling.next_sibling
    #print(hippodrome)
    regexp_hippodrome= re.search('([a-z0-9._ ])+',hippodrome.string,re.M|re.I)
    #hippodrome = soup.find("div", class_="entete")
    #print(regexp_hippodrome.group())
    hippodrome =regexp_hippodrome.group()
    print(hippodrome)
    date = titre.find(class_="date").text
    print(date)
    """
    Fin hippodrome et date

    """

    """
    Recherche du type de course , de la distance, nombre de partants et autostart
    """

    tag1 =soup.find("div", class_="course-info").find(id="conditions").p
    #print(tag1)
    type_course_temp = tag1.strong
    #print(type_course_temp)
    regexp_type_course= re.search('([a-zé0-9._ ])+',type_course_temp.string,re.M|re.I)
    #print(regexp_type_course.group())
    type_course = regexp_type_course.group()
    distance_temp = re.search('([0-9._ ])+',tag1.strong.next_element.next_element.string,re.M|re.I)
    #print(distance.group())
    distance = int(distance_temp.group())
    print(type_course)
    print(distance)

    nb_partants = re.search('([0-9 ])+ partant',tag1.strong.next_element.next_element.string,re.M|re.I)
    #print(nb_partants.group())
    autostart_search = None
    try:
        
        autostart_temp = re.search('Autostart',tag1.strong.next_element.next_element.string,re.M|re.I)
        #print(autostart_temp.group())
        autostart_search = autostart_temp.group()
        if autostart_temp is not None:
            autostart_search = autostart_temp.group()
        else:
            autostart_search == None 

    except:
        print('no autostart course ')
        autostart_search == None 
        #print(autostart_search)

    """
    Fin Recherche du type de course , de la distance, nombre de partants et autostart
    """
    """

    details partant sexe age driver entraineur recul musique rapport

    """
    print('i:', i)
    #mareponse.insert(i,entraineur)

    if re.search('Attelé',type_course,re.M|re.I):
        details = soup.find_all("tr", class_="ligne-participant", limit=5) or soup.find("tr", class_="ligne-participant favorite")
        #print(details)
        
        """"
        for tag in details:
            try:
                details = tag.find("td", class_="txtC").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
                print(details2)
            except:
                print('error')
        """
        id = soup.find_all("tr", class_="ligne-participant", limit=5) or soup.find("tr", class_="ligne-participant favorite")
        #print(len(id))

        sexe,age,driver,deferre,recul,gagnant,place,favori,outsider,entraineur,autostart,longueur= [],[],[],[],[],[],[],[],[],[],[],[]

        #longueur = str(distance_temp.group()) 
        #print(longueur)
       
        for r in range(len(id)):
        #for r in range(1):   
            if autostart_search is not None:
                autostart.append('OUI')
            else:
                autostart.append('NON')

            longueur.insert(r,distance_temp.group())

            sexe.append(details[r].find("td", class_="txtC").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text())
            age.append(details[r].find("td", class_="txtC").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                                                                        next_sibling.next_sibling.get_text())
            driver.append(details[r].find("td", class_="txtC").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                                                                            next_sibling.next_sibling.next_sibling.next_sibling.get_text())
            deferre_temp= details[r].find("b")
            if re.search('deferre',''.join(deferre_temp['class']),re.M|re.I):
                deferre.append('OUI')
                #print('ok',r)
            else:
                deferre.append('NON')
                #print('no ok',r)

            temp =details[r].find("td", class_="txtC").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
            driver_temp = temp.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
            #print(driver_temp)                                              

            entraineur_temp = temp.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
            #print(entraineur_temp)                                                              
            
            if re.search(entraineur_temp,driver_temp,re.M|re.I):
                #print('le driver entraine aussi le cheval')
                entraineur.append('OUI')
                #entraineur='OUI'
               

            else:
                #print("l'entraineur n'entraine pas ce cheval")
                entraineur.append('NON')
                #entraineur='NON'

            
            df1 = jockey.DataFrame({'Entraineur': [entraineur]},
                        index = [driver])


            recul_temp= temp.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
            #print(int(recul_temp))


            if int(recul_temp) == distance:
                #print('le cheval ne part pas avec du recul')
                recul.append('NON')

            else:
                #print("le cheval part avec du recul")
                recul.append('OUI')

            musique_temp = temp.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
            #print(musique_temp)

            l=[]

            for i in musique_temp:
                regexp= re.search('(^[0-9D])+',i,re.M|re.I)
                try:
                    if(regexp.group() != 'D'):
                        l.append(regexp.group())
                    else:
                        l.append('0')
                except:
                    print('0')
            # print(l)

            if len(l) >= 5:
                if (int(l[0]) == int(l[1]) == int(l[2]) == 1) :
                    #print('gagnant')
                    gagnant.append('OUI')
                else:
                    #print('no gagnant')
                    gagnant.append('NON')

                if (int(l[0]) <= 5 and int(l[0]) > 0 and int(l[1]) <= 5 and int(l[1]) > 0 and int(l[2]) <= 5 and int(l[2]) > 0 and  int(l[3]) <= 5 and int(l[3]) > 0 and int(l[4]) <= 5 and int(l[4]) > 0):
                    #print('place ')
                    place.append('OUI')
                else:
                    #print('no place')
                    place.append('NON')
            else:
                gagnant.append('NON')
                place.append('NON')

            cote_temp = details[r].find("td", class_="txtC rapport-probable last").get_text()
            #print(cote_temp.replace(',','.'))

            #regexp_cote= re.sub('(^[0-9D])+',cote,re.M|re.I)
            cote = cote_temp.replace(',','.')

            if  float(cote) <= 10.0:
                    favori.append('OUI')
                    outsider.append('NON')
                    #print('favori')
            elif float(cote) >= 50.0:
                    favori.append('NON')
                    outsider.append('OUI')
                    #print('ousider')
            else:
                    favori.append('NON')
                    outsider.append('NON')
                    #print('ny outsider ny favori')
            
            
                    """"
        quinte1 =({'Entraineur': entraineur,
                            'Autostart':  autostart,
                            'Deferre':   deferre,
                            'Favori': favori, 
                            'Gagnant': gagnant,
                            'Outsider': outsider,
                            'Age': age,
                            'Place': place,
                            'Recul': recul,
                            'Sexe': sexe,
                            'Distance': longueur,
                            'Driver' : driver})
        print('quinte1 :' ,quinte1)
           """ 
         
      
       
            
        #print(deferre_temp['class'])
        #print(deferre_temp[0])
        print('sexe: ',sexe)
        print('age :',age)
        print('driver :',driver)
        print('deferre :',deferre)
        print('entraineur :',entraineur)
        print('recul : ',recul)
        print('gagnant ',gagnant)
        print('place :',place)
        print('favori ',favori)
        print('outsider :',outsider)
        print('distance :', longueur)

       # mareponse.insert(int(i),entraineur)
        
        #print(mareponse)
        print('i:', i)

      
        """"
        result = json_normalize(quinte, 'Driver', 'Entraineur', 'Autostart',
                                                'Deferre', 'Favori',
                                                'Gagnant','Outsider',
                                                'Age','Place',
                                                'Recul','Sexe',
                                                'Distance')
        """

        #result = json_normalize(quinte)

        #print(result)

        """"
        df = jockey.DataFrame({'Entraineur': [entraineur],
                                'Autostart':  [autostart],
                                'Deferre':   [deferre],
                                'Favori': [favori], 
                                'Gagnant': [gagnant],
                                'Outsider': [outsider],
                                'Age': [age],
                                'Place': [place],
                                'Recul': [recul],
                                'Sexe': [sexe],
                                'Distance': [distance]},
                                index = [driver])
        #print(df)
         
        """
        """
        if i == 15:
            df = jockey.DataFrame(result)
            #print(df)

            #print(df['Driver'][0])

            df.set_index('Driver',inplace=True)

            print(df.index.values)

            print(df)
        else:
            print('test')
            """
            
    else :
        print(" ce n'est pas du trot attelé'")
