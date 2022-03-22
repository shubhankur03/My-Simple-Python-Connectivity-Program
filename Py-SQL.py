#date created:8-may-2021
#made by: Shubhankur Singh
import mysql.connector
hst=input("Enter host name:")
usr=input("Enter User name:")
pwd=input("Enter password:")
try:
    mydb=mysql.connector.connect(host=hst, user=usr, passwd=pwd)#connecting database
    print("Connection Established")
    mydb.close() #closing database
except mysql.connector.errors.InterfaceError:
    print("Its look like you have enter wrong username and password")
    print("Program is now exiting....")
    exit()
print()
print("1.Create a new database")
print("2. Use an existing database")
choice=int(input("Enter your choice:"))
if choice==1:
    try:
        mydb=mysql.connector.connect(host=hst, user=usr, passwd=pwd)#connecting database
        mycursor=mydb.cursor()
        dtbs=input("Enter the name of Database:")
        mycursor.execute("CREATE DATABASE %s"%dtbs)
        print("Database",dtbs,"created")
        mycursor.close()
        mydb.close()#closing database
    except mysql.connector.errors.InterfaceError:
        print("Its look like you have enter wrong username and password")
        print("Program is now exiting....")
        exit()
elif choice==2:
    dtbs=input("Enter the name of database:")
    print("Database",dtbs,"is now selected")
else:
    print("Invalid choice....")
    print("Program is now exiting....")
    exit()
print()
#===============================================================================
#database program
try:
    mydb=mysql.connector.connect(host=hst, user=usr, passwd=pwd,database=dtbs)#connecting database
    mycursor=mydb.cursor()
except mysql.connector.errors.InterfaceError:
    print("Unknown error is occured while working with database....")
    print("Program is now exiting....")
    exit()
#table program
print("1.Create a new table")
print("2. Use an existing table")
tbl_choice=int(input("Enter your choice:"))
if tbl_choice==1:
    try:
        tbl=input("Enter the name of table you want to created:")
        mycursor.execute("CREATE TABLE %s (abc int(3))"%tbl)
        print("Table",tbl,"has been created")
    except mysql.connector.errors.ProgrammingError:
        print("It looks like table is already created:")
elif tbl_choice==2:
    tbl=input("Enter the name of table you want to use:")
    print("Table",tbl,"is now selected")
else:
    print("Invalid choice")
    print("Program is now exiting")
    exit()
print()
#================================================================================
#column program
c=input("Do you want to add columns in table(y/n):")
if c=='y':
    cnt=int(input("How many columns do you want to add:"))
    for i in range(1,cnt+1):
        try:
            column_name=input("Enter column name:")
            column_type=input("Enter column type:")
            if column_type in ("VARCHAR","CHAR","Varchar","Char","varchar","char"):
                column_size=int(input("Enter column size:"))
                mycursor.execute("ALTER TABLE %s ADD(%s %s(%s))"%(tbl,column_name,column_type,column_size))
            elif column_type in ("decimal","Decimal"",DECIMAL"):
                x=input("Enter column size:")
                y=input("Enter precision:")
                mycursor.execute("ALTER TABLE %s ADD(%s %s(%s,%s))"%(tbl,column_name,column_type,x,y))
            else:
                mycursor.execute("ALTER TABLE %s ADD(%s %s)"%(tbl,column_name,column_type))
        except mysql.connector.errors.DataError:
            print("Index is out of range or you have enter incorrect values.")
            print("Program is now exiting....")
            exit()
        except mysql.connector.errors.ProgrammingError:
            print("you have enter incorrect format for columns")
            print("Program is now exiting....")
            exit()
if tbl_choice==1:
    mycursor.execute("ALTER TABLE %s DROP abc"%tbl)
while c=='n':
    print("ok")
    break
print()
#============================================================================
#row program
c=input("Do you want to add values for column(y/n):")
if c=='y':
    cnt=int(input("For how many rows do you want to add values:"))
    print("***Enter string and date enclosed in quotation***")
    for n in range(1,cnt+1):
        columns_name=input("Enter column names seperated by commas:")
        rows_name=input("Enter values seperated by commas:")
        mycursor.execute("INSERT INTO %s(%s) VALUES(%s)"%(tbl,columns_name,rows_name))
        print("Record inserted")
        mydb.commit()
while c=='n':
    print("Ok")
    break
print()
mydb.close()#closing database
#===============================================================================
#menu program
mydb=mysql.connector.connect(host=hst,user=usr, passwd=pwd,database=dtbs)#connecting database
mycursor=mydb.cursor()
print("Now you can use the menu for modifying database....")
c='y'
while c=='y':
    print("1. Display Records")
    print("2. Modify Table Structure")
    print("3. Modify Column Values")
    print("4. Delete  Database")
    print("5. Exit")
    choice=int(input("Enter your choice:"))
    print()
    if choice==1:
        mycursor.execute("SELECT * FROM %s"%tbl)
        result=mycursor.fetchall()
        for x in result:
            print(x)
        print()
    elif choice==2:
        print("Which funtion do you want to use")
        print()
        while c=='y':
            print("1. Add a column")
            print("2. Delete a column")
            print("3. Update column definition")
            print("4. Rename a column")
            print("5. Delete Table")
            print("6. Return to main menu")
            ch=int(input("Enter your choice:"))
            print()
            if ch==1:
                cnt=int(input("How many columns do you want to add:"))
                for i in range(1,cnt+1):
                    try:
                        column_name=input("Enter column name:")
                        column_type=input("Enter column type:")
                        if column_type in ("VARCHAR","CHAR","Varchar","Char","varchar","char"):
                            column_size=int(input("Enter column size:"))
                            default=input("Does it have default value(y/n)")
                            if default=='y':
                                default_value=input("Enter default value:")
                                mycursor.execute("ALTER TABLE %s ADD(%s %s(%s) default %s)"%(tbl,column_name,column_type,column_size,default_value))
                            elif default=='n':
                                mycursor.execute("ALTER TABLE %s ADD(%s %s(%s))"%(tbl,column_name,column_type,column_size))
                            else:
                                print("Invalid option")
                                exit()
                        elif column_type in ("decimal","Decimal"",DECIMAL"):
                            x=input("Enter column size:")
                            y=input("Enter precision:")
                            default=input("Does it have default value(y/n)")
                            if default=='y':
                                default_value=input("Enter default value:")
                                mycursor.execute("ALTER TABLE %s ADD(%s %s(%s,%s) default %s)"%(tbl,column_name,column_type,x,y,default_value))
                            elif default=='n':
                                mycursor.execute("ALTER TABLE %s ADD(%s %s(%s,%s))"%(tbl,column_name,column_type,x,y))
                            else:
                                print("Invalid choice:")
                                exit()
                        else:
                            default=input("Does it have default value(y/n)")
                            if default=='y':
                                default_value=input("Enter default value:")
                                mycursor.execute("ALTER TABLE %s ADD(%s %s default %s)"%(tbl,column_name,column_type,default_value))
                            elif default=='n':
                                mycursor.execute("ALTER TABLE %s ADD(%s %s)"%(tbl,column_name,column_type))
                            else:
                                print("Invalid choice")
                                exit()
                    except mysql.connector.errors.ProgrammingError:
                        print("you have enter incorrect format for columns")
                        print("Program is now exiting....")
                        exit()
            elif ch==2:
                column_name=input("Enter column name:")
                mycursor.execute("ALTER TABLE %s DROP %s"%(tbl,column_name))
            elif ch==3:
                cnt=int(input("How many columns do you want to modify:"))
                for i in range(1,cnt+1):
                    try:
                        column_name=input("Enter column name:")
                        column_type=input("Enter column type:")
                        if column_type in ("VARCHAR","CHAR","Varchar","Char","varchar","char"):
                            column_size=int(input("Enter column size:"))
                            mycursor.execute("ALTER TABLE %s modify %s %s(%s)"%(tbl,column_name,column_type,column_size))
                        elif column_type in ("decimal","Decimal"",DECIMAL"):
                            x=input("Enter column size:")
                            y=input("Enter precision:")
                            mycursor.execute("ALTER TABLE %s modify %s %s(%s,%s)"%(tbl,column_name,column_type,x,y))
                        else:
                            mycursor.execute("ALTER TABLE %s modify %s %s"%(tbl,column_name,column_type))
                    except mysql.connector.errors.ProgrammingError:
                        print("you have enter incorrect format for columns")
                        print("Program is now exiting....")
                        exit()
            elif ch==4:
                cnt=int(input("How many columns do you want to rename:"))
                for i in range(1,cnt+1):
                    try:
                        column_name=input("Enter old column name:")
                        column_new=input("Enter new column name:")
                        column_type=input("Enter column type:")
                        if column_type in ("VARCHAR","CHAR","Varchar","Char","varchar","char"):
                            column_size=int(input("Enter column size:"))
                            mycursor.execute("ALTER TABLE %s change %s %s %s(%s)"%(tbl,column_name,column_new,column_type,column_size))
                        elif column_type in ("decimal","Decimal"",DECIMAL"):
                            x=input("Enter column size:")
                            y=input("Enter precision:")
                            mycursor.execute("ALTER TABLE %s change %s %s %s(%s,%s)"%(tbl,column_name,column_new,column_type,x,y))
                        else:
                            mycursor.execute("ALTER TABLE %s change %s %s %s"%(tbl,column_name,column_new,column_type))
                    except mysql.connector.errors.ProgrammingError:
                        print("you have enter incorrect details for columns")
                        print("Program is now exiting....")
                        exit()
            elif ch==5:
                 try:
                     tbl=input("Enter table name:")
                     mycursor.execute("DROP TABLE %s"%tbl)
                     print("Table",tbl,"deleted")
                     print()
                 except mysql.connector.errors.ProgrammingError:
                     print("Table",tbl,"does not exist")
                     print()
            elif ch==6:
                break
            else:
                print("Invalid choice")
                print()
    elif choice==3:
        print("Which funtion do you want to use")
        print()
        while c=='y':
            print("1. Add values to column")
            print("2. Update values using condition")
            print("3. Delete values using condition")
            print("4. Delete all rows")
            print("5. Return to main menu")
            ch=int(input("Enter your choice:"))
            print()
            if ch==1:
                cnt=int(input("For how many rows do you want to add values:"))
                print("***Enter string and date enclosed in quotation***")
                for n in range(1,cnt+1):
                    columns_name=input("Enter column names seperated by commas:")
                    rows_name=input("Enter values seperated by commas:")
                    mycursor.execute("INSERT INTO %s(%s) VALUES(%s)"%(tbl,columns_name,rows_name))
                    print("Record inserted")
                    mydb.commit()
                    print()
            elif ch==2:
                condition_ask=int(input("How many conditon do you want to apply:"))
                for n in range(1,condition_ask+1):
                    print("***Enter string and date enclosed in quotation***")
                    condition=input("Enter condition:")
                    cnt=int(input("For how many rows do you want to add values:"))
                    print("***Enter string and date enclosed in quotation***")
                    print()
                    for i in range(1,cnt+1):
                        try:
                            column_name=input("Enter column name:")
                            row_name=input("Enter value:")
                            mycursor.execute("UPDATE %s SET %s = %s WHERE %s"%(tbl,column_name,row_name,condition))
                            mydb.commit()
                            print("Record updated")
                            print()
                        except mysql.connector.errors.ProgrammingError:
                            print("Unable to update value....check column formatting")
                            print()
            elif ch==3:
                condition_ask=int(input("How many conditon do you want to apply:"))
                for n in range(1,condition_ask+1):
                    print("***Enter string and date enclosed in quotation***")
                    condition=input("Enter condition:")
                    mycursor.execute("DELETE FROM %s WHERE %s"%(tbl,condition))
                    mydb.commit()
                    print("Record deleted")
                    print()
            elif ch==4:
                tbl=input("Enter table name:")
                mycursor.execute("TRUNCATE TABLE %s"%tbl)
                print("All rows are deleted")
                print()
            elif ch==5:
                break
            else:
                print("Invalid option")
                break
    elif choice==4:
        try:
            dtbs=input("Enter database name:")
            mycursor.execute("DROP DATABASE %s"%dtbs)
            print("Database",dtbs,"deleted")
            print()
        except mysql.connector.errors.DatabaseError:
            print("Database not found")
            print()
    elif choice==5:
        print("This program is now exitng")
        exit()
    else:
        print("Invalid Option")
        exit()
    c=input("Do you want to continue or not(y/n):")
    if c=='n':
        print("Thnx for using our program")


mycursor.close()
mydb.close()#closing database
