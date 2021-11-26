#Chandra Bachtiar
#200511151
#K1 Teknik Informatika

#masukan module csv
import csv

#program
print("======================================")
print('===== Entry Data Kendaraaan Baru =====')
print("======================================")

with open('kendaraan.csv','a+',newline='') as kendaraan:
    tulis = csv.writer(kendaraan)
    akhir = 0
    while(akhir == 0):
        #input user
        jenis = input("Masukan Jenis Mobil : ")
        nopol = input("Masukan Nomor Polisi Mobil : ")
        warna = input("Masukan Warna Mobil : ")
        tahun = input("Masukan Tahun Pembuatan Mobil : ")
        #Write ke file
        tulis.writerow([jenis,nopol,warna,tahun])
        print("\n==> Data Disimpan <==")
        lanjut = 0
        ket = ''
        while(lanjut == 0):
            ket = input("\nMasukan Data Lagi (y/n) ? ")
            if(ket == 'y' or ket == 'n'):
                if(ket == 'y'):
                    lanjut = 1
                    akhir = 0
                else:
                    lanjut = 1
                    akhir = 1
            else:
                print("Input tidak dikenal")
                lanjut = 0
print("======================================")
print('========== Program Selesai ===========')
print("======================================")

