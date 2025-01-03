from tkinter import*

win= Tk()


photo = PhotoImage(file="pratik.png")

lable3 = Label(win, image=photo)
lable3.pack(side=TOP,padx=250,pady=250,expand=True)

win.mainloop()