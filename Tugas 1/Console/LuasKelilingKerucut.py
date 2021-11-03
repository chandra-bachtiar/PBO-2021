## Menampilkan luas dan Volume Kerucut
## Nama : Chandra Bachtiar
## NIM : 200511151
## Kelas : K1 Teknik Informatika
import math

print("====== Program Volume & Luas Kerucut ======")

# #Variabel yang di perlukan 
jari = int(input("Masukan Jari Jari alas (cm) : "))
pelukis = int(input("Masukan Panjang Garis Pelukis (cm) : "))

# #Proses Hitung
rs = jari + pelukis
luas = (22/7) * jari * rs

#cari tinggi kerucut rumus t2 = s2 - r2
tmpTinggi = pelukis**2 - jari**2
tinggi = math.sqrt(tmpTinggi)

#Hitung Volume
volume = (1/3) * ((22/7) * (jari**2) * tinggi)

print("Volume Kerucut : ",round(volume,1),"Cm3")
print("Luas Kerucut : ",round(luas,1),"Cm2")
print("====== Program Selesai ======")
