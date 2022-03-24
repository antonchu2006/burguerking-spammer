import re

def convert(string):
    list1=[]
    list1[:0]=string
    return list1

def splitter(email):
    mail = email.split("@")[0]
    chars = convert(mail)
    
    new_chars = []
    
    for c in chars:
        new_chars.append(c+".")
        
    mail_list = []
    
    for x in range(0, len(mail)+1):
        mail2 = convert(mail)

        mail2.insert(x, '.')
        
        mail3 = ''.join(mail2)
        mail_list.append(mail3)  
        
        
        for y in range(x+1,len(mail)+1):
            mail4 = mail3[:y] + "." + mail3[y:]
            mail44 = mail4 + "."
            mail45 = "." + mail4
            if not re.search(r"\.\.", mail4):
                mail_list.append(mail4)
            if not re.search(r"\.\.", mail44):
                mail_list.append(mail44)
            if not re.search(r"\.\.", mail45):
                mail_list.append(mail45)
                          
    
    mail_list = set(mail_list)
    mail_list = list(mail_list)
    
    mail_list.append("." + '.'.join(chars) + ".")
    
    if not re.search(r"\.\.",mail+"."):
        mail_list.append(mail+".")
    if not re.search(r"\.\.","."+mail):
        mail_list.append("."+mail)
    
    mail_list.append(mail)
    
    return mail_list
    

if __name__ == "__main__":
    splitter("example@example.com")
    
    print("[+] Lists: \""+ str(splitter("example@example.com"))+ "\"")
    print("[+] Mails:" + str(len(splitter("example@example.com"))))
