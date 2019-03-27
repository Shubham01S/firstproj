import datetime
from datetime import timedelta
def home():
    a=1
    while a:
        print("Library Management System".center(70,'*'))
        a=int(input('''Select a choice
1.Admin login
2.Student login
3.Admin Signup
4.Student signup
0.Exit\n'''))
        if a is 1:
            adminlog()
        elif a is 2:
            stdlogin()
        elif a is 3:
            adminsign()
        elif a is 4:
            stdsign()
        elif a is 0:
            print("Thank u for using Library Management System")
        else:
            print("Enter a valid Choice")

def adminsign():
    print("Admin Signin".center(60,'*'))
    b="%s,%s\n"%(input("enter the new admin username\n"),input("enter the new admin password\n"))
    if b.split(",")[0] in open("D:/june 2018/projects/lib/adminn.txt").read():
        print("User allready exists...TRY WITH OTHER USERNAME")
        adminsign()
    else:
        open("D:/june 2018/projects/lib/adminn.txt","a").write(b)
        adminlog()
def adminlog():
    print("admin login in".center(60,'*'))
    b="%s,%s\n"%(input("enter the admin username\n"),input("enter the admin password\n"))
    if b in open("D:/june 2018/projects/lib/adminn.txt").read():
        print("You are Loggedin")
        c=1
        while c:
         c=int(input('''Select a choice
1.Add a book
2.Remove a book
3.View issued books
0.Exit\n'''))
         if c is 1:
            addbook()
         elif c is 2:
            removebook()
         elif c is 3:
             print("Books Issued are:.......")
             b=open("D:/june 2018/projects/lib/dminn_book.txt","r")
             d=b.readlines()
             print(*d)
         elif c is 0:
            print("Thank you for using library management system")
         else:
            print("enter a valid choice")
    else:
        print("invalid credentials")
        adminlog()
 
def stdsign():
    print("student signin".center(60,'*'))
    b="%s,%s,%s\n"%(input("enter the student name\n"),input("enter the student usn\n"),input("enter the new student password\n"))
    if b.split(",")[1] in open("D:/june 2018/projects/lib/student.txt").read():
        print("User allready exists")
        stdsign()
    else:
        open("D:/june 2018/projects/lib/student.txt","a").write(b)
        stdlogin()
def stdlogin():
    print("Student login in".center(60,'*'))
    b="%s,%s"%(input("enter the usn\n"),input("enter the  password\n"))
    if b in open("D:/june 2018/projects/lib/student.txt").read():
        print(" Student has been loggedin")
        c=1
        while c:
         c=int(input('''Select a choice
1.Add a book
2.View issued book
0.Exit\n'''))
         if c is 1:
            addbook()
         elif c is 2:
             print("Books Issued are:.......")
             b=open("D:/june 2018/projects/lib/dminn_book.txt","r")
             d=b.readlines()
             print(*d)
         elif c is 0:
            print("Thank you for using library management system")
         else:
            print("enter a valid choice")
    else:
        print("invalid credentials")
        stdlogin()

def addbook():
    print("Book details".center(60,'*'))
    b="%s,%s\n"%(input("enter the book name\n"),input("enter the book isbn number\n"))
    if b.split(",")[0] in open("D:/june 2018/projects/lib/dminn_book.txt").read():
        print("book allready exists")
        addbook()
    else:
           open("D:/june 2018/projects/lib/dminn_book.txt","a").write(b)
           print("Book added successfully....")
           t=datetime.date.today()
           print("Date of issuing is :",t)
           open("D:/june 2018/projects/lib/issue_date.txt","a").write(str(t))
           open("D:/june 2018/projects/lib/issue_date.txt","a").write(',')
           r=t+datetime.timedelta(days=10)
           open("D:/june 2018/projects/lib/issue_date.txt","a").write(str(r))
           open("D:/june 2018/projects/lib/issue_date.txt","a").write('\n')
           print("Date of return is :",r)
           
           
           

def removebook():
     print("Deleting Book".center(60,"*"))
     b="%s,%s\n"%(input("enter the book name to delete \n"),input("enter the book isbn number\n"))
     if b in open("D:/june 2018/projects/lib/dminn_book.txt").read():
         date1=open("D:/june 2018/projects/lib/issue_date.txt").readline()
         date_act=date1.split(",")[1] 
         y1,m1,d1=map(int,date_act.split("-"))
         date_ret=input("Enter the Date when book is returned in YYYY-MM-DD \n")
         y,m,d=map(int,date_ret.split("-"))
         if date_act <= date_ret :
             d1=datetime.date(y1,m1,d1)
             d2=datetime.date(y,m,d)
             timedelta=d2-d1
             d=timedelta.days
             print("Book to return is",b)
             print("THe diff in returned date and actual date is:",d)
             fine=d*10
             print("The fine is :",fine)
        
         else:
            date_ret.split("-")[1] in open("D:/june 2018/projects/lib/dminn_book.txt").read()
            print("No Fine Issued:")
         f=open("D:/june 2018/projects/lib/dminn_book.txt","r")
         lines=f.readlines()
         f.close()
         ft=open("D:/june 2018/projects/lib/dminn_book.txt","w")
         for line in lines:
             if line!=b:
                     ft.write(line)
         ft.close()
         print(b,"has been returned successfully.....")
     else:

         print("Book does'nt exists")
         
          

      

    
          
        

     
