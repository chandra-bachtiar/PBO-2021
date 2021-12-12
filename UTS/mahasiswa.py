#Chandra Bachtiar
#200511151
#K1 Teknik Informatika

#masukan module csv
import csv

#program
print("======================================")
print('======== Entry Data Mahasiswa ========')
print("======================================")

with open('mahasiswa.csv','a+',newline='') as mahasiswa:
    tulis = csv.writer(mahasiswa,delimiter=";")
    akhir = 0
    jumlah = int(input("Masukan Jumlah data : "))
    index = 0
    while(index < jumlah):
        print("\nMasukan data ke-",index+1)
        #input user
        nim = input("Masukan NIM : ")
        nama = input("Masukan Nama Lengkap : ")
        email = input("Masukan Email : ")
        kelas = input("Masukan Kelas : ")
        #Write ke file
        tulis.writerow([nim,nama,email,kelas])
        index += 1
print("======================================")
print('========== Program Selesai ===========')
print("======================================")

