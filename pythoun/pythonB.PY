from tkinter import *
window = Tk ()
#
photo = PhotoImage(file = "D:\\qqq.png")
photo2 = PhotoImage(file = "D:\\qqqq.png")
label1 = Label(window, image = photo)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT)
label2.pack(side=R)
window.mainloop()