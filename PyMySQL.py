import mysql.connector
#ConnectionObj=mysql.connector.connect(host="localhost",user="root",password="121325",database="university",port="3306")
ConnectionObj1=mysql.connector.connect(host="localhost",user="root",database="PythonMySQL",password="121325",port="3306")
ConnectionCursor=ConnectionObj1.cursor()
"""
print("\n\t 1.-------------------------------------- Data from student table:~ -----------------------------------")
ConnectionCursor.execute("select * from student")
for data1 in ConnectionCursor.fetchall():
    print("\n* Tabular info : ",data1)
    print("\t 1  ID : ",data1[0])
    print("\t 2  First Name : ", data1[1])
    print("\t 3  Middle Name : ", data1[2])
    print("\t 4  Last Name : ", data1[3])
    print("\t 5  Department : ", data1[4])
    print("\t 6  CGPA : ", data1[5])
    print("\t 7  Salary : ", data1[6])
    print("\t 8  Address : ", data1[7])
print("\n\t 2.------------------------------------ Data from employee table:~ -------------------------------------")
ConnectionCursor.execute("select * from employee")
for data2 in ConnectionCursor.fetchall():
    print("\n# Tabular info : ", data2)
    print("\t 1  ID : ", data2[0])
    print("\t 2  First Name : ", data2[1])
    print("\t 3  Middle Name : ", data2[2])
    git 
    print("\t 4  Last Name : ", data2[3])
    print("\t 5  Department : ", data2[4])
    print("\t 6  CGPA : ", data2[5])
    print("\t 7  Address : ", data2[6])
    """
#ConnectionCursor.execute("create database PythonMySQL")
#ConnectionCursor.execute("create table PyMysql(ID int not null primary key,FName varchar(30), Minit varchar(30),LName varchar(30),Department varchar(40),Salary float,Address varchar(30))")
#ConnectionCursor.execute("insert into PyMysql(ID,FName,Minit,LName,Department,Salary,Address) values (%s,%s,%s,%s,%s,%s,%s)",(364634,"John","Thomas","Jackson","Computer Science",987676343.3457,"Washington Dc"))
#ConnectionCursor.execute("create table tableA(ID int not null primary key,FName varchar(30) not null,Minit varchar(30) not null, LName varchar(30) not null,Department varchar(40) not null, Salary float,Address varchar(40))")
#ConnectionCursor.execute("create table tableB(ID varchar(30) not null primary key,FName varchar(30) not null,Minit varchar(30) not null, LName varchar(30) not null,Department varchar(40) not null, Salary float,Address varchar(40))")
#ConnectionCursor.execute("insert into tableA(ID,FName,Minit,LName,Department,Salary,Address) values(%s,%s,%s,%s,%s,%s,%s)",(265347,"John","Thomas","Jackson","Computer Science",987676343.3457,"Washington Dc"))
#ConnectionCursor.execute("insert into tableB(ID,FName,Minit,LName,Department,Salary,Address) values(%s,%s,%s,%s,%s,%s,%s)",("UGR/3763/22","Joseph","Biden","Donald","Software Engineernig",887675343.5767,"Newyork"))
#ConnectionObj1.commit()
#print("\n\t",ConnectionCursor.rowcount,"row/rows inserted !")
print("\n 1.---------------------------------------------------------- Information from PyMySQL relation ------------------------------------------------------------")
ConnectionCursor.execute("select * from PyMysql")
for data1 in ConnectionCursor.fetchall():
    print("\n Tabular information : ",data1)
    print("\n\t ID : ", data1[0])
    print("\n\t First Name : ",data1[1])
    print("\n\t Middle Name : ", data1[2])
    print("\n\t Middle Name : ", data1[3])
    print("\n\t Department : ", data1[4])
    print("\n\t Salary : ", data1[5])
    print("\n\t Address : ", data1[6])
print("\n 2.---------------------------------------------------------- Information from tableA relation ------------------------------------------------------------")
ConnectionCursor.execute("select * from tableA")
for data2 in ConnectionCursor.fetchall():
    print("\n Tabular information : ",data2)
    print("\n\t ID : ", data2[0])
    print("\n\t First Name : ",data2[1])
    print("\n\t Middle Name : ", data2[2])
    print("\n\t Middle Name : ", data2[3])
    print("\n\t Department : ", data2[4])
    print("\n\t Salry : ", data2[5])
    print("\n\t Address : ", data2[6])
print("\n 3.---------------------------------------------------------- Information from tableB relation ------------------------------------------------------------")
ConnectionCursor.execute("select * from tableB")
for data3 in ConnectionCursor.fetchall():
    print("\n Tabular information : ",data3)
    print("\n\t ID : ", data3[0])
    print("\n\t First Name : ",data3[1])
    print("\n\t Middle Name : ", data3[2])
    print("\n\t Middle Name : ", data3[3])
    print("\n\t Department : ", data3[4])
    print("\n\t Salry : ", data3[5])
    print("\n\t Address : ", data3[6])
print("\n\n Operation successfully accomplished !")