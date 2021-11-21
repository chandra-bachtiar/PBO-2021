#Nama : Chandra Bachtiar
#NIM : 200511151
#Kelas : K1 Teknik Infomatika

print("===== Program Data Mahasiswa PKL =====")

#deklarasi variabel
mahasiswa = []
jumlahData = int(input("Masukan Banyak data Mahasiswa : "))
print("======================================")

file = open("mahasiswaPKL.txt","a")

#indeks penambah
index = 0
while(index < jumlahData):
    print("Mahasiswa ke-",index+1)
    nama = input("Masukan Nama Mahasiswa : ")
    tmpt = input("Masukan Tempat PKL Mahasiswa : ")
    print("======================================")
    #masukan ke array mahasiswa
    mahasiswa.append((nama,tmpt))
    index += 1

for x in mahasiswa:
    file.writelines("\n|| " + x[0] + " => " + x[1] )

print("======= Berhasil Menambah Data =======")
print("======================================")


print("\n")
print("================ HASIL =================")
file.close()
fs = open("mahasiswaPKL.txt",'r')
print(fs.read())