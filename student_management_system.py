#pip3 install PyMySQL
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#connection later
def connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="Jg3_arciniegas",
        db="students_db"
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
        
    for array in read():
        my_tree.insert(parent="",
                       index="end",
                       iid=array,
                       text="",
                       values=(array),
                       tag="orow")
    my_tree.tag_configure("orow",background="#EEEEEE",font=("Arial",12))
    my_tree.grid(row=8,column=0,columnspan=5,rowspan=11,padx=10,pady=20)
#GUI
root = Tk()
root.title("Student Registration System")
root.geometry("1200x720")
my_tree = ttk.Treeview(root)

#placeholders for entry
ph1=tk.StringVar()
ph2=tk.StringVar()
ph3=tk.StringVar()
ph4=tk.StringVar()
ph5=tk.StringVar()

def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)

#function later
def read():
    conn=connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students")
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results 

def add():
    studid=str(studid_entry.get())
    fname=str(fname_entry.get())
    lname=str(lname_entry.get())
    address=str(address_entry.get())
    number=str(number_entry.get())
    
    if (id=="" or id==" ") or (fname=="" or fname==" ") or (lname=="" or lname==" ") or (address=="" or address==" ") or (number=="" or number==" "):
        messagebox.showinfo("Error","Please fill up the blank entry")
        return
    else:
        try:
            conn=connection()
            cursor=conn.cursor()
            cursor.execute("INSERT INTO students VALUES('"+studid+"','"+fname+"','"+lname+"','"+address+"','"+number+"')")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error","Student ID already exist")
            return
    refreshTable() 

def reset():
    decision=messagebox.askquestion("Warning!!","Delete all data?")
    if decision != "yes":
        return
    else:
        try:
            conn=connection()
            cursor=conn.cursor()
            cursor.execute("DELETE FROM students")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error","Sorry an error occured") 
            return
    refreshTable()  
    
def delete():
    decision=messagebox.askquestion("Warning!!","Delete the selected data?")
    if decision != "yes":
       return
    else:
        selected_item=my_tree.selection()[0]
        deleteData=str(my_tree.item(selected_item)["values"][0])
        try:
            conn=connection()
            cursor=conn.cursor()
            cursor.execute("DELETE FROM students WHERE STUDID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error","Sorry an error occured")
            return
    
    refreshTable()
    
def select():
    
    try:
        selected_item=my_tree.selection()[0]
        studid=str(my_tree.item(selected_item)["values"][0])
        fname=str(my_tree.item(selected_item)["values"][1])
        lname=str(my_tree.item(selected_item)["values"][2])
        address=str(my_tree.item(selected_item)["values"][3])
        phone=str(my_tree.item(selected_item)["values"][4])
        
        setph(studid,1)
        setph(fname,2)
        setph(lname,3)
        setph(address,4)
        setph(phone,5)
        
            
    except:
        messagebox.showinfo("Erorr","Please select a data row")
            
def search():
    studid=str(studid_entry.get())
    fname=str(fname_entry.get())
    lname=str(lname_entry.get())
    address=str(address_entry.get())
    phone=str(number_entry.get())
    
    conn=connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students WHERE STUDID='"+
    studid+"' or FNAME='"+
    fname+"' or LNAME='"+
    lname+"' or ADDRESS='"+
    address+"' or PHONE='"+
    phone+"' ")
    
    try:
        results=cursor.fetchall()
        for num in range(0,5):
            setph(results[0][num],(num+1))
            
        conn.commit()
        conn.close()
        
    except:
        messagebox.showinfo("Error","No data founded")
        
def update():
    selectedstudid=""
    try:
        selected_item=my_tree.selection()[0]
        selectedstudid=str(my_tree.item(selected_item)["values"][0])
    except:
        messagebox.showinfo("Error","Please select a data row")
        
    studid=str(studid_entry.get())
    fname=str(fname_entry.get())
    lname=str(lname_entry.get())
    address=str(address_entry.get())
    phone=str(number_entry.get())
    
    if (studid=="" or studid==" ") or (fname=="" or fname==" ") or (lname=="" or lname==" ") or (address=="" or address==" ") or (phone=="" or phone==" "):
        messagebox.showinfo("Error","Please fill up the blank entry")
        return
    else:
        try:
            conn=connection()
            cursor=conn.cursor()
            cursor.execute("UPDATE students SET STUDID='"+
            studid+"', FNAME='"+
            fname+"', LNAME='"+
            lname+"', ADDRESS='"+
            address+"', PHONE='"+
            phone+"' WHERE STUDID='"+
            selectedstudid+"' ")
        except:
            messagebox.showinfo("Error","Stud ID already exist")
            return
        
    refreshTable()
    
    conn.commit()
    conn.close()
    
    
    
    
    
    
    

#GUI part 2
label = Label(root,text="Student Registration System (CRUD MATRIX)", font=("Arial Bold", 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

#Student_Labels
studid_label = Label(root,text="Student ID", font=("Roboto",15))
fname_label = Label(root, text="First name",font=("Roboto",15))
lname_label = Label(root,text="Last name",font=("Roboto",15))
address_label = Label(root,text="Address", font=("Roboto",15))
number_label = Label(root,text="Phone number",font=("Roboto",15))

#Student_Grids
studid_label.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
fname_label.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
lname_label.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
address_label.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
number_label.grid(row=7,column=0,columnspan=1,padx=50,pady=5)

#Student_Entries
studid_entry = Entry(root, width=55,bd=5, font=("Roboto",15),textvariable=ph1)
fname_entry = Entry(root,width=55,bd=5,font=("Roboto",15),textvariable=ph2)
lname_entry = Entry(root,width=55,bd=5,font=("Roboto",15),textvariable=ph3)
address_entry = Entry(root,width=55,bd=5,font=("Roboto",15),textvariable=ph4)
number_entry = Entry(root,width=55,bd=5,font=("Roboto",15),textvariable=ph5)

#Student_Entry_Grid
studid_entry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
fname_entry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
lname_entry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
address_entry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
number_entry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)

#Button_code
addBtn=Button(
    root,text="Add", padx=65, pady=25, width=10,bd=5,font=("Arial",15),bg="#84F894",command=add
)
updateBtn=Button(
    root,text="Update",padx=65,pady=25, width=10,bd=5,font=("Arial",15),bg="#84F894",command=update
)
deleteBtn=Button(
    root,text="Delete",padx=65,pady=25, width=10,bd=5,font=("Arial",15),bg="#FF9999",command=delete
)
searchBtn=Button(
    root,text="Search",padx=65,pady=25,width=10,bd=5,font=("Arial",15),bg="#F4FE82",command=search
)
resetBtn=Button(
    root,text="Reset",padx=65,pady=25,width=10,bd=5,font=("Arial",15),bg="#F398FF",command=reset
)
selectBtn=Button(
    root,text="Select",padx=65,pady=25,width=10,bd=5,font=("Arial",15),bg="#EEEEEE",command=select
)

addBtn.grid(row=3,column=5,columnspan=1,rowspan=2)
updateBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
deleteBtn.grid(row=7,column=5,columnspan=1,rowspan=2)
searchBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
resetBtn.grid(row=11,column=5,columnspan=1,rowspan=2)
selectBtn.grid(row=13,column=5,columnspan=1,rowspan=2)

style=ttk.Style()
style.configure("Treeview.Heading",font=("Arial Bold",15))
my_tree["column"]=("Stud ID","Firstname","Lastname","Address","Phone")

my_tree.column("#0",width=0,stretch=NO)
my_tree.column("Stud ID",anchor=W,width=170)
my_tree.column("Firstname",anchor=W,width=150)
my_tree.column("Lastname",anchor=W,width=150)
my_tree.column("Address",anchor=W,width=165)
my_tree.column("Phone",anchor=W,width=150)

my_tree.heading("Stud ID",text="Student ID",anchor=W)
my_tree.heading("Firstname",text="Firstname",anchor=W)
my_tree.heading("Lastname",text="Lastname",anchor=W)
my_tree.heading("Address",text="Address",anchor=W)
my_tree.heading("Phone",text="Phone",anchor=W)

refreshTable()

root.mainloop()