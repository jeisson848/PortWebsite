from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
import pymysql
from tkinter import messagebox
from PIL import Image, ImageTk
from pymysql import IntegrityError


def connection():
    
    conn=pymysql.connect(
    host="localhost",
    user="root",
    db="login_patient",
    password="Jg3_arciniegas"
    
    )
    return conn



def create_account(Login, password):
    try:
        conn = connection()
        cursor = conn.cursor()
        # Replace 'users' with your actual table name
        query = "INSERT INTO sign_in (Login, password) VALUES (%s, %s)"
        cursor.execute(query, (Login, password))
        conn.commit()
        messagebox.showinfo("Account Creation", "Account created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error creating account: {e}")
    finally:
        cursor.close()
        conn.close()






def sign_in(Login, Password):
    try:
        conn = connection()
        cursor = conn.cursor()

        query = "SELECT * FROM sign_in WHERE Login = %s AND Password = %s"
        cursor.execute(query, (Login, Password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Sign in", "Sign in successful!")
            main_screen()
        else:
            messagebox.showwarning("Sign in", "Invalid username or password.")
            # Clear entry fields after a failed login attempt
            Entry_login.delete(0, END)
            Entry_password.delete(0, END)

    except Exception as e:
        messagebox.showerror("Error", f"Error signing in: {e}")
    finally:
        cursor.close()
        conn.close()



def open_create_account_window():
    
    
    create_account_window = Toplevel(root)
    create_account_window.title("Create Account")
    create_account_window.geometry("2200x1000")
    create_account_window.configure(bg="lightgrey")


    # Add widgets for account creation in the new window
    Label(create_account_window, text="Create an Account",bd=5, font=("@HP Simplified Hans Light", 50,"bold"),bg="darkgrey",fg="blue").pack(pady=10)
    
    username_label = Label(create_account_window, text="Username:",font=("@HP Simplified Hans Light",30),bd=10,bg="darkgrey",fg="blue")
    username_label.pack()
    username_entry = Entry(create_account_window,bd=10,width=40,font=("@HP Simplified Hans Light",15))
    username_entry.pack()

    password_label = Label(create_account_window, text="Password:",bd=10,font=("@HP Simplified Hans Light",30),bg="darkgrey",fg="blue")
    password_label.pack()
    password_entry = Entry(create_account_window, show="*",bd=10,width=40,font=("@HP Simplified Hans Light",15))
    password_entry.pack()

    create_button = Button(
        create_account_window, text="Create Account",bd=10,
        command=lambda: create_account(username_entry.get(), password_entry.get())
    )
    create_button.pack(pady=50)







def patient_history():
    
    conn=pymysql.connect(
    host="localhost",
    user="root",    
    password="Jg3_arciniegas",
    db="patient_db"    
    )
    return conn


def refreshTable():
    try:
        if my_tree is not None:
            for data in my_tree.get_children():
                my_tree.delete(data)

            results = read()
            if results is not None:
                for array in results:
                    my_tree.insert(parent="",
                                   index="end",
                                   iid=array,
                                   text="",
                                   values=(array),
                                   tag="orow")
                my_tree.tag_configure("orow", background="#EEEEEE", font=("Arial", 12))
                my_tree.pack(padx=10, pady=20)
            else:
                messagebox.showinfo("No Data", "No data to display.")
        else:
            messagebox.showinfo("Error", "Treeview not initialized.")
    except Exception as e:
        messagebox.showerror("Error", f"Error refreshing table: {e}")




    

    


#function later
def read():
    conn=patient_history()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM patient_intel")
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results 

def main_screen():
    global my_tree
    
    main_screen_window = tk.Toplevel(root)
    main_screen_window.configure(bg="lightgrey")
    main_screen_window.geometry('2300x1100')
    
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

    Frame_screen = Frame(main_screen_window, bg="darkgrey")
    Frame_screen.pack(side="left", fill="y", padx=10, anchor='nw')

    New_frame = Frame(main_screen_window, bg="grey")
    New_frame.pack(side="left", fill="y", anchor='nw')

    main_screen_title = Label(Frame_screen, text="Patient Database System", font=("@HP Simplified Hans Light", 20, "bold"),
                              bg="black", fg="white")
    Label_id = Label(Frame_screen, text="Patient ID:", font=("@HP Simplified Hans Light", 10, "bold"))
    Label_name = Label(Frame_screen, text="Patient name:", font=("@HP Simplified Hans Light", 10, "bold"))
    Label_DOB = Label(Frame_screen, text="Birthdate:", font=("@HP Simplified Hans Light", 10, "bold"))
    Label_tooth = Label(Frame_screen, text="Tooth number:", font=("@HP Simplified Hans Light", 10, "bold"))
    Label_insurance = Label(Frame_screen, text="Insurance:", font=("@HP Simplified Hans Light", 10, "bold"), )
    Label_completion = Label(Frame_screen, text="Date Completed:", font=("@HP Simplified Hans Light", 10, "bold"))
    Label_paidment = Label(Frame_screen, text="Paidment:", font=("@HP Simplified Hans Light", 10, "bold"))
    Label_estimate_number = Label(Frame_screen, text="Estimate number:", font=("@HP Simplified Hans Light", 10, "bold"))

    main_screen_title.grid(padx=0, row=0, column=0)
    Label_id.grid(padx=5, row=6, rowspan=2, pady=10, columnspan=5, column=0)
    Label_name.grid(padx=5, row=9, rowspan=5, pady=25, columnspan=5, column=0)
    Label_DOB.grid(padx=5, row=12, rowspan=5, pady=75, columnspan=5, column=0)
    Label_tooth.grid(padx=5, row=16, rowspan=5, pady=10, columnspan=5, column=0)
    Label_insurance.grid(padx=5, row=21, rowspan=5, pady=45, columnspan=5, column=0)
    Label_completion.grid(padx=5, row=28, rowspan=2, pady=10, columnspan=5, column=0)
    Label_paidment.grid(padx=5, row=37, rowspan=2, pady=15, columnspan=5, column=0)
    Label_estimate_number.grid(padx=5, row=43, rowspan=2, pady=20, columnspan=5, column=0)

    Entry_id = Entry(Frame_screen, bd=5, width=20, font=("@HP Simplified Hans Light", 15, "bold"))
    Entry_name = Entry(Frame_screen, bd=5, width=20, font=("@HP Simplified Hans Light", 15, "bold"))
    Entry_DOB = Entry(Frame_screen, bd=5, width=20, font=("@HP Simplified Hans Light", 15, "bold"))
    Entry_tooth = Entry(Frame_screen, bd=5, width=20, font=("@HP Simplified Hans Light", 15, "bold"))
    Entry_insurance = Entry(Frame_screen, bd=5, width=20, font=("@HP Simplified Hans Light", 15, "bold"))
    Entry_completion = Entry(Frame_screen, bd=5, width=20, font=("@HP Simplified Hans Light", 15, "bold"))
    Entry_paidment = Entry(Frame_screen, bd=5, width=20, font=("@HP Simplified Hans Light", 15, "bold"))
    Entry_estimate_number = Entry(Frame_screen, bd=5, width=20, font=("@HP Simplified Hans Light", 15, "bold"))

    Entry_id.grid(padx=5, row=8, column=0, columnspan=5, rowspan=4)
    Entry_name.grid(padx=5, row=12, column=0, columnspan=5, rowspan=3)
    Entry_DOB.grid(padx=5, row=14, column=0, columnspan=5, rowspan=3)
    Entry_tooth.grid(padx=5, row=19, column=0, columnspan=5, rowspan=3)
    Entry_insurance.grid(padx=5, row=24, column=0, columnspan=5, rowspan=3)
    Entry_completion.grid(padx=5, row=31, column=0, columnspan=5, rowspan=3)
    Entry_paidment.grid(padx=5, row=39, column=0, columnspan=5, rowspan=2)
    Entry_estimate_number.grid(padx=5, row=45, column=0, columnspan=5, rowspan=2)

    def add():
        id = str(Entry_id.get())
        name = str(Entry_name.get())
        dob = str(Entry_DOB.get())
        tooth = str(Entry_tooth.get())
        insurance = str(Entry_insurance.get())
        completion = str(Entry_completion.get())
        paidment = str(Entry_paidment.get())
        estimate_number = str(Entry_estimate_number.get())

        if (id == "" or id == " ") or (name == "" or name == " ") or (dob == "" or dob == " ") or \
            (tooth == "" or tooth == " ") or (insurance == "" or insurance == " ") or \
            (completion == "" or completion == " ") or (paidment == "" or paidment == " ") or \
            (estimate_number == "" or estimate_number == " "):
            messagebox.showinfo("Error", "Please fill up the blank entry")
            return
        else:
            try:
                conn = patient_history()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO patient_intel VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                            (id, name, dob, tooth, insurance, completion, paidment, estimate_number))
                conn.commit()
                conn.close()
                refreshTable()
            except IntegrityError as e:
                error_message = f"Error adding data: {e}\n\nRecord with ID {id} already exists."
                messagebox.showerror("Error", error_message)
            except Exception as e:
                print(f"Error: {e}")
                messagebox.showinfo("Error", "An error occurred while adding data.")

            refreshTable()
    def select():
        
        try:
                selected_item=my_tree.selection()[0]
                id=str(my_tree.item(selected_item)["values"][0])
                name=str(my_tree.item(selected_item)["values"][1])
                dob=str(my_tree.item(selected_item)["values"][2])
                tooth=str(my_tree.item(selected_item)["values"][3])
                insurance=str(my_tree.item(selected_item)["values"][4])
                completion=str(my_tree.item(selected_item)["values"][5])
                estimate_number=str(my_tree.item(selected_item)["values"][6])
                setph(id,1)
                setph(name,2)
                setph(dob,3)
                setph(tooth,4)
                setph(insurance,5)
                setph(completion,6)
                setph(estimate_number,7)
                
                
            
            
                
        except:
                messagebox.showinfo("Erorr","Please select a data row")     
    
            
            
    def search():
        id=str(Entry_id.get())
        name=str(Entry_name.get())
        dob=str(Entry_DOB.get())
        tooth=str(Entry_tooth.get())
        insurance=str(Entry_insurance.get())
        completion=str(Entry_completion.get())
        paidment=str(Entry_paidment.get())
        estimate_number=str(Entry_estimate_number.get())
    
        conn=patient_history()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM patient_intel WHERE id='"+
        id+"' or patients_name='"+
        name+"' or DOB='"+
        dob+"' or patients_tooth='"+
        tooth+"' or insurance='"+
        insurance+"' or date_completed='"+
        completion+"' or paidment='"+
        paidment+"' or estimate_number='"+
        estimate_number+"' ")
        
        
    
        try:
            results = cursor.fetchall()
            # Clear existing data in the Treeview
            my_tree.delete(*my_tree.get_children())
            
            for array in results:
                my_tree.insert(parent="", index="end", iid=array, text="", values=(array), tag="orow")
                
            my_tree.tag_configure("orow", background="#EEEEEE", font=("Arial", 12))
            my_tree.pack(padx=10, pady=20)

            conn.commit()
            conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error during search: {e}")
    
            
        
        
        
        
        
                
         
        
            
        
        
        
        
        
        
        
        
        
        
               
        
        
    
    def delete():
        decision=messagebox.askquestion("Warning!!","Delete the selected data?")
        if decision != "yes":
            return
        else:
            # Check if any item is selected
            if not my_tree.selection():
                messagebox.showinfo("Error", "No item selected for deletion")
                return
            selected_item=my_tree.selection()[0]
            deleteData=str(my_tree.item(selected_item)["values"][0])

            try:
                conn=patient_history()
                cursor=conn.cursor()
                cursor.execute("DELETE FROM  patient_intel WHERE id='"+str(deleteData)+"'")
                conn.commit()
                conn.close()
            except:
                messagebox.showinfo("Error","Sorry an error occured")
                return
        
    def update():
        selectedpatid = ""
        try:
            selected_item = my_tree.selection()[0]
            selectedpatid = str(my_tree.item(selected_item)["values"][0])
        except:
            messagebox.showinfo("Error", "Please select a data row")

        id = str(Entry_id.get())
        name = str(Entry_name.get())
        dob = str(Entry_DOB.get())
        tooth = str(Entry_tooth.get())
        insurance = str(Entry_insurance.get())
        completion = str(Entry_completion.get())
        paidment = str(Entry_paidment.get())
        estimate_number = str(Entry_estimate_number.get())

        if (
            id == "" or id == " "
            or name == "" or name == " "
            or dob == "" or dob == " "
            or tooth == "" or tooth == " "
            or insurance == "" or insurance == " "
            or completion == "" or completion == " "
            or paidment == "" or paidment == " "
            or estimate_number == "" or estimate_number == " "
        ):
            messagebox.showinfo("Error", "Please fill up the blank entry")
            return
        else:
            try:
                conn = patient_history()
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE patient_intel SET id='" +
                    id + "', patients_name='" +
                    name + "', DOB='" +
                    dob + "', patients_tooth='" +
                    tooth + "', insurance='" +
                    insurance + "', date_completed='" +
                    completion + "', paidment='" +
                    paidment + "', estimate_number='" +
                    estimate_number + "' WHERE id='" +
                    selectedpatid + "'"
                )

            except:
                messagebox.showinfo("Error", "Patient ID already exists")
                return

        refreshTable()

        conn.commit()
        conn.close()

    

        
        
    
    
    
    
    
    
        
     #Button_code
    addBtn=Button(
            main_screen_window,text="Add", padx=65, pady=25, width=10,bd=5,font=("Arial",15),bg="#84F894",command=add
        )
        
    
    
    selectBtn=Button(
            main_screen_window,text="Select",padx=65,pady=25,width=10,bd=5,font=("Arial",15),bg="#EEEEEE",command=select
        )
    
    
    deleteBtn=Button(
            main_screen_window,text="Delete",padx=65,pady=25, width=10,bd=5,font=("Arial",15),bg="#FF9999",command=delete
        )
    
    searchBtn = Button(
        main_screen_window, text="Search", padx=65, pady=25, width=10, bd=5, font=("Arial", 15), bg="#F4FE82",
        command=search
        )
    
    updateBtn=Button(
           main_screen_window,text="Update",padx=65,pady=25, width=10,bd=5,font=("Arial",15),bg="#84F894",command=update
        )
    
    addBtn.pack(side="bottom", pady=(0, 10), anchor="sw")
    selectBtn.pack(side="bottom", pady=(0, 10), anchor="sw")
    deleteBtn.pack(side="bottom", pady=(0, 10), anchor="sw")
    updateBtn.pack(side="bottom", pady=(0, 10), anchor="sw")
    searchBtn.pack(side="bottom", pady=(0, 10), anchor="sw")
    
    
    
    
    
        
    # Treeview inside the dashboard window
    my_tree = ttk.Treeview(main_screen_window)
    my_tree["column"] = ("ID", "NAME", "DOB", "TOOTH", "INSURANCE","COMPLETION","PAIDMENT","ESTIMATE NUMBER")
        
    # Customize Treeview as needed
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial Bold", 15))
        
    my_tree.pack(padx=300,pady=300,anchor='nw')
        
    my_tree.column("#0",width=1,stretch=NO)
    my_tree.column("ID",anchor=W,width=170)
    my_tree.column("NAME",anchor=W,width=150)
    my_tree.column("DOB",anchor=W,width=140)
    my_tree.column("TOOTH",anchor=W,width=90)
    my_tree.column("INSURANCE",anchor=W,width=140)
    my_tree.column("COMPLETION",anchor=W,width=150)
    my_tree.column("PAIDMENT",anchor=W,width=120)
    my_tree.column("ESTIMATE NUMBER",anchor=W,width=199)
        

    my_tree.heading("ID",text="ID",anchor=W)
    my_tree.heading("NAME",text="NAME",anchor=W)
    my_tree.heading("DOB",text="DOB",anchor=W)
    my_tree.heading("TOOTH",text="TOOTH",anchor=W)
    my_tree.heading("INSURANCE",text="INSURANCE",anchor=W)
    my_tree.heading("COMPLETION",text="COMPLETION",anchor=W)
    my_tree.heading("PAIDMENT",text="PAIDMENT",anchor=W)
    my_tree.heading("ESTIMATE NUMBER",text="ESTIMATE NUMBER",anchor=W)
    
    
           


    refreshTable()

   

root=tk.Tk()
root.geometry("2300x1000")
my_tree=ttk.Treeview(root)
root.configure(background="grey")


#Label for GUI for Login
Label_title=Label(root,text="Patient intel Database",font=("@HP Simplified Hans Light",50,"bold"),bg="grey")
Label_login=Label(root,text="Login",font=("@HP Simplified Hans Light",15,"bold"),bg="darkgrey",bd=5)
Label_password=Label(root,text="Password",font=("@HP Simplified Hans Light",15,"bold"),bg="dark grey",bd=5)


#Grid Label for GUI for Login
Label_title.grid(padx=0,pady=1,rowspan=4,columnspan=2,column=0)
Label_login.grid(padx=2,pady=100,column=0)
Label_password.grid(padx=2,pady=25,column=0)

#Entries for GUI for Login
Entry_login = Entry(root,font=("@HP Simplified Hans Light",15),bd=5,width=40)
Entry_password=Entry(root,font=("@HP Simplified Hans Light",15),bd=5,width=40)


#Grid Entry for GUI for Login
Entry_login.grid(padx=10,row=4,column=1)
Entry_password.grid(padx=10,row=5,column=1)


    

signup=Button(
    root,text="Sign in",font=("@HP Simplified Hans Light",15,"bold"),bd=5,command=lambda: sign_in(Entry_login.get(),Entry_password.get())
)




signup.grid(padx=3,pady=30,column=1)




# Create an account link
create_account_label = tk.Label(root, text="Create an Account", bg="lightgrey", fg="blue", cursor="hand2")
create_account_label.grid(padx=11,row=7,column=1)
# Bind the click event to the link
create_account_label.bind("<Button-1>", lambda event: open_create_account_window())







#Buttons for GUI for Login


    
my_tree = None
root.mainloop()