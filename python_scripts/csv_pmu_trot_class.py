import csv
import re



class MyDialect(csv.Dialect):
    delimiter = ","
    quotechar = "'"
    escapechar = "\\"
    doublequote = None
    lineterminator = "\r\n"
    quoting = csv.QUOTE_NONNUMERIC
    skipinitialspace = False

class CsvQuinte:
    

    #def __init__(self,dicQuinte,fopen1,fopen2,fwrite):
       
      

    def insertCsv(self,dicQuinte,fopen2):
        self.dicQuinte = dicQuinte
        self.fopen2 = fopen2

        file = open(self.fopen2, "w")
        
        try:
            #
            # Création de l'''écrivain'' CSV.
            #
            writer = csv.writer(file)
        # writer = csv.writer(file,MyDialect())
            #
            # Écriture de la ligne d'en-tête avec le titre
            # des colonnes.
            writer.writerow( ['Entraineur', 'Autostart', 'Deferre','Favori','Gagnant','Outsider','Age','Place','Recul','Sexe','Distance','Driver','Hippodrome','Date'])
        
            #
            # Écriture des quelques données.
            for row in range(0,len(self.dicQuinte['Entraineur'])):
                writer.writerow( [self.dicQuinte['Entraineur'][row], self.dicQuinte['Autostart'][row],self.dicQuinte['Deferre'][row],self.dicQuinte['Favori'][row],
                                self.dicQuinte['Gagnant'][row],self.dicQuinte['Outsider'][row],self.dicQuinte['Age'][row],self.dicQuinte['Place'][row],
                self.dicQuinte['Recul'][row],self.dicQuinte['Sexe'][row],self.dicQuinte['Distance'][row],self.dicQuinte['Driver'][row],self.dicQuinte['Hippodrome'][row],self.dicQuinte['Date'][row]])
                #print(self.dicQuinte['Entraineur'][row])
        
        finally:
            #
            # Fermeture du fichier source
            #
            file.close()

    def insertLeTrotCsv(self,dicQuinte,fopen2):
        self.dicQuinte = dicQuinte
        self.fopen2 = fopen2

        file = open(self.fopen2, "w")
        
        try:
            #
            # Création de l'''écrivain'' CSV.
            #
            writer = csv.writer(file)
        # writer = csv.writer(file,MyDialect())
            #
            # Écriture de la ligne d'en-tête avec le titre
            # des colonnes.
            writer.writerow( ['Entraineur', 'Autostart', 'Deferre','Gagnant','Record','Gain','Crack','Age','Place','Recul','Sexe','Distance','Driver','Hippodrome','Date'])
        
            #
            # Écriture des quelques données.
            for row in range(0,len(self.dicQuinte['Entraineur'])):
                writer.writerow( [self.dicQuinte['Entraineur'][row], self.dicQuinte['Autostart'][row],self.dicQuinte['Deferre'][row],
                                self.dicQuinte['Gagnant'][row],self.dicQuinte['Age'][row],self.dicQuinte['Place'][row],self.dicQuinte['Crack'][row],
                                self.dicQuinte['Recul'][row],self.dicQuinte['Sexe'][row],self.dicQuinte['Distance'][row],self.dicQuinte['Driver'][row],
                                self.dicQuinte['Hippodrome'][row],self.dicQuinte['Gain'][row],self.dicQuinte['Record'][row],self.dicQuinte['Date'][row]])
                #print(self.dicQuinte['Entraineur'][row])
        
        finally:
            #
            # Fermeture du fichier source
            #
            file.close()


 
    def insertAnotherCsv(self,fopen1,fopen2,fwrite):
        self.fopen1 = fopen1
        self.fopen2 = fopen2
        self.fwrite = fwrite
       

        delimiter1 = ';'
        delimiter2 = ','

        sexe,age,driver,deferre,recul,gagnant,place,favori,outsider,entraineur,autostart,longueur,date,hippo= [],[],[],[],[],[],[],[],[],[],[],[],[],[]

        
        with open(self.fopen1,newline='', encoding='utf-8') as csvfile1:
            try:
                reader1 = csv.DictReader(csvfile1,delimiter=delimiter1)
            
                for row in reader1:
                    entraineur.append(row['Entraineur'])
                    #driver.append(row['Driver'])
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
                    '''
                    if row['Outsider']:
                        if re.search('oui',row['Outsider'],re.M|re.I):
                            outsider.append('OUI')
                            print('oui')
                        else:
                            outsider.append('NON')

                    if row['Deferre']:
                        if re.search('oui',row['Deferre'],re.M|re.I):
                            deferre.append('OUI')
                        else:
                            deferre.append('NON')'''
                    
                    if row['Driver']:
                        if re.search('bazi',row['Driver'],re.M|re.I):
                            driver.append('BAZIRE')
                        elif re.search('nivar',row['Driver'],re.M|re.I):
                            driver.append('NIVARD')
                        elif re.search('levesq',row['Driver'],re.M|re.I):
                            driver.append('LEVESQUE')
                        elif re.search('verva',row['Driver'],re.M|re.I):
                            driver.append('VERVA')
                        elif re.search('dreux',row['Driver'],re.M|re.I):
                            driver.append('DREUX')
                        elif re.search('raffin',row['Driver'],re.M|re.I):
                            driver.append('RAFFIN')
                        elif re.search('bigeon',row['Driver'],re.M|re.I):
                            driver.append('BIGEON')
                        elif re.search('abriva',row['Driver'],re.M|re.I):
                            driver.append('ABRIVARD')
                        elif re.search('vercru',row['Driver'],re.M|re.I):
                            driver.append('VERCRUYSSE')
                        elif re.search('piton',row['Driver'],re.M|re.I):
                            driver.append('PITON')
                        elif re.search('ouvrie',row['Driver'],re.M|re.I):
                            driver.append('OUVRIE')
                        else:
                            driver.append('AUTRES')



            except:
                print('file error')
        print('entraineeur 1',len(entraineur))
        print('len date 1',len(date))
        print('len place 1',len(place))

        with open(self.fopen2,newline='', encoding='utf-8') as csvfile2:
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

        file = open(self.fwrite, "w")

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



                
                