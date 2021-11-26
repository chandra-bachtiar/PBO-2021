#Chandra Bachtiar
#200511151
#K1 Teknik Informatika

#masukan module csv
import csv

#program
print("======================================")
print('===== Lihat Data Kendaraaan Baru =====')
print("======================================")

listKendaraan = []
with open('kendaraan.csv','r') as kendaraan:
    baca = csv.reader(kendaraan, delimiter=",")
    for x in baca:
        listKendaraan.append(x)

if(len(listKendaraan) > 0):
    print("JENIS,NOPOL,WARNA,TAHUN")
    for x in listKendaraan:
        print(f'{x[0]},{x[1]},{x[2]},{x[3]}')
    
print("======================================")
print('========== Program Selesai ===========')
print("======================================")

