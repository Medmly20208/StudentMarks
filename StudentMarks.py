import sqlite3
#set up of the database and the student Table

db = sqlite3.connect("Student.db")
cr = db.cursor()
cr.execute("Create Table if not exists Stud(Id_S integer,fullname text,math integer,physics integer,chemistry integer,average integer )")

#####################################################################
#set the fucntions
#ADD FUNCTION
def add(name,m,p,c,e):
        j = (m+p+c)/3
        cr.execute(f"""insert into Stud(Id_s,fullname,math,physics,chemistry,average) values({e},'{name}',{m},{p},{c},{j})""")
        print("succefully added")

#DELETE FUNCTION
def delete(idpe):
    cr.execute("select Id_s from Stud")
    z = []
    all_id = cr.fetchall()
    for i in range(0,len(all_id)):
        f = str(all_id[i])
        z.append(f[1:-2])

    if str(idpe) in z:
        cr.execute(f"delete from Stud where Id_s = {idpe}")
        print("succefully deleted")
    else:
        print("this ID doesn't exist ")

#UPDATE FUNCTION
def update(idpe):
    print("if you wanna update chemistry grade type the grade or type -1 to pass")
    ch = int(input())


    if ch !=-1:
        while ch < 0 or ch > 20:
            print("please enter a valid mark")
            ch = int(input())
        cr.execute(f"update Stud set chemistry = {ch} where Id_s = {idpe}")
        cr.execute(f"select physics , math from Stud where Id_s = {idpe}")
        a,b = cr.fetchone()
        to = (a+b+ch)/3
        cr.execute(f"update Stud set average = {to} where Id_s = {idpe}")
        print("updated succefully")
    else:
        pass
    print("if you wanna update math grade type the grade or type -1 to pass")
    ch = int(input())
    if ch !=-1:
        while ch < 0 or ch > 20:
            print("please enter a valid mark")
            ch = int(input())
        cr.execute(f"update Stud set math = {ch} where Id_s = {idpe}")
        cr.execute(f"select physics , chemistry from Stud where Id_s = {idpe}")
        a,b = cr.fetchone()
        to = (a+b+ch)/3
        cr.execute(f"update Stud set average = {to} where Id_s = {idpe}")
        print("updated succefully")
    else:
        pass
    print("if you wanna update physics grade type the grade or type -1 to pass")
    ch = int(input())
    if ch !=-1:
        while ch < 0 or ch > 20:
            print("please enter a valid mark")
            ch = int(input())
        cr.execute(f"update Stud set physics = {ch} where Id_s = {idpe}")
        cr.execute(f"select math,chemistry from Stud where Id_s = {idpe}")
        a,b = cr.fetchone()
        to = (a+b+ch)/3
        cr.execute(f"update Stud set average = {to} where Id_s = {idpe}")
        print("updated succefully")
    else:
        pass
#GET FUNCTION
def get(idpe):
    cr.execute("select * from Stud ")
    l = cr.fetchone()
    print("this is the infos of the ID",idpe,":")
    print(f"name==>{l[1]}\nmath==>{l[2]}\nphysics==>{l[3]}\nchemistry==>{l[4]}\naverage==>{l[5]}")


#succed FUNCTION

def succeed():
    cr.execute("select Id_s,fullname,average from Stud where average >= 10")
    d = cr.fetchall()
    if len(d) == 0:
        print("unfortunately no one succeed")
    else:
        print("number of student who succeed is ",len(d))
        for i in range(0,len(d)):
            print(f"ID ==> {d[i][0]} fullname ==> {d[i][1]} average ==> {d[i][2]}")


def failure():
    cr.execute("select Id_s,fullname,average from Stud where average < 10")
    d = cr.fetchall()
    if len(d) == 0:
        print("fortunately no one failed")
    else:
        print("number of student who failed is ",len(d))
        for i in range(0,len(d)):
            print(f"ID ==> {d[i][0]} fullname ==> {d[i][1]} average ==> {d[i][2]}")

def deleteall():
    cr.execute("delete from Stud where 1")


#FINICH DIFINITION OF FUNCTION
#########################################################################################################################3




print("welcome to my application")
print("choose the equivalent number of the operation you wanna do:")

while True:
    print("choose the equivalent number of the operation you wanna do:")
    print("1- add a student\n2- delete a student\n3- update student grades\n4- get student grades\n5- succeed students \n6- student who failed \n7- delete all the student\n8- quit the app")
    ch = int(input())
    if ch == 8:
        break
    while ch not in list(range(1,8)):
        print("invalid input ")
        print("please enter a number between 1 and 7")
        ch = int(input())


    if ch == 1:
        con = True
        while con:
            print("please enter an id:")
            a = int(input())
            cr.execute("select Id_s from Stud")
            z = []
            all_id = cr.fetchall()
            for i in range(0,len(all_id)):
                f = str(all_id[i])
                z.append(f[1:-2])
            if str(a) in z:
                print("this id already existed")
            else:
                con = False

        print("please enter a name:")
        b = input()

        print("please enter math mark:")
        c = int(input())
        while c < 0 or c > 20:
            print("invalid mark")
            print("please enter math mark:")
            c = int(input())


        print("please enter physics mark:")
        d = int(input())
        while d < 0 or d > 20:
            print("invalid mark")
            print("please enter physics mark:")
            d = int(input())
        print("please enter chemistry mark:")
        r = int(input())
        while r < 0 or r > 20:
            print("invalid mark")
            print("please enter physics mark:")
            r = int(input())
        add(b,c,d,r,a)



    elif ch == 2:
        mlo = list(cr.execute("select * from Stud"))
        if len(mlo) == 0:
            print("no student exist in table you have to add a student to do this operation")
        else:
            con = True
            while con:
                print("please enter an id:")
                k = int(input())
                cr.execute("select Id_s from Stud")
                z = []
                all_id = cr.fetchall()
                for i in range(0,len(all_id)):
                    f = str(all_id[i])
                    z.append(f[1:-2])
                if str(k) not in z:
                    print("this id doesn't existe")
                else:
                    con = False
            delete(k)
            pass

    elif ch == 4:
        mlo = list(cr.execute("select * from Stud"))
        if len(mlo) == 0:
            print("no student exist in table you have to add a student to do this operation")
        else:
            con = True
            while con:
                print("please enter an id:")
                k = int(input())
                cr.execute("select Id_s from Stud")
                z = []
                all_id = cr.fetchall()
                for i in range(0,len(all_id)):
                    f = str(all_id[i])
                    z.append(f[1:-2])
                if str(k) not in z:
                    print("this id doesn't exist")
                else:
                    con = False
            get(k)

    elif ch == 3:
        mlo = list(cr.execute("select * from Stud"))
        if len(mlo) == 0:
            print("no student exist in table you have to add a student to do this operation")
        else:
            con = True
            while con:
                print("please enter an id:")
                k = int(input())
                cr.execute("select Id_s from Stud")
                z = []
                all_id = cr.fetchall()
                for i in range(0,len(all_id)):
                    f = str(all_id[i])
                    z.append(f[1:-2])
                if str(k) not in z:
                    print("this id doesn't exist")
                else:
                    con = False
            update(k)


    elif ch == 5:
        mlo = list(cr.execute("select * from Stud"))
        if len(mlo) == 0:
            print("no student exist in table you have to add a student to do this operation")
        else:
            succeed()
    elif ch==6:
        mlo = list(cr.execute("select * from Stud"))
        if len(mlo) == 0:
            print("no student exist in table you have to add a student to do this operation")
        else:
            failure()

    elif ch == 7:
        mlo = list(cr.execute("select * from Stud"))
        if len(mlo) == 0:
            print("no student exist in table you have to add a student to do this operation")
        else:
            deleteall()
            print("donne succefully")
    else:
        pass



    db.commit()






db.close()
print("thanks for using our app ")
