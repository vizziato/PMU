


import re  

class KeyboardInputJockey:
    

    choix = ['OUI','NON','H','M','F']
    regexp_int = r"(^[0-9])"

    def __init__(self,message):
               
        self.message = message
        keyboard =input(self.message)
    

        if re.match(KeyboardInputJockey.regexp_int, keyboard) is not None:
            print("TRUE")
            keyboard = int(keyboard)
        else:
            print("False")
            keyboard = keyboard.upper()
       
        try:
            if keyboard in KeyboardInputJockey.choix:
                self.result_message = keyboard
            elif keyboard not in KeyboardInputJockey.choix and isinstance(keyboard,str):
                while keyboard not in KeyboardInputJockey.choix:
                    keyboard = input('String Error try again ' + self.message)
                    keyboard = keyboard.upper()
                    if keyboard in KeyboardInputJockey.choix:
                       self.result_message = keyboard 
            elif keyboard not in KeyboardInputJockey.choix and isinstance(keyboard,int) and keyboard <4100:
                self.result_message = keyboard
            else:
                while keyboard > 4100:
                    keyboard = input('String Error try again ' + self.message)
                    keyboard = int(keyboard)
                    if keyboard < 4100:
                        break
                self.result_message = keyboard                  
        except ValueError:
                keyboard = input('try again' + self.message)
        except KeyboardInterrupt:
                keyboard = input('try again' + self.message)

    def getMessage(self): 
        return self.result_message
  

