# PROYEK APLIKASI PEMESANAN TIKET KONSER AREA PURWOKERTO

def pilih_item():
    print("===========SELAMAT DATANG DI PURWOVIBE: PEMESANAN TIKET KONSER PURWOKERTO==============")
    print("Pilih opsi berikut!")
    print("1. Lihat tiket")
    print("2. Pesan tiket")
    print("3. Riwayat pemesanan")
    print("4. Lihat pesanan")
    print("5. Pembayaran")
    print("6. Keluar")

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
        elif pilih == "6":
            print()
        else:
            print("\nPilihan anda Tidak Valid!")
            return pilih_item()

def tampil_tiket(tiket):
    print("Tiket yang tersedia:")
    for nomor, info in tiket.items():
        print(f"Nomor Tiket: {nomor}")
        print(f"Nama Konser: {info['nama_konser']}")
        print(f"Lokasi Konser: {info['lokasi']}")
        print(f"Tanggal Konser: {info['tanggal']}")
        print(f"Harga Tiket: {info['harga']}")
        print(f"Jumlah Tiket Tersedia: {info['jumlah']}")
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
        "nama_konser": "Konser Tulus Manusia 2023",
        "lokasi": "Gor Satria Purwokerto",
        "tanggal": "2 Juli 2023",
        "harga": 500000,
        "jumlah": 10
    },
    "TKT002": {
        "nama_konser": "Purwokerto Fest 2023",
        "lokasi": "Taman Andhang Pangrenan",
        "tanggal": "15 Juli 2023",
        "harga": 750000,
        "jumlah": 5
    },
    "TKT003": {
        "nama_konser": "Yura Yunita Konser Tutur Batin",
        "lokasi": "Gor Satria Purwokerto",
        "harga": 1000000,
        "jumlah": 2,
        "tanggal": "20 Agustus 2023"
    }
}

def riwayat_pemesanan(pesanan):
    if len(pesanan) > 0:
        print("Data Pemesanan: ")
        for index, pemesanan in enumerate(pesanan, start=1):
             print(f"Nomor Pemesanan: {index}")
             print(f"Nomor Tiket: {pemesanan['nomor_tiket']}")
             print(f"Jumlah Tiket: {pemesanan['jumlah_tiket']}")
             print("=======================================")
    else:
        print("Belum ada data pemesanan.")

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


#test