batas = int(input("Masukkan Pembatas : "))
dilarang = int(input("Masukkan Angka yang dilarang : "))

for i in range(batas):
    if i == dilarang:
        continue
    print(i, end="\t")