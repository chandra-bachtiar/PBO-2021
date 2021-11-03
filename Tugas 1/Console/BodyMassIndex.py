## Body Mass Index 
## Nama : Chandra Bachtiar
## NIM : 200511151
## Kelas : K1 Teknik Informatika
print("====== Program Hitung Body Mass Index ======")

berat = int(input("Masukan Berat Badan (Kg) : "))
tinggi = int(input("Masukan Tinggi Badan (cm) : "))

#Hitung Body Mass Index dengan rumus Berat Badan / tinggi * tinggi
ideal = berat / ((tinggi/100) * (tinggi/100))

if ideal < 18.5 :
    print("Anda kekurangan berat badan.")
elif ideal >= 18.5 and ideal <= 24.9:
    print("Anda Normal (Ideal).")
elif ideal >= 25.0 and ideal <= 29.9:
    print("Anda Kelebihan berat badan.")
elif ideal >= 30:
    print("Kegemukan (Obesitas)")

print("====== Program Selesai ======")
