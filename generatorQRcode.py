# pip3 install pillow qrcode

import qrcode

from tkinter import *
from tkinter import messagebox


def generator():
    data = str(input('Вставьте ссылку на сайт... \n'))
    filename = "site.png"
    img = qrcode.make(data)
    img.save(f'MiddleLevel/{filename}')


    def on_closing():
        if messagebox.askokcancel('Закрыть QRcode', 'Вы уверены?'):
            tk.destroy()

    tk = Tk()
    tk.protocol('WM_DELETE_WINDOW', on_closing)
    tk.title('QRcode')
    tk.resizable(0,0)
    tk.wm_attributes('-topmost', 1)
    canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
    canvas.pack()

    my_image = PhotoImage(file='MiddleLevel/site.png')
    my_label = Label(tk)
    my_label.image = my_image
    my_label['image'] = my_label.image
    my_label.place(x=0,y=0)

    tk.mainloop()

generator()