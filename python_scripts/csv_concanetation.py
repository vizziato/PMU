import csv
import re


sexe,age,driver,deferre,recul,gagnant,place,favori,outsider,entraineur,autostart,longueur,date,hippo= [],[],[],[],[],[],[],[],[],[],[],[],[],[]

fopen1 = 'Vincenne_V0_1.csv'
fopen2 = 'MyTestFile2.csv'
fwrite = 'MyTestFile.csv'

delimiter1 =';'
delimiter2 =','
#fichier = open('file.csv','rb')
#fichiercsv = csv.reader(fichier, delimiter=';')


with open(fopen1,newline='', encoding='utf-8') as csvfile1:
    try:
        reader1 = csv.DictReader(csvfile1,delimiter=delimiter1)
    

        #writer = csv.writer(file)
        #writer.writerow( ['Entraineur', 'Autostart', 'Deferre','Favori','Gagnant','Outsider','Age','Place','Recul','Sexe','Distance','Driver','Hippodrome','Date'])

        for row in reader1:
            entraineur.append(row['Entraineur'])
            driver.append(row['Driver'])
            sexe.append(row['Sexe'])
            age.append(row['Age'])
            hippo.append(row['Hippodrome'])
            longueur.append(row['Distance'])
            place.append(row['Place'])
            gagnant.append(row['Gagnant'])
            autostart.append(row['Autostart'])
            recul.append(row['Recul'])
            deferre.append(row['Deferre'])
            favori.append(row['Favori'])
            outsider.append(row['Outsider'])
            date.append(row['Date'])
    except:
        print('file error')

print('entraineeur 1',len(entraineur))
print('len date 1',len(date))
print('len place 1',len(place))

with open(fopen2,newline='', encoding='utf-8') as csvfile2:
    try:
        reader2 = csv.DictReader(csvfile2,delimiter=delimiter2)
    

        for row in reader2:
            entraineur.append(row['Entraineur'])
            driver.append(row['Driver'])
            sexe.append(row['Sexe'])
            age.append(row['Age'])
            hippo.append(row['Hippodrome'])
            longueur.append(row['Distance'])
            place.append(row['Place'])
            gagnant.append(row['Gagnant'])
            autostart.append(row['Autostart'])
            recul.append(row['Recul'])
            deferre.append(row['Deferre'])
            favori.append(row['Favori'])
            outsider.append(row['Outsider'])
            date.append(row['Date'])
    except:
        print('file error')
     

#print('reader 2',reader2.restval)

print('entraineeur 2',len(entraineur))
print('len date 2',len(date))
print('len place 2',len(place))
print('len gagant 2',len(gagnant))
print('len age 2',len(age))
print('len recul 2',len(recul))

#print('date',date)
#date = date[0:len(entraineur)]
print('date[0]', date[0])
print('len date',len(date))

longArray=[len(entraineur),len(date),len(driver)]
print('Array:::',longArray)
#print('max',max(longArray[len(entraineur),len(date),len(driver)]))

sumQuinte =({   'Entraineur': entraineur,
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
                'Driver' : driver,
                'Hippodrome':hippo,
                'Date':date})

#print('sumQuinte :', sumQuinte)
print('sum len',len(sumQuinte['Entraineur']))

file = open(fwrite, "w")

try:
    #
    # Création de l'''écrivain'' CSV.
    #
    writer = csv.writer(file)
    #
    # Écriture de la ligne d'en-tête avec le titre
    # des colonnes.
    writer.writerow( ['Entraineur', 'Autostart', 'Deferre','Favori','Gagnant','Outsider','Age','Place','Recul','Sexe','Distance','Driver','Hippodrome','Date'])

    #
    # Écriture des quelques données.
    for row in range(0,len(sumQuinte['Entraineur'])):
        writer.writerow( [sumQuinte['Entraineur'][row], sumQuinte['Autostart'][row],sumQuinte['Deferre'][row],sumQuinte['Favori'][row],
                        sumQuinte['Gagnant'][row],sumQuinte['Outsider'][row],sumQuinte['Age'][row],sumQuinte['Place'][row],
                        sumQuinte['Recul'][row],sumQuinte['Sexe'][row],sumQuinte['Distance'][row],sumQuinte['Driver'][row],sumQuinte['Hippodrome'][row],sumQuinte['Date'][row]])
        #print(sumQuinte['Entraineur'][row])

finally:
    #
    # Fermeture du fichier source
    #
    file.close()




'''
with open('MyTestFile2.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        writer = csv.writer(file)

            # writer = csv.writer(file,MyDialect())
                #
                # Écriture de la ligne d'en-tête avec le titre
                # des colonnes.
        writer.writerow( ['Entraineur', 'Autostart', 'Deferre','Favori','Gagnant','Outsider','Age','Place','Recul','Sexe','Distance','Driver','Hippodrome','Date'])

        for row in reader:
            print(row)
        
            try:

                
                #writer = csv.writer(file)

            # writer = csv.writer(file,MyDialect())
                #
                # Écriture de la ligne d'en-tête avec le titre
                # des colonnes.
                #writer.writerow( ['Entraineur', 'Autostart', 'Deferre','Favori','Gagnant','Outsider','Age','Place','Recul','Sexe','Distance','Driver','Hippodrome','Date'])

                #
                # Écriture des quelques données.
                #for row in range(0,len('Entraineur')):
                writer.writerow( ['Entraineur', 'Autostart','Deferre','Favori',
                                    'Gagnant','Outsider','Age','Place',
                                    'Recul','Sexe','Distance','Driver','Hippodrome','adieu'])
                writer.writerow( ['Entraineur', 'Autostart','Deferre','Favori',
                                    'Gagnant','Outsider','Age','Place',
                                    'Recul','Sexe','Distance','Driver','Hippodrome','adieu'])
                    #print(sumQuinte['Entraineur'][row])

            finally:
                #
                # Fermeture du fichier source
                #
                #file.close()
                pass
'''