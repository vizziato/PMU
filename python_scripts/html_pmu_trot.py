

import re
import codecs
import pandas as jockey
from pandas.io.json import json_normalize

from bs4 import BeautifulSoup



with codecs.open('/home/giuseppe/Documents/Projets/10112016.html', encoding='utf8', errors='replace') as rd:
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
    print(autostart_temp.group())
    autostart_search = autostart_temp.group()
    if autostart_temp is not None:
        autostart_search = autostart_temp.group()
    else:
        autostart_search == None 

except:
  print('no autostart course ')
  autostart_search == None 
  print(autostart_search)

"""
Fin Recherche du type de course , de la distance, nombre de partants et autostart
"""
"""

details partant sexe age driver entraineur recul musique rapport

"""
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
    print(len(id))

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
        
        

        
        quinte =({'Entraineur': entraineur,
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
    print(quinte)

    """"
    result = json_normalize(quinte, 'Driver', 'Entraineur', 'Autostart',
                                            'Deferre', 'Favori',
                                            'Gagnant','Outsider',
                                            'Age','Place',
                                            'Recul','Sexe',
                                            'Distance')
    """

    result = json_normalize(quinte)

    print(result)

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
    df = jockey.DataFrame(result)
    #print(df)

    #print(df['Driver'][0])

    df.set_index('Driver',inplace=True)

    print(df.index.values)

    print(df)
else :
    print(" ce n'est pas du trot attelé'")
#data = df.to_json(orient = 'index')

#print(data)

#print(details.contents[0].string)
#regexp_details= re.search('autostart',details.contents[0].string,re.M|re.I)

#soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
#tag = soup.find_all('div')
#tag = soup.find("div", id="table1")
#tag = soup.find_all("div", class_="starter")

#print(tag)
#t0 = tag.find_all("td", id='0')
#t1 = tag.find_all("td", id='1')

#tag2 = t

##recherche nom drivers

#deferre = tag.find("td", class_="center jersey").parent.find("td", id=True).next_sibling.next_sibling
#print(deferre.img['title'])
#driver = tag.find("td", class_="center jersey").parent.find("td", id=True).next_sibling.next_sibling.next_sibling.next_sibling
#driver = tag.find("td", id="0")
#print(driver)

#sexe = tag.find("td", class_="center jersey").parent.find("td", id=True).next_sibling.next_element
#print(driver.td)
#distance = driver.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
#print(distance.string)
#sexe = driver.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
#print(sexe.string)
#age = sexe.next_sibling.next_sibling
#print(age.string)
#entraineur = age.next_sibling.next_sibling
#print(entraineur.string)
#courses = entraineur.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
#print(courses.string.split())

#regexp_email = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"
#regexp = re.search('(^[0-9])',courses.string,re.M|re.I)
#d=len(courses.string.split())

#l=[]

#for i in courses.string.split():
    #regexp= re.search('(^[0-9])',i,re.M|re.I)
    #try:
        #print(regexp.group())
        #l.append(regexp.group())
    #except:
        #print('0')
        #l.append('0')
   
    #l.append(regexp.group())

    
    #d = d.append(regexp.group())
#if regexp.group(1)==regexp.group(2)==regexp.group(3)
"""
p"rint(l)


if (l[0] == l[1] == l[2]) :
    print('gagnant')
    gagnant = 'OUI'
else:
    print('no gagnant')
    gagnant = 'NON'

if (int(l[0]) <= 5 and int(l[0]) > 0 and int(l[1]) <= 5 and int(l[1]) > 0 and int(l[2]) <= 5 and int(l[2]) > 0 and  int(l[3]) <= 5 and int(l[3]) > 0 and int(l[4]) <= 5 and int(l[4]) > 0):
    print('place ')
    place = 'OUI'
else:
    print('no place')
    place = 'NON'
#print(driver.td.find("td", id="0").next_sibling)
#  
#for sibling in driver.td.next_siblings:
    #print(repr(sibling))
#driver = tag.find("td", class_="center jersey")

#
#id = tag.find_all("td", id=True)
#print(len(id))

#driver =tag.find_all("td", class_="center jersey")

#for r in range(len(id)):
    #print(driver[r].parent.find("td", id=True).next_sibling.next_sibling.next_sibling.next_sibling.string)
#print(tag2)

#print(tag2.attrs)

#print(tag2.string)
#print(tag2['id'])
#print(tag2.name)
#print(tag2)
#print(tag3)
#regexp = re.search("IRE",tag2.string,re.M|re.I)
#print(regexp.group())
# <class 'bs4.element.Tag'>
    
#for p in tag.find_all("td"):
 #   print(p)

#regexp = re.search("(<body>|</body>)",contenu,re.M|re.I)
#regexp = r"head"
#regexp = re.search('body(\S+)',contenu,re.M|re.I)

#print(regexp.group())
#contenu_filter = re.match(regexp, contenu)

#print(contenu_filter)

"""