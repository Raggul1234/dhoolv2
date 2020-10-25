from tkinter import ttk
import tkinter as tk
import pyodbc


#ConnectingDatabase#

from tkinter import messagebox
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MUTHUCOMPUTER;'
                      'Database=Class4c v2;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


#Adding new record#

def save():
    Names=   (Name.get())
    Ages=    (Age.get())
    Genders= (Gender.get())
    Heights= (height.get())
    Weights= (weight.get())
    Rollnos= (StudentId.get())
    Activitytypes=(Activitytype.get())
    Activities=(Activity.get())
    extras=(extra.get())
#validation
    while True:
        try:
            #validating Name
            int(Names)
            messagebox.showinfo("Tkinter", "Name must be string")
            if len(Names)==0:
                messagebox.showinfo("Tkinter", "Name cannot be empty")
            break
        except:
            try:
                pass  
                cursor.execute("""
                INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,Genders,Heights,Weights))
                conn.commit()
                cursor.execute("""
                INSERT INTO Activity(StudentId,Name,Activitytype,Activity,extra)
                VALUES (?,?,?,?,?)
                """,(Rollnos,Names,Activitytypes,Activities,extras))
                conn.commit()
                clearfields()
                
                messagebox.showinfo("Tkinter", "Saved successfully!")
                break
            except pyodbc.IntegrityError:
                messagebox.showinfo("Tkinter", "StudentId already exists")
                break
        try:
            #validating Age
            str(Ages)
            messagebox.showinfo("Tkinter", "Age must be integer")
            if len(Ages)==0:
                messagebox.showinfo("Tkinter", "Age cannot be empty")
            break
        except:
            try:
                pass  
                cursor.execute("""
                INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,Genders,Heights,Weights))
                conn.commit()
                cursor.execute("""
                INSERT INTO Activity(StudentId,Name,Activitytype,Activity,extra)
                VALUES (?,?,?,?,?)
                """,(Rollnos,Names,Activitytypes,Activities,extras))
                conn.commit()
                clearfields()
                
                messagebox.showinfo("Tkinter", "Saved successfully!")
                break
            except pyodbc.IntegrityError:
                messagebox.showinfo("Tkinter", "StudentId already exists")
                break
        try:
            #validating Gender
            int(Genders)
            messagebox.showinfo("Tkinter", "Genders must be string")
            if Genders not in ["F","f","M","m"]:
                messagebox.showinfo("Tkinter", "Please enter m or M for male and f or F for female")
            if len(Genders)==0:
                messagebox.showinfo("Tkinter", "Gender cannot be empty")
            break
        except:
            try:
                pass  
                cursor.execute("""
                INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,Genders,Heights,Weights))
                conn.commit()
                cursor.execute("""
                INSERT INTO Activity(StudentId,Name,Activitytype,Activity,extra)
                VALUES (?,?,?,?,?)
                """,(Rollnos,Names,Activitytypes,Activities,extras))
                conn.commit()
                clearfields()
                
                messagebox.showinfo("Tkinter", "Saved successfully!")
                break
            except pyodbc.IntegrityError:
                messagebox.showinfo("Tkinter", "StudentId already exists")
                break
        try:
            #validating Height
            str(Heights)
            messagebox.showinfo("Tkinter", "Height must be integer")
            break
        except:
            try:
                pass  
                cursor.execute("""
                INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,Genders,Heights,Weights))
                conn.commit()
                cursor.execute("""
                INSERT INTO Activity(StudentId,Name,Activitytype,Activity,extra)
                VALUES (?,?,?,?,?)
                """,(Rollnos,Names,Activitytypes,Activities,extras))
                conn.commit()
                clearfields()
                
                messagebox.showinfo("Tkinter", "Saved successfully!")
                break
            except pyodbc.IntegrityError:
                messagebox.showinfo("Tkinter", "StudentId already exists")
                break
        try:
            #validating Weight
            str(Weights)
            messagebox.showinfo("Tkinter", "Weight must be integer")
            break
        except:
            try:
                pass  
                cursor.execute("""
                INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,Genders,Heights,Weights))
                conn.commit()
                cursor.execute("""
                INSERT INTO Activity(StudentId,Name,Activitytype,Activity,extra)
                VALUES (?,?,?,?,?)
                """,(Rollnos,Names,Activitytypes,Activities,extras))
                conn.commit()
                clearfields()
                
                messagebox.showinfo("Tkinter", "Saved successfully!")
                break
            except pyodbc.IntegrityError:
                messagebox.showinfo("Tkinter", "StudentId already exists")
                break
        try:
            #validating StudentId
            str(Rollnos)
            messagebox.showinfo("Tkinter", "StudentId must be integer")
            if len(Rollnos)==0:
                messagebox.showinfo("Tkinter", "studentId cannot be empty")
            break
        except:
            try:
                pass  
                cursor.execute("""
                INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,Genders,Heights,Weights))
                conn.commit()
                cursor.execute("""
                INSERT INTO Activity(StudentId,Name,Activitytype,Activity,extra)
                VALUES (?,?,?,?,?)
                """,(Rollnos,Names,Activitytypes,Activities,extras))
                conn.commit()
                clearfields()
                
                messagebox.showinfo("Tkinter", "Saved successfully!")
                break
            except pyodbc.IntegrityError:
                messagebox.showinfo("Tkinter", "StudentId already exists")
                break
        try:
            #validating Activitytypes
            int(Activitytypes)
            messagebox.showinfo("Tkinter", "Activitytype must be string")
            break
        except:
            try:
                pass  
                cursor.execute("""
                INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,Genders,Heights,Weights))
                conn.commit()
                cursor.execute("""
                INSERT INTO Activity(StudentId,Name,Activitytype,Activity,extra)
                VALUES (?,?,?,?,?)
                """,(Rollnos,Names,Activitytypes,Activities,extras))
                conn.commit()
                clearfields()
                
                messagebox.showinfo("Tkinter", "Saved successfully!")
                break
            except pyodbc.IntegrityError:
                messagebox.showinfo("Tkinter", "StudentId already exists")
                break
        try:
            #validating Activity
            int(Activities)
            messagebox.showinfo("Tkinter", "Activity must be string")
            break
        except:
            try:
                pass  
                cursor.execute("""
                INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,Genders,Heights,Weights))
                conn.commit()
                cursor.execute("""
                INSERT INTO Activity(StudentId,Name,Activitytype,Activity,extra)
                VALUES (?,?,?,?,?)
                """,(Rollnos,Names,Activitytypes,Activities,extras))
                conn.commit()
                clearfields()
                
                messagebox.showinfo("Tkinter", "Saved successfully!")
                break
            except pyodbc.IntegrityError:
                messagebox.showinfo("Tkinter", "StudentId already exists")
                break
        try:
            #validating extra
            int(extras)
            messagebox.showinfo("Tkinter", "extra must be string")
            break
        except:
            try:
                pass
                cursor.execute("""
                INSERT INTO Students(StudentId,Name, Age, Gender, Height,weight)
                VALUES (?,?,?,?,?,?)""",(Rollnos,Names,Ages,Genders,Heights,Weights))
                conn.commit()
                cursor.execute("""
                INSERT INTO Activity(StudentId,Name,Activitytype,Activity,extra)
                VALUES (?,?,?,?,?)
                """,(Rollnos,Names,Activitytypes,Activities,extras))
                conn.commit()
                clearfields()
                
                messagebox.showinfo("Tkinter", "Saved successfully!")
                break
            except pyodbc.IntegrityError:
                messagebox.showinfo("Tkinter", "StudentId already exists")
                break
        
        
            



        

#function to clear all entries
def clearfields():
    Name.delete(0 ,tk.END)
    Age.delete(0 ,tk.END)
    Gender.delete(0 ,tk.END)
    height.delete(0 ,tk.END)
    weight.delete(0 ,tk.END)
    StudentId.delete(0 ,tk.END)
    Activitytype.delete(0 ,tk.END)
    Activity.delete(0 ,tk.END)
    extra.delete(0 ,tk.END)

#Searching records    

def Search():
 
        Names= Name.get()
        Ages= Age.get()
        Genders= Gender.get()
        Heights= height.get()
        Weights= weight.get()
        Rollnos= StudentId.get()
        Activitytypes=Activitytype.get()
        Activities=Activity.get()
        extras=extra.get()

        

# clearing the tree
       
        t=tree.get_children()
        for f in t:
            tree.delete(f)
        

#Search starts
            

        if len(Names)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
            from Students A inner join Activity B on A.StudentId=B.StudentId where A.Name like(?)""",(Names))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)
                    
		
        elif  len(Ages)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
            from Students A inner join Activity B on A.StudentId=B.StudentId where A.Age like(?)""",(Ages))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(Genders)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
            from Students A inner join Activity B on A.StudentId=B.StudentId where A.Gender like(?)""",(Genders))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(Heights)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
            from Students A inner join Activity B on A.StudentId=B.StudentId where A.Height like(?)""",(Heights))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)          


        elif  len(Weights)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
            from Students A inner join Activity B on A.StudentId=B.StudentId where A._Weight like(?)""",(Weights))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(Rollnos)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
            from Students A inner join Sports B on A.StudentId=B.StudentId where A.StudentId like(?)""",(Rollnos))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(Activitytypes)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
            from Students A inner join Activity B on A.StudentId=B.StudentId where B.Activitytypes like(?)""",(Activitytypes))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)

                
        elif  len(Activity)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
            from Students A inner join Activity B on A.StudentId=B.StudentId where B.Activity like(?)""",(Activities))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)
                

        elif  len(extra)!=0:
            cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
            from Students A inner join Activity B on A.StudentId=B.StudentId where B.extra like(?)""",(estras))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)

        else:
            
            messagebox.showinfo("Tkinter", "Atleast one search criteria must be given!")     

#Search ends

#function to delete record

def delete():
        x=StudentId.get()
        cursor.execute("""
        DELETE FROM Students
        WHERE StudentId = (?)""",(x))
        conn.commit()
        cursor.execute("""
        DELETE FROM Activity
        WHERE StudentId = (?)""",(x))
        conn.commit()
        clearfields()
        messagebox.showinfo("Tkinter", "Deleted successfully!")


def getallrecords():
    t=tree.get_children()
    for f in t:
        tree.delete(f)
    cursor.execute("""select A.Name,A.Age,A.Gender,A.Height,A.Weight,A.StudentId,B.Activity
    from Students A inner join Activity B on A.StudentId=B.StudentId""")
    records=cursor.fetchall()
    for row in records:
        tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
        tree.pack(side=tk.TOP,fill=tk.X)



# defining the canvas

root= tk.Tk()
root.title("Class4c")
canvas1 = tk.Canvas(root, width = 900, height = 300)
canvas1.pack()

# Defining the fields and labels and validating

Name = tk.Entry (root)
canvas1.create_window(300, 10, window=Name)
label1 = tk.Label(root, text='Name:')
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 10, window=label1)


Age = tk.Entry (root)
canvas1.create_window(300, 40, window=Age)
label2 = tk.Label(root, text='Age:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 40, window=label2)

Gender = tk.Entry (root)
canvas1.create_window(300, 70, window=Gender)
label3 = tk.Label(root, text='Gender:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 70, window=label3)

height = tk.Entry (root)
canvas1.create_window(300, 100, window=height)
label4 = tk.Label(root, text='height in cm:')
label4.config(font=('helvetica', 10))
canvas1.create_window(195, 100, window=label4)

weight = tk.Entry (root)
canvas1.create_window(300, 130, window=weight)
label5 = tk.Label(root, text='weight in kg:')
label5.config(font=('helvetica', 10))
canvas1.create_window(195, 130, window=label5)

StudentId = tk.Entry (root)
canvas1.create_window(300, 160, window=StudentId)
label6 = tk.Label(root, text='StudentId:')
label6.config(font=('helvetica', 10))
canvas1.create_window(200, 160, window=label6)

Activitytype = tk.Entry (root)
canvas1.create_window(300, 190, window=Activitytype)
label7 = tk.Label(root, text='Activitytype:')
label7.config(font=('helvetica', 10))
canvas1.create_window(200, 190, window=label7)


Activity = tk.Entry (root)
canvas1.create_window(500, 10, window=Activity)
label8 = tk.Label(root, text='Activity:')
label8.config(font=('helvetica', 10))
canvas1.create_window(400, 10, window=label8)

extra = tk.Entry (root)
canvas1.create_window(500, 40, window=extra)
label9 = tk.Label(root, text='extra:')
label9.config(font=('helvetica', 10))
canvas1.create_window(400, 40, window=label9)

# Defining the buttons

button1 = tk.Button(text='Save',command = save)
canvas1.create_window(500, 250, window=button1)

button2 = tk.Button(text='Search',command=Search)
canvas1.create_window(400, 250, window=button2)

button3 = tk.Button(text='delete',command=delete)
canvas1.create_window(450, 250, window=button3)

button4 = tk.Button(text='get all records',command=getallrecords)
canvas1.create_window(330, 250, window=button4)


# Defining the tree

tree=ttk.Treeview(root)
tree["columns"]=("one","two","three","four","five","six")
tree.column("#0", width=130, minwidth=270, stretch=tk.NO)
tree.column("one", width=100, minwidth=150, stretch=tk.NO)
tree.column("two", width=100, minwidth=100)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("one", text="Age",anchor=tk.W)
tree.heading("two", text="Gender",anchor=tk.W)
tree.heading("three", text="Height",anchor=tk.W)
tree.heading("four", text="Weight",anchor=tk.W)
tree.heading("five", text="StudentId",anchor=tk.W)
tree.heading("six", text="Activity",anchor=tk.W)
tree.pack()
 
root.mainloop()












































































































