
from tkinter import *


def clear():
    e_user.delete(0,'end')
    e_mail.delete(0,'end')
    e_city.delete(0,'end')

root=Tk()

root.geometry("500x500")
root.title("registration  form")

username =Label(root , text="UserName ",font=("bold",15)).place(x=80 ,y=30)

mail =Label(root , text="Email ",font=("bold",15)).place(x=80 ,y=70)

city =Label(root , text="City",font=("bold",15)).place(x=80 ,y=110)

gender=Label(root , text="Gender",font=("bold",15)).place(x=80,y=150)


e_user=Entry(width=150,borderwidth="5")
e_user.place(x=200,y=35)

e_mail=Entry(width=150,borderwidth="5")
e_mail.place(x=200,y=75)

e_city=Entry(width=150,borderwidth="5")
e_city.place(x=200,y=115)


  
Checkbutton1 = IntVar()   
Checkbutton2 = IntVar()   
  
Button1 = Checkbutton(root, text = "male",  
                      variable = Checkbutton1, 
                      onvalue = 1, 
                      offvalue = 0, 
                      height = 2, 
                      width = 10) 
Button1.place(x=180,y=150)

Button2 = Checkbutton(root, text = "Female",  
                      variable = Checkbutton2, 
                      onvalue = 1, 
                      offvalue = 0, 
                      height = 2, 
                      width = 10) 
Button2.place(x=300,y=150)



login=Button(root , text="login" ,bd="5",width="15",command=clear)
login.place(x=190,y=200)




root.mainloop()