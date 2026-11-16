jumlah = int(input("Masukkan jumlah mahasiswa: "))

lulus = 0
tidak_lulus = 0

for i in range(jumlah):
    print("\nData Mahasiswa ke-", i + 1)

    nama = input("Masukkan nama: ")
    nilai = int(input("Masukkan nilai: "))

    if nilai >= 85 and nilai <= 100:
        kategori = "A (Sangat Baik)"
        lulus += 1
    elif nilai >= 75:
        kategori = "B (Baik)"
        lulus += 1
    elif nilai >= 60:
        kategori = "C (Cukup)"
        lulus += 1
    elif nilai >= 0:
        kategori = "D (Tidak Lulus)"
        tidak_lulus += 1
    else:
        kategori = "Nilai tidak valid"

    print("Nama:", nama)
    print("Nilai:", nilai)
    print("Kategori:", kategori)

print("\n===== HASIL AKHIR =====")
print("Jumlah mahasiswa:", jumlah)
print("Jumlah mahasiswa lulus:", lulus)
print("Jumlah mahasiswa tidak lulus:", tidak_lulus)