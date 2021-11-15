#-------------------------IMPORTING MODULES-------------------------------
import mysql.connector as mysql         #from mysql import connector as msql
import time
#=========================FUNCTIONS=======================================

def tables():
    curs.execute('show tables')
    data=curs.fetchall()
    return data
    

def showtable():
    curs.execute('show tables')
    data=curs.fetchall()
    print('The database contains the following tables:')
    for i in data:
        print(i)

def showdata(tname):
    query="select * from {}"
    curs.execute(query.format(tname))

    data=curs.fetchall()
    for i in data:
        print(i)

def spdata(st):
    query='select {} from {};'.format(st,tn)
    curs.execute(query) 
    data=curs.fetchall()
    for i in data:
        print(i)

def search(co):
    query="select * from sample"
    curs.execute(query)
    data=curs.fetchall()
    for i in data:
        if i[0]==co:
            print('RECORD FOUND!!!!!')
            print(i)
            return 1
            break
    else:
        print('ENTRY NOT FOUND!!!')

def delete(co,tn):
    query="delete from {} where item_id='{}'".format(tn,co)
    curs.execute(query)
    print('DELETION SUCCESFUL')
    mcon.commit()
    
def update(co,v1,v2,tn):
    if tn=='sample':
        query='update sample set {}={} where item_id={}'.format(v1,v2,co)
        curs.execute(query)
        print('UPDATION SUCCESFUL')
        mcon.commit()
    elif tn=='emp':
        query='update emp set {}={} where empid={}'.format(v1,v2,co)
        curs.execute(query)
        print('UPDATION SUCCESFUL')
        mcon.commit()
    
    
    
        
#-------------------------ESTABLISHING CONNECTION--------------------------
mcon=mysql.connect(host='sql5.freemysqlhosting.net', user='sql5451247', passwd='WKLnNUY5SR', database='sql5451247')
if mcon.is_connected():
    print("Successfully connected")

curs=mcon.cursor()

#-------------------------MAIN MENU---------------------------------------

ch=None
while True:
    print('''---------------------------------------------------
                      MAIN MENU
---------------------------------------------------
1)SHOW TABLES
2)SHOW ALL RECORDS
3)SHOW ALL RECORDS(SPECIFIC COLUMNS)
===>(TO USE THE FOLLOWING FUNCTIONS PLEASE SELECT TABLE IN OPTION 2 FIRST)
4)SEARCH RECORD
5)ADD ENTRY
6)DELETE ENTRY
7)UPDATE ENTRY
---------------------------------------------------''')
    ch=int(input('ENTER YOUR CHOICE: '))

    if ch==1:
        showtable()
        inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
        if inc in ['n','N']:
            break

#----------------------------------SHOW ALL RECORDS-------------------------

    if ch==2:
        global tn
        ch=0
        while True:
            global tn
            tn=input('ENTER TABLE NAME: ')
            tn=tn.lower()
            t=tables()
            for i in t:
                if tn in i:
                    print('TABLE FOUND!!')
                    ch+=1
                    break
                
            else:
                print('Enter a valid table name!!!!!')
                
            if ch==1:
                break
   
        showdata(tn)
        inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
        if inc in ['n','N']:
            break

#-----------------------------SHOW SPECIFIC COLUMNS--------------------------

    if ch==3:                                   
        print('COLUMN NAMES: ')
        cnm=curs.column_names
        for i in cnm:
            print(i)
        cno=int(input('HOW MANY COLUMNS DO YOU WANT TO SELECT: '))
        sample=[]
        for i in range(cno):
            nm=input('ENTER COLUMN NAME: ')
            sample.append(nm)
        
        st=''
        for i in sample:
            st+=i
            st+=','
        spdata(st[:-1])
        
        inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
        if inc in ['n','N']:
            break

#-----------------------------SEARCH RECORD----------------------------------

    if ch==4:
        co=input("Enter the item id which you want to search: ")
        search(co)

        inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
        if inc in ['n','N']:
            break
#----------------------------NEW ENTRY----------------------------------------
    if ch==5:
        if tn=='sample':
            while True:
                i=input("Enter ITEM ID: ")
                n=input("Enter ITEM NAME: ")
                q=int(input("Enter QUANTITY: "))
                p=int(input("Enter PRICE: "))
                s=input("Enter SELLER NAME: ")
                ps=input("Enter DATE OF PURCHASE:(YYYY,MM,DD) ")
                query="Insert into sample values('{}','{}',{},{},'{}','{}')".format(i,n,q,p,s,ps)
                curs.execute(query)
                mcon.commit()

                ch=input('DO YOU WANT TO ENTER MORE VALUES: ')
                if ch in ['n','N']:
                    break
        elif tn=='emp':
            while True:
                i=int(input("Enter EMP ID: "))
                n=input("Enter EMP NAME: ")
                q=int(input("Enter SALARY: "))
                query="Insert into emp values({},'{}',{})".format(i,n,q)
                curs.execute(query)
                mcon.commit()

                ch=input('DO YOU WANT TO ENTER MORE VALUES: ')
                if ch in ['n','N']:
                    break
        else:
            print('PLEASE SELECT A VALID TABLE ON OPTION 2!!!')
            break
        
        inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
        if inc in ['n','N']:
            break

#------------------------------------DELETE ENTRY----------------------------------------
    if ch==6:
        while True:
            co=input('ENTER ID WHOSE ENTRY IS TO BE DELETED: ')
            if search(co)==1:
                ch=input('ARE YOU SURE YOU WANT TO DELETE THIS RECORD? [Y/N]  ')
                if ch in ['n','N']:
                    print('-------RECORD NOT DELETED-------')
                    break
                else:
                
                    delete(co,tn)
                    c=input('DO YOU WANT TO DELETE MORE? [Y/N]  ')
                    if c in ['n','N']:
                        break
            else:
                c=input('DO YOU WANT TO TRY AGAIN? [Y/N]  ')
                if c in['n','N']:
                    break

        inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
        if inc in ['n','N']:
            break

#----------------------------UPDATE ENTRY---------------------------------------

    if ch==7:
        while True:
            co=input('ENTER ID WHOSE ENTRY IS TO BE UPDATED: ')
            if search(co)==1:
                ch=input('ARE YOU SURE YOU WANT TO UPDATE THIS RECORD? [Y/N]  ')
                if ch in ['n','N']:
                    print('-------RECORD NOT UPDATED-------')
                    break
                else:
                    
                    v1=input('ENTER COLUMN NAME: ')
                    cnm=curs.column_names
                    if v1 in cnm:
                        v2=input('ENTER NEW VALUE: ')
                        update(co,v1,v2,tn)
                        c=input('DO YOU WANT TO UPDATE MORE? [Y/N]  ')
                        if c in ['n','N']:
                            break
                        
                    else:
                        print('COLUMN NOT FOUND')
                        break
                    
            else:
                c=input('DO YOU WANT TO TRY AGAIN? [Y/N]  ')
                if c in['n','N']:
                    break

        inc=input('DO YOU WANT TO CONTINUE? [Y/N] ')
        if inc in ['n','N']:
            break

#-----------------------------INVALID CHOICE-----------------------------------------
        
    else:
        print('SELECT A VALID OPTION!!!')
        
#-----------------------------------------------END---------------------------------------------------------

time.sleep(200)    
        
         























        
        
