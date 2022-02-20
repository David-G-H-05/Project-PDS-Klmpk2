from cgitb import text
from distutils import command
from faulthandler import disable
from sys import dllhandle
from tkinter import *
from tkinter import font
from tkinter.ttk import Labelframe
from tokenize import String
from turtle import left, right


# Function untuk Menu Makanan

def nasgor():
    if var1.get() == 1:
        input_nasgor.config(state=NORMAL)
        input_nasgor.delete(0, END) # yang berguna saat di ceklis tanda min akan hilang 
        input_nasgor.focus() 
    else:
        input_nasgor.config(state=DISABLED)
        root_nasgor.set('-') # jika saat ceklis dihilangkan makan akan kembali seperti semula

def martabak():
    if var2.get() == 1:
        input_martabak.config(state=NORMAL)
        input_martabak.delete(0, END)
        input_martabak.focus()
    else:
        input_martabak.config(state=DISABLED)
        root_martabak.set('-')

def sate():
    if var3.get() == 1:
        input_sate.config(state=NORMAL)
        input_sate.delete(0, END)
        input_sate.focus()
    else:
        input_sate.config(state=DISABLED)
        root_sate.set('-')

def kebab():
    if var4.get() == 1:
        input_kebab.config(state=NORMAL)
        input_kebab.delete(0, END)
        input_kebab.focus()
    else:
        input_kebab.config(state=DISABLED)
        root_kebab.set('-')

def roba():
    if var5.get() == 1:
        input_roba.config(state=NORMAL)
        input_roba.delete(0, END)
        input_roba.focus()
    else:
        input_roba.config(state=DISABLED)
        root_roba.set('-')

def naskun():
    if var6.get() == 1:
        input_naskun.config(state=NORMAL)
        input_naskun.delete(0, END)
        input_naskun.focus()
    else:
        input_naskun.config(state=DISABLED)
        root_naskun.set('-')

def nasbak():
    if var7.get() == 1:
        input_nasbak.config(state=NORMAL)
        input_nasbak.delete(0, END)
        input_nasbak.focus()
    else:
        input_nasbak.config(state=DISABLED)
        root_nasbak.set('-')

def nashim():
    if var8.get() == 1:
        input_nashim.config(state=NORMAL)
        input_nashim.delete(0, END)
        input_nashim.focus()
    else:
        input_nashim.config(state=DISABLED)
        root_nashim.set('-')

def nasput():
    if var9.get() == 1:
        input_nasput.config(state=NORMAL)
        input_nasput.delete(0, END)
        input_nasput.focus()
    else:
        input_nasput.config(state=DISABLED)
        root_nasput.set('-')


# Function untuk Menu Minuman

def fanta():
    if var10.get() == 1:
        input_fanta.config(state=NORMAL)
        input_fanta.delete(0, END)
        input_fanta.focus()
    else:
        input_fanta.config(state=DISABLED)
        root_fanta.set('-')

def cocacola():
    if var11.get() == 1:
        input_cocacola.config(state=NORMAL)
        input_cocacola.delete(0, END)
        input_cocacola.focus()
    else:
        input_cocacola.config(state=DISABLED)
        root_cocacola.set('-')

def sprite():
    if var12.get() == 1:
        input_sprite.config(state=NORMAL)
        input_sprite.delete(0, END)
        input_sprite.focus()
    else:
        input_sprite.config(state=DISABLED)
        root_sprite.set('-')

def jusmangga():
    if var13.get() == 1:
        input_jusmangga.config(state=NORMAL)
        input_jusmangga.delete(0, END)
        input_jusmangga.focus()
    else:
        input_jusmangga.config(state=DISABLED)
        root_jusmangga.set('-')

def jusjeruk():
    if var14.get() == 1:
        input_jusjeruk.config(state=NORMAL)
        input_jusjeruk.delete(0, END)
        input_jusjeruk.focus()
    else:
        input_jusjeruk.config(state=DISABLED)
        root_jusjeruk.set('-')

def jusalpukat():
    if var15.get() == 1:
        input_jusalpukat.config(state=NORMAL)
        input_jusalpukat.delete(0, END)
        input_jusalpukat.focus()
    else:
        input_jusalpukat.config(state=DISABLED)
        root_jusalpukat.set('-')

def jusapel():
    if var16.get() == 1:
        input_jusapel.config(state=NORMAL)
        input_jusapel.delete(0, END)
        input_jusapel.focus()
    else:
        input_jusapel.config(state=DISABLED)
        root_jusapel.set('-')

def jusdurian():
    if var17.get() == 1:
        input_jusdurian.config(state=NORMAL)
        input_jusdurian.delete(0, END)
        input_jusdurian.focus()
    else:
        input_jusdurian.config(state=DISABLED)
        root_jusdurian.set('-')

def juspisang():
    if var18.get() == 1:
        input_juspisang.config(state=NORMAL)
        input_juspisang.delete(0, END)
        input_juspisang.focus()
    else:
        input_juspisang.config(state=DISABLED)
        root_juspisang.set('-')


# Function untuk Menu Kue

def bolu():
    if var19.get() == 1:
        input_bolu.config(state=NORMAL)
        input_bolu.delete(0, END)
        input_bolu.focus()
    else:
        input_bolu.config(state=DISABLED)
        root_bolu.set('-')

def brownis():
    if var20.get() == 1:
        input_brownis.config(state=NORMAL)
        input_brownis.delete(0, END)
        input_brownis.focus()
    else:
        input_brownis.config(state=DISABLED)
        root_brownis.set('-')

def lapiskukus():
    if var21.get() == 1:
        input_lapiskukus.config(state=NORMAL)
        input_lapiskukus.delete(0, END)
        input_lapiskukus.focus()
    else:
        input_lapiskukus.config(state=DISABLED)
        root_lapiskukus.set('-')

def marble():
    if var22.get() == 1:
        input_marble.config(state=NORMAL)
        input_marble.delete(0, END)
        input_marble.focus()
    else:
        input_marble.config(state=DISABLED)
        root_marble.set('-')

def sponge():
    if var23.get() == 1:
        input_sponge.config(state=NORMAL)
        input_sponge.delete(0, END)
        input_sponge.focus()
    else:
        input_sponge.config(state=DISABLED)
        root_sponge.set('-')

def butter():
    if var24.get() == 1:
        input_butter.config(state=NORMAL)
        input_butter.delete(0, END)
        input_butter.focus()
    else:
        input_butter.config(state=DISABLED)
        root_butter.set('-')

def cotton():
    if var25.get() == 1:
        input_cotton.config(state=NORMAL)
        input_cotton.delete(0, END)
        input_cotton.focus()
    else:
        input_cotton.config(state=DISABLED)
        root_cotton.set('-')

def cheese():
    if var26.get() == 1:
        input_cheese.config(state=NORMAL)
        input_cheese.delete(0, END)
        input_cheese.focus()
    else:
        input_cheese.config(state=DISABLED)
        root_cheese.set('-')

def mocha():
    if var27.get() == 1:
        input_mocha.config(state=NORMAL)
        input_mocha.delete(0, END)
        input_mocha.focus()
    else:
        input_mocha.config(state=DISABLED)
        root_mocha.set('-')










a = Tk()
window_name = a.title('Cashier Management System') #Pemberian Title/Judul pada Project

window_size = a.geometry('1270x690+155+55') #Set ukuran window  (diubah) (

size_tetap = a.resizable(0,0)

window_color= a.config(bg='red') #Set warna windows (diubah)


#  Text in Window = 'CASHIER MANAGEMENT SYSTEM'

topframe = Frame(a, bd=11, relief=RIDGE, bg='red') # untuk background bisa (diubah)
topframe.pack(side=TOP)

project_name = Label(topframe, text='CASHIER MANAGEMENT SYSTEM', font=('Times New Roman', 30, 'bold'), bg='blue', fg='white', width=51) # (diubah)
project_name.grid(row=0, column=0)

# Frame


menuframe = Frame(a, bd=16, relief=RIDGE, bg='firebrick4') #bisa menambahkan warna background  (bg)
menuframe.pack(side=LEFT)

hargaframe = Frame(menuframe, bd=4, relief=RIDGE, bg='firebrick4', pady=10) #bisa menambahkan warna background  (bg)
hargaframe.pack(side=BOTTOM)

makanan_frame = LabelFrame(menuframe, text='MAKANAN', font=('Times New Roman', 19, 'bold'), bd=10, relief=RIDGE, fg='black')
makanan_frame.pack(side=LEFT)

minuman_frame = LabelFrame(menuframe, text='MINUMAN', font=('Times New Roman', 19, 'bold'), bd=10, relief=RIDGE, fg='black')
minuman_frame.pack(side=LEFT)

cake_frame = LabelFrame(menuframe, text='KUE', font=('Times New Roman', 19, 'bold' ), bd=10, relief=RIDGE, fg='black')
cake_frame.pack(side=LEFT)


# ------------
rightframe = Frame(a, bd=15, relief=RIDGE, bg='red4')
rightframe.pack(side=RIGHT)

# Fitur bagian kanan

calculatorframe = Frame(rightframe, bd=1, relief=RIDGE, bg='red4')
calculatorframe.pack()

strukframe = Frame(rightframe, bd=4, relief=RIDGE, bg='red4')
strukframe.pack()

tombolframe = Frame(rightframe, bd=3, relief=RIDGE, bg='red4')
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
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

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
root_jusmangga = StringVar()
root_jusjeruk = StringVar()
root_jusalpukat = StringVar()
root_jusapel = StringVar()
root_jusdurian = StringVar()
root_juspisang = StringVar()

# Kue

root_bolu = StringVar()
root_brownis = StringVar()
root_lapiskukus = StringVar()
root_marble = StringVar()
root_sponge = StringVar()
root_butter = StringVar()
root_cotton = StringVar()
root_cheese = StringVar()
root_mocha = StringVar()


# Pengisian Jumlah pada Kolom daftar makanan,minuman & cake

# Makanan
root_nasgor.set('-')
root_martabak.set('-')
root_sate.set('-')
root_kebab.set('-')
root_roba.set('-')
root_naskun.set('-')
root_nasbak.set('-')
root_nashim.set('-')
root_nasput.set('-')


# Minuman

root_fanta.set('-')
root_cocacola.set('-')
root_sprite.set('-')
root_jusmangga.set('-')
root_jusjeruk.set('-')
root_jusalpukat.set('-')
root_jusapel.set('-')
root_jusdurian.set('-')
root_juspisang.set('-')


# Kue

root_bolu.set('-')
root_brownis.set('-')
root_lapiskukus.set('-')
root_marble.set('-')
root_sponge.set('-')
root_butter.set('-')
root_cotton.set('-')
root_cheese.set('-')
root_mocha.set('-')

# Harga Frame

makanan_var = StringVar()
minuman_var = StringVar()
cake_var = StringVar()
subtotal = StringVar()
pajak = StringVar()
total = StringVar()

#---------------------------------------------

# Daftar MAKANAN
# sticky digunakan untuk meluruskan daftar makanan/minuman


nasgor = Checkbutton(makanan_frame, text='Nasi Goreng', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var1, command=nasgor) # untuk var disesuaikan dengan Variabelnya
nasgor.grid(row=0, column=0, sticky=W) 

martabak = Checkbutton(makanan_frame, text='Martabak', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var2, command=martabak)
martabak.grid(row=1, column=0, sticky=W)

sate = Checkbutton(makanan_frame, text='Sate', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var3, command=sate)
sate.grid(row=2, column=0, sticky=W)

kebab = Checkbutton(makanan_frame, text='Kebab', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var4, command=kebab)
kebab.grid(row=3, column=0, sticky=W)

roba = Checkbutton(makanan_frame, text='Roti Bakar', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var5, command=roba)
roba.grid(row=4, column=0, sticky=W)

naskun = Checkbutton(makanan_frame, text='Nasi Kuning', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var6, command=naskun)
naskun.grid(row=5, column=0, sticky=W)

nasbak = Checkbutton(makanan_frame, text='Nasi Bakar', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var7, command=nasbak) 
nasbak.grid(row=6, column=0, sticky=W)

nashim = Checkbutton(makanan_frame, text='Nasi Hitam', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var8, command=nashim)
nashim.grid(row=7, column=0, sticky=W)

nasput = Checkbutton(makanan_frame, text='Nasi Putih', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var9, command=nasput)
nasput.grid(row=8, column=0, sticky=W)

# ---------------- input jumlah makanan

input_nasgor = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_nasgor)
input_nasgor.grid(row=0, column=1)

input_martabak = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_martabak)
input_martabak.grid(row=1, column=1)

input_sate = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_sate)
input_sate.grid(row=2, column=1)

input_kebab = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_kebab)
input_kebab.grid(row=3, column=1)

input_roba = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_roba)
input_roba.grid(row=4, column=1)

input_naskun = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_naskun)
input_naskun.grid(row=5, column=1)

input_nasbak = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_nasbak)
input_nasbak.grid(row=6, column=1)

input_nashim = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_nashim)
input_nashim.grid(row=7, column=1)

input_nasput = Entry(makanan_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_nasput)
input_nasput.grid(row=8, column=1)

#----------------------------------------------------------

# Daftar MINUMAN

fanta = Checkbutton(minuman_frame, text='Fanta', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var10, command=fanta)
fanta.grid(row=0, column=0, sticky=W)

cocacola = Checkbutton(minuman_frame, text='Cocacola', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var11, command=cocacola)
cocacola.grid(row=1, column=0, sticky=W)

sprite = Checkbutton(minuman_frame, text='Sprite', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var12, command=sprite)
sprite.grid(row=2, column=0, sticky=W)

jusmangga = Checkbutton(minuman_frame, text='Jus Mangga', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var13, command=jusmangga)
jusmangga.grid(row=3, column=0, sticky=W)

jusjeruk = Checkbutton(minuman_frame, text='Jus Jeruk', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var14, command=jusjeruk)
jusjeruk.grid(row=4, column=0, sticky=W)

jusalpukat = Checkbutton(minuman_frame, text='Jus Alpukat', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var15, command=jusalpukat)
jusalpukat.grid(row=5, column=0, sticky=W)

jusapel = Checkbutton(minuman_frame, text='Jus Apel', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var16, command=jusapel)
jusapel.grid(row=6, column=0, sticky=W)

jusdurian = Checkbutton(minuman_frame, text='Jus Durian', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var17, command=jusdurian)
jusdurian.grid(row=7, column=0, sticky=W)

juspisang = Checkbutton(minuman_frame, text='Jus Pisang', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var18, command=juspisang)
juspisang.grid(row=8, column=0, sticky=W)


# ---------------- input jumlah minuman

input_fanta = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_fanta)
input_fanta.grid(row=0, column=1)

input_cocacola = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_cocacola)
input_cocacola.grid(row=1, column=1)

input_sprite = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_sprite)
input_sprite.grid(row=2, column=1)

input_jusmangga = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_jusmangga)
input_jusmangga.grid(row=3, column=1)

input_jusjeruk = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_jusjeruk)
input_jusjeruk.grid(row=4, column=1)

input_jusalpukat = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_jusalpukat)
input_jusalpukat.grid(row=5, column=1)

input_jusapel = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_jusapel)
input_jusapel.grid(row=6, column=1)

input_jusdurian = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_jusdurian)
input_jusdurian.grid(row=7, column=1)

input_juspisang = Entry(minuman_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_juspisang)
input_juspisang.grid(row=8, column=1)


# Daftar CAKE

bolu = Checkbutton(cake_frame, text='Bolu Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var19, command=bolu)
bolu.grid(row=0, column=0, sticky=W)

brownis = Checkbutton(cake_frame, text='Bolu Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var20, command=brownis)
brownis.grid(row=1, column=0, sticky=W)

lapiskukus = Checkbutton(cake_frame, text='Lapis Kukus', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var21, command=lapiskukus)
lapiskukus.grid(row=2, column=0, sticky=W)

marble = Checkbutton(cake_frame, text='Marble Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var22, command=marble)
marble.grid(row=3, column=0, sticky=W)

sponge = Checkbutton(cake_frame, text='Sponge Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var23, command=sponge)
sponge.grid(row=4, column=0, sticky=W)

butter = Checkbutton(cake_frame, text='Butter Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var24, command=butter)
butter.grid(row=5, column=0, sticky=W)

cotton = Checkbutton(cake_frame, text='Cotton Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var25, command=cotton)
cotton.grid(row=6, column=0, sticky=W)

cheese = Checkbutton(cake_frame, text='Cheese Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var26, command=cheese)
cheese.grid(row=7, column=0, sticky=W)

mocha = Checkbutton(cake_frame, text='Mocha Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var27, command=mocha)
mocha.grid(row=8, column=0, sticky=W)


# ---------------- input jumlah cake

input_bolu = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_bolu)
input_bolu.grid(row=0, column=1)

input_brownis = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_brownis)
input_brownis.grid(row=1, column=1)

input_lapiskukus = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_lapiskukus)
input_lapiskukus.grid(row=2, column=1)

input_marble = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_marble)
input_marble.grid(row=3, column=1)

input_sponge = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_sponge)
input_sponge.grid(row=4, column=1)

input_butter = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_butter)
input_butter.grid(row=5, column=1)

input_cotton = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_cotton)
input_cotton.grid(row=6, column=1)

input_cheese = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_cheese)
input_cheese.grid(row=7, column=1)

input_mocha = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_mocha)
input_mocha.grid(row=8, column=1)


# Membuat Label Total harga makanan, minuman & cake

# Makanan
labelmakanan = Label(hargaframe, text='Total Harga Makanan', font=('Times New Roman', 16, 'bold'), bg='firebrick4', fg='white')
labelmakanan.grid(row=0,column=0)

textlabelmakanan = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'), bd=6, width=14, fg='white', state='readonly', textvariable='makanan_var') 
textlabelmakanan.grid(row=0, column=1, padx=35)

# Minuman
labelminuman = Label(hargaframe, text='Total Harga Minuman', font=('Times New Roman', 16, 'bold'), bg='firebrick4', fg='white')
labelminuman.grid(row=1,column=0)

textlabelminuman = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'), bd=6, width=14, state='readonly', textvariable='minuman_var') 
textlabelminuman.grid(row=1, column=1, padx=35)

# Cake
labelcake = Label(hargaframe, text='Total Harga Cake', font=('Times New Roman', 16, 'bold'), bg='firebrick4', fg='white')
labelcake.grid(row=2,column=0, sticky=W)

textlabelcake = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'), bd=6, width=14, fg='white', state='readonly', textvariable='cake_var') 
textlabelcake.grid(row=2, column=1, padx=35)

# Sub total
# Sub total itu gabungan harga makanan, minuman & cake
labelsubtotal = Label(hargaframe, text='Sub Total', font=('Times New Roman', 16, 'bold'), bg='firebrick4', fg='white')
labelsubtotal.grid(row=0, column=2)

textsubtotal = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'), bd=6, width=14, state='readonly', textvariable='subtotal_var') 
textsubtotal.grid(row=0, column=3, padx=35)

# Pajak
labelpajak = Label(hargaframe, text='Pajak', font=('Times New Roman', 16, 'bold'), bg='firebrick4', fg='white')
labelpajak.grid(row=1, column=2, sticky=W)

textpajak = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'), bd=6, width=14, state='readonly', textvariable='pajak_var') 
textpajak.grid(row=1, column=3, padx=35)

# Total
# Total berbeda dengan subtotal karena subtotal tidak termasuk pajak
labeltotal = Label(hargaframe, text='Total', font=('Times New Roman', 16, 'bold'), bg='firebrick4', fg='white')
labeltotal.grid(row=2, column=2, sticky=W)

texttotal = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'), bd=6, width=14, fg='white', state='readonly', textvariable='total_var') 
texttotal.grid(row=2, column=3, padx=35)

# Keterangan: 
# Grid = adalah sebuah penempatan suatu widget kedalam tabel, contohnya seperti row(baris), column(kolom), dll
# untuk pengaturan grid kita bisa mampu mengubahnya dan mengatur sesuai dengan keinginan kita.  


#---------------------------------------------------------------------------------------------

# Membuat Tombol untuk menghitung total harga
#Keterangan = menggunakan variabel tombolframe untuk membuat sebuah tombol

tombol_total = Button(tombolframe, text='Total', font=('Times New Roman', 14, 'bold'), bg='firebrick4', fg='white', bd=3, padx=6)
tombol_total.grid(row=0, column=0)

tombol_struk = Button(tombolframe, text='Struk', font=('Times New Roman', 14, 'bold'), bg='firebrick4', fg='white', bd=3, padx=6)
tombol_struk.grid(row=0, column=1)

tombol_simpan = Button(tombolframe, text='Simpan', font=('Times New Roman', 14, 'bold'), bg='firebrick4', fg='white', bd=3, padx=6)
tombol_simpan.grid(row=0, column=2)

tombol_kirim = Button(tombolframe, text='Kirim', font=('Times New Roman', 14, 'bold'), bg='firebrick4', fg='white', bd=3, padx=6)
tombol_kirim.grid(row=0, column=3)

tombol_reset = Button(tombolframe, text='Reset', font=('Times New Roman', 14, 'bold'), bg='firebrick4', fg='white', bd=3, padx=6)
tombol_reset.grid(row=0, column=4)


# Membuat Tempat untuk hasil Struk 

text_struk = Text(strukframe,  font=('Times New Roman', 14, 'bold'), bg='white', fg='black',width=42, height=14)
text_struk.grid(row=0, column=0)


#---------------------------------------------------------------------------------------------


# Calculator
#Function
operator = ''
def tombolclick(angka): #Function untuk mengambil nilai dari tombol
    global operator 
    operator = operator + angka
    kalkulatorfield.delete(0, END)
    kalkulatorfield.insert(END, operator)

def clear(): #Function untuk menghapus semua nilai dari kalkulator
    global operator # jika tidak menggunakan global maka nilai yang sebelumnya akan muncul kembali 
    operator = ''
    kalkulatorfield.delete(0, END)

def hasil(): #Function untuk menghitung hasil dari kalkulator
    global operator
    hasil = str(eval(operator))
    kalkulatorfield.delete(0, END)
    kalkulatorfield.insert(END, hasil)
    operator = ''



kalkulatorfield = Entry(calculatorframe, font=('Times New Roman', 16, 'bold'), width=42)
kalkulatorfield.grid(row=0, column=0, columnspan=10)


tombol1 = Button(calculatorframe, text='1', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('1'))
tombol1.grid(row=1, column=0)

tombol2 = Button(calculatorframe, text='2', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('2'))
tombol2.grid(row=1, column=1)

tombol3 = Button(calculatorframe, text='3', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('3'))
tombol3.grid(row=1, column=2) 

tombolplus = Button(calculatorframe, text='+', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('+'))
tombolplus.grid(row=1, column=3)

tombol6 = Button(calculatorframe, text='6', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('6'))
tombol6.grid(row=2, column=0)

tombol5 = Button(calculatorframe, text='5', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('5'))
tombol5.grid(row=2, column=1)

tombol4 = Button(calculatorframe, text='4', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('4'))
tombol4.grid(row=2, column=2)

tombolminus = Button(calculatorframe, text='-', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('-'))
tombolminus.grid(row=2, column=3)

tombol7 = Button(calculatorframe, text='7', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('7'))
tombol7.grid(row=3, column=0)

tombol8 = Button(calculatorframe, text='8', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('8'))
tombol8.grid(row=3, column=1)

tombol9 = Button(calculatorframe, text='9', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('9'))
tombol9.grid(row=3, column=2)

tombolkali = Button(calculatorframe, text='*', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('*'))
tombolkali.grid(row=3, column=3)

tombolhasil = Button(calculatorframe, text='=', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=hasil)
tombolhasil.grid(row=4, column=0)

tombol0 = Button(calculatorframe, text='0', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('0'))
tombol0.grid(row=4, column=1)

tombolclear = Button(calculatorframe, text='Clear', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=clear)
tombolclear.grid(row=4, column=2)

tombolbagi = Button(calculatorframe, text='/', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6, command=lambda: tombolclick('/'))
tombolbagi.grid(row=4, column=3)


#---------------------------------------------------------------------------------------------










mainloop()
