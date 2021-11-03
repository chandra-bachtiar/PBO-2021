## Menampilkan luas dan Volume Bola
## Nama : Chandra Bachtiar
## NIM : 200511151
## Kelas : K1 Teknik Informatika

print("====== Program Volume & Luas Bola ======")

# #Variabel yang di perlukan 
jari = int(input("Masukan Jari Jari (cm) : "))

#Proses Hitung Luas || rumus Luas = 4 x π x r2
luas = 4 * (22/7) * (jari**2)

#Proses Hitung Volume || rumus Volume = 4/3 x π x r3
volume = 4/3 * ((22/7) * (jari**3))

print("Volume Bola : ",round(volume,1),"Cm3")
print("Luas Bola : ",round(luas,1),"Cm2")
print("====== Program Selesai ======")
