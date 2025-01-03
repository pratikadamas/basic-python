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
win.maxsize(1200,1200)

label1 = Label(win,text="Good Morning!",font=("Time new Roman",20,"bold"),background="red")

label1.grid(row=0,column=0)
label2 = Label(win,text="Happy New Year!",font=("Time new Roman",30,"bold"),background="yellow")
label2.grid(row=1,column=0)
win.geometry("500x500+50+50")
win.attributes("-alpha",0.7)
win.config(background="green")

win.mainloop()
