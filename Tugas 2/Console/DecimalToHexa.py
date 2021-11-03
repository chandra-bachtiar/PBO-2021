## Chandra Bachtiar
## 200511151

print("===== Program Konvert Decimal ke Hexadecimal =====")
decimal = int(input("Masukan Angka Decimal : "))
hexa = str(hex(decimal)).replace('0x','').upper()
print("Hasil Konvert dari decimal ",decimal," adalah ",hexa)
print("===== Program Selesai =====")