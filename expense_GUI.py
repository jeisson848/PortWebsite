import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pymysql


def connection():
    
    conn=pymysql.connect(
    host="localhost",
    user="root",    
    password="Jg3_arciniegas",
    db="Login_page"    
    )
    return conn


def create_account(Login, password):
    try:
        conn = connection()
        cursor = conn.cursor()
        # Replace 'users' with your actual table name
        query = "INSERT INTO Login_Password (Login, password) VALUES (%s, %s)"
        cursor.execute(query, (Login, password))
        conn.commit()
        messagebox.showinfo("Account Creation", "Account created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error creating account: {e}")
    finally:
        cursor.close()
        conn.close()

def open_dashboard():
    def go_back():
        dashboard_window.destroy()
    
    dashboard_window = tk.Toplevel(root)
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("2200x1000")
    dashboard_window.configure(bg="darkgreen")
    
  
    
# Sidebar menu
    sidebar_frame = Frame(dashboard_window, bg="lightgreen", width=20, height=600)
    sidebar_frame.pack(side="left", fill="y")

    # Add widgets to the sidebar
    sidebar_label = Label(sidebar_frame, text="Sidebar Menu", font=("Arial", 25), bg="beige", fg="darkgreen")
    sidebar_label.pack(pady=20)

    sidebar_button1 = Button(sidebar_frame, text="Option 1", bg="darkgreen", fg="white",width=20)
    sidebar_button1.pack(pady=5)

    sidebar_button2 = Button(sidebar_frame, text="Option 2", bg="darkgreen", fg="white",width=20)
    sidebar_button2.pack(pady=5)
    
    sidebar_button3= Button(sidebar_frame,text="Option 3",bg="darkgreen",fg="white",width=20)
    sidebar_button3.pack(pady=5)
    
    sidebar_button4 = Button(sidebar_frame,text="Option 4",bg="darkgreen",fg="white",width=20)
    sidebar_button4.pack(pady=5)
    
    sidebar_button5 = Button(sidebar_frame,text="Option 5",bg="darkgreen",fg="white",width=20)
    sidebar_button5.pack(pady=5)
    
    back_button = Button(sidebar_frame, text="Back", command=go_back)
    back_button.pack(pady=10)
    
    

    global my_tree
    
   # Treeview inside the dashboard window
    my_tree = ttk.Treeview(dashboard_window)
    my_tree["column"] = ("PaymentType", "Deposits", "Purchase", "Withdrawls", "Payments","Amount","Writtento","Date")
    
    # Customize Treeview as needed
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial Bold", 15))
    
    my_tree.pack(padx=200,pady=150)
    
    my_tree.column("#0",width=30,stretch=NO)
    my_tree.column("PaymentType",anchor=W,width=170)
    my_tree.column("Deposits",anchor=W,width=150)
    my_tree.column("Purchase",anchor=W,width=150)
    my_tree.column("Withdrawls",anchor=W,width=165)
    my_tree.column("Payments",anchor=W,width=150)
    my_tree.column("Amount",anchor=W,width=150)
    my_tree.column("Writtento",anchor=W,width=150)
    my_tree.column("Date",anchor=W,width=90)
    

    my_tree.heading("PaymentType",text="PaymentType",anchor=W)
    my_tree.heading("Deposits",text="Deposits",anchor=W)
    my_tree.heading("Purchase",text="Purchase",anchor=W)
    my_tree.heading("Withdrawls",text="Withdrawls",anchor=W)
    my_tree.heading("Payments",text="Payments",anchor=W)
    my_tree.heading("Amount",text="Amount",anchor=W)
    my_tree.heading("Writtento",text="Writtento",anchor=W)
    my_tree.heading("Date",text="Date",anchor=W)

    
    monday_label = Label(dashboard_window,text="Monday", font=("Arial", 25),bg="white")
    monday_label.pack(side='left',padx=50,anchor=NW)
    
    tuesday_label = Label(dashboard_window,text="Tuesday", font=("Arial",25),bg="white")
    tuesday_label.pack(side='left',padx=25,anchor=NW)
    
    wednesday_label = Label(dashboard_window,text="Wednesday", font=("Arial", 25),bg="white")
    wednesday_label.pack(side='left',padx=25,anchor=NW)
    
    thursday_label = Label(dashboard_window,text="Thursday", font=("Arial",25),bg="white")
    thursday_label.pack(side='left',padx=25,anchor=NW)
    
    friday_label = Label(dashboard_window,text="Friday", font=("Arial", 25),bg="white")
    friday_label.pack(side='left',padx=25,anchor=NW)
    
    saturday_label = Label(dashboard_window,text="Saturday", font=("Arial",25),bg="white")
    saturday_label.pack(side='left',padx=25,anchor=NW)
    
    sunday_label = Label(dashboard_window,text="Sunday", font=("Arial",25),bg="white")
    sunday_label.pack(side='left',padx=25,anchor=NW)
    
    
    
    
    refreshTable()
    
    
    
    
    





   
        
        
   
def sign_in(Login, password):
    
    try:
        conn = connection()
        cursor = conn.cursor()
        # Replace 'users' with your actual table name
        query = "SELECT * FROM Login_Password WHERE Login = %s AND Password = %s"
        cursor.execute(query, (Login, password))
        user = cursor.fetchone()
        if user:
            messagebox.showinfo("Sign In", "Sign in successful!")
            open_dashboard()
        else:
            messagebox.showwarning("Sign In", "Invalid username or password.")
    except Exception as e:
        messagebox.showerror("Error", f"Error signing in: {e}")
    finally:
        cursor.close()
        conn.close()
        
def open_create_account_window():
    
    
    create_account_window = Toplevel(root)
    create_account_window.title("Create Account")
    create_account_window.geometry("2200x1000")
    create_account_window.configure(bg="lightgreen")
    create_account_window.configure(background="darkgreen")

    # Add widgets for account creation in the new window
    Label(create_account_window, text="Create an Account",bd=5, font=("Harrington", 50,"bold"),bg="darkgreen",fg="gold").pack(pady=10)
    
    username_label = Label(create_account_window, text="Username:",font=("Arial bold",30),bd=10,bg="darkgreen",fg="gold")
    username_label.pack()
    username_entry = Entry(create_account_window,bd=10,width=40,font=("Arial",15))
    username_entry.pack()

    password_label = Label(create_account_window, text="Password:",bd=10,font=("Arial bold",30),bg="darkgreen",fg="gold")
    password_label.pack()
    password_entry = Entry(create_account_window, show="*",bd=10,width=40,font=("Arial",15))
    password_entry.pack()

    create_button = Button(
        create_account_window, text="Create Account",bd=10,
        command=lambda: create_account(username_entry.get(), password_entry.get())
    )
    create_button.pack(pady=50)



def report_history():
    
    conn=pymysql.connect(
    host="localhost",
    user="root",    
    password="Jg3_arciniegas",
    db="expense_report"    
    )
    return conn
    
def refreshTable():
    try:
        global my_tree
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
        my_tree.pack(padx=10,pady=20)

    except Exception as e:
        messagebox.showerror("Error", f"Error refreshing table: {e}")


    


#function later
def read():
    conn=report_history()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM expense_history")
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results 















 


    
root=tk.Tk()
root.title("Expense Report")
root.configure(bg="lightgreen")
root.configure(background="darkgreen")
root.geometry("2200x1000")
my_tree=ttk.Treeview(root)




image_path=r"C:\Users\berna\Downloads\New_image_dollar_tree-removebg-preview.png"
img=PhotoImage(file=image_path)


image_label=tk.Label(root,image=img,bg="lightgreen")  
image_label.grid(row=0,column=1,columnspan=5,rowspan=10,padx=40,pady=125)
    

#"C:\Users\berna\OneDrive\Pictures\dollar_house_tree.png"

title_name=tk.Label(root,text="Mana House",font=("Harrington",100,"bold"),fg="gold",bg="darkgreen")
title_name.grid(row=0,column=8)#,columnspan=0,rowspan=0,padx=10,pady=200



Login_text = Label(root,text="Login",font=("Arial",30,"bold"),bg="darkgreen",fg="gold")
Login_text.grid(row=3,column=6,columnspan=1)

Login_entry=Entry(root,width=50,bd=5,font=("Arial",15))
Login_entry.grid(row=3,column=8,columnspan=1)



Password_text=Label(root,text="Password",font=("Arial Bold",30),bg="darkgreen",fg="gold")
Password_text.grid(row=4,column=6)

Password_entry=Entry(root,width=50,bd=5,show="*",font=("Arial",15))
Password_entry.grid(row=4,column=8)

Sign_in_Label=Label(root,text="Sign in",font=("Arial Bold",15),bg="darkgreen",fg="lightgreen")

Quotes_text=Label(root,text="""...Down Bread From Heaven For You""",font=("Vivaldi",40,"bold"),bg="darkgreen",fg="lightgreen")
Quotes_text.grid(row=8,column=8)

Book_Quote=Label(root,text="- Exodus 16:4",font=("Vivaldi",40,"bold"),bg="darkgreen",fg="lightgreen")
Book_Quote.grid(row=9,column=8)



#first label title

#grid the title

Sign_inbttn=Button(
    root,text="Sign in",bd=5,width=7,padx=10,pady=10,font=("Arial Bold",15),bg="lightgreen",fg="darkgreen",
    command=lambda: sign_in(Login_entry.get(), Password_entry.get())
)


Sign_inbttn.grid(row=5,column=8)

# Create an account link
create_account_label = tk.Label(root, text="Create an Account", bg="lightgreen", fg="blue", cursor="hand2")
create_account_label.grid(row=6, column=8, columnspan=1)
# Bind the click event to the link
create_account_label.bind("<Button-1>", lambda event: open_create_account_window())

# Placeholder for Treeview
my_tree = None


root.mainloop()





