print("----------------- Program Kasir Sederhana WM Kiled -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmakan
   global porsi
   global makan
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Ayam goreng/bakar - Rp 15000")
   print("2. Lele goreng/bakar - Rp 9000")
   print("3. ayan ungkep - Rp 11000")
   nomor=int(input("Masukan Pilihan Angka Makanan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmakan=porsi*15000
       print (porsi," porsi Ayam goreng/bakar = Rp", totalmakan)
       makan=("Ayam goreng/bakar")
   elif nomor==2:
       totalmakan=porsi*9000
       print (porsi," porsi Lele goreng/bakar = Rp", totalmakan)
       makan=("Lele goreng/bakar")
   elif nomor==3:
       totalmakan=porsi*11000
       print (porsi, " porsi Ayam ungkep = Rp", totalmakan)
       makan=("Ayam ungkep")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalminum
   global minum
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh - Rp 2000")
   print("2. Es jeruk - Rp 3500")
   print("3. Good day - Rp 4000")
   nomor=int(input("Masukan Angka Pilihan Minuman: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalminum=gelas*2000
       print (gelas," Es Teh = Rp", totalminum)
       minum=(" Gelas Es Teh")
   elif nomor==2:
       totalminum=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", totalminum)
       minum=("Es Jeruk")
   elif nomor==3:
       totalminum=gelas*4000
       print (gelas, " Gelas Good day = Rp", totalminum)
       minum=("Good day")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmakan+totalminum

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,makan,"( Rp", totalmakan,")")
print ("\t\t ",gelas,minum,"( Rp", totalminum,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")