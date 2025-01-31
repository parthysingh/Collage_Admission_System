#menu driven project using database connectivity
print("Name : PARTH SINGH")
print("PYTHON & MySQL DATABASE MANAGEMENT")
print('Project Name : "COLLEGE ADMISSION SYSTEM"')
import mysql.connector
import sys
while True:
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345")
    mycursor=mydb.cursor()
    if mydb.is_connected()==True:
        print()
        print("#-----MENU-----#")
        print()
        print("1-CREATE DATABASE\n2-SHOW DATABASE\n3-CREATE TABLE\n4-SHOW TABLES")
        print("5-DESC TABLE\n6-INSERT DYNAMICALLY\n7-SELECT QUERY\n8-WHERE CLAUSE")
        print("9-SEARCH AND DISPLAY\n10-UPDATE FEES\n11-DELETE\n12-EXIT\n")
        ch=int(input("Enter your choice : "))
        def choose():
            print("1-BCA\n2-BBA\n3-BCOM\n4-BTECH")
            s=int(input("Enter your choice (1,2,3,4) : "))
            return s
        if ch==1:
            mycursor.execute("CREATE DATABASE college")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="college")
        mycursor=mydb.cursor()
        if ch==2:
            mycursor.execute("SHOW DATABASES")
            for x in mycursor:
                print (x)
        if ch==3:
            mycursor.execute("CREATE TABLE student (ADMNO INTEGER(3),NAME VARCHAR(20),COURSE VARCHAR(5),FEES INTEGER(10));")
        if ch==4:
            mycursor.execute("SHOW TABLES")
            for x in mycursor:
                print(x)
        if ch==5:
            mycursor.execute("DESC student")
            for x in mycursor:
                print(x) 
        if ch==6:
            Z=int(input("Enter how many record you want to insert : "))
            for i in range(Z):
                r=int(input("Enter student's admission number : "))
                n=input("Enter student's name : ")
                o=input("Enter Your Course (BCA,BBA,BCOM,BTECH) : ")
                m=int(input("Enter course's fees : "))
                mycursor.execute("INSERT INTO student(admno,name,course,fees) VALUES({},'{}','{}',{})".format(r,n,o,m))
                mydb.commit()
                print(mycursor.rowcount,"RECORD IS INSERTED")
        if ch==7:
            mycursor.execute("select * from student")
            r=mycursor.fetchone()
            while r is not None:
                print(r)
                r=mycursor.fetchone()
        if ch==8:
            s=choose()
            if s==1 :
                mycursor.execute("select * from student where course='BCA' OR course='bca'")
            if s==2 :
                mycursor.execute("select * from student where course='BBA' OR course='bba'")
            if s==3 :
                mycursor.execute("select * from student where course='BCOM' OR course='bcom'")
            if s==4 :
                mycursor.execute("select * from student where course='BTECH' OR course='btech'")
            r=mycursor.fetchall()
            count=mycursor.rowcount
            print("total no of rows : ",count)
            for row in r :
                print(row)
        if ch==9:
            mycursor.execute("SELECT * FROM student")
            rs=mycursor.fetchall()
            n=input("Enter name to search : ")
            for row in rs:
                if row[1]==n:
                    print(row)
        if ch==10: 
            s=choose()
            if s==1 :
                mycursor.execute("UPDATE student SET fees=1000 where course='BCA' OR course='bca'")
            if s==2 :
                mycursor.execute("UPDATE student SET fees=2000 where course='BBA' OR course='bba'")
            if s==3 :
                mycursor.execute("UPDATE student SET fees=3000 where course='BCOM' OR course='bcom'")
            if s==4 :
                mycursor.execute("UPDATE student SET fees=4000 where course='BTECH' OR course='btech'")
            mydb.commit()
            print(mycursor.rowcount,"RECORD IS UPDATED")
        if ch==11:
            s=choose()
            if s==1 :
                mycursor.execute("DELETE FROM student where course='BCA' OR course='bca'")
            if s==2 :
                mycursor.execute("DELETE FROM student where course='BBA' OR course='bba'")
            if s==3 :
                mycursor.execute("DELETE FROM student where course='BCOM' OR course='bcom'")
            if s==4 :
                mycursor.execute("DELETE FROM student where course='BTECH' OR course='btech'")
            mydb.commit()
            print(mycursor.rowcount,"RECORD IS DELETED")
        if ch==12:
            sys.exit()