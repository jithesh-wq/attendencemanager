import sqlite3
import getpass
import os
import time
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
                    showUserMenu(uname)
                else:
                    print("WRONG PASSWORD!")     
                    
# creating a new user
def createUser():   
    os.system("clear")
    print ("\n\t\t************************")
    print ("\t\t*        SIGNUP        *")
    print ("\t\t************************\n")
    uname=input("Enter a username-->")
    passwd=getpass.getpass(prompt="Create a password-->")
    rpasswd=getpass.getpass(prompt="Retype password-->")
    if (passwd==rpasswd):
        userlist=[]
        cursor.execute('''SELECT username FROM user''')
        user=cursor.fetchall()
        for row in user:
            userlist.append(row[0])
        if uname in userlist or uname=='':
                os.system("clear")
                print ("\n\n\n\n\t\tUSE ANOTHER USERNAME!")
                time.sleep(3)
                createUser()
        else:
                cursor.execute('''INSERT INTO user (username,password) VALUES(?,?)''',(uname,passwd))
                dbconn.commit()
                os.system("clear")
                print ("\n\n\n\n\t\tSIGNUP SUCCESSFULL!")
                time.sleep(3)
                main()
    else:
        os.system("clear")
        print ("\n\n\n\n\t\tPASSWORD MISSMATCH!")
        time.sleep(3)
        createUser()
 #showing user menu
def showUserMenu(uname):
    os.system("clear")
    print("Hi "+uname+" Welcome to Attendence Manager")
    time.sleep(3)
    os.system("clear")
    print ("\n\t\t************************")
    print ("\t\t*  ATTENDENCE MANAGER  *")
    print ("\t\t************************\n")
    print ("\t1.VIEW ATTENDENCE\n\t2.UPDATE ATTENDENCE\n\t3.CLEAR DATA\n\t4.LOGOUT\n")
    ch=input("-->")
    if ch=="1":
        viewAttendence(uname)
    elif ch=="2":
        updateAttendence()
    elif ch=="3":
        clearData()
    elif ch=="4":
        main()
    else:
        showUserMenu(uname)

    
    #  cursor.execute('''CREATE TABLE IF NOT EXISTS'''+uname+'''(username TEXT PRIMARY KEY,password TEXT)''')
    #  dbconn.commit()
def viewAttendence(uname):
    print("viewattendence")
def updateAttendence(uname):
    print("updateattendence")
def clearData():
    print("cleardata")
# main page starts here
def main():
    os.system("clear")
    print ("\n\t\t************************")
    print ("\t\t*  ATTENDENCE MANAGER  *")
    print ("\t\t************************\n")
    print ("\t1.LOGIN\n\t2.SIGNUP\n\t3.QUIT\n")
    ch=input("-->")
    os.system("clear")
    if (ch=="1"):
        print ("\n\t\t************************")
        print ("\t\t*        LOGIN         *")
        print ("\t\t************************\n")
        uname=input("USERNAME-->")
        passwd=getpass.getpass(prompt="PASSWORD-->")
        checkusr(uname,passwd)
    elif (ch=="2"):
        createUser()
    elif (ch=="3"):
        exit
    else:
        print("\n\n\n\n\t\tINVALID CHOICE")
        time.sleep(1)
        main()
main()
dbconn.close()