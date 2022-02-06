from cgitb import text
from faulthandler import disable
from sys import dllhandle
from tkinter import *
from tkinter import font
from tkinter.ttk import Labelframe
from tokenize import String
from turtle import left, right

a = Tk()
window_name = a.title('Cashier Management System') #Pemberian Title/Judul pada Project

window_size = a.geometry('1270x690+0+0') #Set ukuran window  (diubah) (

size_tetap = a.resizable(0,0)

window_color= a.config(bg='#0B141A') #Set warna windows (diubah)


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
root_fanta = StringVar()
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
root_nasgor.set('--')
root_martabak.set('--')
root_sate.set('--')
root_kebab.set('--')
root_roba.set('--')
root_naskun.set('--')
root_nasbak.set('--')
root_nashim.set('--')
root_nasput.set('--')


# Minuman

root_fanta.set('--')
root_cocacola.set('--')
root_sprite.set('--')
root_fanta.set('--')
root_jusmangga.set('--')
root_jusjeruk.set('--')
root_jusalpukat.set('--')
root_jusapel.set('--')
root_jusdurian.set('--')
root_juspisang.set('--')


# Kue

root_bolu.set('--')
root_brownis.set('--')
root_lapiskukus.set('--')
root_marble.set('--')
root_sponge.set('--')
root_butter.set('--')
root_cotton.set('--')
root_cheese.set('--')
root_mocha.set('--')

# Harga Frame

makanan_var = StringVar()
minuman_var = StringVar()
cake_var = StringVar()
subtotal = StringVar()
pajak = StringVar()
total = StringVar()

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


# Daftar CAKE

bolu = Checkbutton(cake_frame, text='Bolu Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var19)
bolu.grid(row=0, column=0, sticky=W)

brownis = Checkbutton(cake_frame, text='Bolu Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var20)
brownis.grid(row=1, column=0, sticky=W)

lapiskukus = Checkbutton(cake_frame, text='Lapis Kukus', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var21)
lapiskukus.grid(row=2, column=0, sticky=W)

marble = Checkbutton(cake_frame, text='Marble Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var22)
marble.grid(row=3, column=0, sticky=W)

sponge = Checkbutton(cake_frame, text='Sponge Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var23)
sponge.grid(row=4, column=0, sticky=W)

butter = Checkbutton(cake_frame, text='Butter Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var24)
butter.grid(row=5, column=0, sticky=W)

cotton = Checkbutton(cake_frame, text='Cotton Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var25)
cotton.grid(row=6, column=0, sticky=W)

cheese = Checkbutton(cake_frame, text='Cheese Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var26)
cheese.grid(row=7, column=0, sticky=W)

mocha = Checkbutton(cake_frame, text='Mocha Cake', font=('Times New Roman', 18, 'bold'), onvalue=1, offvalue=0, variable=var27)
mocha.grid(row=8, column=0, sticky=W)


# ---------------- input jumlah cake

bolu = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_bolu)
bolu.grid(row=0, column=1)

brownis = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_brownis)
brownis.grid(row=1, column=1)

lapiskukus = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_lapiskukus)
lapiskukus.grid(row=2, column=1)

marble = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_marble)
marble.grid(row=3, column=1)

sponge = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_sponge)
sponge.grid(row=4, column=1)

butter = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_butter)
butter.grid(row=5, column=1)

cotton = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_cotton)
cotton.grid(row=6, column=1)

cheese = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_cheese)
cheese.grid(row=7, column=1)

mocha = Entry(cake_frame, font=('Times New Roman', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=root_mocha)
mocha.grid(row=8, column=1)


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

kalkulatorfield = Entry(calculatorframe, font=('Times New Roman', 16, 'bold'), width=42)
kalkulatorfield.grid(row=0, column=0, columnspan=8)



tombol1 = Button(calculatorframe, text='1', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombol1.grid(row=1, column=0)

tombol2 = Button(calculatorframe, text='2', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombol2.grid(row=1, column=1)

tombol3 = Button(calculatorframe, text='3', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombol3.grid(row=1, column=2) 

tombolplus = Button(calculatorframe, text='+', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombolplus.grid(row=1, column=3)

tombol6 = Button(calculatorframe, text='6', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombol6.grid(row=2, column=0)

tombol5 = Button(calculatorframe, text='5', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombol5.grid(row=2, column=1)

tombol4 = Button(calculatorframe, text='4', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombol4.grid(row=2, column=2)

tombolminus = Button(calculatorframe, text='-', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombolminus.grid(row=2, column=3)

tombol7 = Button(calculatorframe, text='7', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombol7.grid(row=3, column=0)

tombol8 = Button(calculatorframe, text='8', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombol8.grid(row=3, column=1)

tombol9 = Button(calculatorframe, text='9', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombol9.grid(row=3, column=2)

tombolkali = Button(calculatorframe, text='*', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombolkali.grid(row=3, column=3)

tombolhasil = Button(calculatorframe, text='=', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombolhasil.grid(row=4, column=0)

tombol0 = Button(calculatorframe, text='0', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombol0.grid(row=4, column=1)

tombolclear = Button(calculatorframe, text='Clear', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombolclear.grid(row=4, column=2)

tombolbagi = Button(calculatorframe, text='/', font=('Times New Roman', 15, 'bold'), bg='grey', fg='white', bd=6, width=6)
tombolbagi.grid(row=4, column=3)






mainloop()
