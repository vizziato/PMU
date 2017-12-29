import re

from bs4 import BeautifulSoup

class PartantsAttele:


    def __init__(self,contenu,arrivee,type_course, autostart_search, distance_temp, nb_partants):
        
        self.contenu = contenu
        self.arrivee = arrivee
        self.type_course = type_course
        self.autostart_search =  autostart_search
        self.distance_temp =  distance_temp
        self.nb_partants =  nb_partants
        """
        Parser document .html
        """
        soup = BeautifulSoup(self.contenu,'lxml')
        soup_a = BeautifulSoup(self.arrivee,'lxml')

        if re.search('Attel',self.type_course,re.M|re.I):
            details =  soup.find_all("td", class_="sorting_1")
            details_a =  soup_a.find_all("td", class_="sorting_1",limit=5)

            

            sexe,age,driver,deferre,recul,gagnant,place,rec,cra,ga,entraineur,autostart,longueur,numero,arr= [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
            
            for y in range(len(details_a)):
                arr.append(int(details_a[y].next_sibling.next_sibling.text))
                

            print('arrivee numero',arr)
            
            for r in range(self.nb_partants):

                print('r', r)

                
                numero= details[r].find("span").text
                #arr= details_a[r].next_sibling.next_sibling.text

                print('numero',numero)
                #print('arrivee numero',arr)

                if int(numero) in arr:
                    regexp_dis = re.search('([0-9 ])+',details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text,re.M|re.I).group()
                    dis = re.sub(' ',"",regexp_dis)
                    #print(dis)
                    #print('int',int(dis))
                    #print(int(self.distance_temp))
                    if self.autostart_search is not None:
                        autostart.append('OUI')
                        #print('autostart',autostart)

                        if (int(numero) > 9):
                            recul.append('OUI')
                        else: 
                            recul.append('NON')
                    else:
                        autostart.append('NON')
                        if int(dis) == int(self.distance_temp):
                            recul.append('NON')
                        else:
                            recul.append('OUI')
                    
                    #print('autostart',autostart)
                    #print('recul',recul)
                    
                    
                    #longueur.insert(r,distance_temp.group())
                    #print('distance,',distance_temp.group())
                    if int(self.distance_temp) > 2700:
                        longueur.append('LONG')
                    else:
                        longueur.append('COURT')
                    #sexe.append(re.search('([a-zA-Z])',details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text,re.M|re.I).group())
                    #print(sexe)
                    
                        #age.append(re.search('([0-9])',details[r].find("td", class_="participants-tbody-td txtC").get_text(),re.M|re.I).group())
                    if re.search('([0-9])',details[1].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text,re.M|re.I):
                        #print('age::',re.search('([0-9])',details[r].find("td", class_="participants-tbody-td txtC").get_text(),re.M|re.I).group())
                        if int(re.search('([0-9])+',details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text,re.M|re.I).group()) >= 3 and int(re.search('([0-9])+',details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text,re.M|re.I).group()) <=5:
                            age.append('JEUNE')
                        elif int(re.search('([0-9])+',details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text,re.M|re.I).group()) >= 6 and int(re.search('([0-9])+',details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text,re.M|re.I).group()) <= 9:
                            age.append('MEDIUM')
                        else:
                            age.append('VIEUX')

                    #print('longueur',longueur)
                    #print('age',age)

                    if (details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find("div")):
                        deferre.append('OUI')
                    else:
                        deferre.append('NON')

                    print('deferre',deferre)
                    
                        #print('jockey class QuinteAttele',details[r].find("span", class_="participants-jokey").text)
                        #print('entraineur class QuinteAttele',details[r].find("span", class_="participants-entraineur").text)

                    # if re.search(entraineur_temp,driver_temp,re.M|re.I):
                    # entraineur.append('OUI')
                    # else:
                    #entraineur.append('NON')
                    tag = details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling

                    d = details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find("span").text

                    entra = details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find("span").text
                    
                    #print(d)
                    #print(entra)

                
                    
                    if re.search(entra,d,re.M|re.I):
                        entraineur.append('OUI')
                    else:
                        entraineur.append('NON')
            
                    driver.append(d)

                    sexe.append(details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text)

                    #print('entrineur',entraineur)
                    #print('driver',driver)


                    '''   

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
                    
                    
                    '''   

                        musique_temp = details[r].find("td", class_="participants-tbody-td gains").next_sibling.next_sibling.next_sibling.next_sibling.get_text()
                        #print('musique_temp', musique_temp)
                        #regexp= re.search("([()])([0-9])+([)])",musique_temp,re.M|re.I)
                        regexp= re.sub("([()])([0-9])+([)])","",musique_temp)
                        #print('regexp',regexp)
                    '''    
                    mus = details[r].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
                    #print(mus)
                
                    musique,l=[],[]
                    
                    for i in mus:
                        regexp_mus= re.search('([0-9D])+',i,re.M|re.I)
                        
                        try:
                            if(regexp_mus.group() != 'D'):
                                musique.append(regexp_mus.group())
                            else:
                                musique.append('0')

                        except:
                            #print('0')
                            pass
                        
                    print('musique:', musique)

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
                    #print('place',place)
                    

                    rec.append(int(tag.next_sibling.next_sibling.next_sibling.next_sibling.find("span").text))
                    #recherche de lu cheval avec le meilleur record de piste
                    #print('record',rec)
                    #print('min record  = ',min(rec))

                    record=[]
                    for x in rec:
                        try:
                            if(x == min(rec)):
                                record.append('OUI')
                            else:
                                record.append('NON')

                        except:
                            #print('0')
                            pass
                        
                    #print('record:', record)

                    cra.append(int(tag.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text))
                    #print('cra',cra)
                    #print('min cra',min(cra))
                    
                    
                    crack=[]
                    for c in cra:
                        try:
                            if(c == min(cra)):
                                crack.append('OUI')
                            else:
                                crack.append('NON')

                        except:
                            #print('0')
                            pass
                        
                    print('crack:', crack)


                    ga.append(re.search('([0-9 ])+',tag.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find("div").text,re.M|re.I).group())
                    print('gain',ga)
                    print('max cra',max(ga))
                    
                    
                    gain=[]
                    for g in ga:
                        try:
                            if(g == max(ga)):
                                gain.append('OUI')
                            else:
                                gain.append('NON')

                        except:
                            #print('0')
                            pass
                        
                    print('gain:', gain)
                

                    '''
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
                    '''
            
                                    
                    
                            

                    



            self.quinte =({ 'Entraineur': entraineur,
                        'Autostart':  autostart,
                        'Deferre':   deferre,
                        'Record': record, 
                        'Gagnant': gagnant,
                        'Gain': gain,
                        'Crack': crack,
                        'Age': age,
                        'Place': place,
                        'Recul': recul,
                        'Sexe': sexe,
                        'Distance': longueur,
                        'Driver' : driver})

            print('class quinteAttele: ', self.quinte)
            

        else :
            print(" ce n'est pas du trot attelé'")

    def getQuinte(self):
        
        return self.quinte
       

        
