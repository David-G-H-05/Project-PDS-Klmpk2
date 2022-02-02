from faulthandler import disable
from tkinter import *
from tkinter import font
from tkinter.ttk import Labelframe
from tokenize import String
from turtle import left, right

a = Tk()
window_name = a.title('Cashier Management System') #Pemberian Title/Judul pada Project

window_size = a.geometry('1406x770+0+0') #Set ukuran window  (diubah) (

size_tetap = a.resizable(0,0)

window_color= a.config(bg='firebrick4') #Set warna windows (diubah)


#  Text in Window = 'CASHIER MANAGEMENT SYSTEM'

topframe = Frame(a, bd=11, relief=RIDGE, bg='red') # untuk background bisa (diubah)
topframe.pack(side=TOP)

project_name = Label(topframe, text='CASHIER MANAGEMENT SYSTEM', font=('Times New Roman', 32, 'bold'), bg='blue', fg='white', width=53) # (diubah)
project_name.grid(row=0, column=0)

# Frame

menuframe = Frame(a, bd=10, relief=RIDGE, bg='firebrick4') #bisa menambahkan warna background  (bg)
menuframe.pack(side=LEFT)

hargaframe = Frame(menuframe, bd=4, relief=RIDGE)
hargaframe.pack(side=BOTTOM)

makanan_frame = LabelFrame(menuframe, text='MAKANAN', font=('Times New Roman', 19, 'bold'), bd=10, relief=RIDGE)
makanan_frame.pack(side=LEFT)

minuman_frame = LabelFrame(menuframe, text='MINUMAN', font=('Times New Roman', 19, 'bold'), bd=10, relief=RIDGE)
minuman_frame.pack(side=LEFT)

# ------------
rightframe = Frame(a, bd=15, relief=RIDGE)
rightframe.pack(side=RIGHT)

# Calculator

calculatorframe = Frame(rightframe, bd=1, relief=RIDGE)
calculatorframe.pack()

recieptframe = Frame(rightframe, bd=4, relief=RIDGE)
recieptframe.pack()

tombolframe = Frame(rightframe, bd=3, relief=RIDGE)
tombolframe.pack()

#VARIABEL yang menghubungkan dengan daftar makanan

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()

# Makanan

root_nasgor = StringVar()
root_martabak = StringVar()
root_sate = StringVar()
root_kebab = StringVar()
root_roba = StringVar()
root_naskun = StringVar()
root_nasbak = StringVar()
root_nashim = StringVar()
root_nasput = StringVar()

# Minuman

root_fanta = StringVar()
root_cocacola = StringVar()
root_sprite = StringVar()
root_fanta = StringVar()
root_jusmangga = StringVar()
root_jusjeruk = StringVar()
root_jusalpukat = StringVar()
root_jusapel = StringVar()
root_jusdurian = StringVar()
root_juspisang = StringVar()


#---------------------------------------------

# Daftar MAKANAN

nasgor = Checkbutton(makanan_frame, text='Nasi Goreng', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var1) # untuk var disesuaikan dengan Variabelnya
nasgor.grid(row=0, column=0, sticky=W) #sticky digunakan untuk meluruskan daftar makanan/minuman

martabak = Checkbutton(makanan_frame, text='Martabak', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var2)
martabak.grid(row=1, column=0, sticky=W)

sate = Checkbutton(makanan_frame, text='Sate', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var3)
sate.grid(row=2, column=0, sticky=W)

kebab = Checkbutton(makanan_frame, text='Kebab', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var4)
kebab.grid(row=3, column=0, sticky=W)

roba = Checkbutton(makanan_frame, text='Roti Bakar', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var5)
roba.grid(row=4, column=0, sticky=W)

naskun = Checkbutton(makanan_frame, text='Nasi Kuning', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var6)
naskun.grid(row=5, column=0, sticky=W)

nasbak = Checkbutton(makanan_frame, text='Nasi Bakar', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var7) 
nasbak.grid(row=6, column=0, sticky=W)

nashim = Checkbutton(makanan_frame, text='Nasi Hitam', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var8)
nashim.grid(row=7, column=0, sticky=W)

nasput = Checkbutton(makanan_frame, text='Nasi Putih', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var9)
nasput.grid(row=8, column=0, sticky=W)

# ---------------- input jumlah makanan

kotaknasgor = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_nasgor)
kotaknasgor.grid(row=0, column=1)

kotakmartabak = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_martabak)
kotakmartabak.grid(row=1, column=1)

kotaksate = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_sate)
kotaksate.grid(row=2, column=1)

kotakkebab = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_kebab)
kotakkebab.grid(row=3, column=1)

kotakroba = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_roba)
kotakroba.grid(row=4, column=1)

kotaknaskun = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_naskun)
kotaknaskun.grid(row=5, column=1)

kotaknasbak = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_nasbak)
kotaknasbak.grid(row=6, column=1)

kotaknashim = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_nashim)
kotaknashim.grid(row=7, column=1)

kotaknasput = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_nasput)
kotaknasput.grid(row=8, column=1)

#----------------------------------------------------------

# Daftar MINUMAN

fanta = Checkbutton(minuman_frame, text='Fanta', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var10)
fanta.grid(row=0, column=0, sticky=W)

cocacola = Checkbutton(minuman_frame, text='Cocacola', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var11)
cocacola.grid(row=1, column=0, sticky=W)

sprite = Checkbutton(minuman_frame, text='Sprite', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var12)
sprite.grid(row=2, column=0, sticky=W)

jusmangga = Checkbutton(minuman_frame, text='Jus Mangga', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var13)
jusmangga.grid(row=3, column=0, sticky=W)

jusjeruk = Checkbutton(minuman_frame, text='Jus Jeruk', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var14)
jusjeruk.grid(row=4, column=0, sticky=W)

jusalpukat = Checkbutton(minuman_frame, text='Jus Alpukat', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var15)
jusalpukat.grid(row=5, column=0, sticky=W)

jusapel = Checkbutton(minuman_frame, text='Jus Apel', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var16)
jusapel.grid(row=6, column=0, sticky=W)

jusdurian = Checkbutton(minuman_frame, text='Jus Durian', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var17)
jusdurian.grid(row=7, column=0, sticky=W)

juspisang = Checkbutton(minuman_frame, text='Jus Pisang', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var18)
juspisang.grid(row=8, column=0, sticky=W)


# ---------------- input jumlah minuman

fanta = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_fanta)
fanta.grid(row=0, column=1)

cocacola = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_cocacola)
cocacola.grid(row=1, column=1)

sprite = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_sprite)
sprite.grid(row=2, column=1)

jusmangga = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_jusmangga)
jusmangga.grid(row=3, column=1)

jusjeruk = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_jusjeruk)
jusjeruk.grid(row=4, column=1)

jusalpukat = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_jusalpukat)
jusalpukat.grid(row=5, column=1)

jusapel = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_jusapel)
jusapel.grid(row=6, column=1)

jusdurian = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_jusdurian)
jusdurian.grid(row=7, column=1)

juspisang = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_juspisang)
juspisang.grid(row=8, column=1)






mainloop()
