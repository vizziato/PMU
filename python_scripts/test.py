
from firebase_auth import FirebaseAuth
from firebase_input_to_db import KeyboardInputJockey

import pandas as jockey
import pyrebase

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


email_temp = input("Creer un nouveau utilisateur: insérer une adresse email:")
password_temp =input("Creer un nouveau utilisateur: insérer un mot de passe:")

f = FirebaseAuth(config,email_temp,password_temp)

print(f.getConnect())


driver =  input('Nom du drivers:')

entraineur = KeyboardInputJockey("Est-il Entraineur aussi: [OUI,NON] ").getMessage()
autostart = KeyboardInputJockey("Départ à l'autostart: [OUI,NON] ").getMessage()
deferre = KeyboardInputJockey("Le cheval est-il déferré: [OUI,NON] ").getMessage()
place = KeyboardInputJockey("C'est -il placé ces 5 dernières courses: [OUI,NON] ").getMessage()
gagnant = KeyboardInputJockey("A-t-il gangné c'est 3 dernières courses: [OUI,NON] ").getMessage()
favori = KeyboardInputJockey("Avait-il une petite côte: [OUI,NON] ").getMessage()
outsider = KeyboardInputJockey("Avait-il une grosse côte: [OUI,NON] ").getMessage()
recul = KeyboardInputJockey("Est il parti avec du recul: [OUI,NON] ").getMessage()
sexe = KeyboardInputJockey("Quel est le sexe du cheval: [H,M,F] ").getMessage()
distance = KeyboardInputJockey ("Distance de la course: [2100,2700,etc] ").getMessage()
age = KeyboardInputJockey ("L'age du cheval: 3 à 10 ").getMessage()


df = jockey.DataFrame({'Entraineur': [entraineur],'Autostart': [autostart],'Deferre': [deferre],'Favori': [favori], 'Gagnant': [gagnant],
                        'Outsider': [outsider],'Age': [age],'Place': [place],'Recul': [recul],'Sexe': [sexe],'Distance': [distance]}, index = [driver])



data = df.to_json(orient = 'index')


db.child("jockeys").push(data,f.getUser()['idToken'])


#df1.to_csv('/home/giuseppe/Documents/Projets/MyFile.csv', sep = ',')


