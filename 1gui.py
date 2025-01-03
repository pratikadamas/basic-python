from tkinter import*
# Tk() class and root object
root = Tk()
root.title("MY 1st GUI")
root.geometry("500x500+0+0")
# root.wm_iconbitmap("logo.jpeg")
# lable1=Label(root,text="Hello World",font=('times new roman',30,'bold'),fg="red",bg="black")
# #
# # #pack()
# lable1.pack(side=BOTTOM)
# # lable1=pack(side=LEFT/BOTTOM/RIGHT)

#grid()
lable2=Label(root,text="Have a nice day!",font=('Sixtyfour',30,'bold'),fg="red",bg="black")
lable2.grid(row=0,column=0)

lable2=Label(root,text="Have a nice day!!!",font=('Sixtyfour',30,'bold'),fg="red",bg="green")
lable2.grid(row=5,column=1)








root.mainloop()