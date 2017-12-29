
import re

from bs4 import BeautifulSoup

class LeTrotHead:


    def __init__(self,contenu):
        
       
        """
        Parser document .html
        """
        soup = BeautifulSoup(contenu,'lxml')


        """
        Recherche de l'hippodrome et de la date'
        """
        self.autostart_search = None
        
        try:

            if soup.find("div", class_="infos_hippodrome_course"):
                #regexp_hippodrome= re.search('([a-zé0-9._ ])+',hippodrome.string,re.M|re.I)
                hippodrome = soup.find("div", class_="infos_hippodrome_course").text
                regexp_hippodrome= re.search('([a-z ])+',hippodrome,re.M|re.I)
                self.hippodrome =regexp_hippodrome.group()
                #print('hippodrome dans trothead class:', self.hippodrome)
                #print('hippodrome dans trothead class:', regexp_hippodrome)
                #print('hippodrome dans trothead class:', hippodrome)
            else:
                self.hippodrome = None
        except:
                self.hippodrome = None
           
        try:
            if soup.find("div",class_="date-course"):
                date = soup.find("div",class_="date-course").text
                regexp_date= re.search('([^,])+\S+',date,re.M|re.I).group().upper()
                self.date = re.sub(',',"",regexp_date)

                #print('date dans trotClass:',date)
                #print('date dans trotClass:',regexp_date)
            else:
                self.date = None
        except:
                self.date = None
       
       
        """
        Fin hippodrome et date

        """

        """
        Recherche du type de course , de la distance, nombre de partants et autostart
        
        """
        try:
            if soup.find("div", class_="description-course"):
      
                #print('old version')
                tag1 = soup.find("div", class_="description-course").text
                #print('tag1',tag1)
               # print('dans class trothead tag1', tag1)

                regexp_type_course= re.search('([-])+([a-zA-Zé ])+',tag1,re.M|re.I).group()
                #print('dans class trothead type course', regexp_type_course)
                self.type_course = re.sub('-',"",regexp_type_course)

                
            
                #print('class Pmuhead autostart:', autostart_temp.group())
                if re.search('autostart',tag1,re.M|re.I):
                    regexp_autostart= re.search('autostart',tag1,re.M|re.I).group()
                    #print('class leTrothead autostart:', regexp_autostart)
                    self.autostart_search = regexp_autostart
                else:
                    self.autostart_search = None



                #self.distance_temp = re.search('([0-9._ ])\S+',tag1.strong.next_element.next_element.string,re.M|re.I)
                regexp_distance = re.search('([0-9 -])+m',tag1,re.M|re.I).group()
                distance_temp = re.sub('-',"",regexp_distance)
                distance = re.sub('m',"",distance_temp)
                #print('tag1.text:',tag1.text )
                #print('distance::',distance)
                self.distance_temp = distance
                self.distance = int(distance)
                #print(self.distance)
            
           
        except:
            self.type_course = None
            self.distance = None
            self.distance_temp = None
            self.autostart_search = None
        
        try:
            if soup.find_all("td", class_="sorting_1"):
                par = soup.find_all("td", class_="sorting_1")
                #print('mapfunction  ',par)
                print('mapfunction len ',len(par))
                self.nb_partants = len(par)
            else:
                self.nb_partants = None
        except:
                self.nb_partants = None
     

  
       

        self.head = (self.hippodrome,self.date,self.type_course, self.distance,self.distance_temp,self.autostart_search,self.nb_partants)
        print('self.head', self.head)
    def getHead(self):
        
        #if self.nb_partants > 15 : return self.head
        return self.head
       

        
