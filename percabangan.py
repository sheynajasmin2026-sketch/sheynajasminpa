nama = input("Masukkan nama mahasiswa: ").capitalize()

if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    print("Nama mahasiswa tidak terdaftar!")
    exit()

print("Nama mahasiswa:", nama)
print("Target nilai:", target)

percobaan = 1
lulus = False

while percobaan <= 3 and lulus == False:
    nilai = int(input("Masukkan nilai ujian ke-" + str(percobaan) + ": "))

    if nilai >= target:
        lulus = True
        print(nama, "berhasil lulus!")
        print("Lulus pada percobaan ke-", percobaan)
    else:
        print("Nilai belum mencapai target!")
        percobaan += 1

if lulus == False:
    print(nama, "dinyatakan TIDAK LULUS.")
    print("Sudah melakukan 3 kali percobaan.")