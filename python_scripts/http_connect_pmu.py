

import httplib2
import re
import codecs

from bs4 import BeautifulSoup



#print(reponse['content-type'])

#regexp_utf8 = re.search('charset=(\S+)',reponse['content-type'],re.M|re.I)

#print(regexp_utf8.group(1))
#contenu = contenu.decode(regexp_utf8.group(1))
#print(contenu)

#with codecs.open('/home/giuseppe/Documents/Projets/PythonPMU/14112016.html','r','utf8') as contenu:
    #rd = contenu.reader()
#with open("/home/giuseppe/Documents/Projets/PythonPMU/14112016.html", "r") as fichier:
	#contenu = fichier.read()


#print(contenu)
#s=codecs.open(ton_fichier, 'r','utf-8')
#print 'fichier lu = ',s.read()

#soup = BeautifulSoup(contenu,'html.parser')

#print(soup.attrs.get(1))
    
#for p in soup.find_all('body'):
    #print(p)



h = httplib2.Http(".cache")

#print(h)

#reponse,contenu = h.request("https://www.pmu.fr/turf/14112016/R1/C2","GET")
#reponse,contenu = h.request("http://www.tierce-magazine.com/accueil/les-courses-avc/pid111-partants.html?race_id=1002743","GET")

#reponse,contenu = h.request('file:///home/giuseppe/Documents/Projets/Turf,%20Courses%20Hippiques,%20Courses%20en%20direct%20-%20PMU_15112016.html',"GET")


with codecs.open('/home/giuseppe/Documents/Projets/15112016.html', encoding='utf8', errors='replace') as rd:
    contenu = rd.read()
print(contenu)

#print(reponse['content-type'])

#regexp_utf8 = re.search('charset=(\S+)',reponse['content-type'],re.M|re.I)

#print(regexp_utf8.group(1))
#contenu = contenu.decode(regexp_utf8.group(1))
print(contenu)

soup = BeautifulSoup(contenu,'lxml')
#print(soup.prettify())

soup = BeautifulSoup(contenu,'lxml')

hippodrome = soup.h1.string
#print(hippodrome)
regexp_hippodrome= re.search(': ([a-z0-9._-])+',hippodrome,re.M|re.I)
#hippodrome = soup.find("div", class_="entete")
print(regexp_hippodrome.group())


details = soup.find("div", class_="detail")
#print(details)
print(details.contents[0].string)
regexp_details= re.search('autostart',details.contents[0].string,re.M|re.I)
print(regexp_details.group())
if regexp_details.group() is not None:
    autostart = 'OUI'
else:
    autostart = 'NON'
print(autostart)
#soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
#tag = soup.find_all('div')
tag = soup.find("div", id="table1")
#tag = soup.find_all("div", class_="starter")

#print(tag)
#t0 = tag.find_all("td", id='0')
#t1 = tag.find_all("td", id='1')

#tag2 = tag.find("td", id=True)


##recherche nom drivers

deferre = tag.find("td", class_="center jersey").parent.find("td", id=True).next_sibling.next_sibling
print(deferre.img['title'])
driver = tag.find("td", class_="center jersey").parent.find("td", id=True).next_sibling.next_sibling.next_sibling.next_sibling
#driver = tag.find("td", id="0")
print(driver)

#sexe = tag.find("td", class_="center jersey").parent.find("td", id=True).next_sibling.next_element
#print(driver.td)
distance = driver.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
print(distance.string)
sexe = driver.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
print(sexe.string)
age = sexe.next_sibling.next_sibling
print(age.string)
entraineur = age.next_sibling.next_sibling
print(entraineur.string)
courses = entraineur.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
print(courses.string.split())

#regexp_email = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"
#regexp = re.search('(^[0-9])',courses.string,re.M|re.I)
d=len(courses.string.split())

l=[]

for i in courses.string.split():
    regexp= re.search('(^[0-9])',i,re.M|re.I)
    try:
        #print(regexp.group())
        l.append(regexp.group())
    except:
        #print('0')
        l.append('0')
   
    #l.append(regexp.group())

    
    #d = d.append(regexp.group())
#if regexp.group(1)==regexp.group(2)==regexp.group(3)

print(l)


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

