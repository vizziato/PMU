
_autor_ = 'gdm'

import pyrebase
import re



class FirebaseAuth:
    
    

    def __init__ (self,config,email,password): 
        self.email = email
        self.password = password
        self.config = config
       
        firebase = pyrebase.initialize_app(self.config)

        # Get a reference to the auth service
        self.auth = firebase.auth()
        
        regexp_email = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"

        if re.match(regexp_email, self.email) is not None:
            print("TRUE")
            self.email_check = re.search(regexp_email, self.email, re.M|re.I)
            print(self.email_check.group())
        else:
            print("False")
       
        try:    
            self.user = self.auth.sign_in_with_email_and_password(self.email_check.group(),self.password)
            userToken = self.user['idToken']
            if self.auth.send_email_verification(userToken)['email'] == self.email_check.group():
                print("l'utilisateur existe")
                self.connect = True
            else:
                print("l'utilisateur n'existe pas")
                self.connect= False
                self.auth.create_user_with_email_and_password(self.email_check.group(), self.password)
        except:
            print("provider error")
            self.connect= False

    def getConnect(self):
        return self.connect

    def getUser(self):
        return self.user
