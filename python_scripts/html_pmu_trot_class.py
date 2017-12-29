import re

from bs4 import BeautifulSoup

class QuinteAttele:


    def __init__(self,contenu,type_course, autostart_search, distance_temp, nb_partants):
        
        self.contenu = contenu
        self.type_course = type_course
        self.autostart_search =  autostart_search
        self.distance_temp =  distance_temp
        self.nb_partants =  nb_partants
        """
        Parser document .html
        """
        soup = BeautifulSoup(self.contenu,'lxml')

        if re.search('Attel',self.type_course,re.M|re.I):
            if soup.find_all("tr", class_="ligne-participant", limit=5):
                details = soup.find_all("tr", class_="ligne-participant", limit=5) or soup.find("tr", class_="ligne-participant favorite")
                id = soup.find_all("tr", class_="ligne-participant", limit=5) or soup.find_all("tr", class_="participants-tbody-tr", limit=5) or soup.find("tr", class_="ligne-participant favorite")
                #print(len(id))
                #print('atteleé old')
                numero = 0
                #print('details:::', details)

            else:
                details =  soup.find_all("tr", class_="participants-tbody-tr")
                #print(details[1])
                numero= soup.find_all("span", class_="participants-num")
                #print('numero dans Class QuinteAttele: ', numero)
                id = soup.find_all("tr", class_="participants-tbody-tr") 
                #print(len(id))
                #print('numero 1:', numero[1])
                #id = soup.find_all("tr", class_="ligne-participant",limit=5) or soup.find_all("tr", class_="participants-tbody-tr",limit=5) or soup.find("tr", class_="ligne-participant favorite")
                #print('id 1:', id[1])
                arriveArray = soup.find("div", class_="course-participants").find("ul", class_="participants-arrivee-list-chevaux participants-arrivee-list-chevaux--definitive").find_all("li")
                #print('arrive dans Class QuinteAttele: ', arriveArray)
                #arrive.append(arriveArray[r].text
               # print('arrayerrive:',len(arriveArray))
                arrive = [int(elem.text) for elem in arriveArray]
                #print('arrive dans Class QuinteAttele: ', arrive)
                #print('regexp id:::::',id[1].find("span", class_="participants-num").text)
                choice = [int(elem.find("span", class_="participants-num").text) in arrive for elem in id]
                #print(choice)

            sexe,age,driver,deferre,recul,gagnant,place,favori,outsider,entraineur,autostart,longueur= [],[],[],[],[],[],[],[],[],[],[],[]

           
          
            #print('numero:', numero)
                   
    
            for r in range(len(id)):
                if numero == 0:
                    #print('numero == false')
                    #print('y::',r)

                    if self.autostart_search is not None:
                        autostart.append('OUI')
                    else:
                        autostart.append('NON')
                    
                    #longueur.insert(r,distance_temp.group())
                    longueur.insert(r,distance_temp)
                    #numero.append(numero_all[r].find("span", class_="participants-num"))
                    #print('numero dans Class QuinteAttele: ', numero)
                    
                    sexe.append(details[r].find("td", class_="txtC").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text())
                    age.append(details[r].find("td", class_="txtC").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                                                                                next_sibling.next_sibling.get_text())
                    driver.append(details[r].find("td", class_="txtC").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                                                                                    next_sibling.next_sibling.next_sibling.next_sibling.get_text())
                    deferre_temp= details[r].find("b")
                    
                    if re.search('deferre',''.join(deferre_temp['class']),re.M|re.I):
                        deferre.append('OUI')
                    else:
                        deferre.append('NON')

                    temp =details[r].find("td", class_="txtC").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
                    driver_temp = temp.next_sibling.next_sibling.next_sibling.next_sibling.get_text()

                    entraineur_temp = temp.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
                    if re.search(entraineur_temp,driver_temp,re.M|re.I):
                        entraineur.append('OUI')
                    

                    else:
                        entraineur.append('NON')

            

                    recul_temp= temp.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
                    #print(int(recul_temp))


                    #if int(recul_temp) == int(distance_temp.group()):
                    if int(recul_temp) == int(distance_temp):
                        recul.append('NON')

                    else:
                        recul.append('OUI')

                    musique_temp = temp.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()

                    l=[]

                    for i in musique_temp:
                        regexp= re.search('(^[0-9D])+',i,re.M|re.I)
                        try:
                            if(regexp.group() != 'D'):
                                l.append(regexp.group())
                            else:
                                l.append('0')
                        except:
                            #print('0')
                            pass

                    if len(l) >= 5:
                        if (int(l[0]) == int(l[1]) == int(l[2]) == 1) :
                            gagnant.append('OUI')
                        else:
                            gagnant.append('NON')

                        if (int(l[0]) <= 5 and int(l[0]) > 0 and int(l[1]) <= 5 and int(l[1]) > 0 and int(l[2]) <= 5 and int(l[2]) > 0 and  int(l[3]) <= 5 and int(l[3]) > 0 and int(l[4]) <= 5 and int(l[4]) > 0):
                            place.append('OUI')
                        else:
                            place.append('NON')
                    else:
                        gagnant.append('NON')
                        place.append('NON')

                    cote_temp = details[r].find("td", class_="txtC rapport-probable last").get_text()

                    cote = cote_temp.replace(',','.')

                    if  float(cote) <= 5.0:
                            favori.append('OUI')
                            outsider.append('NON')
                            #print('favori')
                    elif float(cote) >= 15.0:
                            favori.append('NON')
                            outsider.append('OUI')
                            #print('ousider')
                    else:
                            favori.append('NON')
                            outsider.append('NON')
                            #print('ny outsider ny favori')

           
            
                else:
                    #print('else')
                    #print('r', r)
                    #print('choice[r]',choice[r])
                    #print('self.autostart_search', self.autostart_search)
                    if choice[r] == True and self.nb_partants > 15:
                        if self.autostart_search is not None:
                            autostart.append('OUI')
                            #print('autostart',autostart)

                            if (int(numero[r].text) > 9):
                                recul.append('OUI')
                            else: 
                                recul.append('NON')
                        else:
                            autostart.append('NON')

                            if int(details[r].find("td", class_="participants-tbody-td gains").next_sibling.next_sibling.text) == int(self.distance_temp.group()):
                                recul.append('NON')
                            else:
                                recul.append('OUI')
                        
                        #print('autostart',autostart)
                        #print('autostart',recul)

                        #longueur.insert(r,distance_temp.group())
                        #print('distance,',distance_temp.group())
                        if int(distance_temp.group()) > 2700:
                            longueur.append('LONG')
                        else:
                            longueur.append('COURT')
                        sexe.append(re.search('([a-zA-Z])',details[r].find("td", class_="participants-tbody-td txtC").get_text(),re.M|re.I).group())
                        #print(sexe)
                        
                         #age.append(re.search('([0-9])',details[r].find("td", class_="participants-tbody-td txtC").get_text(),re.M|re.I).group())
                        if re.search('([0-9])',details[r].find("td", class_="participants-tbody-td txtC").get_text(),re.M|re.I):
                            #print('age::',re.search('([0-9])',details[r].find("td", class_="participants-tbody-td txtC").get_text(),re.M|re.I).group())
                            if int(re.search('([0-9])+',details[r].find("td", class_="participants-tbody-td txtC").get_text(),re.M|re.I).group()) >= 3 and int(re.search('([0-9])+',details[r].find("td", class_="participants-tbody-td txtC").get_text(),re.M|re.I).group()) <=5:
                                age.append('JEUNE')
                            elif int(re.search('([0-9])+',details[r].find("td", class_="participants-tbody-td txtC").get_text(),re.M|re.I).group()) >= 6 and int(re.search('([0-9])+',details[r].find("td", class_="participants-tbody-td txtC").get_text(),re.M|re.I).group()) <= 9:
                                age.append('MEDIUM')
                            else:
                                age.append('VIEUX')
                        
                        if (details[r].find("div", class_="participants-details").li):
                            deferre.append('OUI')
                        else:
                            deferre.append('NON')
                            
                        #print('jockey class QuinteAttele',details[r].find("span", class_="participants-jokey").text)
                        #print('entraineur class QuinteAttele',details[r].find("span", class_="participants-entraineur").text)

                        # if re.search(entraineur_temp,driver_temp,re.M|re.I):
                       # entraineur.append('OUI')
                        # else:
                        #entraineur.append('NON')

                        if re.search(details[r].find("span", class_="participants-jokey").text,details[r].find("span", class_="participants-entraineur").text,re.M|re.I):
                            entraineur.append('OUI')
                        else:
                            entraineur.append('NON')
                
                        #driver.append(details[r].find("span", class_="participants-jokey").text)

                        

                        if re.search('bazi',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('BAZIRE')
                        elif re.search('nivar',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('NIVARD')
                        elif re.search('leve',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('LEVESQUE')
                            #driver.append('AUTRES')

                        elif re.search('verva',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('VERVA')
                            #driver.append('AUTRES')

                        elif re.search('dreux',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('DREUX')
                            #driver.append('AUTRES')
                        elif re.search('raffin',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('RAFFIN')
                        elif re.search('big',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('BIGEON')
                            #driver.append('AUTRES')

                        elif re.search('abriva',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('ABRIVARD')
                        elif re.search('vercru',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('VERCRUYSSE')
                        elif re.search('piton',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('PITON')
                            #driver.append('AUTRES')
                        elif re.search('ouvrie',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('OUVRIE')
                        elif re.search('mary',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('MARY')
                            #driver.append('AUTRES')

                        elif re.search('locqu',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('LOCQUENAUX')
                            #driver.append('AUTRES')

                        elif re.search('ernau',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('ERNAULT')
                            #driver.append('AUTRES')

                        elif re.search('thom',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('THOMAIN')
                        elif re.search('rouss',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('ROUSSEL')
                            #driver.append('AUTRES')

                        elif re.search('mart',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('MARTENS')
                            #driver.append('AUTRES')
  
                        elif re.search('bonne',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('BONNE') 
                            #driver.append('AUTRES')

                        elif re.search('alla',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('ALLARD') 
                            #driver.append('AUTRES')

                        elif re.search('guelpa',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('GUELPA') 
                           # driver.append('AUTRES')

                        elif re.search('dub',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('DUBOIS')
                            #driver.append('AUTRES')

                        elif re.search('deri',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('DERIEUX')  
                            #driver.append('AUTRES')
                        elif re.search('laura',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('LAURANT')  
                            #driver.append('AUTRES')
                        elif re.search('baud',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('BAUDE')  
                            #driver.append('AUTRES')
                        elif re.search('barr',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('BARRIER')  
                            #driver.append('AUTRES')
                        elif re.search('viel',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('VIEL')  
                            #driver.append('AUTRES')
                        elif re.search('goop',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('GOOP')  
                            #driver.append('AUTRES')
                        elif re.search('daug',details[r].find("span", class_="participants-jokey").text,re.M|re.I):
                            driver.append('DAUREGARD')  
                            #driver.append('AUTRES')
                        else:
                            driver.append('')
                        # print(details[r].find("td", class_="participants-tbody-td gains").next_sibling.next_sibling.text)
                        #print(self.distance_temp)
                        #print('driver',driver)
                        #print('numero:', numero[r].text)
                        '''
                        if (self.autostart_search is not None) and (numero[r].text >= 9):
                            recul.append('OUI')
                        elif (self.autostart_search is not None) and (numero[r].text < 9):
                            recul.append('NON')
                        elif int(details[r].find("td", class_="participants-tbody-td gains").next_sibling.next_sibling.text) == int(self.distance_temp.group()):
                            recul.append('NON')
                        else:
                            recul.append('OUI')
                       '''

                        musique_temp = details[r].find("td", class_="participants-tbody-td gains").next_sibling.next_sibling.next_sibling.next_sibling.get_text()
                        #print('musique_temp', musique_temp)
                        #regexp= re.search("([()])([0-9])+([)])",musique_temp,re.M|re.I)
                        regexp= re.sub("([()])([0-9])+([)])","",musique_temp)
                        #print('regexp',regexp)
                        


                        musique,l=[],[]

                        for i in regexp:
                            regexp_temp= re.search('(^[0-9D])+',i,re.M|re.I)

                            try:
                                if(regexp_temp.group() != 'D'):
                                    musique.append(regexp_temp.group())
                                else:
                                    musique.append('0')

                            except:
                                #print('0')
                                pass
                        #print('musique:', musique)

                        #Modifier code pour trouver une fois gagnant dans trois premières course et placé 3 priere courses
                        '''
                        if len(musique) >= 5:
                            if (int(musique[0]) == int(musique[1]) == int(musique[2]) == 1) :
                                gagnant.append('OUI')
                            else:
                                gagnant.append('NON')

                            if (int(musique[0]) <= 5 and int(musique[0]) > 0 and int(musique[1]) <= 5 and int(musique[1]) > 0 and int(musique[2]) <= 5 and int(musique[2]) > 0 and  int(musique[3]) <= 5 and int(musique[3]) > 0 and int(musique[4]) <= 5 and int(musique[4]) > 0):
                                place.append('OUI')
                            else:
                                place.append('NON')
                        else:
                            gagnant.append('NON')
                            place.append('NON')
                        '''
                        #Cherche si ganagant une des 3 courses
                        if len(musique) >= 5:
                            #if (int(musique[0]) == 1 or int(musique[1]) == 1 or int(musique[2]) == 1) :
                            if (int(musique[0]) == 1 or int(musique[1]) == 1 or int(musique[2]) == 1 or int(musique[3]) == 1 or int(musique[4]) == 1) :
                            #if ( (int(musique[0]) == int(musique[1]) == int(musique[2]) == 1) or (int(musique[1]) == int(musique[2]) == int(musique[3]) == 1)  or (int(musique[2]) == int(musique[3]) == int(musique[4]) == 1) or (int(musique[3]) == int(musique[4]) == int(musique[5]) == 1)) :
                                gagnant.append('OUI')
                                #print('gagnat')
                            else:
                                gagnant.append('NON')
                            #Cherche si placé dans 5 premieres course
                            #if (int(musique[0]) <= 5 and int(musique[0]) > 0 or int(musique[1]) <= 5 and int(musique[1]) > 0 and int(musique[2]) <= 5 and int(musique[2]) > 0):
                            #if (int(musique[0]) <= 3 and int(musique[0]) > 0 or int(musique[1]) <= 5 and int(musique[1]) > 0 or int(musique[2]) <= 5 and int(musique[2]) > 0 or  int(musique[3]) <= 3 and int(musique[3]) > 0 or int(musique[4]) <= 5 and int(musique[4]) > 0):
                            if (int(musique[0]) <= 5 and int(musique[0]) > 0 and int(musique[1]) <= 5 and int(musique[1]) > 0 and int(musique[2]) <= 5 and int(musique[2]) > 0 and  int(musique[3]) <= 5 and int(musique[3]) > 0 and int(musique[4]) <= 5 and int(musique[4]) > 0):
                                place.append('OUI')
                            else:
                                place.append('NON')
                        else:
                            gagnant.append('')
                            place.append('')
                       
                        #print('gagnant',gagnant)


                        #recherche de la Cote finale
                        cote_temp = details[r].find("td", class_="participants-tbody-td participants-tbody-td--rapport-probable-last").get_text()
                        #print(re.search('([0-9,.])+',details[r].find("td", class_="participants-tbody-td participants-tbody-td--rapport-probable-last").get_text(),re.M|re.I))

                        if (re.search('([0-9,.])+',details[r].find("td", class_="participants-tbody-td participants-tbody-td--rapport-probable-last").get_text(),re.M|re.I)) is not None:
                            cote = cote_temp.replace(',','.')
                            #print('cote',cote)

                            #Calcul du favori ou Outsider
                            if  float(cote) <= 10.0:
                                    favori.append('OUI')
                                    outsider.append('NON')
                                    #print('favori')
                            elif float(cote) >= 28.0:
                                    favori.append('NON')
                                    outsider.append('OUI')
                                    #print('ousider')
                            else:
                                    favori.append('NON')
                                    outsider.append('NON')
                                    #print('ny outsider ny favori')
                        else:
                            favori.append(' ')
                            outsider.append(' ')

                
                                       
                        
            

                    



            self.quinte =({ 'Entraineur': entraineur,
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

            #print('class quinteAttele: ', self.quinte)
            

        else :
            print(" ce n'est pas du trot attelé'")

    def getQuinte(self):
        
        return self.quinte
       

        
