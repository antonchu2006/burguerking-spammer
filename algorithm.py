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
            if not re.search(r"\.\.", mail4):
                mail_list.append(mail4) 
            
            for z in range(x+1, len(mail)+1):
                mail5 = mail4[:y] + "." + mail4[y:]
                if not re.search(r"\.\.", mail4):
                    mail_list.append(mail4) 
                if not re.search(r"\.\.", mail5):
                    mail_list.append(mail5) 
            

    
    mail_list = set(mail_list)
    mail_list = list(mail_list)
    
    mail_list.append("." + '.'.join(chars) + ".")
    
    return mail_list
    

if __name__ == "__main__":
    splitter("antondc555@gmail.com")