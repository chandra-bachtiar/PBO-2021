LANJUT = True
print("====== PROGRAM MATA KULIAH =======")
nomor = 1
MATA_KULIAH = []


def addData():
    matkul = input(f"Masukan Nama Mata Kuliah ke-{nomor} : ")
    MATA_KULIAH.append(matkul)

def lanjut():
    x = 0
    goto = ''
    while(x == 0):
        goto = input('Tambah Mata Kuliah Lagi (y/n) ? ')
        if(goto == 'y' or goto == 'n'):
            x = 1
        else:
            x = 0
            print("Input tidak di kenal!")
    if(goto == 'y'):
        return True
    elif(goto == 'n'):
        tampil()
        return False

def tampil():
    print("="*20)
    print(f"Kamu Memiliki {nomor-1} Mata Kuliah : ")
    y = 1
    for X in MATA_KULIAH:
        print(f"[{y}]. {X}")
        y += 1
    

while(LANJUT == True):
    addData()
    nomor += 1
    LANJUT = lanjut()
