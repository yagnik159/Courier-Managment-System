import cx_Oracle as oc 
con=oc.connect('yagnik/yagnik@localhost')      #Your Account Name and password
coursor=con.cursor()

# coursor.execute("drop table del_add")
# coursor.execute("drop table drop_add")
# coursor.execute("drop table location")
# coursor.execute("drop table delivary")
# coursor.execute("drop table product_details")
# coursor.execute("drop table employee")
# coursor.execute("drop table customer")
# coursor.execute("drop table admin")

try:
    coursor.execute("CREATE TABLE Admin(U_name_admin varchar2(10) PRIMARY KEY,Password_admin varchar2(10) NOT NULL,Name_admin varchar2(20) NOT NULL,Contact_admin varchar2(10) NOT NULL)")
    coursor.execute("CREATE TABLE Customer(C_id int NOT NULL PRIMARY KEY,Name_cus varchar2(10) NOT NULL,contact_cus varchar2(10) NOT NULL,Address_cus varchar2(50) NOT NULL,Email_cus varchar2(50) NOT NULL,U_name_cus varchar2(10) NOT NULL,Password_cus varchar2(10) NOT NULL) ")
    coursor.execute("CREATE TABLE Employee(E_id int  NOT NULL PRIMARY KEY,Name_emp varchar2(20) NOT NULL,contact_emp varchar2(10) NOT NULL,Address_emp varchar2(50) NOT NULL,Email_emp varchar2(50) NOT NULL,U_name_emp varchar2(10) NOT NULL,Password_emp varchar2(10) NOT NULL) ")
    coursor.execute("CREATE TABLE Product_details(P_id int  NOT NULL PRIMARY KEY,P_type varchar2(10) NOT NULL,Amount int NOT NULL,E_id int NOT NULL,C_id int NOT NULL,bre_b float NOT NULL,len_b float NOT NULL,height_b float not NULL,weight_b float not NULL) ")
    coursor.execute("ALTER TABLE Product_details add FOREIGN key (E_id) REFERENCES Employee(E_id) ")
    coursor.execute("ALTER TABLE Product_details add FOREIGN key (C_id) REFERENCES Customer(C_id) ")
    coursor.execute("CREATE TABLE Delivary(P_id int NOT NULL,del_date date NOT NULL,del_time TIMESTAMP NOT NULL,pin_1 int NOT NULL,pin_2 int NOT NULL,status_del VARCHAR2(10) NOT NULL) ")
    coursor.execute("ALTER TABLE Delivary add FOREIGN key (P_id) REFERENCES Product_details(P_id) ")
    coursor.execute("CREATE TABLE Location(Pincode int NOT NULL PRIMARY KEY,city_name varchar2(10) NOT NULL,state_name varchar(10) NOT NULL)")
    coursor.execute("CREATE TABLE drop_add(P_id int NOT NULL,Name_drop varchar2(20) NOT NULL,contact_drop varchar2(10) NOT NULL,pincode_drop int NOT NULL,state_drop varchar2(10) NOT NULL,city_drop varchar2(10) NOT NULL) ")
    coursor.execute("ALTER TABLE drop_add add FOREIGN key (P_id) REFERENCES Product_details(P_id) ")
    coursor.execute("ALTER TABLE drop_add add FOREIGN key (pincode_drop) REFERENCES Location(pincode) ")
    coursor.execute("CREATE TABLE del_add(P_id int NOT NULL,Name_del varchar2(20) NOT NULL,contact_del varchar2(10) NOT NULL,pincode_del int NOT NULL,state_del varchar2(10) NOT NULL,city_del varchar2(10) NOT NULL) ")
    coursor.execute("ALTER TABLE del_add add FOREIGN key (P_id) REFERENCES Product_details(P_id) ")
    coursor.execute("ALTER TABLE del_add add FOREIGN key (pincode_del) REFERENCES Location(pincode)")
    coursor.execute("INSERT INTO admin VALUES('yagnik','1234','Yagnik Thummar','7929328329')") 
    coursor.execute("INSERT INTO admin VALUES('maulik','1234','Maulik Virpariya','7929328329')") 
    coursor.execute("INSERT INTO admin VALUES('yash','1234','Yash Savani','7929248329')") 


    coursor.execute("INSERT INTO Customer VALUES(10001,'yagnik','7783392739','surat','yagnik@gmail.com','yagnik_1','yag')")
    coursor.execute("INSERT INTO Customer VALUES(10002,'maulik','9364856294','morbi','maulik@gmail.com','maulik_1','mau')")
    coursor.execute("INSERT INTO Customer VALUES(10003,'savan','6472947294','surat','savan@gmail.com','savan_1','sav')")
    coursor.execute("INSERT INTO Customer VALUES(10004,'yash','9506734957','ahmedabad','yash@gmail.com','yash_1','yas')")
    coursor.execute("INSERT INTO Customer VALUES(10005,'utsav','8365936496','rajkot','utsav@gmail.com','utsav_1','uts')")
    coursor.execute("INSERT INTO Customer VALUES(10006,'priyank','9364964137','vadodara','priyank@gmail.com','priyank_1','pri')") 
    coursor.execute("INSERT INTO Customer VALUES(10007,'pratik','9364825485','rajkot','pratik@gmail.com','pratik_1','pra')")


    coursor.execute("INSERT INTO LOCATION VALUES(395001,'surat','gujrat')")
    coursor.execute("INSERT INTO LOCATION VALUES(395002,'ahmebadab','gujrat')") 
    coursor.execute("INSERT INTO LOCATION VALUES(395003,'rajkot','gujrat')")
    coursor.execute("INSERT INTO LOCATION VALUES(395004,'vadodara','gujrat')") 
    coursor.execute("INSERT INTO LOCATION VALUES(395005,'morbi','gujrat')")
    coursor.execute("INSERT INTO LOCATION VALUES(395006,'mumbai','maharastra')") 
    coursor.execute("INSERT INTO LOCATION VALUES(395007,'delhi','delhi')")
    coursor.execute("INSERT INTO LOCATION VALUES(395008,'banglore','karnataka')") 
    coursor.execute("INSERT INTO LOCATION VALUES(395009,'hydrabad','telangana')")
    coursor.execute("INSERT INTO LOCATION VALUES(395010,'chennai','tamilnadu')")


    coursor.execute("INSERT INTO Employee VALUES(20001,'sanjay','9364836274','surat','sanjay@gmail.com','sanjay_1','san')")
    coursor.execute("INSERT INTO Employee VALUES(20002,'henish','9362462846','rajkot','henish@gmail.com','hensih_1','hen')")
    coursor.execute("INSERT INTO Employee VALUES(20003,'sahaj','7395739475','jasdan','sahaj@gmail.com','sahaj_1','sah')")
    coursor.execute("INSERT INTO Employee VALUES(20004,'nevil','8374927483','tapi','nevil@gmail.com','nevil_1','nev')")
    coursor.execute("INSERT INTO Employee VALUES(20005,'utsav','9374837483','gandhinagar','utsav@gmail.com','utsav_1','uts')") 
    coursor.execute("INSERT INTO Employee VALUES(20006,'chirag','9363846273','lathi','chirag@gmail.com','chirag_1','chi')")
    coursor.execute("INSERT INTO Employee VALUES(20007,'jainish','8263727349','surat','jainish@gmail.com','jainish_1','jai')") 
    coursor.execute("INSERT INTO Employee VALUES(20008,'raj','7235383628','ahmedabad','raj@gmail.com','raj_1','raj')")
    coursor.execute("INSERT INTO Employee VALUES(20009,'priyal','9203828393','ahmedabad','priyal@gmail.com','priyal_1','pri')") 
    coursor.execute("INSERT INTO Employee VALUES(20010,'nishidh','6382648291','katch','nishidh@gmail.com','nishidh_1','nis')")

    coursor.execute("insert into product_details values(30001,'document',100,20001,10001,2.4,3.4,4.5,29)")
    coursor.execute("insert into delivary values(30001,sysdate,CURRENT_TIMESTAMP,395001,395002,'delivary')")
    coursor.execute("insert into del_add values(30001,'dipak',8475926384,395001,'surat','gujrat')")
    coursor.execute("insert into drop_add values(30001,'bhargav',4958394857,395002,'ahmebadab','gujrat')")

except:
    pass

import tkinter as tk
from tkinter import messagebox
import random

from PIL import ImageTk,Image 
win =tk.Tk()

# win.geometry("1920x1017+660+210")
win.minsize(1400, 850)
win.maxsize(1400, 850)
win.resizable(1,  1)
win.title("Courier Management System")
win.configure(background="#d9d9d9")


Frame1 = tk.Frame(win)
Frame1.place(x=0,y=0,width=1400,height=850)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#d9d9d9")

navigation=tk.Frame(Frame1)
navigation.place(x=0,y=0,width=300,height=850)
navigation.configure(relief='flat')
navigation.configure(borderwidth="2")
# navigation.configure(relief="groove")
navigation.configure(background="#F4A950")


home = tk.Button(Frame1,command=lambda : Home())
home.place(x=30, y=300)
home.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 20,'bold'),text='''HOME''')

employee_btn = tk.Button(Frame1, command= lambda : employee_login())
employee_btn.place(x=30, y=400)
employee_btn.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 20,'bold'),text='''EMPLOYEE''')

admin_btn = tk.Button(Frame1,command= lambda : admin_log_in())
admin_btn.place(x=30, y=500)
admin_btn.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 20,'bold'),text='''ADMIN''')

# Settings = tk.Button(Frame1)
# Settings.place(x=30, y=540)
# Settings.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 20,'bold'),text='''SETTINGS''')

Frame2 = tk.Frame(Frame1)
Frame2.place(x=300,y=0,width=1100,height=850)
Frame2.configure(relief='flat')
Frame2.configure(borderwidth="2")
# Frame2.configure(relief="groove")
Frame2.configure(background="#161B21")

# new = ImageTk.PhotoImage(Image.open(r"new.png"))

new = ImageTk.PhotoImage(Image.open(r"images\new.png"))
track = ImageTk.PhotoImage(Image.open(r"images\track.png"))
employee = ImageTk.PhotoImage(Image.open(r"images\user.png"))
admin = ImageTk.PhotoImage(Image.open(r"images\admin.png"))
terms_icon = ImageTk.PhotoImage(Image.open(r"images\terms.png"))
employee_detail_icon = ImageTk.PhotoImage(Image.open(r"images\employee_detail.png"))


detail_icon = ImageTk.PhotoImage(Image.open(r"images\details.png"))
pending_icon = ImageTk.PhotoImage(Image.open(r"images\pending.png"))
completed_icon = ImageTk.PhotoImage(Image.open(r"images\completed.png"))
more_icon = ImageTk.PhotoImage(Image.open(r"images\more.png"))

customer_icon = ImageTk.PhotoImage(Image.open(r"images\customer.png"))
cancelled_icon = ImageTk.PhotoImage(Image.open(r"images\cancelled.png"))

#######################  Customer-Home  ########################
def Home():
    for widget in Frame2.winfo_children():
            widget.destroy()
    
    Track_oreder_L = tk.Label(Frame2)
    Track_oreder_L.place(x=210, y=180)
    Track_oreder_L.configure(background="#161B21",font=('Helvetica', 35,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Courier Management System''')
    
    home.configure(foreground="#F4A950",background="#161B21")
    employee_btn.configure(background="#F4A950",foreground="#161B21")
    admin_btn.configure(background="#F4A950",foreground="#161B21")
    
    Label1 = tk.Label(Frame2)
    Label1.place(x=410, y=270)
    Label1.configure(background="#161B21",foreground="#F4A950",text="Log in",font=('Helvetica', 42,'bold'))

    Label_name = tk.Label(Frame2)
    Label_name.place(x=250, y=400, height=40, width=126)
    Label_name.configure(background="#161B21",font=('Helvetica', 34,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''ID''')

    Label_password = tk.Label(Frame2)
    Label_password.place(x=250, y=470, height=40, width=227)
    Label_password.configure(background="#161B21",font=('Helvetica', 34,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Password''')


    Id=tk.StringVar()
    Entry_Name = tk.Entry(Frame2,textvariable=Id)
    Entry_Name.place(x=500, y=400, height=40, width=250)
    Entry_Name.configure(takefocus="",cursor="ibeam",font=('Helvetica', 26,'bold'))

    password=tk.StringVar()
    Entry_password = tk.Entry(Frame2, show="*",textvariable=password)
    Entry_password.place(x=500, y=470,height=40, width=250)
    Entry_password.configure(takefocus="",cursor="ibeam",font=('Helvetica', 26,'bold'))

    def validte():
        # print(Id.get(),password.get())
        pass_1=coursor.execute(f'select password_cus from customer where c_id={Id.get()}')
        pass_1=pass_1.fetchall()
        if password.get()==pass_1[0][0]:
            after_login()
        else:
            tk.messagebox.showerror("Wrong Entry", "Enter valid ID or password")

            

    Button1 = tk.Button(Frame2,command=validte)
    Button1.place(x=410, y=530, height=40, width=250)
    Button1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),text='''Submit''')

####################### Atfer- Customer Log in  ########################
def after_login():
    for widget in Frame2.winfo_children():
            widget.destroy()
    
    New_delivery = tk.Button(Frame2,command=lambda:delivery())
    New_delivery.place(x=50, y=250, height=310, width=310)
    New_delivery.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=new)

    Track_order = tk.Button(Frame2, command=lambda : track_order())
    Track_order.place(x=400, y=250, height=310, width=310)
    Track_order.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=track)

    terms = tk.Button(Frame2,command=lambda:terms_condition())
    terms.place(x=750, y=250, height=310, width=310)
    terms.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=terms_icon)
    # terms.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=terms)

    # Employee = tk.Button(Frame2)
    # Employee.place(x=225, y=400, height=310, width=310)
    # Employee.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=employee)


    # icon_new=tk.Label(New_delivery,image=new)
    # icon_new.place(x=0, y=0, height=290, width=310)
'''New Delivary
    
    form

    customer id
    product type
    physical structure 
    height
    length
    bredth
    weight
    delivery date
    delivery time

    delivery_add
    name
    contact
    pincode:must be between 395001 to 395010 use drop down
    
    drop_add
    name 
    contact
    pincode'''
####################### Delivery ##################
def delivery():
    for widget in Frame2.winfo_children():
            widget.destroy()
    L_customer_id = tk.Label(Frame2)
    L_customer_id.place(x=50, y=100)
    L_customer_id.configure(background="#161B21",foreground="#F4A950",font=('Helvetica', 20,'bold'),text='''Customer_id''')

    customer_id=tk.StringVar()
    customer_id_e = tk.Entry(Frame2,textvariable=customer_id)#state=tk.DISABLED
    customer_id_e.place(x=295, y=100, height=32, width=250)
    customer_id_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")

    L_name = tk.Label(Frame2)
    L_name.place(x=50, y=150)
    L_name.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Sender name ''')

    Name=tk.StringVar(value="Like Yagnik...")
    Name_e = tk.Entry(Frame2,textvariable=Name)#state=tk.DISABLED
    Name_e.place(x=295, y=150, height=32, width=250)
    Name_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")


    L_S_contact = tk.Label(Frame2)
    L_S_contact.place(x=50, y=200)
    L_S_contact.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Sender Phon No ''')

    S_contact=tk.IntVar()
    S_contact_e = tk.Entry(Frame2,textvariable=S_contact)#state=tk.DISABLED
    S_contact_e.place(x=295, y=200, height=32, width=250)
    S_contact_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")
 
    L_pincode = tk.Label(Frame2)
    L_pincode.place(x=50, y=250)
    L_pincode.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Sender Pincode ''')

    S_Pincode=tk.IntVar()
    S_Pincode_e = tk.Entry(Frame2,textvariable=S_Pincode)#state=tk.DISABLED
    S_Pincode_e.place(x=295, y=250, height=32, width=250)
    S_Pincode_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")
 
    # L_customer_id = tk.Label(Frame2)
    # L_customer_id.place(x=625, y=100)
    # L_customer_id.configure(background="#161B21",foreground="#F4A950",font=('Helvetica', 20,'bold'),text='''Customer_id''')

    L_R_name = tk.Label(Frame2)
    L_R_name.place(x=570, y=125)
    L_R_name.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Receiver name ''')

    R_name=tk.StringVar()
    R_name_e = tk.Entry(Frame2,textvariable=R_name)#state=tk.DISABLED
    R_name_e.place(x=825, y=125, height=32, width=250)
    R_name_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")

    L_R_contact = tk.Label(Frame2)
    L_R_contact.place(x=570, y=175)
    L_R_contact.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Receiver Phon No ''')
    
    L_contact=tk.IntVar()
    L_contact_e = tk.Entry(Frame2,textvariable=L_contact)#state=tk.DISABLED
    L_contact_e.place(x=825, y=175, height=32, width=250)
    L_contact_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")
 
    L_pincode = tk.Label(Frame2)
    L_pincode.place(x=570, y=225)
    L_pincode.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Receiver Pincode ''')

    R_Pincode=tk.IntVar()
    R_Pincode_e = tk.Entry(Frame2,textvariable=R_Pincode)#state=tk.DISABLED
    R_Pincode_e.place(x=825, y=225, height=32, width=250)
    R_Pincode_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")
 
    L_product_type = tk.Label(Frame2)
    L_product_type.place(x=50, y=375)
    L_product_type.configure(background="#161B21",font=('Helvetica', 35,'bold'),disabledforeground="#a3a3a3",foreground="#efefef",text='''Product Details''')

    L_product_type = tk.Label(Frame2)
    L_product_type.place(x=50, y=480)
    L_product_type.configure(background="#161B21",font=('Helvetica', 25,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Product Type ''')

    product_type=tk.StringVar(value="Like doc, Gift, etc")
    product_type = tk.Entry(Frame2,textvariable=product_type)#state=tk.DISABLED
    product_type.place(x=275, y=480, height=35, width=250)
    product_type.configure(background="#F4A950",font=('Helvetica', 20,'bold'),foreground="#161B21",relief="flat")

    L_lenght = tk.Label(Frame2)
    L_lenght.place(x=50, y=550)
    L_lenght.configure(background="#161B21",font=('Helvetica', 25,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Lenght ''')
    
    P_lenght=tk.IntVar(value="In cm")
    P_lenght_e = tk.Entry(Frame2,textvariable=P_lenght)#state=tk.DISABLED
    P_lenght_e.place(x=275, y=550, height=35, width=250)
    P_lenght_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")
 
    L_width = tk.Label(Frame2)
    L_width.place(x=50, y=620)
    L_width.configure(background="#161B21",font=('Helvetica', 25,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Width ''')
    
    
    P_width=tk.IntVar()
    P_width_e = tk.Entry(Frame2,textvariable=P_width)#state=tk.DISABLED
    P_width_e.place(x=275, y=620, height=35, width=250)
    P_width_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")
 
    L_height = tk.Label(Frame2)
    L_height.place(x=50, y=690)
    L_height.configure(background="#161B21",font=('Helvetica', 25,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Height ''')
    
    p_height=tk.IntVar()
    p_height_e = tk.Entry(Frame2,textvariable=p_height)#state=tk.DISABLED
    p_height_e.place(x=275, y=690, height=35, width=250)
    p_height_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")
 
    L_weight = tk.Label(Frame2)
    L_weight.place(x=50, y=760)
    L_weight.configure(background="#161B21",font=('Helvetica', 25,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Weight ''')

    L_price = tk.Label(Frame2)
    L_price.place(x=600, y=680)
    L_price.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''price ''')

    Price="On Weight"
    Price_e = tk.Label(Frame2,text=Price)
    Price_e.place(x=825, y=680, height=30, width=250)
    Price_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")

    def change_value(object):
        Price=(P_weight.get())*0.3
        Price_e.configure(text=Price)
        print(Price)

    P_weight=tk.IntVar(value="In Gram")
    P_weight_e = tk.Entry(Frame2,textvariable=P_weight)#state=tk.DISABLED
    P_weight_e.place(x=275, y=760, height=35, width=250)
    P_weight_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")

    P_weight_e.bind('<FocusOut>', change_value)

    

    L_Date = tk.Label(Frame2)
    L_Date.place(x=600, y=550)
    L_Date.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Date ''')

    Date=tk.StringVar(value="Like DD/MM/YYYY")
    Date_e = tk.Entry(Frame2,textvariable=Date)#state=tk.DISABLED
    Date_e.place(x=825, y=552, height=30, width=250)
    Date_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")

    L_Time = tk.Label(Frame2)
    L_Time.place(x=600, y=620)
    L_Time.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Time ''')
    
    Time=tk.StringVar(value="HH:MM in 24 hour")
    Time_e = tk.Entry(Frame2,textvariable=Time)#state=tk.DISABLED
    Time_e.place(x=825, y=620, height=30, width=250)
    Time_e.configure(background="#F4A950",font=('Helvetica', 19,'bold'),foreground="#161B21",relief="flat")

    def make_delivery():
        emp=coursor.execute('select max(E_id) from employee')
        emp=emp.fetchall()
        emp_max=emp[0][0]
        # print(type(emp_max))
        que=coursor.execute('select max(p_id) from product_details')
        que=que.fetchall()
        id_1=que[0][0]+1
        e_id=random.randint(20001,emp_max)

        s1='insert into product_details values'
        s1+=f'({id_1},\'{product_type.get()}\',{Price},{e_id},{customer_id},{P_weight.get()},{P_lenght.get()},{p_height.get()},{P_weight.get()})'

        status='booked'
        s2='insert into delivary values'
        s2+=f'({id_1},sysdate,CURRENT_TIMESTAMP,{S_Pincode.get()},{R_Pincode.get()},\'{status}\')'


        city=coursor.execute(f"select city_name,state_name from location where pincode={S_Pincode.get()}")
        data_1=city.fetchall()

        city=coursor.execute(f"select city_name,state_name from location where pincode={R_Pincode.get()}")
        data_2=city.fetchall()

        s3='insert into del_add values'
        s3+=f'({id_1},\'{Name.get()}\',\'{S_contact.get()}\',{S_Pincode.get()},\'{data_1[0][1]}\',\'{data_1[0][0]}\')'
        s4='insert into drop_add values'
        s4+=f'({id_1},\'{R_name.get()}\',\'{R_Pincode.get()}\',{R_Pincode.get()},\'{data_2[0][1]}\',\'{data_2[0][0]}\')'
        # print(s1+"\n"+s2+"\n"+s3+"\n"+s4)
        sender=f"Sender name::\t{Name.get()}\nCustomer id::\t{customer_id.get()}\n Sender Phone Number::\t{S_contact.get()}\nSender Pincode::\t{S_Pincode.get()}\n"
        receiver=f"Receiver Name::\t{R_name.get()}\n Receiver Phon No::\t{L_contact.get()}\n Receiver Pincode::\t{R_Pincode.get()} \n"
        Product_d=f"\n\tProduct Details\n\n product type::\t{product_type.get()}\nProduct Length::\t{P_lenght.get()}\nProduct Width ::\t{P_width.get()}\nProduct Height::\t{p_height.get()}\nProduct  Weight::\t{P_weight.get()}\n"
        parcel=f"\nPrice ::\t{Price}\n PiD::\t{id_1}\n Employee_ID::\t{e_id}"
        res=tk.messagebox.askyesno("Your Order Details",f"{sender} {receiver}{Product_d}{parcel}")
        # tk.messagebox.showinfo("Your Order Details"f"name")
        if res=='yes':
            coursor.execute(s1)
            coursor.execute(s2)
            coursor.execute(s3)
            coursor.execute(s4)
            coursor.execute("commit")

    Button1 = tk.Button(Frame2, command=make_delivery)
    Button1.place(x=790, y=740,height=40)
    Button1.configure(foreground="#161B21",background="#F4A950",relief = 'flat',font=('Helvetica', 34),text='''Submit''')

###################### Track Order ###############
def track_order():
    for widget in Frame2.winfo_children():
            widget.destroy()
    
    Track_oreder_L = tk.Label(Frame2)
    Track_oreder_L.place(x=270, y=170)
    Track_oreder_L.configure(background="#161B21",font=('Helvetica', 55,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Track Order''')
    
    Track_oreder_L = tk.Label(Frame2)
    Track_oreder_L.place(x=270, y=300)
    Track_oreder_L.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''PID''')

    Pid=tk.IntVar()
    Pid_e=tk.Entry(Frame2,textvariable=Pid)
    Pid_e.place(x=345,y=300)
    Pid_e.configure(foreground="#161B21",background="#F4A950",font=('Helvetica', 20,'bold'))

    # cancle_order_L = tk.Label(Frame2)
    # cancle_order_L.place(x=270, y=400)
    # cancle_order_L.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Cancel Courier''')

    check=tk.IntVar()
    Radiobutton1_2 = tk.Checkbutton(Frame2)
    Radiobutton1_2.place(x=270, y=400,height=28)
    Radiobutton1_2.configure(activebackground="#161B21",activeforeground="#F4A950",background="#161B21",foreground="#F4A950",font=('Helvetica', 20,'bold'),relief='flat',text='''Cancel Courier''')
    Radiobutton1_2.configure( onvalue=1, offvalue=0,variable=check)
    
    def track_():
        cancle=check.get()
        print(Pid.get(),type(Pid.get()))
        if cancle==1:
            s=f'update delivary set status_del=\'cancel\' where p_id={Pid.get()}'
            coursor.execute(s)
        l=[Pid.get()]
        s1=f'select p_type,e_id from product_details where p_id={Pid.get()}'
        pro=coursor.execute(s1)
        pro_1=pro.fetchall()
        l.append(pro_1[0][0])

        s2=f'select name_emp,contact_emp from employee where e_id={pro_1[0][1]}'
        emp=coursor.execute(s2)
        emp_2=emp.fetchall()
        l.append(emp_2[0][0])
        l.append(emp_2[0][1])

        s3=f'select del_date,del_time,status_del from delivary where p_id={Pid.get()}'
        delv=coursor.execute(s3)
        delv_2=delv.fetchall()
        date=str(delv_2[0][0]).split()
        l.append(date[0])
        l.append(date[1])
        l.append(delv_2[0][2])
        print(l)
        Text1 = tk.Text(Frame2)
        Text1.place(x=70, y=530, height=40, width=1000)
        Text1.configure(background="#F4A950",font=('Consolas',18,'bold'),foreground="#161B21",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")

        for row in l:

            # p="{:10s}{:15s}{:10s}{:15s}{:20s}".format(str(row[0]),row[1],row[2],row[3],row[4])
        #     print(p)
            Text1.insert(tk.END,row)
            Text1.insert(tk.END,"\t  ")
        Text1.insert(tk.END,"\n")
        coursor.execute("commit")
        # print(cancle)

    Button1 = tk.Button(Frame2, command=track_)
    Button1.place(x=360, y=475,height=36)
    Button1.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 34),text='''Submit''')
    
###################### Terms and Condition ############
def terms_condition():
    for widget in Frame2.winfo_children():
            widget.destroy()
    terms_condition_l = tk.Label(Frame2)
    terms_condition_l.place(x=70, y=40)
    terms_condition_l.configure(background="#161B21",font=('Helvetica', 55,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Terms And Condition''')
    
    Text1 = tk.Text(Frame2)
    Text1.place(x=70, y=120, height=660, width=1000)
    Text1.configure(background="#F4A950",font=('Consolas',16,'bold'),foreground="#161B21",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")

    condition_1="1. In this contract; ‘Courier’ shall mean and include the business T&C Couriers, its proprietors, employees and agents. ‘Independent Carrier’ shall mean and include any person, firm or company with whom the Courier may arrange for the transportation of any goods under this contract and any person who is now or hereafter an employee, agent or subcontractor of any Independent Carrier, ‘Customer’ shall mean and include any person, firm or company who engages or enters into a contract with the Courier, for the Courier to provide transport of or for the goods and articles,‘Goods’ shall mean and include any goods, items, articles transported or to be transported by the Courier\n"
    condition_2="2. The Courier is not a common carrier. All goods are transported or stored, and all services are performed by the Courier subject to these conditions of contract. The Courier reserves the right to refuse to transport any goods for any person, firm or company at its discretion and the Courier shall not be bound to give any reason for such refusal.\n"
    condition_3="3. The Customer hereby authorises the Courier to arrange with any Independent Carrier(s) for the transportation of any such goods under this contract. The Independent Carrier shall be entitled to the full benefit of these terms and conditions to the same extent as the Courier, and the Courier shall be deemed to have entered into this contract for its own benefit, and also as agent for the Independent Carrier(s)\n"
    condition_4="4. The person delivering the goods to the Courier shall be deemed to be the agent of the Customer for the purposes of this contract, and the Customer hereby warrants that such a person is authorised to enter into the contract and sign the consignment note as agent for the Customer\n"
    condition_5="5. The Customer expressly warrants to the Courier that the Customer is either the owner of or an authorised agent for the owner of any goods under this contract.\n"
    condition_6="6. The Customer hereby authorises the Courier to handle, store or carry the goods by any method or route which the Courier in its discretion shall think fit.\n"
    condition_7="7. Subject to clause 8, the goods are at the risk of the Customer and not the Courier, and the Courier shall not be responsible in tort or contract or otherwise for any reason whatsoever (including without limiting the foregoing, the negligent or wilful act or default of the Courier, its employees or agents or Independent Carriers or any other person) for any loss or detriment or damage suffered by the Customer or any other person by any reason whatsoever, including, without limiting the forgoing, by reason of loss of or damage to or deterioration of the goods or by reason of misdelivery or the failure to deliver or delay in delivering the goods, including perishable goods, either in transport or in storage. The provisions of this clause apply to any loss, detriment or damage suffered by the Customer or any other person whether or not the acts or defaults or events giving rise to the loss, detriment or damage occurred in the course of performance by the Courier of this contract are or such that would constitute a fundamental breach of the contract or a breach of the fundamental term thereof.\n"
    condition_8="8. The Courier shall continue to be subject to any implied warranty which the Trade Practices Act 1974 (as amended) or any other legislation provides if and to the extent that the said legislation is applicable to this contract and prevents any exclusion, restriction or modification of the warranty.\n"
    condition_9="9. All rights, immunities and limitations of liability granted to the Courier by the provisions of this contract, shall continue to have full force and effect notwithstanding any breach of the contract or conditions hereof by the Courier.\n"
    condition_10="10. If the customer or any other person fails to pay any charges or monies due to the Courier in respect of any service rendered by the Courier, on reasonable demand being made in accordance with the contract, the Courier may retain and sell all or any of the goods of that person which are in its possession and, out of monies arising from the sale, retain charges due to the Courier and all charges and expenses of any detention and sale shall render the surplus, if any, of the moneys arising from the sale of the goods and shall render any goods remaining unsold to the person entitled thereto. Any such sale shall not prejudice or affect the charges or other moneys due and payable in respect of such a service or in respect of the said detention and sale.\n"
    condition_11="11. The Customer shall not tender for transportation of any explosive or inflammable or otherwise dangerous goods, or goods capable of damaging other goods without giving to the Courier a full description disclosing the explosive, inflammable or dangerous or damaging character of the goods and, in the default of so doing, the Customer shall be liable for all loss and damage caused thereby.\n"
    condition_12="12. The Customer shall comply with all laws, customs or regulations of any State or Territory including those relating to the packaging, carriage or delivery of goods and shall furnish information and attach such documents to the consignment note as may be necessary, to comply with such laws and regulations. The Courier shall not be liable to any person for loss or expense due to the Customers failure to comply with this provision.\n"
    condition_13="13. The Customer will remain responsible to the Courier for all its proper charges incurred for any reason. Labour to load or unload any vehicle shall be the responsibility of the Courier, and at the expense of the Customer."

    Text1.insert(tk.END,condition_1+"\n"+condition_2+"\n"+condition_3+"\n"+condition_4+"\n"+condition_5+"\n"+condition_6+"\n"+condition_7+"\n"+condition_8+"\n"+condition_9+"\n"+condition_10+"\n"+condition_11+"\n"+condition_12+"\n"+condition_13)
    # Text1.insert(tk.END,"\n")
    Button1 = tk.Button(Frame2, command=lambda: after_login())
    Button1.place(x=475, y=790,height=36)
    Button1.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 34),text='''Submit''')
    
####################### Log in for Employee ###########################
def employee_login():
    for widget in Frame2.winfo_children():
            widget.destroy()
    
    employee_btn.configure(foreground="#F4A950",background="#161B21")
    home.configure(background="#F4A950",foreground="#161B21")
    admin_btn.configure(background="#F4A950",foreground="#161B21")


    Label1 = tk.Label(Frame2)
    Label1.place(x=410, y=270)
    Label1.configure(background="#161B21",foreground="#F4A950",text="Log in",font=('Helvetica', 42,'bold'))

    Label_name = tk.Label(Frame2)
    Label_name.place(x=250, y=400, height=40, width=126)
    Label_name.configure(background="#161B21",font=('Helvetica', 34,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''ID''')

    Label_password = tk.Label(Frame2)
    Label_password.place(x=250, y=470, height=40, width=227)
    Label_password.configure(background="#161B21",font=('Helvetica', 34,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Password''')


    Id=tk.IntVar()
    Entry_Name = tk.Entry(Frame2,textvariable=Id)
    Entry_Name.place(x=500, y=400, height=40, width=250)
    Entry_Name.configure(takefocus="",cursor="ibeam",font=('Helvetica', 26,'bold'))

    password=tk.StringVar()
    Entry_password = tk.Entry(Frame2, show="*",textvariable=password)
    Entry_password.place(x=500, y=470,height=40, width=250)
    Entry_password.configure(takefocus="",cursor="ibeam",font=('Helvetica', 26,'bold'))

    def validte():
        # print(Id.get(),password.get())
        pass_1=coursor.execute(f'select password_emp from employee where e_id={Id.get()}')
        pass_1=pass_1.fetchall()
        if password.get()==pass_1[0][0]:
            after_employee_login(Id.get())
        else:
            tk.messagebox.showerror("Wrong Entry", "Enter valid ID or password")


    Button1 = tk.Button(Frame2,command= validte)
    Button1.place(x=410, y=530, height=40, width=250)
    Button1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),text='''Submit''')
    
####################### employee log in  ########################
def after_employee_login(Id):
    for widget in Frame2.winfo_children():
            widget.destroy()
     
    Label_name = tk.Label(Frame2)
    Label_name.place(x=250, y=400, height=40, width=126)
    Label_name.configure(background="#161B21",font=('Helvetica', 34,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''ID''')

    My_detail = tk.Button(Frame2,command=lambda:employee_detail(Id))
    My_detail.place(x=50, y=250, height=310, width=310)
    My_detail.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=detail_icon)

    pending = tk.Button(Frame2,command= lambda:pending_order(Id))
    pending.place(x=400, y=235, height=310, width=310)
    pending.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=pending_icon)

    completed = tk.Button(Frame2,command=lambda:completed_order("Employee",Id))
    completed.place(x=750, y=250, height=310, width=310)
    completed.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=completed_icon)
    # terms.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=terms)

    # Employee = tk.Button(Frame2)
    # Employee.place(x=400, y=400, height=310, width=310)
    # Employee.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=more_icon)

    # Admin = tk.Button(Frame2)
    # Admin.place(x=570, y=400, height=310, width=310)
    # Admin.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=admin)

def employee_detail(Id):
    for widget in Frame2.winfo_children():
            widget.destroy()
    
    # Label_name = tk.Label(Frame2)
    # Label_name.place(x=250, y=400, height=40, width=126)
    # Label_name.configure(background="#161B21",font=('Helvetica', 34,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''ID''')

    # Id=tk.IntVar()
    # Entry_Name = tk.Entry(Frame2,textvariable=Id)
    # Entry_Name.place(x=500, y=400, height=40, width=250)
    # Entry_Name.configure(takefocus="",cursor="ibeam",font=('Helvetica', 26,'bold'))

    # def validate():
    #     for widget in Frame2.winfo_children():
    #         widget.destroy()
    
    employee_detail_L = tk.Label(Frame2)
    employee_detail_L.place(x=400, y=100, height=310, width=310)
    employee_detail_L.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=employee_detail_icon)

    Y=450
    l1=tk.Label(Frame2)
    l1.place(x=350,y=Y,height=35)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 25,"bold"),text="Id")
    Y+=45
    l1=tk.Label(Frame2)
    l1.place(x=350,y=Y,height=35)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',25,"bold"),text="Name")
    Y+=45
    l1=tk.Label(Frame2)
    l1.place(x=350,y=Y,height=35)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',25,"bold"),text="Contact No.")
    Y+=45
    l1=tk.Label(Frame2)
    l1.place(x=350,y=Y,height=35)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',25,"bold"),text="City")
    Y+=45
    l1=tk.Label(Frame2)
    l1.place(x=350,y=Y,height=35)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',25,"bold"),text="E-Mail")
    Y+=45
    l1=tk.Label(Frame2)
    l1.place(x=350,y=Y,height=35)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',25,"bold"),text="User Name")
    
    Y=450
    for i in range(0,6):
        l1=tk.Label(Frame2)
        l1.place(x=560,y=Y,height=35)
        l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',25,"bold"),text=":")
        Y+=45
    s=f'select e_id,name_emp,contact_emp,address_emp,email_emp,u_name_emp from employee where e_id={int(Id)}'
    emp_data=coursor.execute(s)
    emp_1=emp_data.fetchall()
    # print(emp_1)
    Y=450
    for i in emp_1[0]:
        l1=tk.Label(Frame2)
        l1.place(x=590,y=Y,height=35)
        l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',21,"bold"),text=i)
        Y+=45

    Button1 = tk.Button(Frame2, command=lambda:after_employee_login(Id))
    Button1.place(x=360, y=Y+50,height=36)
    Button1.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 25),text='''Back''')
    
    # Button1 = tk.Button(Frame2, command=validate)
    # Button1.place(x=360, y=475,height=36)
    # Button1.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 25),text='''Submit''')
    

def pending_order(Id):
    for widget in Frame2.winfo_children():
            widget.destroy()
    
    Text1 = tk.Text(Frame2)
    Text1.place(x=70, y=120, height=520, width=1000)
    Text1.configure(background="#F4A950",font=('Consolas',22,'bold'),foreground="#161B21",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")
    
    Track_oreder_L = tk.Label(Frame2)
    Track_oreder_L.place(x=70, y=50)
    Track_oreder_L.configure(background="#161B21",font=('Helvetica', 35,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Pending Order''')
    
    pen=coursor.execute(f'select product_details.p_id,product_details.p_type,product_details.amount,product_details.c_id,delivary.status_del from delivary,product_details where delivary.p_id=product_details.p_id and delivary.status_del!=\'delivery\' and product_details.e_id={Id}')
    pe_1=pen.fetchall()
    print(pe_1)

    for row in pe_1:

        p="{:10s}{:15s}{:10s}{:15s}{:20s}".format(str(row[0]),row[1],str(row[2]),str(row[3]),row[4])
        # print(p)
        Text1.insert(tk.END,p)
        Text1.insert(tk.END,"\n")
    Text1.configure(state=tk.DISABLED)


    Track_oreder_L = tk.Label(Frame2)
    Track_oreder_L.place(x=70, y=650)
    Track_oreder_L.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Update''')
    
    Track_oreder_L = tk.Label(Frame2)
    Track_oreder_L.place(x=70, y=700)
    Track_oreder_L.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''PID''')
    

    Pid=tk.IntVar()
    Pid_e=tk.Entry(Frame2,textvariable=Pid)
    Pid_e.place(x=180, y=700)
    Pid_e.configure(foreground="#161B21",background="#F4A950",font=('Helvetica', 20,'bold'))

    cancle_order_L = tk.Label(Frame2)
    cancle_order_L.place(x=70, y=750)
    cancle_order_L.configure(background="#161B21",font=('Helvetica', 20,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Status''')

    status=tk.StringVar()
    status_e=tk.Entry(Frame2,textvariable=status)
    status_e.place(x=180, y=750)
    status_e.configure(foreground="#161B21",background="#F4A950",font=('Helvetica', 20,'bold'))

    Button1 = tk.Button(Frame2,command=lambda: after_employee_login(Id))
    Button1.place(x=170, y=800,height=36)
    Button1.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 20,'bold'),text='''Back''')
    def update():
        # print(f'update delivary set status_del=\'{status.get()}\' where p_id={Pid.get()}')
        coursor.execute(f'update delivary set status_del=\'{status.get()}\' where p_id={Pid.get()}')
        coursor.execute("commit")

    Button1 = tk.Button(Frame2,command=update)
    Button1.place(x=300, y=800,height=36)
    Button1.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 20,'bold'),text='''Update''')

def completed_order(from1,Id):
    for widget in Frame2.winfo_children():
            widget.destroy()
    
    Track_oreder_L = tk.Label(Frame2)
    Track_oreder_L.place(x=70, y=50)
    Track_oreder_L.configure(background="#161B21",font=('Helvetica', 35,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Completed Order''')
    
    Text1 = tk.Text(Frame2)
    Text1.place(x=70, y=120, height=660, width=1000)
    Text1.configure(background="#F4A950",font=('Consolas',20,'bold'),foreground="#161B21",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")
    


    if from1=="Employee":
        Button1 = tk.Button(Frame2,command=lambda: after_employee_login(Id))
        pen=coursor.execute(f'select product_details.p_id,product_details.p_type,product_details.amount,product_details.c_id,delivary.status_del from delivary,product_details where delivary.p_id=product_details.p_id and delivary.status_del=\'delivery\' and product_details.e_id={Id}')
        pe_1=pen.fetchall()
        print(pe_1)
        for row in pe_1:

            p="{:10s}{:15s}{:10s}{:15s}{:20s}".format(str(row[0]),row[1],str(row[2]),str(row[3]),row[4])
            print(p)
            Text1.insert(tk.END,p)
            Text1.insert(tk.END,"\n")
        Text1.configure(state=tk.DISABLED)
    
    else:
        pen=coursor.execute(f'select product_details.p_id,product_details.p_type,product_details.amount,product_details.c_id,product_details.e_id from delivary,product_details where delivary.p_id=product_details.p_id and delivary.status_del=\'delivery\'')
        pe_1=pen.fetchall()
        print(pe_1)
        for row in pe_1:

            p="{:10s}{:15s}{:10s}{:15s}{:20s}".format(str(row[0]),row[1],str(row[2]),str(row[3]),str(row[4]))
            print(p)
            Text1.insert(tk.END,p)
            # Text1.insert(tk.END,"\n")
        Text1.configure(state=tk.DISABLED)
        Button1 = tk.Button(Frame2,command=lambda: after_admin_login())
    Button1.place(x=475, y=790,height=36)
    Button1.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 20,'bold'),text='''Back''')

####################### admin log in  ########################
def admin_log_in():
    for widget in Frame2.winfo_children():
            widget.destroy()
    admin_btn.configure(foreground="#F4A950",background="#161B21")
    home.configure(background="#F4A950",foreground="#161B21")
    employee_btn.configure(background="#F4A950",foreground="#161B21")

    Label1 = tk.Label(Frame2)
    Label1.place(x=410, y=270)
    Label1.configure(background="#161B21",foreground="#F4A950",text="Log in",font=('Helvetica', 42,'bold'))

    Label_name = tk.Label(Frame2)
    Label_name.place(x=250, y=400, height=40, width=126)
    Label_name.configure(background="#161B21",font=('Helvetica', 34,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Name''')

    Label_password = tk.Label(Frame2)
    Label_password.place(x=250, y=470, height=40, width=227)
    Label_password.configure(background="#161B21",font=('Helvetica', 34,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Password''')


    Id=tk.StringVar()
    Entry_Name = tk.Entry(Frame2,textvariable=Id)
    Entry_Name.place(x=500, y=400, height=40, width=250)
    Entry_Name.configure(takefocus="",cursor="ibeam",font=('Helvetica', 26,'bold'))

    password=tk.StringVar()
    Entry_password = tk.Entry(Frame2, show="*",textvariable=password)
    Entry_password.place(x=500, y=470,height=40, width=250)
    Entry_password.configure(takefocus="",cursor="ibeam",font=('Helvetica', 26,'bold'))

    def validte():
        print(Id.get(),password.get())
        pass_1=coursor.execute(f'select password_admin from admin where u_name_admin=\'{Id.get()}\'')
        pass_1=pass_1.fetchall()
        if password.get()==pass_1[0][0]:
            after_admin_login()
        else:
            tk.messagebox.showerror("Wrong Entry", "Enter valid ID or password")


    Button1 = tk.Button(Frame2, command=validte)
    Button1.place(x=410, y=530, height=40, width=250)
    Button1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),text='''Submit''')

def after_admin_login():
    for widget in Frame2.winfo_children():
            widget.destroy()
    
    New_delivery = tk.Button(Frame2,command=lambda:display("Employee"))
    New_delivery.place(x=50, y=50, height=310, width=310)
    New_delivery.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=employee)

    Track_order = tk.Button(Frame2,command=lambda:completed_order('admin',"admin"))
    Track_order.place(x=400, y=50, height=310, width=310)
    Track_order.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=completed_icon)

    terms = tk.Button(Frame2,command=lambda:display("customer"))
    terms.place(x=750, y=50, height=310, width=310)
    terms.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=customer_icon)

    Employee = tk.Button(Frame2,command=lambda:cancel_order())
    Employee.place(x=400, y=400, height=310, width=310)
    Employee.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=cancelled_icon)

    # Admin = tk.Button(Frame2)
    # Admin.place(x=570, y=400, height=310, width=310)
    # Admin.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 34),cursor="hand2",image=admin)

def cancel_order():
    for widget in Frame2.winfo_children():
            widget.destroy()
    
    Track_oreder_L = tk.Label(Frame2)
    Track_oreder_L.place(x=70, y=50)
    Track_oreder_L.configure(background="#161B21",font=('Helvetica', 35,'bold'),disabledforeground="#a3a3a3",foreground="#F4A950",text='''Cancel Order''')
    
    Text1 = tk.Text(Frame2)
    Text1.place(x=70, y=120, height=660, width=1000)
    Text1.configure(background="#F4A950",font=('Consolas',16,'bold'),foreground="#161B21",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")
    
    pen=coursor.execute(f'select product_details.p_id,product_details.p_type,product_details.amount,product_details.c_id,product_details.e_id from delivary,product_details where delivary.p_id=product_details.p_id and delivary.status_del=\'cancled\'')
    pe_1=pen.fetchall()
    print(pe_1)
    for row in pe_1:

        p="{:10s}{:15s}{:10s}{:15s}{:20s}".format(str(row[0]),row[1],str(row[2]),str(row[3]),str(row[4]))
        print(p)
        Text1.insert(tk.END,p)
        Text1.insert(tk.END,"\n")
    Text1.configure(state=tk.DISABLED)
    Button1 = tk.Button(Frame2,command=lambda: after_admin_login())
    Button1.place(x=475, y=790,height=36)
    Button1.configure(background="#F4A950",foreground="#161B21",relief = 'flat',font=('Helvetica', 20,'bold'),text='''Back''')

####################### Display(employee, admin)  ########################
def display(variable="customer"):
    for widget in Frame2.winfo_children():
            widget.destroy()
    Y=10
    l1=tk.Label(Frame2)
    l1.place(x=50,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 15,"bold"),text="Id")
    l1=tk.Label(Frame2)
    l1.place(x=140,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="Name")
    l1=tk.Label(Frame2)
    l1.place(x=260,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="Contact No.")
    l1=tk.Label(Frame2)
    l1.place(x=415,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="City")
    l1=tk.Label(Frame2)
    l1.place(x=595,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="E-Mail")
    l1=tk.Label(Frame2)
    l1.place(x=830,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="User Name")
    l1=tk.Label(Frame2)
    l1.place(x=950,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="Password")

    Text1 = tk.Text(Frame2)
    Text1.place(x=50, y=40, height=600, width=1000)
    Text1.configure(background="#F4A950",font=('Consolas',16,'bold'),foreground="#161B21",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")

    Y=650
    l1=tk.Label(Frame2)
    l1.place(x=50,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 15,"bold"),text="C_Id")

    C_ID=tk.IntVar()
    C_ID_e = tk.Entry(Frame2,textvariable=C_ID)#state=tk.DISABLED
    C_ID_e.place(x=50,y=Y+40,height=20,width=70)
    C_ID_e.configure(background="#F4A950",font=('Helvetica', 15,'bold'),foreground="#161B21",relief="flat")

    l1=tk.Label(Frame2)
    l1.place(x=140,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="Name")

    Name=tk.StringVar()
    Name_e = tk.Entry(Frame2,textvariable=Name)#state=tk.DISABLED
    Name_e.place(x=140,y=Y+40,height=20,width=100)
    Name_e.configure(background="#F4A950",font=('Helvetica', 15,'bold'),foreground="#161B21",relief="flat")

    l1=tk.Label(Frame2)
    l1.place(x=260,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="Contact No.")

    Contact=tk.IntVar()
    Contact_e = tk.Entry(Frame2,textvariable=Contact)#state=tk.DISABLED
    Contact_e.place(x=260,y=Y+40,height=20,width=130)
    Contact_e.configure(background="#F4A950",font=('Helvetica', 15,'bold'),foreground="#161B21",relief="flat")


    l1=tk.Label(Frame2)
    l1.place(x=415,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="City")

    City=tk.StringVar()
    City_e = tk.Entry(Frame2,textvariable=City)#state=tk.DISABLED
    City_e.place(x=415,y=Y+40,height=20,width=160)
    City_e.configure(background="#F4A950",font=('Helvetica', 15,'bold'),foreground="#161B21",relief="flat")


    l1=tk.Label(Frame2)
    l1.place(x=595,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="E-Mail")

    Email=tk.StringVar()
    Email_e = tk.Entry(Frame2,textvariable=Email)#state=tk.DISABLED
    Email_e.place(x=595,y=Y+40,height=20,width=210)
    Email_e.configure(background="#F4A950",font=('Helvetica', 15,'bold'),foreground="#161B21",relief="flat")

    l1=tk.Label(Frame2)
    l1.place(x=830,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="User Name")

    Uname=tk.StringVar()
    Uname_e = tk.Entry(Frame2,textvariable=Uname)#state=tk.DISABLED
    Uname_e.place(x=830,y=Y+40,height=20,width=105)
    Uname_e.configure(background="#F4A950",font=('Helvetica', 15,'bold'),foreground="#161B21",relief="flat")

    l1=tk.Label(Frame2)
    l1.place(x=950,y=Y,height=20)
    l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica',15,"bold"),text="Password")

    password=tk.StringVar()
    password_e = tk.Entry(Frame2,textvariable=password)#state=tk.DISABLED
    password_e.place(x=950,y=Y+40,height=20,width=95)
    password_e.configure(background="#F4A950",font=('Helvetica', 15,'bold'),foreground="#161B21",relief="flat")

    if variable=="Employee":
        customer=coursor.execute("select * from Employee")
        rows=customer.fetchall()


        for row in rows:

            p="{:7s}{:10s}{:13s}{:15s}{:20s}{:10s}{:10s}".format(str(row[0]),row[1],row[2],row[3],row[4],row[5],row[6])
            # print(p)
            Text1.insert(tk.END,p)
            Text1.insert(tk.END,"\n")
        Text1.configure(state=tk.DISABLED)
       
        l1=tk.Label(Frame2)
        l1.place(x=50,y=Y,height=20)
        l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 15,"bold"),text="E_Id")

        E_ID=tk.IntVar()
        E_ID_e = tk.Entry(Frame2,textvariable=E_ID)#state=tk.DISABLED
        E_ID_e.place(x=50,y=Y+40,height=20,width=70)
        E_ID_e.configure(background="#F4A950",font=('Helvetica', 15,'bold'),foreground="#161B21",relief="flat")


    if variable.lower()=="customer":
        customer=coursor.execute("select * from Customer")
        rows=customer.fetchall()


        for row in rows:

            p="{:7s}{:10s}{:13s}{:15s}{:20s}{:10s}{:10s}".format(str(row[0]),row[1],row[2],row[3],row[4],row[5],row[6])
            # print(p)
            Text1.insert(tk.END,p)
            Text1.insert(tk.END,"\n")
        Text1.configure(state=tk.DISABLED)

        l1=tk.Label(Frame2)
        l1.place(x=50,y=Y,height=20)
        l1.configure(background="#161B21",foreground="#F4A950",relief = 'flat',font=('Helvetica', 15,"bold"),text="C_Id")

        C_ID=tk.IntVar()
        C_ID_e = tk.Entry(Frame2,textvariable=C_ID)#state=tk.DISABLED
        C_ID_e.place(x=50,y=Y+40,height=20,width=70)
        C_ID_e.configure(background="#F4A950",font=('Helvetica', 15,'bold'),foreground="#161B21",relief="flat")

    def add_new():
        if variable=="Employee":
            que=coursor.execute('select max(e_id) from employee')
            que=que.fetchall()
            print(que)
            print(f'insert into employee values({que[0][0]+1},\'{Name.get()}\',{Contact.get()},\'{str(City.get())}\',\'{Email.get()}\',\'{Uname.get()}\',{password.get()})')
            coursor.execute(f'insert into employee values({que[0][0]+1},\'{Name.get()}\',\'{Contact.get()}\',\'{City.get()}\',\'{Email.get()}\',\'{Uname.get()}\',\'{password.get()}\')')
            coursor.execute("commit")
            display('Employee')
        if variable=="customer":
            que=coursor.execute('select max(c_id) from customer')
            que=que.fetchall()
            print(que)
            print(f'insert into customer values({que[0][0]+1},\'{Name.get()}\',{Contact.get()},\'{str(City.get())}\',\'{Email.get()}\',\'{Uname.get()}\',{password.get()})')
            coursor.execute(f'insert into customer values({que[0][0]+1},\'{Name.get()}\',\'{Contact.get()}\',\'{City.get()}\',\'{Email.get()}\',\'{Uname.get()}\',\'{password.get()}\')')
            coursor.execute("commit")
            display('customer')

    Add_new_customer = tk.Button(Frame2,command=add_new)# command=lambda: after_login()) like this Your function came here
    Add_new_customer.place(x=200, y=750,height=32)
    Add_new_customer.configure(foreground="#161B21",background="#F4A950",relief = 'flat',font=('Helvetica', 25),text='''Add New''')

    Back = tk.Button(Frame2,command=lambda:after_admin_login())# command=lambda: after_login()) like this Your function came here
    Back.place(x=500, y=750,height=32)
    Back.configure(foreground="#161B21",background="#F4A950",relief = 'flat',font=('Helvetica', 25),text='''Back''')

####################### sign-up  ########################

# display('customer')
Home()
# after_login()
# after_emplyee_login()
# after_employee_login()
# after_admin_login()
# delivery()
# track_order()
# pending_order(20001)
# employee_detail(30001)
# completed_order("admin",'admin')
# completed_order("Employee",20001)
# cancel_order()
# coursor.execute("commit")
win.mainloop()