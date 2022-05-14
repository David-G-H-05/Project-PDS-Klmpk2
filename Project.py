from tkinter import *
import random
import time


def reset(): 
    text_struk.delete(1.0, END)
#     # SNACK   (Revisi ganti menunya, untuk root_ = dibiarin saja)
    root_pisgor.set('-')
    root_nachos.set('-')
    root_onion.set('-')
    root_chrispy.set('-')
    root_mushroom.set('-')
    root_frech.set('-')
    root_sandwich.set('-')
    root_telur.set('-')
    root_dimsum.set('-')


    # DRINK   (Revisi ganti menunya, untuk root_ = dibiarin saja)

    root_lavamilk.set('-')
    root_milotsunami.set('-')
    root_sodaconi.set('-')
    root_bluetea.set('-')
    root_whitejack.set('-')
    root_americano.set('-')
    root_iceblend.set('-')
    root_macchiato.set('-')
    root_juice.set('-')


    # DESSERT   (Revisi ganti menunya, untuk root_ = dibiarin saja)

    root_brownies.set('-')
    root_choco.set('-')
    root_cupcake.set('-')
    root_pudding.set('-')
    root_paisusu.set('-')
    root_muffin.set('-')
    root_cookies.set('-')
    root_chocolava.set('-')
    root_desertbox.set('-')

    
    input_pisgor.config(state=DISABLED)
    input_nachos.config(state=DISABLED)
    input_onion.config(state=DISABLED)
    input_chrispy.config(state=DISABLED)
    input_mushroom.config(state=DISABLED)
    input_frech.config(state=DISABLED)
    input_sandwich.config(state=DISABLED)
    input_telur.config(state=DISABLED)
    input_dimsum.config(state=DISABLED)

    input_lavamilk.config(state=DISABLED)
    input_milotsunami.config(state=DISABLED)
    input_sodaconi.config(state=DISABLED)
    input_bluetea.config(state=DISABLED)
    input_whitejack.config(state=DISABLED)
    input_americano.config(state=DISABLED)
    input_iceblend.config(state=DISABLED)
    input_macchiato.config(state=DISABLED)
    input_juice.config(state=DISABLED)

    input_brownies.config(state=DISABLED)
    input_choco.config(state=DISABLED)
    input_cupcake.config(state=DISABLED)
    input_pudding.config(state=DISABLED)
    input_paisusu.config(state=DISABLED)
    input_muffin.config(state=DISABLED)
    input_cookies.config(state=DISABLED)
    input_chocolava.config(state=DISABLED)
    input_desertbox.config(state=DISABLED)
    

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var16.set(0)
    var16.set(0)
    var16.set(0)
    var16.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    snack_var.set('')
    drink_var.set('')
    dessert_var.set('')
    subtotal_var.set('')
    pajak_var.set('')
    total_var.set('')





def struk():
    if snack_var!='' or drink_var!='' or dessert_var!='':
        text_struk.delete(1.0, END)
        x = random.randint(100, 1000)
        tanggal = time.strftime("%d/%m/%Y")  # Memasukkan bagian tanggal
        jam = time.strftime("%H:%M:%S")  # memasukkan bagian waktu
        text_struk.insert(END, "Cafe Indah Jaya \n")
        text_struk.insert(END,tanggal + "\t\t\t        " + jam + '\n')    # jika menggunakan /t maka jarak pisahnya terlalu jauh
        text_struk.insert(END, "----------------------------------------------------------\n")
        text_struk.insert(END, "  Menu: \t\t" + "\tHarga (Rp)\n\n")
        if root_pisgor.get() != "-":
            text_struk.insert(END, f"  Pigor Elite:\t\t\t {int(root_pisgor.get())*19000} \n\n")
        if root_nachos.get() != "-":
            text_struk.insert(END, f"  Nachos:\t\t\t {int(root_nachos.get())*25000} \n\n")
        if root_onion.get() != "-":
            text_struk.insert(END, f"  Onion Ring:\t\t\t {int(root_onion.get())*15000} \n\n")
        if root_chrispy.get() != "-":
            text_struk.insert(END, f"  Chrispy Chicken Ball:\t\t\t {int(root_chrispy.get())*20000} \n\n")
        if root_mushroom.get() != "-":
            text_struk.insert(END, f"  Mushroom Chrispy:\t\t\t {int(root_mushroom.get())*25000} \n\n")
        if root_frech.get() != "-":
            text_struk.insert(END, f"  Frech Fries Big Size:\t\t\t {int(root_frech.get())*15000} \n\n")
        if root_sandwich.get() != "-":
            text_struk.insert(END, f"  Sandwich 3pcs:\t\t\t {int(root_sandwich.get())*15000} \n\n")
        if root_telur.get() != "-":
            text_struk.insert(END, f"  Telur Gulung 10pcs:\t\t\t {int(root_telur.get())*15000} \n\n")
        if root_dimsum.get() != "-":
            text_struk.insert(END, f"  Dimsum:\t\t\t {int(root_dimsum.get())*12000} \n\n")

        if root_lavamilk.get() != "-":
            text_struk.insert(END, f"  Lavamilk:\t\t\t {int(root_lavamilk.get())*15000} \n\n")
        if root_milotsunami.get() != "-":
            text_struk.insert(END, f"  Milo Tsunami:\t\t\t {int(root_milotsunami.get())*15000} \n\n")
        if root_sodaconi.get() != "-":
            text_struk.insert(END, f"  Soda Coni:\t\t\t {int(root_sodaconi.get())*17000} \n\n")
        if root_bluetea.get() != "-":
            text_struk.insert(END, f"  Blue Ocean Tea:\t\t\t {int(root_bluetea.get())*19000} \n\n")
        if root_whitejack.get() != "-":
            text_struk.insert(END, f"  white Jack Coffe:\t\t\t {int(root_whitejack.get())*20000} \n\n")
        if root_americano.get() != "-":
            text_struk.insert(END, f"  Americano:\t\t\t {int(root_americano.get())*20000} \n\n")
        if root_iceblend.get() != "-":
            text_struk.insert(END, f"  Ice Blend Coffe:\t\t\t {int(root_iceblend.get())*17000} \n\n")
        if root_macchiato.get() != "-":
            text_struk.insert(END, f"  Macchiato:\t\t\t {int(root_macchiato.get())*25000} \n\n")
        if root_juice.get() != "-":
            text_struk.insert(END, f"  Juice:\t\t\t {int(root_juice.get())*12000} \n\n")

        if root_brownies.get() != "-":
            text_struk.insert(END, f"  Brownies:\t\t\t {int(root_brownies.get())*14500} \n\n")
        if root_choco.get() != "-":
            text_struk.insert(END, f"  Choco Oreo Cake:\t\t\t {int(root_choco.get())*12000} \n\n")
        if root_cupcake.get() != "-":
            text_struk.insert(END, f"  Cupcake:\t\t\t {int(root_cupcake.get())*7000} \n\n")
        if root_pudding.get() != "-":
            text_struk.insert(END, f"  Pudding:\t\t\t {int(root_pudding.get())*7000} \n\n")
        if root_paisusu.get() != "-":
            text_struk.insert(END, f"  Pai Susu:\t\t\t {int(root_paisusu.get())*5000} \n\n")
        if root_muffin.get() != "-":
            text_struk.insert(END, f"  Muffin:\t\t\t {int(root_muffin.get())*8000} \n\n")
        if root_cookies.get() != "-":
            text_struk.insert(END, f"  Cookies:\t\t\t {int(root_cookies.get())*5000} \n\n")
        if root_chocolava.get() != "-":
            text_struk.insert(END, f"  Choco Lava:\t\t\t {int(root_chocolava.get())*15000} \n\n")
        if root_desertbox.get() != "-":
            text_struk.insert(END, f"  Dessert Box:\t\t\t {int(root_desertbox.get())*20000} \n\n")

        text_struk.insert(END, "----------------------------------------------------------\n")
        if harga_snack != "-":
            text_struk.insert(END, f"  Total Harga Snack:\t\t\tRp. {harga_snack} \n\n")
        if  harga_drink != "-":
            text_struk.insert(END, f"  Total Harga Drink:\t\t\tRp. {harga_drink} \n\n")
        if harga_dessert != "-":
            text_struk.insert(END, f"  Total Harga Dessert:\t\t\tRp. {harga_dessert} \n\n")

        text_struk.insert(END, "----------------------------------------------------------\n")

        text_struk.insert(END, f"   Subtotal:\t\t\tRp. {int(harga_snack)+int(harga_drink)+int(harga_dessert)} \n\n")
        text_struk.insert(END, f"   Pajak:\t\t\tRp. {2000} \n\n")
        text_struk.insert(END, f"   Total:\t\t\tRp. {int(harga_snack)+int(harga_drink)+int(harga_dessert)+2000} \n\n")




# Funtion untuk menghitung total harga
def totalharga():
    global harga_snack,harga_drink, harga_dessert
    # replace berguna untuk mengganti string
    item1 = int(root_pisgor.get().replace("-", "0"))
    item2 = int(root_nachos.get().replace("-", "0"))
    item3 = int(root_onion.get().replace("-", "0"))
    item4 = int(root_chrispy.get().replace("-", "0"))
    item5 = int(root_mushroom.get().replace("-", "0"))
    item6 = int(root_frech.get().replace("-", "0"))
    item7 = int(root_sandwich.get().replace("-", "0"))
    item8 = int(root_telur.get().replace('-', '0'))
    item9 = int(root_dimsum.get().replace('-', '0'))

    item10 = int(root_lavamilk.get().replace('-', '0'))
    item11 = int(root_milotsunami.get().replace('-', '0'))
    item12 = int(root_sodaconi.get().replace('-', '0'))
    item13 = int(root_bluetea.get().replace('-', '0'))
    item14 = int(root_whitejack.get().replace('-', '0'))
    item15 = int(root_americano.get().replace('-', '0'))
    item16 = int(root_iceblend.get().replace('-', '0'))
    item17 = int(root_macchiato.get().replace('-', '0'))
    item18 = int(root_juice.get().replace('-', '0'))

    item19 = int(root_brownies.get().replace('-', '0'))
    item20 = int(root_choco.get().replace('-', '0'))
    item21 = int(root_cupcake.get().replace('-', '0'))
    item22 = int(root_pudding.get().replace('-', '0'))
    item23 = int(root_paisusu.get().replace('-', '0'))
    item24 = int(root_muffin.get().replace('-', '0'))
    item25 = int(root_cookies.get().replace('-', '0'))
    item26 = int(root_chocolava.get().replace('-', '0'))
    item27 = int(root_desertbox.get().replace('-', '0'))

    # Pemberian harga

    harga_snack = (item1*19000) + (item2*25000) + (item3*15000) + (item4*20000) + \
         (item5*25000) + (item6*15000) + (item7*15000) + (item8*15000) + (item9*12000)

    harga_drink = (item10*15000) + (item11*15000) + (item12*17000) + (item13*19000) + \
        (item14*20000) + (item15*20000) + (item16*17000) + (item17*25000) + (item18*12000)

    harga_dessert = (item19*14500) + (item20*12000) + (item21*7000) + (item22*7000) + \
        (item23*5000) + (item24*8000) + (item25*5000) + (item26*15000) + (item27*20000)

    snack_var.set('Rp. '+ str(harga_snack))
    drink_var.set('Rp. '+ str(harga_drink))
    dessert_var.set('Rp. '+ str(harga_dessert))

    subtotal = harga_snack + harga_drink + harga_dessert
    subtotal_var.set('Rp. '+ str(subtotal))

    pajak_var.set('Rp. 2000')

    total = subtotal + 2000
    total_var.set('Rp. '+ str(total))


# Function untuk Menu Makanan

def pisgor():
    if var1.get() == 1:
        input_pisgor.config(state=NORMAL)
        input_pisgor.delete(0, END)
        input_pisgor.focus()
    else:
        input_pisgor.config(state=DISABLED)
        root_pisgor.set('-')

def nachos():
    if var2.get() == 1:
        input_nachos.config(state=NORMAL)
        input_nachos.delete(0, END)
        input_nachos.focus()
    else:
        input_nachos.config(state=DISABLED)
        root_nachos.set('-')

def onion():
    if var3.get() == 1:
        input_onion.config(state=NORMAL)
        input_onion.delete(0, END)
        input_onion.focus()
    else:
        input_onion.config(state=DISABLED)
        root_onion.set('-')

def chrispy():
    if var4.get() == 1:
        input_chrispy.config(state=NORMAL)
        input_chrispy.delete(0, END)
        input_chrispy.focus()
    else:
        input_chrispy.config(state=DISABLED)
        root_chrispy.set('-')

def mushroom():
    if var5.get() == 1:
        input_mushroom.config(state=NORMAL)
        input_mushroom.delete(0, END)
        input_mushroom.focus()
    else:
        input_mushroom.config(state=DISABLED)
        root_mushroom.set('-')

def frech():
    if var6.get() == 1:
        input_frech.config(state=NORMAL)
        input_frech.delete(0, END)
        input_frech.focus()
    else:
        input_frech.config(state=DISABLED)
        root_frech.set('-')

def sandwich():
    if var7.get() == 1:
        input_sandwich.config(state=NORMAL)
        input_sandwich.delete(0, END)
        input_sandwich.focus()
    else:
        input_sandwich.config(state=DISABLED)
        root_sandwich.set('-')

def telur():
    if var8.get() == 1:
        input_telur.config(state=NORMAL)
        input_telur.delete(0, END)
        input_telur.focus()
    else:
        input_telur.config(state=DISABLED)
        root_telur.set('-')

def dimsum():
    if var9.get() == 1:
        input_dimsum.config(state=NORMAL)
        input_dimsum.delete(0, END)
        input_dimsum.focus()
    else:
        input_dimsum.config(state=DISABLED)
        root_dimsum.set('-')


def lavamilk():
    if var10.get() == 1:
        input_lavamilk.config(state=NORMAL)
        input_lavamilk.delete(0, END)
        input_lavamilk.focus()
    else:
        input_lavamilk.config(state=DISABLED)
        root_lavamilk.set('-')

def milotsunami():
    if var11.get() == 1:
        input_milotsunami.config(state=NORMAL)
        input_milotsunami.delete(0, END)
        input_milotsunami.focus()
    else:
        input_milotsunami.config(state=DISABLED)
        root_milotsunami.set('-')

def sodaconi():
    if var12.get() == 1:
        input_sodaconi.config(state=NORMAL)
        input_sodaconi.delete(0, END)
        input_sodaconi.focus()
    else:
        input_sodaconi.config(state=DISABLED)
        root_sodaconi.set('-')

def bluetea():
    if var13.get() == 1:
        input_bluetea.config(state=NORMAL)
        input_bluetea.delete(0, END)
        input_bluetea.focus()
    else:
        input_bluetea.config(state=DISABLED)
        root_bluetea.set('-')

def whitejack():
    if var14.get() == 1:
        input_whitejack.config(state=NORMAL)
        input_whitejack.delete(0, END)
        input_whitejack.focus()
    else:
        input_whitejack.config(state=DISABLED)
        root_whitejack.set('-')

def americano():
    if var15.get() == 1:
        input_americano.config(state=NORMAL)
        input_americano.delete(0, END)
        input_americano.focus()
    else:
        input_americano.config(state=DISABLED)
        root_americano.set('-')

def iceblend():
    if var16.get() == 1:
        input_iceblend.config(state=NORMAL)
        input_iceblend.delete(0, END)
        input_iceblend.focus()
    else:
        input_iceblend.config(state=DISABLED)
        root_iceblend.set('-')

def macchiato():
    if var17.get() == 1:
        input_macchiato.config(state=NORMAL)
        input_macchiato.delete(0, END)
        input_macchiato.focus()
    else:
        input_macchiato.config(state=DISABLED)
        root_macchiato.set('-')

def juice():
    if var18.get() == 1:
        input_juice.config(state=NORMAL)
        input_juice.delete(0, END)
        input_juice.focus()
    else:
        input_juice.config(state=DISABLED)
        root_juice.set('-')



def brownies():
    if var19.get() == 1:
        input_brownies.config(state=NORMAL)
        input_brownies.delete(0, END)
        input_brownies.focus()
    else:
        input_brownies.config(state=DISABLED)
        root_brownies.set('-')

def choco():
    if var20.get() == 1:
        input_choco.config(state=NORMAL)
        input_choco.delete(0, END)
        input_choco.focus()
    else:
        input_choco.config(state=DISABLED)
        root_choco.set('-')

def cupcake():
    if var21.get() == 1:
        input_cupcake.config(state=NORMAL)
        input_cupcake.delete(0, END)
        input_cupcake.focus()
    else:
        input_cupcake.config(state=DISABLED)
        root_cupcake.set('-')

def pudding():
    if var22.get() == 1:
        input_pudding.config(state=NORMAL)
        input_pudding.delete(0, END)
        input_pudding.focus()
    else:
        input_pudding.config(state=DISABLED)
        root_pudding.set('-')

def paisusu():
    if var23.get() == 1:
        input_paisusu.config(state=NORMAL)
        input_paisusu.delete(0, END)
        input_paisusu.focus()
    else:
        input_paisusu.config(state=DISABLED)
        root_paisusu.set('-')

def muffin():
    if var24.get() == 1:
        input_muffin.config(state=NORMAL)
        input_muffin.delete(0, END)
        input_muffin.focus()
    else:
        input_muffin.config(state=DISABLED)
        root_muffin.set('-')

def cookies():
    if var25.get() == 1:
        input_cookies.config(state=NORMAL)
        input_cookies.delete(0, END)
        input_cookies.focus()
    else:
        input_cookies.config(state=DISABLED)
        root_cookies.set('-')

def chocolava():
    if var26.get() == 1:
        input_chocolava.config(state=NORMAL)
        input_chocolava.delete(0, END)
        input_chocolava.focus()
    else:
        input_chocolava.config(state=DISABLED)
        root_chocolava.set('-')

def desertbox():
    if var27.get() == 1:
        input_desertbox.config(state=NORMAL)
        input_desertbox.delete(0, END)
        input_desertbox.focus()
    else:
        input_desertbox.config(state=DISABLED)
        root_desertbox.set('-')







#----------------------------------------------------------------------------------------------------------------------

# Bagian tampilan (Frontend)
a = Tk()
# Pemberian Title/Judul pada Project
window_name = a.title('Cashier Management System')

window_size = a.geometry('1300x670+100+50')  # Set ukuran window  (diubah) (

size_tetap = a.resizable(0, 0)

window_color = a.config(bg='red')  # Set warna windows (diubah)


#  Text in Window = 'CASHIER MANAGEMENT SYSTEM'

# untuk background bisa (diubah)
topframe = Frame(a, bd=14, relief=RIDGE, bg='#4B4B4B')
topframe.pack(side=TOP)

project_name = Label(topframe, text='CASHIER MANAGEMENT SYSTEM', font=(
    'PragmataPro', 30, 'bold'), bg='#4B4B4B', fg='white', width=53, bd=1 , pady=1)  # (diubah)
project_name.grid(row=0, column=0)

# Frame


# bisa menambahkan warna background  (bg)
menuframe = Frame(a, bd=13,pady=4, relief=RIDGE, bg='#4B4B4B')
menuframe.pack(side=LEFT)

# bisa menambahkan warna background  (bg)
hargaframe = Frame(menuframe, relief=RIDGE, bg='#4B4B4B', bd=10,padx=35, pady=12)
hargaframe.pack(side=BOTTOM)

makanan_frame = LabelFrame(menuframe, text='SNACK', font=(
    'Times New Roman', 20, 'bold'), bd=15,pady=6,relief=RIDGE, fg='white', bg='#4B4B4B')
makanan_frame.pack(side=LEFT)

minuman_frame = LabelFrame(menuframe, text='DRINK', font=(
    'Times New Roman', 20, 'bold'), bd=15,pady=6 ,relief=RIDGE, fg='white', bg='#4B4B4B')
minuman_frame.pack(side=LEFT)

cake_frame = LabelFrame(menuframe, text='DESSERT', font=(
    'Times New Roman', 20, 'bold'), bd=15 ,pady=8, relief=RIDGE, fg='white', bg='#4B4B4B')
cake_frame.pack(side=LEFT)


# ------------
rightframe = Frame(a, bd=10, relief=RIDGE, bg='#4B4B4B', )
rightframe.pack(side=RIGHT)

# Fitur bagian kanan

calculatorframe = Frame(rightframe, bd=1, relief=RIDGE, bg='#4B4B4B')
calculatorframe.pack()

strukframe = Frame(rightframe, bd=7, relief=RIDGE, bg='#4B4B4B')
strukframe.pack()

tombolframe = Frame(rightframe, bd=2, relief=RIDGE, bg='#4B4B4B')
tombolframe.pack()

# VARIABEL yang menghubungkan dengan daftar makanan

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
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

# SNACK (Revisi ganti menunya, untuk root_ = dibiarin saja)

root_pisgor = StringVar()
root_nachos = StringVar()
root_onion = StringVar()
root_chrispy = StringVar()
root_mushroom = StringVar()
root_frech = StringVar()
root_sandwich = StringVar()
root_telur = StringVar()
root_dimsum = StringVar()

# DRINK (Revisi ganti menunya, untuk root_ = dibiarin saja)

root_lavamilk = StringVar()
root_milotsunami = StringVar()
root_sodaconi = StringVar()
root_bluetea = StringVar()
root_whitejack = StringVar()
root_americano = StringVar()
root_iceblend = StringVar()
root_macchiato = StringVar()
root_juice = StringVar()

# DESSERT (Revisi ganti menunya, untuk root_ = dibiarin saja)

root_brownies = StringVar()
root_choco = StringVar()
root_cupcake = StringVar()
root_pudding = StringVar()
root_paisusu = StringVar()
root_muffin = StringVar()
root_cookies = StringVar()
root_chocolava = StringVar()
root_desertbox = StringVar()


# Pengisian Jumlah pada Kolom daftar makanan,minuman & cake

# SNACK   (Revisi ganti menunya, untuk root_ = dibiarin saja)
root_pisgor.set('-')
root_nachos.set('-')
root_onion.set('-')
root_chrispy.set('-')
root_mushroom.set('-')
root_frech.set('-')
root_sandwich.set('-')
root_telur.set('-')
root_dimsum.set('-')


# DRINK   (Revisi ganti menunya, untuk root_ = dibiarin saja)

root_lavamilk.set('-')
root_milotsunami.set('-')
root_sodaconi.set('-')
root_bluetea.set('-')
root_whitejack.set('-')
root_americano.set('-')
root_iceblend.set('-')
root_macchiato.set('-')
root_juice.set('-')


# DESSERT   (Revisi ganti menunya, untuk root_ = dibiarin saja)

root_brownies.set('-')
root_choco.set('-')
root_cupcake.set('-')
root_pudding.set('-')
root_paisusu.set('-')
root_muffin.set('-')
root_cookies.set('-')
root_chocolava.set('-')
root_desertbox.set('-')

# Harga Frame

snack_var = StringVar()
drink_var = StringVar()
dessert_var = StringVar()
subtotal_var = StringVar()
pajak_var = StringVar()
total_var = StringVar()

# ---------------------------------------------

# Daftar MAKANAN
# sticky digunakan untuk meluruskan daftar makanan/minuman

# mengganti variable dan text sesuai masing" menu

pisgor = Checkbutton(makanan_frame, text='Pisgor Elite', font=('Deja Vu Sans Mono', 14),
                     onvalue=1, offvalue=0, variable=var1, bg='#4B4B4B', command=pisgor, fg='white')  
pisgor.grid(row=0, column=0, sticky=W)

nachos = Checkbutton(makanan_frame, text='Nachos', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var2, bg='#4B4B4B', command=nachos, fg='white')
nachos.grid(row=1, column=0, sticky=W)

onion = Checkbutton(makanan_frame, text='Onion Ring', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var3, bg='#4B4B4B', command=onion, fg='white')
onion.grid(row=2, column=0, sticky=W)

chrispy = Checkbutton(makanan_frame, text='Chrispy Chiken Ball', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var4, bg='#4B4B4B', command=chrispy, fg='white')
chrispy.grid(row=3, column=0, sticky=W)

mushroom = Checkbutton(makanan_frame, text='Mushroom Chrispy', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var5, bg='#4B4B4B', command=mushroom, fg='white')
mushroom.grid(row=4, column=0, sticky=W)

french = Checkbutton(makanan_frame, text='French Fries Big Size', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var6, bg='#4B4B4B', command=frech, fg='white')
french.grid(row=5, column=0, sticky=W)

sandwich = Checkbutton(makanan_frame, text='Sandwich 3pcs', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var7, bg='#4B4B4B', command=sandwich, fg='white')
sandwich.grid(row=6, column=0, sticky=W)

telur = Checkbutton(makanan_frame, text='Telur Gulung 10pcs', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var8, bg='#4B4B4B', command=telur, fg='white')
telur.grid(row=7, column=0, sticky=W)

dimsum = Checkbutton(makanan_frame, text='Dimsum', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var9, bg='#4B4B4B', command=dimsum, fg='white')
dimsum.grid(row=8, column=0, sticky=W)


# ---------------- input jumlah makanan (mengganti variable dan text sesuai masing" menu)

input_pisgor = Entry(makanan_frame, font=('Times New Roman', 14, 'bold'),
                     bd=7, width=6, state=DISABLED, textvariable=root_pisgor)
input_pisgor.grid(row=0, column=1)

input_nachos = Entry(makanan_frame, font=('Times New Roman', 14, 'bold'),
                       bd=7, width=6, state=DISABLED, textvariable=root_nachos)
input_nachos.grid(row=1, column=1)

input_onion = Entry(makanan_frame, font=('Times New Roman', 14, 'bold'),
                   bd=7, width=6, state=DISABLED, textvariable=root_onion)
input_onion.grid(row=2, column=1)

input_chrispy = Entry(makanan_frame, font=('Times New Roman', 14, 'bold'),
                    bd=7, width=6, state=DISABLED, textvariable=root_chrispy)
input_chrispy.grid(row=3, column=1)

input_mushroom = Entry(makanan_frame, font=('Times New Roman', 14, 'bold'),
                   bd=7, width=6, state=DISABLED, textvariable=root_mushroom)
input_mushroom.grid(row=4, column=1)

input_frech = Entry(makanan_frame, font=('Times New Roman', 14, 'bold'),
                     bd=7, width=6, state=DISABLED, textvariable=root_frech)
input_frech.grid(row=5, column=1)

input_sandwich = Entry(makanan_frame, font=('Times New Roman', 14, 'bold'),
                     bd=7, width=6, state=DISABLED, textvariable=root_sandwich)
input_sandwich.grid(row=6, column=1)

input_telur = Entry(makanan_frame, font=('Times New Roman', 14, 'bold'),
                     bd=7, width=6, state=DISABLED, textvariable=root_telur)
input_telur.grid(row=7, column=1)

input_dimsum = Entry(makanan_frame, font=('Times New Roman', 14, 'bold'),
                     bd=7, width=6, state=DISABLED, textvariable=root_dimsum)
input_dimsum.grid(row=8, column=1)

# ----------------------------------------------------------

# Daftar MINUMAN

# mengganti variable dan text sesuai masing" menu

lavamilk = Checkbutton(minuman_frame, text='Lava Milk Shake', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var10, bg='#4B4B4B', command=lavamilk, fg='white')
lavamilk.grid(row=0, column=0, sticky=W)

milotsunami = Checkbutton(minuman_frame, text='Milo Tsunami', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var11, bg='#4B4B4B', command=milotsunami, fg='white')
milotsunami.grid(row=1, column=0, sticky=W)

sodaconi = Checkbutton(minuman_frame, text='Soda Coni', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var12, bg='#4B4B4B', command=sodaconi, fg='white')
sodaconi.grid(row=2, column=0, sticky=W)

bluetea = Checkbutton(minuman_frame, text='Blue Ocean Tea', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var13, bg='#4B4B4B', command=bluetea, fg='white')
bluetea.grid(row=3, column=0, sticky=W)

whitejack = Checkbutton(minuman_frame, text='white Jack Coffe', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var14, bg='#4B4B4B', command=whitejack, fg='white')
whitejack.grid(row=4, column=0, sticky=W)

americano = Checkbutton(minuman_frame, text='Americano', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var15, bg='#4B4B4B', command=americano, fg='white')
americano.grid(row=5, column=0, sticky=W)

iceblend = Checkbutton(minuman_frame, text='Ice Blend Coffe', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var16, bg='#4B4B4B', command=iceblend, fg='white')
iceblend.grid(row=6, column=0, sticky=W)

macchiato = Checkbutton(minuman_frame, text='Macchiato', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var17, bg='#4B4B4B', command=macchiato, fg='white')
macchiato.grid(row=7, column=0, sticky=W)

juice = Checkbutton(minuman_frame, text='Juice', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var18, bg='#4B4B4B', command=juice, fg='white')
juice.grid(row=8, column=0, sticky=W)


# ---------------- input jumlah minuman (mengganti variable dan text sesuai masing" menu)

input_lavamilk = Entry(minuman_frame, font=('Times New Roman', 14, 'bold'),
                    bd=7, width=6, state=DISABLED, textvariable=root_lavamilk)
input_lavamilk.grid(row=0, column=1)

input_milotsunami= Entry(minuman_frame, font=('Times New Roman', 14, 'bold'),
                       bd=7, width=6, state=DISABLED, textvariable=root_milotsunami)
input_milotsunami.grid(row=1, column=1)

input_sodaconi = Entry(minuman_frame, font=('Times New Roman', 14, 'bold'),
                     bd=7, width=6, state=DISABLED, textvariable=root_sodaconi)
input_sodaconi.grid(row=2, column=1)

input_bluetea = Entry(minuman_frame, font=('Times New Roman', 14, 'bold'),
                        bd=7, width=6, state=DISABLED, textvariable=root_bluetea)
input_bluetea.grid(row=3, column=1)

input_whitejack = Entry(minuman_frame, font=('Times New Roman', 14, 'bold'),
                       bd=7, width=6, state=DISABLED, textvariable=root_whitejack)
input_whitejack.grid(row=4, column=1)

input_americano = Entry(minuman_frame, font=('Times New Roman', 14, 'bold'),
                         bd=7, width=6, state=DISABLED, textvariable=root_americano)
input_americano.grid(row=5, column=1)

input_iceblend = Entry(minuman_frame, font=('Times New Roman', 14, 'bold'),
                      bd=7, width=6, state=DISABLED, textvariable=root_iceblend)
input_iceblend.grid(row=6, column=1)

input_macchiato = Entry(minuman_frame, font=('Times New Roman', 14, 'bold'),
                        bd=7, width=6, state=DISABLED, textvariable=root_macchiato)
input_macchiato.grid(row=7, column=1)

input_juice = Entry(minuman_frame, font=('Times New Roman', 14, 'bold'),
                        bd=7, width=6, state=DISABLED, textvariable=root_juice)
input_juice.grid(row=8, column=1)


# Daftar CAKE

# mengganti variable dan text sesuai masing" menu

brownies = Checkbutton(cake_frame, text='Brownies', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var19, bg='#4B4B4B', command=brownies, fg='white')
brownies.grid(row=0, column=0, sticky=W)

choco = Checkbutton(cake_frame, text='Choco Oreo Cake', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var20, bg='#4B4B4B', command=choco, fg='white')
choco.grid(row=1, column=0, sticky=W)

cupcake = Checkbutton(cake_frame, text='Cupcake', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var21, bg='#4B4B4B', command=cupcake, fg='white')
cupcake.grid(row=2, column=0, sticky=W)

pudding = Checkbutton(cake_frame, text='Pudding', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var22, bg='#4B4B4B', command=pudding, fg='white')
pudding.grid(row=3, column=0, sticky=W)

paisusu= Checkbutton(cake_frame, text='Pai Susu ', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var23, bg='#4B4B4B', command=paisusu, fg='white')
paisusu.grid(row=4, column=0, sticky=W)

muffin = Checkbutton(cake_frame, text='Muffin', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var24, bg='#4B4B4B', command=muffin, fg='white')
muffin.grid(row=5, column=0, sticky=W)

cookies= Checkbutton(cake_frame, text='Cookies', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var25, bg='#4B4B4B', command=cookies, fg='white')
cookies.grid(row=6, column=0, sticky=W)

chocolava = Checkbutton(cake_frame, text='Choco Lava', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var26, bg='#4B4B4B', command=chocolava, fg='white')
chocolava.grid(row=7, column=0, sticky=W)

desertbox = Checkbutton(cake_frame, text='Dessert Box', font=(
    'Deja Vu Sans Mono', 14), onvalue=1, offvalue=0, variable=var27, bg='#4B4B4B', command=desertbox, fg='white')
desertbox.grid(row=8, column=0, sticky=W)


# ---------------- input jumlah cake (mengganti variable dan text sesuai masing" menu)

input_brownies = Entry(cake_frame, font=('Times New Roman', 14, 'bold'),
                   bd=7, width=6, state=DISABLED, textvariable=root_brownies)
input_brownies.grid(row=0, column=1)

input_choco = Entry(cake_frame, font=('Times New Roman', 14, 'bold'),
                      bd=7, width=6, state=DISABLED, textvariable=root_choco)
input_choco.grid(row=1, column=1)

input_cupcake = Entry(cake_frame, font=('Times New Roman', 14, 'bold'),
                         bd=7, width=6, state=DISABLED, textvariable=root_cupcake)
input_cupcake.grid(row=2, column=1)

input_pudding = Entry(cake_frame, font=('Times New Roman', 14, 'bold'),
                     bd=7, width=6, state=DISABLED, textvariable=root_pudding)
input_pudding.grid(row=3, column=1)

input_paisusu = Entry(cake_frame, font=('Times New Roman', 14, 'bold'),
                     bd=7, width=6, state=DISABLED, textvariable=root_paisusu)
input_paisusu.grid(row=4, column=1)

input_muffin = Entry(cake_frame, font=('Times New Roman', 14, 'bold'),
                     bd=7, width=6, state=DISABLED, textvariable=root_muffin)
input_muffin.grid(row=5, column=1)

input_cookies = Entry(cake_frame, font=('Times New Roman', 14, 'bold'),
                     bd=7, width=6, state=DISABLED, textvariable=root_cookies)
input_cookies.grid(row=6, column=1)

input_chocolava = Entry(cake_frame, font=('Times New Roman', 14, 'bold'),
                     bd=7, width=6, state=DISABLED, textvariable=root_chocolava)
input_chocolava.grid(row=7, column=1)

input_desertbox = Entry(cake_frame, font=('Times New Roman', 14, 'bold'),
                    bd=7, width=6, state=DISABLED, textvariable=root_desertbox)
input_desertbox.grid(row=8, column=1)


# Membuat Label Total Harga Snack, Drink, dan Dessert

# Snack
labelsnack = Label(hargaframe, text='Total Harga Snack', font=(
    'Deja Vu Sans Mono', 16, 'bold'), bg='#4B4B4B', fg='white')
labelsnack.grid(row=0, column=0)

textlabelsnack = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'),
                         bd=6, width=14, fg='black', state='readonly', textvariable=snack_var)
textlabelsnack.grid(row=0, column=1, padx=35)

# Minuman
labeldrink = Label(hargaframe, text='Total Harga Drink', font=(
    'Deja Vu Sans Mono', 16, 'bold'), bg='#4B4B4B', fg='white')
labeldrink.grid(row=1, column=0)

textlabeldrink = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'),
                         bd=6, width=14, state='readonly', fg='black', textvariable=drink_var)
textlabeldrink.grid(row=1, column=1, padx=35)

# Cake
labeldessert = Label(hargaframe, text='Total Harga Cake', font=(
    'Deja Vu Sans Mono', 16, 'bold'), bg='#4B4B4B', fg='white')
labeldessert.grid(row=2, column=0, sticky=W)

textlabeldessert = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'),
                      bd=6, width=14, fg='black', state='readonly', textvariable=dessert_var)
textlabeldessert.grid(row=2, column=1, padx=35)


# Sub total
# Sub total itu gabungan harga makanan, minuman & cake
labelsubtotal = Label(hargaframe, text='Sub Total', font=(
    'Deja Vu Sans Mono', 16, 'bold'), bg='#4B4B4B', fg='white')
labelsubtotal.grid(row=0, column=2)

textsubtotal = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'),
                     bd=6, width=14, state='readonly', textvariable=subtotal_var)
textsubtotal.grid(row=0, column=3, padx=35)

# Pajak
labelpajak = Label(hargaframe, text='Pajak', font=(
    'Deja Vu Sans Mono', 16, 'bold'), bg='#4B4B4B', fg='white')
labelpajak.grid(row=1, column=2, sticky=W)

textpajak = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'),
                  bd=6, width=14, state='readonly', textvariable=pajak_var)
textpajak.grid(row=1, column=3, padx=35)

# Total
# Total berbeda dengan subtotal karena subtotal tidak termasuk pajak
labeltotal = Label(hargaframe, text='Total', font=(
    'Deja Vu Sans Mono', 16, 'bold'), bg='#4B4B4B', fg='white')
labeltotal.grid(row=2, column=2, sticky=W)

texttotal = Entry(hargaframe, font=('Times Nem Roman', 16, 'bold'),
                  bd=6, width=14, state='readonly', textvariable=total_var)
texttotal.grid(row=2, column=3, padx=35)

# Keterangan:
# Grid = adalah sebuah penempatan suatu widget kedalam tabel, contohnya seperti row(baris), column(kolom), dll
# untuk pengaturan grid kita bisa mampu mengubahnya dan mengatur sesuai dengan keinginan kita.


# ---------------------------------------------------------------------------------------------

# Membuat Tombol untuk menghitung total harga
# Keterangan = menggunakan variabel tombolframe untuk membuat sebuah tombol

tombol_total = Button(tombolframe, text='Total', font=(
    'Times New Roman', 14, 'bold'), bg='orange', fg='white', bd=3, padx=29, command=totalharga)
tombol_total.grid(row=0, column=0)

tombol_struk = Button(tombolframe, text='Struk', font=(
    'Times New Roman', 14, 'bold'), bg='orange', fg='white', bd=3, padx=29, command=struk)
tombol_struk.grid(row=0, column=1)

tombol_reset = Button(tombolframe, text='Reset', font=(
    'Times New Roman', 14, 'bold'), bg='orange', fg='white', bd=3, padx=29, command=reset)
tombol_reset.grid(row=0, column=2)


# Membuat Tempat untuk hasil Struk

text_struk = Text(strukframe,  font=('Times New Roman', 14,
                  'bold'), bg='#4B4B4B', fg='white', width=35, height=13)
text_struk.grid(row=0, column=0)


# ---------------------------------------------------------------------------------------------


# Calculator
# Function pada Kalkulator
operator = ''


def tombolclick(angka):  # Function untuk mengambil nilai dari tombol
    global operator
    operator = operator + angka
    kalkulatorfield.delete(0, END)
    kalkulatorfield.insert(END, operator)


def clear():  # Function untuk menghapus semua nilai dari kalkulator
    # jika tidak menggunakan global maka nilai yang sebelumnya akan muncul kembali
    global operator
    operator = ''
    kalkulatorfield.delete(0, END)


def hasil():  # Function untuk menghitung hasil dari kalkulator
    global operator
    hasil = str(eval(operator))
    kalkulatorfield.delete(0, END)
    kalkulatorfield.insert(END, hasil)
    operator = ''


kalkulatorfield = Entry(calculatorframe, font=(
    'Times New Roman', 16, 'bold'), width=32)
kalkulatorfield.grid(row=0, column=0, columnspan=10)


tombol1 = Button(calculatorframe, text='1', font=('Times New Roman', 15, 'bold'),
                 bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('1'))
tombol1.grid(row=1, column=0)

tombol2 = Button(calculatorframe, text='2', font=('Times New Roman', 15, 'bold'),
                 bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('2'))
tombol2.grid(row=1, column=1)

tombol3 = Button(calculatorframe, text='3', font=('Times New Roman', 15, 'bold'),
                 bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('3'))
tombol3.grid(row=1, column=2)

tombolplus = Button(calculatorframe, text='+', font=('Times New Roman', 15, 'bold'),
                    bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('+'))
tombolplus.grid(row=1, column=3)

tombol6 = Button(calculatorframe, text='6', font=('Times New Roman', 15, 'bold'),
                 bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('6'))
tombol6.grid(row=2, column=0)

tombol5 = Button(calculatorframe, text='5', font=('Times New Roman', 15, 'bold'),
                 bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('5'))
tombol5.grid(row=2, column=1)

tombol4 = Button(calculatorframe, text='4', font=('Times New Roman', 15, 'bold'),
                 bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('4'))
tombol4.grid(row=2, column=2)

tombolminus = Button(calculatorframe, text='-', font=('Times New Roman', 15, 'bold'),
                     bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('-'))
tombolminus.grid(row=2, column=3)

tombol7 = Button(calculatorframe, text='7', font=('Times New Roman', 15, 'bold'),
                 bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('7'))
tombol7.grid(row=3, column=0)

tombol8 = Button(calculatorframe, text='8', font=('Times New Roman', 15, 'bold'),
                 bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('8'))
tombol8.grid(row=3, column=1)

tombol9 = Button(calculatorframe, text='9', font=('Times New Roman', 15, 'bold'),
                 bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('9'))
tombol9.grid(row=3, column=2)

tombolkali = Button(calculatorframe, text='*', font=('Times New Roman', 15, 'bold'),
                    bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('*'))
tombolkali.grid(row=3, column=3)

tombolhasil = Button(calculatorframe, text='=', font=(
    'Times New Roman', 15, 'bold'), bg='orange', fg='white', bd=6, width=6, command=hasil)
tombolhasil.grid(row=4, column=0)

tombol0 = Button(calculatorframe, text='0', font=('Times New Roman', 15, 'bold'),
                 bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('0'))
tombol0.grid(row=4, column=1)

tombolclear = Button(calculatorframe, text='Clear', font=(
    'Times New Roman', 15, 'bold'), bg='orange', fg='white', bd=6, width=6, command=clear)
tombolclear.grid(row=4, column=2)

tombolbagi = Button(calculatorframe, text='/', font=('Times New Roman', 15, 'bold'),
                    bg='orange', fg='white', bd=6, width=6, command=lambda: tombolclick('/'))
tombolbagi.grid(row=4, column=3)

# ---------------------------------------------------------------------------------------------

mainloop()

