from tkinter import*
def love():
      label1.config(text="I LOVE U!!!", fg="red", bg="white", font=("Arial",10,'bold'),width=15,height=5)


win=Tk()
win.title("Botton GUI")
bu1=Button(win,text="YES",width=10,height=5,background="black",fg="white",command=love)
bu2=Button(win,text="NO",width=10,height=5,background="red",fg="white")
bu1.place(x =10,y =15)
bu2.place(x =100,y = 15)

label1=Label(win,text="WELCOME!",font=("Arial",12,"bold"),width=15,height=6)
label1.place(x=200,y = 15)
win.mainloop()



