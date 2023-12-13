from tkinter import*
from tkinter import messagebox
import os,random,tempfile,smtplib
win=Tk()
win.title("Billing system")
win.geometry("700x600")
win.state("zoomed")
win.iconbitmap('bill.ico')
if not os.path.exists('Bills'):
    os.mkdir('Bills')
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

def save_bill():
    global billno
    result=messagebox.askyesno('Confirm','Do you want to save the bill')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'Bills/{billno}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number {billno} is savesuccessfully')
billno=random.randint(500,1000)

def search_bill():
    found=False
    for i in os.listdir('Bills/'):
        if i.split('_')[0]==bill_no_entry.get():
            f=open(f'Bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            found=True
            break
    if not found:
        messagebox.showerror('Error','Invalid Bill Number')
                
    
def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login('bansalchirag12345@gmail.com','bmna xljf tvft rvvr')
            message=email_textarea.get(1.0,END)
            ob.sendmail('bansalchirag12345@gmailcom',recipient_entry.get(),message)
            ob.quit
            messagebox.showinfo('Success','Bill is successfully Sent')
        except Exception as e:
            print(e)
            messagebox.showerror('Error','Something Went wrong')
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error',"Bill is Empty")
    else:
        newwin=Toplevel()
        newwin.title("Send E-Mail")
        newwin.config(bg='gray20')

        recipient_frame=LabelFrame(newwin,text="RECIPENT",font=('arial',14,'bold'),bg='gray20',fg='white',border=6)
        recipient_frame.grid(row=0,column=0,padx=40,pady=20)
        recipient_label=Label(recipient_frame,text="E-Mail Address",font=('arial',14,'bold'),bg='gray20',fg='white')
        recipient_label.grid(row=0,column=0,padx=10,pady=8)
        recipient_entry=Entry(recipient_frame,font=('arial',14,'bold'),bg='white',fg='black',border=2,relief='ridge',width=23)
        recipient_entry.grid(row=0,column=1,padx=10,pady=8)
        message_label=Label(recipient_frame,text="Message",font=('arial',14,'bold'),bg='gray20',fg='white')
        message_label.grid(row=2,column=0,padx=10,pady=8)
        email_textarea=Text(recipient_frame,font=('arial',14,'bold'),border=2,relief=SUNKEN,width=40,height=11)
        email_textarea.grid(row=3,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        send_button=Button(newwin,text="send",font=('arial',14,'bold'),width=15,command=send_gmail)
        send_button.grid(row=3,column=0)
        newwin.mainloop()

        
def bill_area():
    if cus_name_entry.get()=='' or phn_no_entry.get()=='':
        messagebox.showerror('Error','Customer Details Are Require')
    elif cosmetic_price_entry.get=='' and grocery_price_entry=='' and softdrink_price_entry=='':
        messagebox.showerror('Error',"No Product Selected")
    elif cosmetic_price_entry.get()=='0 Rs' and grocery_price_entry.get()=='0 Rs'and softdrink_price_entry.get()=='0 Rs':
        messagebox.showerror("error","Plz Select Any Product ")  
    else:
        
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill No:{billno}')
        textarea.insert(END,f'\nCustomer Name:{cus_name_entry.get()}')
        textarea.insert(END,f'\nPhone Number:{phn_no_entry.get()}')
        textarea.insert(END,'\n======================================================')
        textarea.insert(END,'\nProduct \t\t\t Quantity \t\tPrice')
        textarea.insert(END,'\n======================================================')
        
        if soap_entry.get()!='0':
            textarea.insert(END,f'\nBathsoap \t\t\t {soap_entry.get()}\t\t{soapprice}Rs ')
        if coldcream_entry.get()!='0':
            textarea.insert(END,f'\nCold Cream \t\t\t {coldcream_entry.get()} \t\t{coldcreamprice}Rs')   
        if facewash_entry.get()!='0':
            textarea.insert(END,f'\nFace Wash \t\t\t {facewash_entry.get()} \t\t{facewashprice}Rs')
        if hairspray_entry.get()!='0':
            textarea.insert(END,f'\nHair Spray \t\t\t {hairspray_entry.get()} \t\t{hairsprayprice}Rs')
        if hairgel_entry.get()!='0':
            textarea.insert(END,f'\nHair Gel \t\t\t {hairgel_entry.get()} \t\t{hairgelprice}Rs')
        if bodylotion_entry.get()!='0':
            textarea.insert(END,f'\nBody Lotion \t\t\t {bodylotion_entry.get()} \t\t{bodylotionprice}Rs')

        if rice_entry.get()!='0':
            textarea.insert(END,f'\nRice \t\t\t {rice_entry.get()} \t\t{riceprice}Rs')
        if oil_entry.get()!='0':
            textarea.insert(END,f'\nOil \t\t\t {oil_entry.get()} \t\t{oilprice}Rs')
        if daal_entry.get()!='0':
            textarea.insert(END,f'\nDaal \t\t\t {daal_entry.get()} \t\t{daalprice}Rs')        
        if wheat_entry.get()!='0':
            textarea.insert(END,f'\nWheat \t\t\t {wheat_entry.get()} \t\t{wheatprice}Rs')
        if sugar_entry.get()!='0':
            textarea.insert(END,f'\nSugar \t\t\t {rice_entry.get()} \t\t{sugarprice}Rs')    
        if tea_entry.get()!='0':
            textarea.insert(END,f'\nTea \t\t\t {rice_entry.get()} \t\t{teaprice}Rs')

        if pepsi_entry.get()!='0':
            textarea.insert(END,f'\nPepsi \t\t\t {pepsi_entry.get()} \t\t{pepsiprice}Rs')
        if maaza_entry.get()!='0':
            textarea.insert(END,f'\nMaaza \t\t\t {maaza_entry.get()} \t\t{maazaprice}Rs')
        if cocacola_entry.get()!='0':
            textarea.insert(END,f'\nCoca-Cola \t\t\t {cocacola_entry.get()} \t\t{cocacolaprice}Rs')
        if Realjuice_entry.get()!='0':
            textarea.insert(END,f'\nReal Juice \t\t\t {Realjuice_entry.get()} \t\t{realjuiceprice}Rs')
        if redbull_entry.get()!='0':
            textarea.insert(END,f'\nRed Bull \t\t\t {redbull_entry.get()} \t\t{redbullprice}Rs')
        if clubsoda_entry.get()!='0':
            textarea.insert(END,f'\nClub Soda \t\t\t {clubsoda_entry.get()} \t\t{clubsodaprice}Rs')
        textarea.insert(END,'\n------------------------------------------------------')

        if grocery_tax_entry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Grocery Tax \t\t\t\t\t {grocery_tax_entry.get()}')
        if cosmetic_tax_entry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Cosmetic Tax \t\t\t\t\t {cosmetic_tax_entry.get()}')
        if softdrink_tax_entry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Softdrink Tax \t\t\t\t\t {softdrink_tax_entry.get()}')
        textarea.insert(END,f'\n Total Bill \t\t\t\t\t {totalbill}')
        save_bill()



def total():
    global soapprice,coldcreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice
    global riceprice,oilprice,daalprice,wheatprice,sugarprice,teaprice
    global pepsiprice,maazaprice,cocacolaprice,realjuiceprice,redbullprice,clubsodaprice
    global totalbill

    soapprice=int(soap_entry.get())*25 
    coldcreamprice=int(coldcream_entry.get())*52
    facewashprice=int(facewash_entry.get())*100
    hairsprayprice=int(hairspray_entry.get())*80
    hairgelprice=int(hairgel_entry.get())*150
    bodylotionprice=int(bodylotion_entry.get())*155

    riceprice=int(rice_entry.get())*90 
    oilprice=int(oil_entry.get())*120
    daalprice=int(daal_entry.get())*130
    wheatprice=int(wheat_entry.get())*30
    sugarprice=int(sugar_entry.get())*47
    teaprice=int(tea_entry.get())*60

    pepsiprice=int(pepsi_entry.get())*80
    maazaprice=int(maaza_entry.get())*60
    cocacolaprice=int(cocacola_entry.get())*95
    realjuiceprice=int(Realjuice_entry.get())*110
    redbullprice=int(redbull_entry.get())*115
    clubsodaprice=int(clubsoda_entry.get())*20

    totalcosmeticprice=soapprice+coldcreamprice+facewashprice+hairgelprice+hairsprayprice+bodylotionprice
    totalgroceryprice=riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice
    totaldrinksprice=pepsiprice+maazaprice+cocacolaprice+realjuiceprice+redbullprice+clubsodaprice

    cosmetic_price_entry.delete(0,END)
    cosmetic_price_entry.insert(0,str(totalcosmeticprice)+'Rs')
    cosmetic_tax=totalcosmeticprice*0.15
    cosmetic_tax_entry.delete(0,END)
    cosmetic_tax_entry.insert(0,str(cosmetic_tax)+'rs')

    grocery_price_entry.delete(0,END)
    grocery_price_entry.insert(0,str(totalgroceryprice)+'Rs')
    grocery_tax=totalgroceryprice*0.70
    grocery_tax_entry.delete(0,END)
    grocery_tax_entry.insert(0,str(grocery_tax)+'Rs')

    softdrink_price_entry.delete(0,END)
    softdrink_price_entry.insert(0,str(totaldrinksprice)+'Rs')
    softdrink_tax=totaldrinksprice*0.25
    softdrink_tax_entry.delete(0,END)
    softdrink_tax_entry.insert(0,str(softdrink_tax)+'Rs')

    totalbill=totalcosmeticprice+totaldrinksprice+totalgroceryprice+cosmetic_tax+grocery_tax+softdrink_tax


heading_label=Label(win,text="Retail Billing System",fg="gold",bg="gray20",font=('times new roman',26,'bold'),height=1  ,border=12,relief=GROOVE)
heading_label.pack(fill=X)

customer_detail_frame=LabelFrame(win,text="Customer Details",fg='gold',font=('times new roman',15,'bold'),bg='gray20',border=8,relief=GROOVE)
customer_detail_frame.pack(fill=X)

cus_name_label=Label(customer_detail_frame,text="Name",fg="white",bg="gray20",font=('times new roman',15,'bold'))
cus_name_label.grid(row=1,column=0,padx=20)
cus_name_entry=Entry(customer_detail_frame,font=('arial',15),border=7,width=18)
cus_name_entry.grid(row=1,column=1,padx=8)

phn_no_label=Label(customer_detail_frame,text="Phone Number",fg="white",bg="gray20",font=('times new roman',15,'bold'))
phn_no_label.grid(row=1,column=2,padx=20)
phn_no_entry=Entry(customer_detail_frame,font=('arial',15),border=7,width=18)
phn_no_entry.grid(row=1,column=3,padx=8)

bill_no_label=Label(customer_detail_frame,text="Bill Number",fg="white",bg="gray20",font=('times new roman',15,'bold'))
bill_no_label.grid(row=1,column=4,padx=20)
bill_no_entry=Entry(customer_detail_frame,font= ('arial',15),border=7,width=18)
bill_no_entry.grid(row=1,column=5,padx=8)

search_button=Button(customer_detail_frame,text="search",fg="black",font=('times new roman',13,'bold'),width=18,border=4,height=1,command=search_bill)
search_button.grid(row=1,column=6,padx=40)  
 
product_frame=Frame(win)
product_frame.pack(fill=X)

cosmetic_frame=LabelFrame(product_frame,text="Cosmetic",fg='gold',font=('times new roman',15,'bold'),bg='gray20',border=8,relief=GROOVE)
cosmetic_frame.grid(row=0,column=0) 

soap_label=Label(cosmetic_frame,text="Bath Soap",fg="white",bg="gray20",font=('times new roman',15,'bold'))
soap_label.grid(row=0,column=0,padx=10,pady=9,sticky=W)
soap_entry=Entry(cosmetic_frame,font=('arial',15),border=5,width=13)
soap_entry.grid(row=0,column=1,padx=10,pady=9)
soap_entry.insert(0,0)

coldcream_label=Label(cosmetic_frame,text="Cold Cream",fg="white",bg="gray20",font=('times new roman',15,'bold'))
coldcream_label.grid(row=1,column=0,padx=10,pady=9,sticky=W)
coldcream_entry=Entry(cosmetic_frame,font=('arial',15),border=5,width=13)
coldcream_entry.grid(row=1,column=1,padx=10,pady=9)
coldcream_entry.insert(0,0)

facewash_label=Label(cosmetic_frame,text="Face Wash",fg="white",bg="gray20",font=('times new roman',15,'bold'))
facewash_label.grid(row=2,column=0,padx=10,pady=9,sticky=W)
facewash_entry=Entry(cosmetic_frame,font=('arial',15),border=5,width=13)
facewash_entry.grid(row=2,column=1,padx=10,pady=9)
facewash_entry.insert(0,0)

hairspray_label=Label(cosmetic_frame,text="Hair Spray",fg="white",bg="gray20",font=('times new roman',15,'bold'))
hairspray_label.grid(row=3,column=0,padx=10,pady=9,sticky=W)
hairspray_entry=Entry(cosmetic_frame,font=('arial',15),border=5,width=13)
hairspray_entry.grid(row=3,column=1,padx=10,pady=9)
hairspray_entry.insert(0,0)

hairgel_label=Label(cosmetic_frame,text="Hair Gel",fg="white",bg="gray20",font=('times new roman',15,'bold'))
hairgel_label.grid(row=4,column=0,padx=10,pady=9,sticky=W)
hairgel_entry=Entry(cosmetic_frame,font=('arial',15),border=5,width=13)
hairgel_entry.grid(row=4,column=1,padx=10,pady=9)
hairgel_entry.insert(0,0)

bodylotion_label=Label(cosmetic_frame,text="Body Lotion",fg="white",bg="gray20",font=('times new roman',15,'bold'))
bodylotion_label.grid(row=5,column=0,padx=10,pady=9,sticky=W)
bodylotion_entry=Entry(cosmetic_frame,font=('arial',15),border=5,width=13)
bodylotion_entry.grid(row=5,column=1,padx=10,pady=9)
bodylotion_entry.insert(0,0)

grocery_frame=LabelFrame(product_frame,text="Grocery",fg='gold',font=('times new roman',15,'bold'),bg='gray20',border=8,relief=GROOVE)
grocery_frame.grid(row=0,column=1) 

rice_label=Label(grocery_frame,text="Rice",fg="white",bg="gray20",font=('times new roman',15,'bold'))
rice_label.grid(row=0,column=0,padx=10,pady=9,sticky=W)
rice_entry=Entry(grocery_frame,font=('arial',15),border=5,width=13)
rice_entry.grid(row=0,column=1,padx=10,pady=9)
rice_entry.insert(0,0)

oil_label=Label(grocery_frame,text="Oil",fg="white",bg="gray20",font=('times new roman',15,'bold'))
oil_label.grid(row=1,column=0,padx=10,pady=9,sticky=W)
oil_entry=Entry(grocery_frame,font=('arial',15),border=5,width=13)
oil_entry.grid(row=1,column=1,padx=10,pady=9)
oil_entry.insert(0,0)

daal_label=Label(grocery_frame,text="Daal",fg="white",bg="gray20",font=('times new roman',15,'bold'))
daal_label.grid(row=2,column=0,padx=10,pady=9,sticky=W)
daal_entry=Entry(grocery_frame,font=('arial',15),border=5,width=13)
daal_entry.grid(row=2,column=1,padx=10,pady=9)
daal_entry.insert(0,0)

wheat_label=Label(grocery_frame,text="Wheat",fg="white",bg="gray20",font=('times new roman',15,'bold'))
wheat_label.grid(row=3,column=0,padx=10,pady=9,sticky=W)
wheat_entry=Entry(grocery_frame,font=('arial',15),border=5,width=13)
wheat_entry.grid(row=3,column=1,padx=10,pady=9)
wheat_entry.insert(0,0)

sugar_label=Label(grocery_frame,text="Sugar",fg="white",bg="gray20",font=('times new roman',15,'bold'))
sugar_label.grid(row=4,column=0,padx=10,pady=9,sticky=W)
sugar_entry=Entry(grocery_frame,font=('arial',15),border=5,width=13)
sugar_entry.grid(row=4,column=1,padx=10,pady=9)
sugar_entry.insert(0,0)

tea_label=Label(grocery_frame,text="Tea",fg="white",bg="gray20",font=('times new roman',15,'bold'))
tea_label.grid(row=5,column=0,padx=10,pady=9,sticky=W)
tea_entry=Entry(grocery_frame,font=('arial',15),border=5,width=13)
tea_entry.grid(row=5,column=1,padx=10,pady=9)
tea_entry.insert(0,0)

grocery_frame=LabelFrame(product_frame,text="Grocery",fg='gold',font=('times new roman',15,'bold'),bg='gray20',border=8,relief=GROOVE)
grocery_frame.grid(row=0,column=1) 

softdrink_frame=LabelFrame(product_frame,text="Soft Drinks",fg='gold',font=('times new roman',15,'bold'),bg='gray20',border=8,relief=GROOVE)
softdrink_frame.grid(row=0,column=2) 

pepsi_label=Label(softdrink_frame,text="Pepsi",fg="white",bg="gray20",font=('times new roman',15,'bold'))
pepsi_label.grid(row=0,column=0,padx=10,pady=9,sticky=W)
pepsi_entry=Entry(softdrink_frame,font=('arial',15),border=5,width=13)
pepsi_entry.grid(row=0,column=1,padx=10,pady=9)
pepsi_entry.insert(0,0)

maaza_label=Label(softdrink_frame,text="Maaza",fg="white",bg="gray20",font=('times new roman',15,'bold'))
maaza_label.grid(row=1,column=0,padx=10,pady=9,sticky=W)
maaza_entry=Entry(softdrink_frame,font=('arial',15),border=5,width=13)
maaza_entry.grid(row=1,column=1,padx=10,pady=9)
maaza_entry.insert(0,0)

cocacola_label=Label(softdrink_frame,text="Coca-Cola",fg="white",bg="gray20",font=('times new roman',15,'bold'))
cocacola_label.grid(row=2,column=0,padx=10,pady=9,sticky=W)
cocacola_entry=Entry(softdrink_frame,font=('arial',15),border=5,width=13)
cocacola_entry.grid(row=2,column=1,padx=10,pady=9)
cocacola_entry.insert(0,0)

Realjuice_label=Label(softdrink_frame,text="Real Juice",fg="white",bg="gray20",font=('times new roman',15,'bold'))
Realjuice_label.grid(row=3,column=0,padx=10,pady=9,sticky=W)
Realjuice_entry=Entry(softdrink_frame,font=('arial',15),border=5,width=13)
Realjuice_entry.grid(row=3,column=1,padx=10,pady=9)
Realjuice_entry.insert(0,0)

redbull_label=Label(softdrink_frame,text="Red Bull",fg="white",bg="gray20",font=('times new roman',15,'bold'))
redbull_label.grid(row=4,column=0,padx=10,pady=9,sticky=W)
redbull_entry=Entry(softdrink_frame,font=('arial',15),border=5,width=13)
redbull_entry.grid(row=4,column=1,padx=10,pady=9)
redbull_entry.insert(0,0)

clubsoda_label=Label(softdrink_frame,text="Club Soda",fg="white",bg="gray20",font=('times new roman',15,'bold'))
clubsoda_label.grid(row=5,column=0,padx=10,pady=9,sticky=W)
clubsoda_entry=Entry(softdrink_frame,font=('arial',15),border=5,width=13)
clubsoda_entry.grid(row=5,column=1,padx=10,pady=9)
clubsoda_entry.insert(0,0)

bill_frame=Frame(product_frame,border=8,relief=GROOVE)
bill_frame.grid(row=0,column=3,padx=10)

billarea_label=Label(bill_frame,text="Bill Area",fg="gold",bg="gray20",font=('times new roman',15,'bold'),border=8,relief=GROOVE)
billarea_label.pack(fill=X)

scrollbar=Scrollbar(bill_frame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(bill_frame,height=18,width=54,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

bill_menu_frame=LabelFrame(win,text="Bill Menu",fg='gold',font=('times new roman',15,'bold'),bg='gray20',border=8,relief=GROOVE)
bill_menu_frame.pack(fill=X)

cosmetic_price_label=Label(bill_menu_frame,text="Cosmetic Price",fg="white",bg="gray20",font=('times new roman',15,'bold'))
cosmetic_price_label.grid(row=0,column=0,padx=10,pady=9,sticky=W)
cosmetic_price_entry=Entry(bill_menu_frame,font=('arial',15),border=5,width=13)
cosmetic_price_entry.grid(row=0,column=1,padx=10,pady=9)

grocery_price_label=Label(bill_menu_frame,text="grocery Price",fg="white",bg="gray20",font=('times new roman',15,'bold'))
grocery_price_label.grid(row=1,column=0,padx=10,pady=9,sticky=W)
grocery_price_entry=Entry(bill_menu_frame,font=('arial',15),border=5,width=13)
grocery_price_entry.grid(row=1,column=1,padx=10,pady=9)

softdrink_price_label=Label(bill_menu_frame,text="Soft Drink Price",fg="white",bg="gray20",font=('times new roman',15,'bold'))
softdrink_price_label.grid(row=2,column=0,padx=10,pady=9,sticky=W)
softdrink_price_entry=Entry(bill_menu_frame,font=('arial',15),border=5,width=13)
softdrink_price_entry.grid(row=2,column=1,padx=10,pady=9)

cosmetic_tax_label=Label(bill_menu_frame,text="Cosmetic Tax",fg="white",bg="gray20",font=('times new roman',15,'bold'))
cosmetic_tax_label.grid(row=0,column=2,padx=10,pady=9,sticky=W)
cosmetic_tax_entry=Entry(bill_menu_frame,font=('arial',15),border=5,width=13)
cosmetic_tax_entry.grid(row=0,column=3,padx=10,pady=9)

grocery_tax_label=Label(bill_menu_frame,text="grocery Tax",fg="white",bg="gray20",font=('times new roman',15,'bold'))
grocery_tax_label.grid(row=1,column=2,padx=10,pady=9,sticky=W)
grocery_tax_entry=Entry(bill_menu_frame,font=('arial',15),border=5,width=13)
grocery_tax_entry.grid(row=1,column=3,padx=10,pady=9)

softdrink_tax_label=Label(bill_menu_frame,text="Soft Drink tax",fg="white",bg="gray20",font=('times new roman',11,'bold'))
softdrink_tax_label.grid(row=2,column=2,padx=10,pady=9,sticky=W)
softdrink_tax_entry=Entry(bill_menu_frame,font=('arial',15),border=5,width=13)
softdrink_tax_entry.grid(row=2,column=3,padx=10,pady=9)

button_frame=Frame(bill_menu_frame,border=7,relief=GROOVE,)
button_frame.grid(row=0,column=4,rowspan=3)

total_button=Button(button_frame,text="Total",font=('arial',16,'bold'),fg='gold',bg='gray20',width=8,border=5,command=total)
total_button.grid(row=0,column=0,padx=5,pady=20)

bill_button=Button(button_frame,text="Bill",font=('arial',16,'bold'),fg='gold',bg='gray20',width=8,border=5,command=bill_area)
bill_button.grid(row=0,column=1,padx=5,pady=20)

email_button=Button(button_frame,text="E-mail",font=('arial',16,'bold'),fg='gold',bg='gray20',width=8,border=5,command=send_email)
email_button.grid(row=0,column=2,padx=5,pady=20)

print_button=Button(button_frame,text="Print",font=('arial',16,'bold'),fg='gold',bg='gray20',width=8,border=5,command=print_bill)
print_button.grid(row=0,column=6,padx=5,pady=20)

clear_button=Button(button_frame,text="Clear",font=('arial',16,'bold'),fg='gold',bg='gray20',width=8,border=5,command=win.destroy)
clear_button.grid(row=0,column=7,padx=5,pady=20)

win.mainloop()