
import pyrebase
import re
import pandas as jockey

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

# Log the user in
##email_temp="i500enculé@gmail.com"
#password="giulia09"

#auth.create_user_with_email_and_password(email_temp, password)
email_temp = input("Creer un nouveau utilisateur: insérer une adresse email:")
password=input("Creer un nouveau utilisateur: insérer un mot de passe:")
#password_temp = input("Password svp:")

def checkEmail(): 
    regexp_email = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"

    if re.match(regexp_email, email_temp) is not None:
        print("TRUE")
        email = re.search(regexp_email, email_temp, re.M|re.I)
        print(email.group())
        return email.group()
    else:
        print("False")

try:    
    user = auth.sign_in_with_email_and_password(checkEmail(), password)
    userToken = user['idToken']
    if auth.send_email_verification(userToken)['email'] == checkEmail():
        print("l'utilisateur existe")
    else:
        print("l'utilisateur n'existe pas")
        auth.create_user_with_email_and_password(checkEmail(), password)
except:
    print("provider error")





#Test data jockey

#with codecs.open('/home/giuseppe/Documents/Projets/VincenneCsv.csv', encoding='utf8', errors='replace') as jockey:
    #rd = csv.reader(jockey, delimiter=',')
    #departements = [r[2] for r in rd]
choix = ['OUI','NON','H','M','F']
output = jockey.read_csv('/home/giuseppe/Documents/Projets/VincenneCsv.csv',sep=',',header=5,skiprows=0,index_col=1,skip_blank_lines=True)


nettoye = output.drop(output.ix[:,'Unnamed: 0':'Unnamed: 0'].head(0).columns, axis=1)



nettoye = output.drop(output.ix[:,'Unnamed: 0':'Unnamed: 0'].head(0).columns, axis=1)

df_csv_propre = jockey.DataFrame(nettoye)


#for r in df_csv_propre:
 #   df2.append(r)

#df2 = {r[1]:r[2:] for r in output}

#for r in range(1):
for r in range(len(df_csv_propre)):
    indexdf = df_csv_propre.iloc[r].name
    #print(indexdf)
    
    df = jockey.DataFrame({'Entraineur': [df_csv_propre.iloc[r].Entraineur],
                           'Autostart':  [df_csv_propre.iloc[r].Autostart],
                            'Deferre':   [df_csv_propre.iloc[r].Deferre],
                            'Favori': [df_csv_propre.iloc[r].Favori], 
                            'Gagnant': [df_csv_propre.iloc[r].Gagnant],
                            'Outsider': [df_csv_propre.iloc[r].Outsider],
                            'Age': [df_csv_propre.iloc[r].Age],
                            'Place': [df_csv_propre.iloc[r].Place],
                            'Recul': [df_csv_propre.iloc[r].Recul],
                            'Sexe': [df_csv_propre.iloc[r].Sexe],
                            'Distance': [df_csv_propre.iloc[r].Distance]},
                             index = [indexdf])
    #print(df)
    #df2 = jockey.DataFrame(index = [indexdf])
    data = df.to_json(orient = 'index')
    #db.child("jockeys").set(df_json)

    db.child("jockeys").push(data, user['idToken'])


    #print(df2_json)
    
#print(df2_json)
# data to save
#data = {
    #"name": "Mortimer 'Morty' Smith"
#}

# Pass the user's idToken to the push method
#results = db.child("users").push(data, user['idToken'])








def input_keyboard_str (message):
    keyboard =input(message)
    keyboard = keyboard.upper()
    try:
        if keyboard in choix:
            return keyboard
        else:
            while keyboard not in choix:
                keyboard = input('String Error try again ' + message)
                keyboard = keyboard.upper()
                if keyboard in choix:
                    break
            return keyboard               
    except ValueError:
            keyboard = input('try again' + message)
    except KeyboardInterrupt:
            keyboard = input('try again' + message)
            
def input_keyboard_int (message):
    keyboard =input(message)
    keyboard = int(keyboard)
    try:
        if keyboard < 4100:
            return keyboard
        else:
            while keyboard > 4100:
                keyboard = input('String Error try again ' + message)
                keyboard = int(keyboard)
                if keyboard < 4100:
                    break
            return keyboard               
    except ValueError:
            keyboard = input('try again' + message)
    except KeyboardInterrupt:
            keyboard = input('try again' + message)
           
                  

driver =  input('Nom du drivers:')
entraineur = input_keyboard_str ("Est-il Entraineur aussi: [OUI,NON] ")
autostart = input_keyboard_str ("Départ à l'autostart: [OUI,NON] ")
deferre = input_keyboard_str ("Le cheval est-il déferré: [OUI,NON] ")
place = input_keyboard_str ("C'est -il placé ces 5 dernières courses: [OUI,NON] ")
gagnant = input_keyboard_str ("A-t-il gangné c'est 3 dernières courses: [OUI,NON] ")
favori = input_keyboard_str ("Avait-il une petite côte: [OUI,NON] ")
outsider = input_keyboard_str ("Avait-il une grosse côte: [OUI,NON] ")
recul = input_keyboard_str ("Est il parti avec du recul: [OUI,NON] ")
sexe = input_keyboard_str ("Quel est le sexe du cheval: [H,M,F] ")
distance = input_keyboard_int ("Distance de la course: [2100,2700,etc] ")
age = input_keyboard_int ("L'age du cheval: 3 à 10 ")


df = jockey.DataFrame({'Entraineur': [entraineur],'Autostart': [autostart],'Déferré': [deferre],'Favori': [favori], 'Gagnant': [gagnant],
                        'Outsider': [outsider],'AGE': [age],'Placé': [place],'Recul': [recul],'Sexe': [sexe],'Distance': [distance]}, index = [driver])


#df = jockey.merge(df1, nettoye)
#df1 = nettoye.append(df)

#df1.to_csv('/home/giuseppe/Documents/Projets/MyFile.csv', sep = ',')

#df1 = {"Morty": {"name": "Mortimer 'Morty' Smith"}}
#db.child("jockeys").set(df1)