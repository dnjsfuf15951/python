#count
from tkinter import *

tk = Tk()
counter = 0

def clicked():
    global counter
    counter -= 1
    Label1['text'] = '버튼 클릭 수:' + str(counter)

def clicked():
    global counter
    counter += 1
    Label1['text'] = '버튼 클릭 수:' + str(counter)

def reset():
    global counter
    counter = 0
    Label1['text'] = '옆에 버튼 있음'
        
tk.title('GUI 카운터')
Label1 = Label(tk, text='옆에 버튼 있음', fg='blue',font=20)
Label1.pack(side=LEFT, padx=10, pady=10)

#button1
Button1 = Button(tk,text='클릭하세요', bg='green', font='15', width='30',height='5',command=clicked)
Button1.pack(side=LEFT,padx=10,pady=10)

Button2 = Button(tk,text='리셋', bg='red', font='15', width='30',height='5',command=reset)
Button2.pack(side=LEFT,padx=10,pady=10)

Button3 = Button(tk,text='감소', bg='green', font='15', width='30',height='5',command=clicked)
Button3.pack(side=LEFT,padx=10,pady=10)
tk.mainloop()