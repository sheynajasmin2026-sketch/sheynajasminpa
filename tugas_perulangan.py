jumlah = int(input("Jumlah mahasiswa (5-10): "))

if jumlah >= 5:
    if jumlah <= 10:
        total = 0
        for i in range(1, jumlah + 1):
            print("Masukkan nilai mahasiswa", i)
            nilai = int(input("Nilai: "))
            total = total + nilai
        print("Nilai rata-rata:", total / jumlah)
    else:
        print("Jumlah terlalu banyak, maksimal 10")
else:
    print("Jumlah terlalu sedikit, minimal 5")   