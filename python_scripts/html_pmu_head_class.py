
import re

from bs4 import BeautifulSoup

class PmuHead:


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
            soup.find("h2", class_="course-title")
            soup.find ("header", class_="course-infos-header").p

            if soup.find("h2", class_="course-title") or soup.find ("header", class_="course-infos-header").p:
                self.titre =  soup.find("h2", class_="course-title") or soup.find ("header", class_="course-infos-header").p
            else:
                self.titre = None
        except:
            self.titre = None
        #print('titre dans Pmuhead class:' ,self.titre)
        try:

            if soup.find("h2", class_="course-title"):
                hippodrome = self.titre.b.next_sibling.next_sibling
                regexp_hippodrome= re.search('([a-zé0-9._ ])+',hippodrome.string,re.M|re.I)
                self.hippodrome =regexp_hippodrome.group()
                #print('hippodrome dans Pmuhead class:', self.hippodrome)
                #print('hippodrome dans Pmuhead class:', hippodrome)
            else:
                hippodrome = soup.find("div", class_="reunion-hippodrome").span.text
                regexp_hippodrome= re.search('([a-zé0-9._ ])+',hippodrome,re.M|re.I)
                self.hippodrome =regexp_hippodrome.group()
                #print('hippodrome dans Pmuhead class:', self.hippodrome)
        except:
            self.hippodrome = None
           
        try:
            if self.titre.find(class_="date"):
                self.date = self.titre.find(class_="date").text
                self.date.upper()
            else:

                d  = soup.find("p", class_="course-infos-statut-date").b.text
                regexp_date = re.search('([0-9 ])+([a-zéA-Z])+([0-9 ])+',d,re.M|re.I).group()
                regexp_date_sub = re.sub("([é])+",'E',regexp_date)
                #regexp_date = re.search('([a-zéA-Z])+',d,re.M|re.I).group()
                #print('regexp_date dans Pmuhead class:', regexp_date.group())
                #print('regexp_date dans Pmuhead class:', regexp_date)
                #print('regexp_date_sub dans Pmuhead class:', regexp_date_sub)
                self.date = regexp_date_sub.upper()
                print('self.date dans Pmuhead class:', self.date)
        except:
            self.date = None
        """
        Fin hippodrome et date

        """

        """
        Recherche du type de course , de la distance, nombre de partants et autostart
        """
        if soup.find("div", class_="course-info"):
            try:
                #print('old version')
                tag1 =soup.find("div", class_="course-info").find(id="conditions").p
                #print('tag1',tag1)
                type_course_temp = tag1.strong

                if(re.search('([a-zé0-9._ ])+',type_course_temp.string,re.M|re.I)):
                    regexp_type_course= re.search('([a-zé0-9._ ])+',type_course_temp.string,re.M|re.I)
                    self.type_course = regexp_type_course.group()
                else:
                    self.type_course = None


                #self.distance_temp = re.search('([0-9._ ])\S+',tag1.strong.next_element.next_element.string,re.M|re.I)
                self.distance_temp = re.sub('m',"",re.search('([0-9])+m',tag1.text,re.M|re.I).group())
                #print('tag1.text:',tag1.text )
                #print('distance::',self.distance_temp)

                #print('distamce in classhead::',distance.group())
                #self.distance = int(self.distance_temp.group())
                self.distance = int(self.distance_temp)
                nb_partants_temp = re.search('([0-9 ])+ partant',tag1.strong.next_element.next_element.string,re.M|re.I).group()
                nb_partants = re.search('([0-9])+',nb_partants_temp,re.M|re.I)

                self.nb_partants = int(nb_partants.group())


                autostart_temp = re.search('Autostart',tag1.strong.next_element.next_element.string,re.M|re.I)
            except:
                self.type_course = None
                self.autostart_search = None
                self.distance = None
                self.distance_temp = None
                self.nb_partants = None



        else:
            try:
                tag1 =soup.find("div", class_="course-infos-conditions").p.find("span", class_="icon-infos").next_element
                #print('tag1 dans Pmuhead :' ,tag1)
                #type_course_temp = tag1
                type_course_temp= self.titre.b.text
                #print('type_course_temp dans Pmuhead :' ,type_course_temp)
                #print('new version')
                #print('type:',type(type_course_temp))

                if(re.search('([ -])([a-zé0-9])+',type_course_temp,re.M|re.I)):
                    regexp_type_course= re.search('([ -])([a-zé0-9])+',type_course_temp,re.M|re.I)
                    self.type_course = regexp_type_course.group()
                    #print('self.type_course dans Pmuhead :' ,self.type_course)
                else:
                    self.type_course = None
                    #print('self.type_course dans Pmuhead :' ,self.type_course)

                #nb_partants = re.search('([0-9 ])+ partant',self.titre.b,re.M|re.I)
                #nb_partants = self.titre.b.next_sibling.next_sibling.next_sibling
                self.distance_temp = re.search('([ | ])([0-9])+',self.titre.b.next_sibling.next_sibling.next_sibling,re.M|re.I)
                self.distance = int(self.distance_temp.group())
                #print('class Pmuhead self.distance: ', self.distance)


                nb_partants_temp = re.search('([0-9 ])+ partant',self.titre.b.next_sibling.next_sibling.next_sibling,re.M|re.I).group()
                #print('nb_partants_temp: ', nb_partants_temp)

                self.nb_partants = int(re.search('([0-9])+',nb_partants_temp,re.M|re.I).group())

                #print('nombre partant: ', nb_partants)
                #print('nombre partant: ', nb_partants)
                autostart_temp = re.search('Autostart',tag1,re.M|re.I)
                #print('autostart_temp: ', autostart_temp)
            except:
                self.type_course = None
                self.autostart_search = None
                self.distance = None
                self.distance_temp = None
                self.nb_partants = None



        #print(tag1)
        #print(type_course_temp)
        #print(regexp_type_course.group())
       
        #print('self.type_course dans Pmuhead :' , self.type_course)

       

  
        try:
            
            #print('class Pmuhead autostart:', autostart_temp.group())
            self.autostart_search = autostart_temp.group()
            if autostart_temp is not None:
                self.autostart_search = autostart_temp.group()
            else:
                self.autostart_search == None 

        except:
            #print('no autostart course ')
            self.autostart_search == None 
            #print(autostart_search)

        self.head = (self.hippodrome,self.date,self.type_course, self.distance,self.distance_temp,self.autostart_search,self.nb_partants)

    def getHead(self):
        
        if self.nb_partants > 15 : return self.head
       

        
