import sqlite3
import getpass
dbconn=sqlite3.connect('attendence.db')
cursor=dbconn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user (username TEXT PRIMARY KEY,password TEXT)''')
dbconn.commit()

# verifying usr login
def checkusr(uname,passwd):
    cursor.execute('''SELECT username,password FROM user''')
    user=cursor.fetchall()
    userlist=[]
    pwdlist=[]
    for row in user:
        userlist.append(row[0])
        pwdlist.append(row[1])
    if uname not in userlist:
        print("USER NOT EXISTS IN DATABASE!")
    else:
        for i in userlist:
            if uname==i:
                uid=userlist.index(i)
                if pwdlist[uid]==passwd:
                    print("LOGIN SUCCESSFUL!")
                else:
                    print("WRONG PASSWORD!")     
                    
# creating a new user
def createuser(uname,passwd):
    userlist=[]
    cursor.execute('''SELECT username FROM user''')
    user=cursor.fetchall()
    for row in user:
        userlist.append(row[0])
    if uname in userlist:
            print ("USER EXISTS!")
            print ("USE ANOTHER USERNAME!")
    else:
            cursor.execute('''INSERT INTO user (username,password) VALUES(?,?)''',(uname,passwd))
            dbconn.commit()
            print ("SIGNUP SUCCESSFULL!")
        
# main page starts here
print ("\n\t\t************************")
print ("\t\t*  ATTENDENCE MANAGER  *")
print ("\t\t************************\n")
print ("\t1.LOGIN\n\t2.SIGNUP\n")
ch=input("-->")
if (ch=="1"):
    uname=input("USERNAME-->")
    passwd=getpass.getpass(prompt="PASSWORD-->")
    checkusr(uname,passwd)
elif (ch=="2"):
    cuname=input("Enter a username-->")
    cpasswd=getpass.getpass(prompt="Create a password-->")
    rpasswd=getpass.getpass(prompt="Retype password-->")
    if (cpasswd==rpasswd):
        createuser(cuname,cpasswd)
    else:
        print ("Password missmatch")
else:
    print("Error!")

dbconn.close()
    