#!/usr/bin/env python
# coding: utf-8

# In[7]:





# In[59]:


from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import time
import sqlite3

try:
    conobj=sqlite3.connect(database='bank.sqlite')
    curobj=conobj.cursor()
    curobj.execute("create table acn(acn_no integer primary key autoincrement,acn_name text,acn_pass text,acn_email text,acn_mob text,acn_bal float,acn_opendate text,acn_gender text)")
    conobj.close()
    print("table created")
except:
    print("something went wrong,mightbe table already Exist")

win=Tk()
win.state('zoomed')
win.configure(bg='pink')
win.resizable(width=False,height=False)
title=Label(win,text="Banking Automation",font=('arial',50,'bold','underline'),bg='pink')
title.pack()
dt=time.strftime("%d-%B-%y")
date=Label(win,text=f"{dt}",font=('arial',20,'bold'),bg='pink',fg='black')
date.place(relx=.85,rely=.1)

def main_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=.0,rely=.2,relwidth=1,relheight=.85)

    def forgotpass():
        frm.destroy()
        forgotpass_screen()

    def newscreen():
        frm.destroy()
        new_screen()

    def login():
        global gacn
        gacn=e_acn.get()
        pwd=e_pass.get()
        if len(gacn)==0 or len(pwd)==0:
            messagebox.showwarning("Validation",'Empty fields are not allowed')
            return
        else:
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select * from acn where acn_no=? and acn_pass=?",(gacn,pwd))
            tup=curobj.fetchone()
            conobj.close()
            if tup==None:
                messagebox.showerror("Login","Invalid ACN/PASS")
            else:
                frm.destroy()
                welcome_screen()

    def clear():
        e_acn.delete(0,'end')
        e_pass.delete(0,'end')
        e_acn.focus()
        
    lbl_acn=Label(frm,text="Account no",font=('arial',20,'bold'),bg='powder blue',fg='black')
    lbl_acn.place(relx=.3,rely=.1)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.45,rely=.1)
    e_acn.focus()

    lbl_pass=Label(frm,text="password",font=('arial',20,'bold'),bg='powder blue',fg='black')
    lbl_pass.place(relx=.3,rely=.2)

    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.45,rely=.2)

    btn_login=Button(frm,text="login",font=('arial',15,'bold'),bd=5,command=login)
    btn_login.place(relx=.50,rely=.3)

    btn_clear=Button(frm,text="Clear",font=('arial',15,'bold'),bd=5,command=clear)
    btn_clear.place(relx=.58,rely=.3)

    btn_fp=Button(frm,text="Forgot password",font=('arial',18,'bold'),bd=5,command=forgotpass)
    btn_fp.place(relx=.48,rely=.42)

    btn_nu=Button(frm,text="Open New Account",font=('arial',18,'bold'),bd=5,command=newscreen)
    btn_nu.place(relx=.47,rely=.55)


def forgotpass_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=.0,rely=.2,relwidth=1,relheight=.85)

    def back():
        frm.destroy()
        main_screen()

    def clear():
        e_acn.delete(0,'end')
        e_email.delete(0,'end')
        e_mob.delete(0,'end')
        e_acn.focus()

    def forgotpass_db():
        acn=e_acn.get()
        email=e_email.get()
        mob=e_mob.get()

        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_pass from acn where acn_no=? and acn_email=? and acn_mob=?",(acn,email,mob))
        tup=curobj.fetchone()
        if tup==None:
            messagebox.showerror("Forgot pass","Reocrd not found")

        else:
            messagebox.showinfo("Forgot pass",f"Your password={tup[0]}")
            
    btn_nu=Button(frm,text="back",font=('arial',18,'bold'),bd=5,command=back)
    btn_nu.place(relx=.00,rely=.00)

    lbl_acn=Label(frm,text="Account no",font=('arial',20,'bold'),bg='powder blue',fg='black')
    lbl_acn.place(relx=.3,rely=.1)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.45,rely=.1)
    e_acn.focus()

    lbl_email=Label(frm,text="E-mail",font=('arial',20,'bold'),bg='powder blue',fg='black')
    lbl_email.place(relx=.32,rely=.2)

    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.45,rely=.2)

    lbl_mob=Label(frm,text="Mobile no",font=('arial',20,'bold'),bg='powder blue',fg='black')
    lbl_mob.place(relx=.30,rely=.3)

    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.45,rely=.3)

    btn_clear=Button(frm,text="Clear",font=('arial',15,'bold'),bd=5,command=clear)
    btn_clear.place(relx=.50,rely=.4)

    btn_sub=Button(frm,text="submit",font=('arial',15,'bold'),bd=5,command=forgotpass_db)
    btn_sub.place(relx=.58,rely=.4)
    

def new_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=.0,rely=.2,relwidth=1,relheight=.85)

    def back():
        frm.destroy()
        main_screen()
        
    def clear():
        e_name.delete(0,'end')
        e_pass.delete(0,'end')
        e_email.delete(0,'end')
        e_mob.delete(0,'end')
        cb_gen.delete(0,'end')
        e_name.focus()

    def newuser_db():
        name=e_name.get()
        pwd=e_pass.get()
        email=e_email.get()
        mob=e_mob.get()
        gen=cb_gen.get()
        bal=0
        opendate=time.strftime("%d-%B-%y")

        import sqlite3
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("insert into acn(acn_name,acn_pass,acn_email,acn_mob,acn_gender,acn_opendate,acn_bal)values(?,?,?,?,?,?,?)",(name,pwd,email,mob,gen,opendate,bal))
        conobj.commit()
        conobj.close()

        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select max(acn_no)from acn")
        tup=curobj.fetchone()
        conobj.close()
        messagebox.showinfo("New user",f"Account created with ACN NO={tup[0]}")
        e_name.delete(0,'end')
        e_pass.delete(0,'end')
        e_email.delete(0,'end')
        e_mob.delete(0,'end')

        
    btn_nu=Button(frm,text="back",font=('arial',18,'bold'),bd=5,command=back)
    btn_nu.place(relx=.00,rely=.00)

    lbl_name=Label(frm,text="Name",font=('arial',20,'bold'),bg='powder blue',fg='black')
    lbl_name.place(relx=.3,rely=.1)

    e_name=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_name.place(relx=.45,rely=.1)
    e_name.focus()

    lbl_pass=Label(frm,text="Password",font=('arial',20,'bold'),bg='powder blue',fg='black')
    lbl_pass.place(relx=.3,rely=.2)

    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show="*")
    e_pass.place(relx=.45,rely=.2)
    
    lbl_email=Label(frm,text="E-mail",font=('arial',20,'bold'),bg='powder blue',fg='black')
    lbl_email.place(relx=.3,rely=.3)

    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.45,rely=.3)

    lbl_mob=Label(frm,text="Mobile no",font=('arial',20,'bold'),bg='powder blue',fg='black')
    lbl_mob.place(relx=.3,rely=.4)

    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.45,rely=.4)

    lbl_gen=Label(frm,text="Gender",font=('arial',20,'bold'),bg='powder blue',fg='black')
    lbl_gen.place(relx=.3,rely=.5)

    cb_gen=Combobox(frm,values=['---select''','Male','Female','Transgender'],font=('arial',20,'bold'))
    cb_gen.place(relx=.45,rely=.5)

    btn_sub=Button(frm,text="sumbit",font=('arial',15,'bold'),bd=5,command=newuser_db)
    btn_sub.place(relx=.50,rely=.7)

    btn_clear=Button(frm,text="Clear",font=('arial',15,'bold'),bd=5,command=clear)
    btn_clear.place(relx=.60,rely=.7)

def welcome_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=.0,rely=.2,relwidth=1,relheight=.85)

    def logout():
        frm.destroy()
        main_screen()

    def details():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.6)

        lbl_wel=Label(ifrm,text='This is Details screen',font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_wel.pack()

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute("select acn_opendate,acn_bal,acn_gender,acn_email,acn_mob from acn where acn_no=?",(gacn))
        tup=curobj.fetchone()
        conobj.close()
        
        lbl_opendate=Label(ifrm,text=f'Open date:{tup[0]}',font=('arial',15,'bold'),bg='white')
        lbl_opendate.place(relx=.2,rely=.12)

        lbl_bal=Label(ifrm,text=f'Balance:{tup[1]}',font=('arial',15,'bold'),bg='white')
        lbl_bal.place(relx=.2,rely=.2)

        lbl_gender=Label(ifrm,text=f'Gender:{tup[2]}',font=('arial',15,'bold'),bg='white')
        lbl_gender.place(relx=.2,rely=.28)

        lbl_email=Label(ifrm,text=f'E-mail:{tup[3]}',font=('arial',15,'bold'),bg='white')
        lbl_email.place(relx=.2,rely=.36)

        lbl_mob=Label(ifrm,text=f'Mobile no:{tup[4]}',font=('arial',15,'bold'),bg='white')
        lbl_mob.place(relx=.2,rely=.44)


    def update():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.6)

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute("select acn_name,acn_pass,acn_email,acn_mob from acn where acn_no=?",(gacn))
        tup=curobj.fetchone()
        conobj.close()
        
        lbl_wel=Label(ifrm,text='This is Update screen',font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_wel.pack()

        lbl_name=Label(ifrm,text="Name",font=('arial',20,'bold'),bg='white',fg='black')
        lbl_name.place(relx=.1,rely=.1)
    
        e_name=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_name.place(relx=.1,rely=.2)
        e_name.insert(0,tup[0])
        e_name.focus()
    
        lbl_pass=Label(ifrm,text="Password",font=('arial',20,'bold'),bg='white',fg='black')
        lbl_pass.place(relx=.1,rely=.4)
    
        e_pass=Entry(ifrm,font=('arial',20,'bold'),bd=5,show="*")
        e_pass.place(relx=.1,rely=.5)
        e_pass.insert(0,tup[1])
        
        lbl_email=Label(ifrm,text="E-mail",font=('arial',20,'bold'),bg='white',fg='black')
        lbl_email.place(relx=.5,rely=.1)
    
        e_email=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_email.place(relx=.5,rely=.2)
        e_email.insert(0,tup[2])
    
        lbl_mob=Label(ifrm,text="Mobile no",font=('arial',20,'bold'),bg='white',fg='black')
        lbl_mob.place(relx=.5,rely=.4)
    
        e_mob=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_mob.place(relx=.5,rely=.5)
        e_mob.insert(0,tup[3])


        def update_db():
            name=e_name.get()
            pwd=e_pass.get()
            email=e_email.get()
            mob=e_mob.get()

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute("update acn set acn_name=?,acn_pass=?,acn_email=?,acn_mob=? where acn_no=?",(name,pwd,email,mob,gacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update","Record Updated")
            welcome_screen()
        
        btn_update=Button(ifrm,width=10,text="Update",font=('arial',15,'bold'),bd=5,command=update_db)
        btn_update.place(relx=.6,rely=.7)

    
    def deposit():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.6)
    
        lbl_wel=Label(ifrm,text='This is Deposit screen',font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_wel.pack()

        lbl_amt=Label(ifrm,text="Amount",font=('arial',20,'bold'),bg='white',fg='black')
        lbl_amt.place(relx=.1,rely=.2)
    
        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.3,rely=.2)
        e_amt.focus()
        def deposit_db():
            amt=float(e_amt.get())
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute("update acn set acn_bal=acn_bal+? where acn_no=?",(amt,gacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update",f"{amt}Amount Deposited")
            

        
        btn_update=Button(ifrm,width=10,text="Sumbit",font=('arial',15,'bold'),bd=5,command=deposit_db)
        btn_update.place(relx=.3,rely=.4)

    def withdraw():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.6)
    
        lbl_wel=Label(ifrm,text='This is Withdraw screen',font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_wel.pack()

        lbl_amt=Label(ifrm,text="Amount",font=('arial',20,'bold'),bg='white',fg='black')
        lbl_amt.place(relx=.1,rely=.2)
    
        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.3,rely=.2)
        e_amt.focus()
        
        def withdraw_db():
            amt=float(e_amt.get())

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from acn where acn_no=?",(gacn,))
            tup=curobj.fetchone()
            avail_bal=tup[0]
            conobj.close()

            if avail_bal>=amt:
                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                curobj.execute("update acn set acn_bal=acn_bal-? where acn_no=?",(amt,gacn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Update",f"{amt}Amount withdraw")
            else:
                messagebox.showwarning("Withdraw","Insufficient Balance")

        
        btn_update=Button(ifrm,width=10,text="Sumbit",font=('arial',15,'bold'),bd=5,command=withdraw_db)
        btn_update.place(relx=.3,rely=.4)


    def transfer():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.6)
    
        lbl_wel=Label(ifrm,text='This is Transfer screen',font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_wel.pack()

        lbl_amt=Label(ifrm,text="Amount",font=('arial',20,'bold'),bg='white',fg='black')
        lbl_amt.place(relx=.1,rely=.2)
    
        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.3,rely=.2)
        e_amt.focus()

        lbl_to=Label(ifrm,text="To",font=('arial',20,'bold'),bg='white',fg='black')
        lbl_to.place(relx=.1,rely=.4)
    
        e_to=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_to.place(relx=.3,rely=.4)
        e_to.focus()
        
        def transfer_db():
            to_acn=e_to.get()
            amt=float(e_amt.get())
            
            if to_acn==gacn:
                messagebox.showwarning("Transfer  ","To and From cannot be same")
                return
                
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from acn where acn_no=?",(gacn,))
            tup=curobj.fetchone()
            avail_bal=tup[0]
            conobj.close()

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute("select acn_no from acn where acn_no=?",(to_acn,))
            tup=curobj.fetchone()
            conobj.close()

            if tup==None:
                messagebox.showwarning("Transfer","Invalid to ACN")
                return
            if avail_bal>=amt:
                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                curobj.execute("update acn set acn_bal=acn_bal+? where acn_no=?",(amt,to_acn))
                curobj.execute("update acn set acn_bal=acn_bal-? where acn_no=?",(amt,gacn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Transfer",f"{amt} Transfered to ACN {to_acn}")
                
                

        btn_update=Button(ifrm,width=10,text="Sumbit",font=('arial',15,'bold'),bd=5,command=transfer_db)
        btn_update.place(relx=.5,rely=.6)

    conobj=sqlite3.connect("bank.sqlite")
    curobj=conobj.cursor()
    curobj.execute("select acn_name from acn where acn_no=?",(gacn))
    tup=curobj.fetchone()
    conobj.close()
    
    lbl_wel=Label(frm,text=f"Welcome,{tup[0]}",font=('arial',20,'bold'),bg='powder blue',fg='black')
    lbl_wel.place(relx=.0,rely=.0)

    btn_logout=Button(frm,text="Logout",font=('arial',15,'bold'),bd=5,command=logout)
    btn_logout.place(relx=.88,rely=.0)

    btn_details=Button(frm,command=details,width=10,text="Details",font=('arial',15,'bold'),bd=5)
    btn_details.place(relx=0,rely=.1)

    btn_update=Button(frm,command=update,width=10,text="Update",font=('arial',15,'bold'),bd=5)
    btn_update.place(relx=0,rely=.2)

    btn_deposit=Button(frm,command=deposit,width=10,text="Deposit",font=('arial',15,'bold'),bd=5)
    btn_deposit.place(relx=0,rely=.3)

    btn_withdraw=Button(frm,command=withdraw,width=10,text="Withdraw",font=('arial',15,'bold'),bd=5)
    btn_withdraw.place(relx=0,rely=.4)

    btn_transfer=Button(frm,command=transfer,width=10,text="Transfer",font=('arial',15,'bold'),bd=5)
    btn_transfer.place(relx=0,rely=.5)

main_screen()
win.mainloop()


# In[ ]:





# In[ ]:




