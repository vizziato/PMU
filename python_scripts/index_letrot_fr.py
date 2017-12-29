
import re
import csv
import codecs
import pandas as jockey
from pandas.io.json import json_normalize
import asyncio

from bs4 import BeautifulSoup

from html_leTrot_class import PartantsAttele
from html_leTrot_head_class import LeTrotHead
from csv_pmu_trot_class import CsvQuinte

from firebase_auth import FirebaseAuth
from firebase_input_to_db import KeyboardInputJockey

import pyrebase


"""

START CONNECTION TO Firebase **********************************************************************************************************************************

"""

config = {
    "apiKey": "AIzaSyDfCAAw9RxKCoJL12PETvTGEQuG6CpfqHc",
    "authDomain":  "jockey-43b92.firebaseapp.com",
    "databaseURL": "https://jockey-43b92.firebaseio.com",
    "storageBucket": "jockey-43b92.appspot.com"
    }

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()
# Get a reference to the db
db = firebase.database()


#email_temp = input("Creer un nouveau utilisateur: insérer une adresse email:")
#password_temp =input("Creer un nouveau utilisateur: insérer un mot de passe:")

email_temp = 'python@gmail.com'
password_temp = 'python'


f = FirebaseAuth(config,email_temp,password_temp)

print('connection status: ', f.getConnect())



"""

END CONNECTION TO Firebase **********************************************************************************************************************************

"""
url_directory = "C:/Users/Giuseppe/Documents/Python/PythonPMU/files_html_recorded_letrot_fr/"
url_default = "C:/Users/Giuseppe/Documents/Python/PythonPMU/files_html_uploader/"

sexe,age,driver,deferre,recul,gagnant,place,record,gain,crack,favori,outsider,entraineur,autostart,longueur,month_temp,hippoArray,dateArray= [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

with codecs.open(url_default +'01011001.html', encoding='utf8', errors='replace') as rd:
    defaultFileHtml = rd.read()

anneeArray = [7]
courseArray = [1,2,3,4,5,6,7,8,9]
#courseArray = [2]


for mois in range(1,2):
    for jour in range(1,3):
        for annee in anneeArray:
             for course in courseArray:
                print('course', course)
                print('annee', annee)
                try:
                    if jour < 10 and mois < 10:
                        try:
                            
                            if annee < 10:
                                with codecs.open(url_directory+'letrot_0{0}0{1}200{2}C{3}.html'.format(jour,mois,annee,course), encoding='utf8', errors='replace') as rd:
                                    contenu = rd.read()
                                    print('contenu')
                            else:
                                with codecs.open(url_directory+'letrot_0{0}0{1}20{2}C{3}.html'.format(jour,mois,annee,course), encoding='utf8', errors='replace') as rd:
                                    contenu = rd.read()
                                    print('contenu')
                           
                        except:
                            print("file dosn't exist")
                            contenu = defaultFileHtml
                            arrivee = defaultFileHtml

                            
                    elif jour < 10 and mois >= 10:
                        try:

                            if annee < 10:
                                with codecs.open(url_directory+'letrot_0{0}{1}200{2}C{3}.html'.format(jour,mois,annee,course), encoding='utf8', errors='replace') as rd:
                                    contenu = rd.read()
                            else:
                                with codecs.open(url_directory+'letrot_0{0}{1}20{2}C{3}.html'.format(jour,mois,annee,course), encoding='utf8', errors='replace') as rd:
                                    contenu = rd.read()


                        except:
                            #print("file dosn't exist")
                            contenu = defaultFileHtml
                            arrivee = defaultFileHtml

                    elif jour >=  10 and mois < 10:
                        try:

                            if annee < 10:
                                with codecs.open(url_directory+'letrot_{0}0{1}200{2}C{3}.html'.format(jour,mois,annee,course), encoding='utf8', errors='replace') as rd:
                                    contenu = rd.read()
                            else:
                                with codecs.open(url_directory+'letrot_{0}0{1}20{2}C{3}.html'.format(jour,mois,annee,course), encoding='utf8', errors='replace') as rd:
                                    contenu = rd.read()


                        except:
                            #print("file dosn't exist")
                            contenu = defaultFileHtml
                            arrivee = defaultFileHtml
                    
                    else:
                        try:
                            if annee < 10:
                                with codecs.open(url_directory+'letrot_{0}{1}200{2}C{3}.html'.format(jour,mois,annee,course), encoding='utf8', errors='replace') as rd:
                                contenu = rd.read()
                            else:
                                with codecs.open(url_directory+'letrot_{0}{1}20{2}C{3}.html'.format(jour,mois,annee,course), encoding='utf8', errors='replace') as rd:
                                contenu = rd.read()

                        except:
                            #print("file dosn't exist")
                            contenu = defaultFileHtml
                            arrivee = defaultFileHtml
                except:
                    pass
                

                try:
                    hippodrome,date,type_course,distance,distance_temp,autostart_search,nb_partants  =  LeTrotHead(contenu).getHead()
                    print('date :' ,date);
                    print('hippodrome :' , hippodrome);
                    print('type de course :' ,type_course);
                    print('autostart :' , autostart_search);
                    print('nbpartants :' , nb_partants);
                   
                    hippodrome_ar,date_ar,type_course_ar,distance_ar,distance_temp_ar,autostart_search_ar,nb_partants_ar  =  LeTrotHead(arrivee).getHead()
                    print('date arrivee :' ,date_ar);
                    print('hippodrome arrivee :' , hippodrome_ar);
                    print('type de course arrivee:' ,type_course_ar);
                    print('autostart arrivve :' , autostart_search_ar);
                    print('nbpartants arrivee:' , nb_partants_ar);
                    
                except:
                    print('nb partant < 15')

                try:
                    if hippodrome == hippodrome_ar and date == date_ar and nb_partants == nb_partants_ar:
                        mareponse =  PartantsAttele(contenu,arrivee,type_course,autostart_search, distance_temp,nb_partants).getQuinte()
                        print('mareponse:', mareponse)

                        type_course1 = (re.search('([a-zA-Z])',type_course,re.M|re.I).group())
                        #print('type de course 1:', type_course)

                        if date is not None:
                            month_temp.append(re.search('([^0-9])\S+',date,re.M|re.I).group() )

                            #hippoArray += [hippodrome,hippodrome,hippodrome,hippodrome,hippodrome]
                            hippoArray += [hippodrome]*5
                            #hippoArray.append(hippodrome)*4
                            #dateArray.insert[date,date,date,date,date]
                            dateArray += [date]*5
                            #print('dateArray', dateArray)
                            #dateArray.append(date)
                            #print('mois_temp',month_temp)
                        else:
                            month_temp.append('Mois')
                            hippoArray += ['HIPPO','HIPPO','HIPPO','HIPPO','HIPPO']
                            dateArray += ['DATE','DATE','DATE','DATE','DATE']
                    


                        #month += mareponse['Mois']
                        #entraineur.append(mareponse['Entraineur'])
                        entraineur += mareponse['Entraineur']
                        #autostart.append(mareponse['Autostart'])
                        autostart += mareponse['Autostart']

                        #deferre.append(mareponse['Deferre'])
                        deferre += mareponse['Deferre']

                        #record.append(mareponse['Favori'])
                        record += mareponse['Record']

                        #gagnant.append(mareponse['Gagnant'])
                        gagnant += mareponse['Gagnant']

                        #outsider.append(mareponse['Outsider'])
                        gain += mareponse['Gain']

                        #age.append(mareponse['Age'])
                        age += mareponse['Age']

                        #place.append(mareponse['Place'])
                        place += mareponse['Place']

                        #recul.append(mareponse['Recul'])
                        recul += mareponse['Recul']

                        #sexe.append(mareponse['Sexe'])
                        sexe += mareponse['Sexe']

                        #longueur.append(mareponse['Distance'])
                        longueur += mareponse['Distance']

                        #crack.append(mareponse['Distance'])
                        crack += mareponse['Crack']


                        #driver.append(mareponse['Driver'])
                        driver += mareponse['Driver']

                except:
                    pass


sumQuinte =({   'Entraineur': entraineur,
                'Autostart':  autostart,
                'Deferre':   deferre,
                'Record': record, 
                'Gagnant': gagnant,
                'Gain': gain,
                'Age': age,
                'Place': place,
                'Recul': recul,
                'Sexe': sexe,
                'Distance': longueur,
                'Crack': crack,
                'Driver' : driver,
                'Hippodrome':hippoArray,
                'Date':dateArray})
print('SumQuinte :', sumQuinte)

print('len entraineur :' ,len(sumQuinte['Entraineur']))
print('len date:' ,len(sumQuinte['Date']))


#fname1 = "MyTestFile2.csv"
#fname2 = "MyPredictionFile.csv"

#fopen1 = './tables/Vincenne_V0_1.csv'
#fopen1 = 'AtteleQuinte_v0_4.csv'

fopen2 = './tables/LeTrotAtteleQuinte_v0_1.csv'
#fopen2 = 'MyPredictionFile_v0_2.csv'
fwrite = './tables/MyLeTrotFileWrite_v0_1.csv'

#CsvQuinte().insertAnotherCsv(fopen1,fopen2,fwrite)
#CsvQuinte().insertAnotherCsv(fopen1,fopen2,fwrite)

#CsvQuinte(sumQuinte,fopen1,fopen2,fwrite).insertCsv()
CsvQuinte().insertLeTrotCsv(sumQuinte,fopen2)

url_csv = "C:/Users/Giuseppe/Documents/Python/PythonPMU/"


output = jockey.read_csv(url_csv +fopen2,sep=',',header=0,index_col=['Driver'],skip_blank_lines=True)


df_csv_propre = jockey.DataFrame(output)
#print('df propre' ,df_csv_propre)

#print('manipulation df' ,df_csv_propre.Date.map(lambda x: x == '0 Novembre 1001') )
#df_dup = df_csv_propre.drop_duplicates(subset='Date')
#print('df duplicate', df_dup)
#df_dup = df_csv_propre.drop(df_csv_propre.Date.map(lambda x: x == '0 Novembre 1001') , axis=0, level=None, inplace=False, errors='raise')

#df_dup = df_csv_propre[df_csv_propre.Date != df_csv_propre.Date.map(lambda x: x == '0 Novembre 1001') ]
#df_dup = df_csv_propre[df_csv_propre.Date.map(lambda x: x == '0 Novembre 1001') ]
#df_dup = df_csv_propre[df_csv_propre.Date != '0 Novembre 1001']
df_csv_propre = df_csv_propre[df_csv_propre.Date != '0 Novembre 1001']

#print('df duplicate', df_csv_propre)



for r in range(len(df_csv_propre)):
    indexdf = df_csv_propre.iloc[r].name
    #print(indexdf)
 
    df = jockey.DataFrame({'Entraineur': [df_csv_propre.iloc[r].Entraineur],
                           'Autostart':  [df_csv_propre.iloc[r].Autostart],
                            'Deferre':   [df_csv_propre.iloc[r].Deferre],
                            'Favori': [df_csv_propre.iloc[r].Favori],
                            'Record': [df_csv_propre.iloc[r].Record], 
                            'Gain': [df_csv_propre.iloc[r].Gain], 
                            'Gagnant': [df_csv_propre.iloc[r].Gagnant],
                            'Outsider': [df_csv_propre.iloc[r].Outsider],
                            'Age': [df_csv_propre.iloc[r].Age],
                            'Place': [df_csv_propre.iloc[r].Place],
                            'Recul': [df_csv_propre.iloc[r].Recul],
                            'Sexe': [df_csv_propre.iloc[r].Sexe],
                            'Distance': [df_csv_propre.iloc[r].Distance],
                            'Hippodrome':[df_csv_propre.iloc[r].Hippodrome],
                            'Crack':[df_csv_propre.iloc[r].Crack],
                            'Date':[df_csv_propre.iloc[r].Date]},
                             index = [indexdf])

    #print(df)force_ascii=False

    #df2 = jockey.DataFrame(index = [indexdf])
    data = df.to_json(orient = 'index',date_format ='iso',force_ascii=False)
    #data = df.to_json()
    #print(data)
    #db.child("jockeys").set(df_json)

    #db.child('attele/'+hippodrome+'/'+[df_csv_propre.iloc[r].Mois]).push(data,f.getUser()['idToken'])
    #db.child('items').push(data,f.getUser()['idToken'])

#print('data frame ',df)
#print('df to json ',data)