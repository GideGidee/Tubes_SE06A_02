# PROYEK APLIKASI PEMESANAN TIKET KONSER AREA PURWOKERTO

def pilih_item():
    print("===========SELAMAT DATANG==============")
    print("Pilih opsi berikut!")
    print("1. Lihat tiket")
    print("2. Pesan tiket")
    print("3. Riwayat pemesanan")
    print("4. Lihat pesanan")
    print("5. Keluar")
    print("Selesai")

def tampil_tiket(tiket):
    print("Tiket yang tersedia:")
    for nomor, info in tiket.items():
        print(f"Nomor Tiket: {nomor}")
        print(f"Nama Artis: {info['artis']}")
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

# Contoh penggunaan
tampil_tiket(tiket)
nomor_tiket_terpilih = pilih_tiket(tiket)
print("Anda telah memilih tiket dengan nomor:", nomor_tiket_terpilih)
