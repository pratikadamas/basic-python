from tkinter import*

win = Tk()
win.title(" lable Frame ")
lable_frame = LabelFrame(win, text="CODE WITH PRATIK!",font=(20) ,padx=15, pady=10, relief=SUNKEN,width=600, height=300, background="white", borderwidth=20,labelanchor=N,)
lable_frame.place(x = 100,y = 100)

lable1 = Label(lable_frame, text="JavaScript",font=(20) ,padx=25, pady=1, relief=SUNKEN,borderwidth=2)
lable1.place(x =5 ,y = 150)


lable2 = Label(lable_frame, text="Java",font=(20) ,padx=25, pady=1, relief=SUNKEN,borderwidth=2)
lable2.place(x =170 ,y = 150)





win.mainloop()