nama = str(input("masukkan nama : "))
i = 0
j = 0

for i in nama:
    j = j + 1
    print(nama[:j])

for i in nama:
    j = j - 1
    print(nama[:j])