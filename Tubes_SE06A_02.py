# PROYEK APLIKASI PEMESANAN TIKET KONSER AREA PURWOKERTO

def pilih_item():
    print("===========SELAMAT DATANG DI CAHAYA TRANS==============")
    print("Pilih opsi berikut!")
    print("1. Lihat tiket")
    print("2. Pesan tiket")
    print("3. Riwayat pemesanan")
    print("4. Lihat pesanan")
    print("5. Keluar")

    pilih = (input("\nMasukkan Pilihan Anda : "))
    while True:
        if pilih == "1":
            tampil_tiket(tiket)
            break
        elif pilih == "2":
            print("\nHasil Perkalian : ")
        elif pilih == "3":
            print("\nHasil Pembagian : ")
        elif pilih == "4":
            print("\nHasil Pengurangan : ")
        elif pilih == "5":
            keluar()
            break
        else:
            print("\nPilihan anda Tidak Valid!")
            return pilih_item()

def tampil_tiket(tiket):
    print("Tiket yang tersedia:")
    for nomor, info in tiket.items():
        print("======================================")
        print(f"Nomor Tiket: {'TKT001'}")
        print(f"Tanggal Keberangkatan: {info['25 Juni 2023']}")
        print(f"Jam Keberangkatan: {info['19.00 WIB']}")
        print(f"Harga Tiket: {info['60000']}")
        print(f"Jenis Kelas: {info['Ekonomi']}")
        print(f"Jumlah Tiket Tersedia: {info['4']}")
        print("======================================")
        print("======================================")
        print(f"Nomor Tiket: {'TKT002'}")
        print(f"Tanggal Keberangkatan: {info['25 Juni 2023']}")
        print(f"Jam Keberangkatan: {info['22.15 WIB']}")
        print(f"Harga Tiket: {info['120000']}")
        print(f"Jenis Kelas: {info['Bisnis']}")
        print(f"Jumlah Tiket Tersedia: {info['5']}")
        print("======================================")
        print("======================================")
        print(f"Nomor Tiket: {'TKT003'}")
        print(f"Tanggal Keberangkatan: {info['26 Juni 2023']}")
        print(f"Jam Keberangkatan: {info['14.20 WIB']}")
        print(f"Harga Tiket: {info['150000']}")
        print(f"Jenis Kelas: {info['Eksekutif']}")
        print(f"Jumlah Tiket Tersedia: {info['3']}")
        print("======================================")
        print("======================================")
        print(f"Nomor Tiket: {'TKT004'}")
        print(f"Tanggal Keberangkatan: {info['26 Juni 2023']}")
        print(f"Jam Keberangkatan: {info['18.45 WIB']}")
        print(f"Harga Tiket: {info['95000']}")
        print(f"Jenis Kelas: {info['Bisnis']}")
        print(f"Jumlah Tiket Tersedia: {info['6']}")
        print("======================================")
        print("======================================")
        print(f"Nomor Tiket: {'TKT005'}")
        print(f"Tanggal Keberangkatan: {info['27 Juni 2023']}")
        print(f"Jam Keberangkatan: {info['10.00 WIB']}")
        print(f"Harga Tiket: {info['180000']}")
        print(f"Jenis Kelas: {info['Eksekutif']}")
        print(f"Jumlah Tiket Tersedia: {info['2']}")
        print("======================================")
        print("======================================")
        print(f"Nomor Tiket: {'TKT006'}")
        print(f"Tanggal Keberangkatan: {info['27 Juni 2023']}")
        print(f"Jam Keberangkatan: {info['16.00 WIB']}")
        print(f"Harga Tiket: {info['70000']}")
        print(f"Jenis Kelas: {info['Ekonomi']}")
        print(f"Jumlah Tiket Tersedia: {info['1']}")
        print("======================================")
        print("======================================")
        print(f"Nomor Tiket: {'TKT007'}")
        print(f"Tanggal Keberangkatan: {info['28 Juni 2023']}")
        print(f"Jam Keberangkatan: {info['20.55 WIB']}")
        print(f"Harga Tiket: {info['145000']}")
        print(f"Jenis Kelas: {info['Eksekutif']}")
        print(f"Jumlah Tiket Tersedia: {info['3']}")
        print("======================================")
        print("======================================")
        print(f"Nomor Tiket: {'TKT008'}")
        print(f"Tanggal Keberangkatan: {info['28 Juni 2023']}")
        print(f"Jam Keberangkatan: {info['23.00 WIB']}")
        print(f"Harga Tiket: {info['80000']}")
        print(f"Jenis Kelas: {info['Bisnis']}")
        print(f"Jumlah Tiket Tersedia: {info['5']}")
        print("======================================")

def pilih_tiket(tiket):
    nomor_tiket = input("Masukkan nomor tiket yang ingin dipesan: ")
    if nomor_tiket in tiket:
        return nomor_tiket
    else:
        print("Nomor tiket tidak valid. Silakan coba lagi.")
        return pilih_tiket(tiket)

def pesan_tiket(tiket):
    nomor_tiket = input("Masukkan nomor tiket yang ingin dipesan: ")
    if nomor_tiket in tiket:
        jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
        if jumlah_tiket <= tiket[nomor_tiket]['jumlah']:
            tiket[nomor_tiket]['jumlah'] -= jumlah_tiket
            data_pemesanan = {
                'nomor_tiket': nomor_tiket,
                'jumlah_tiket': jumlah_tiket
            }
            return data_pemesanan
        else:
            print("Maaf, jumlah tiket yang diminta tidak tersedia.")
    else:
        print("Nomor tiket tidak valid. Silakan coba lagi.")

    return None

# Contoh data tiket
tiket = {
    "TKT001": {
        "artis": "Artis A",
        "tanggal": "10 Juni 2023",
        "harga": 500000,
        "jumlah": 10
    },
    "TKT002": {
        "artis": "Artis B",
        "tanggal": "15 Juli 2023",
        "harga": 750000,
        "jumlah": 5
    },
    "TKT003": {
        "artis": "Artis C",
        "tanggal": "20 Agustus 2023",
        "harga": 1000000,
        "jumlah": 2
    }
}

pesanan = []

def keluar():
    while True:
        terus = input("\nApakah Anda ingin melanjutkan? (iya/tidak) = ")
        if terus == "iya" or terus == "tidak":
            break
        else:
            print("Pilihan Anda Tidak Valid!")
    if terus == "tidak":
        print("Sampai jumpa dan Terima kasih!")
