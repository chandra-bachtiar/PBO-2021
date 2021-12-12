print('======== Program Loop Bintang ========\n')

bintang = int(input("Masukan Jumlah Maksimal Bintang : "))
index = 0
while(index < bintang):
    print('*'*(bintang-index))
    index += 1
index = 0
while(index < bintang):
    print('*'*(index+1))
    index += 1

print('======== Program Selesai ========\n')