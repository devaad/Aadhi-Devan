#dooooone
import re
def register():
    print('REGISTER')
    print("ENTER EMAIL/USERNAME IN THE FORMAT --'adbc@gmail.com','sherlock@yahoo.com'")
    email = input('set username/email_id:')
    E = r'\b[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}\b'
    while True:
        if (re.fullmatch(E, email)):
            print("VALID")
            break
        else:
            email = input('NOT MATCH THE CRITERIA, enter again :')
    while True:
        print("PASSWORD MUST HAVE MINIMUM 'ONE SPECIAL CHARACTER,'ONE DIGIT','ONE UPPERCASE AND LOWERCASE CHARACTER'")
        password = input('set password:')
        if len(password) > 5 and len(password) < 16:
            if re.search("[a-z]", password):
                if re.search("[A-Z]", password):
                    if re.search("[0-9]", password):
                        if re.search("[_@$]", password):
                            print('YOU HAVE SUCCESFULLY REGISTERED, WELCOME')
                            break
        else:
            print('doesnt match the critirea,enter again:')

    file = open('Assignment', 'a')
    file.write(email + " " + password + "\n")
    file.close()
def login():
    while True:
        print('LOGIN')
        usernamel = input("Enter username/email id:")
        l = []
        l1 = []
        f = open("Assignment")
        for line in f.readlines():
            username, password = line.split()
            l.append(username)
            l1.append(password)
        if usernamel in l:
            passl = input("Enter password:")
            index = l.index(usernamel)
            if l1[index] == passl:
                print("Succefully loged in")
                break
            else:
                print('Password is wrong')
                uf()
                break

        else:
            print("Username doesn't exist\nPlease Register")
            register()
            break

def fp():
    usernamef = input("Enter username/emiald:")
    r = []
    r1 = []
    f = open("Assignment")
    for line in f.readlines():
        username, password = line.split()
        r.append(username)
        r1.append(password)
    if usernamef in r:
        index = r.index(usernamef)
        print(r1[index])
    else:
        print("User doesn't exist\nPlease Register")
        uf()
def uf():
    select = input('Enter 1 or 2\n1.Register\n2.Login\n3.Forgot password ?\n')
    if select=='1':
        register()
    elif select=='2':
        login()
    elif select=='3':
        fp()
# f=open("Assignment","w")                         #These are the usernames and passwords saved in the file
# f.write("aaaa@gmail.com"+" "+"Qwer@123"+"\n")
# f.write("bbbb@gmail.com"+" "+"Asdf@123"+"\n")
# f.write("cccc@gmail.com"+" "+"Zxcv@123"+"\n")
# f.write("dddd@gmail.com"+" "+"Qazw@123"+"\n")
# f.close()
# f=open("Assignment","r")
# f.read()
uf()
