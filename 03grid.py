from tkinter import*

win= Tk()
win.title("Code With Pratik!")
win.iconbitmap("logo.ico")
width=500
height=500

sys_width = win.winfo_screenwidth()
sys_height = win.winfo_screenheight()
c_x = int(sys_width/2-width/2)
c_y = int(sys_height/2-height/2)
win.minsize(400,400)
win.maxsize(1600,1600)

data = input("Enter Your Name:",)
var = StringVar()
var.set(data)
label = Label(win,textvariable=var,font=("Arial",20),fg="blue",bg="pink",borderwidth=2,relief=SUNKEN)
label.place(x=0,y=40,width=200,height=40)
#insert a IMAGE


photo = PhotoImage(file="pratik.png")

lable3 = Label(win, image=photo)
lable3.place(x=150,y=150,width=600,height=800)

label1 = Label(win,text="Happy New Year!",font=("Time new Roman",20,"bold"),background="red")

label1.grid(row=0,column=0)
label2 = Label(win,text="Soumyajit",font=("Time new Roman",20,"bold"),background="yellow")
label2.grid(row=0,column=1)
win.geometry("500x500+50+50")
win.attributes("-alpha",1)
win.config(background="white")

win.mainloop()
