import time 
# PROYEK APLIKASI PEMESANAN TIKET KONSER AREA PURWOKERTO

def pilih_login():
    print("========== SELAMAT DATANG DI PurwoVibe ==========")
    print("Pilih opsi berikut!")
    print("1. Admin")
    print("2. User")

    pilihan = (input("\nMasukkan Pilihan Anda : "))

    if pilihan == "1":
        login_admin()
    elif pilihan == "2":
        pilih_item()
    else:
        print("Pilihan yang Anda pilih tidak ada")
    return pilihan

def login_admin():
    login = 0
    while True:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        if username == "admin" and password == "kelompok2nihbos":
            print("Sugeng Rawuh", username, "!")
            pilihan_admin()
            break
        if login == 3:
            print("Username dan Password yang Anda input ada yang salah, coba lagi!")
            time.sleep(5)
            pilih_login()
            break
        else:
            print("Login tidak dapat diteruskan, Anda akan dikembalikan!")
            login += 1

def pilih_item():
    print("========== SELAMAT DATANG DI PurwoVibe ==========")
    print("Pilih opsi berikut!")
    print("1. Lihat tiket")
    print("2. Pesan tiket")
    print("3. Lihat pesanan")
    print("4. Pembayaran")
    print("5. Keluar")

    pilih = (input("\nMasukkan Pilihan Anda : "))
    while True:
        if pilih == "1":
            tampil_tiket_u(tiket)
            break
        elif pilih == "2":
            pesan_tiket(tiket)
            break
        elif pilih == "3":
            lihat_pesanan_nama(pesanan)
            break
        elif pilih == "4":
            print("\nPembayaran update")
        elif pilih == "5":
            keluar()
            break
        else:
            print("\nPilihan Anda Tidak Valid!")
            return pilih_item()

def pilihan_admin():
    print("\n========== SELAMAT DATANG DI PurwoVibe ==========")
    print("Pilih opsi berikut!")
    print("1. Lihat Tiket")
    print("2. Lihat Tiket yang terjual")
    print("3. Tambah Tiket")
    print("4. Hapus Tiket")
    print("5. Keluar")
    pilih = (input("\nMasukkan Pilihan Anda : "))
    while True:
        if pilih == "1":
            tampil_tiket_a(tiket)
            break
        elif pilih == "2":
            print("\nTiket Terjual Update ")
        elif pilih == "3":
            tambah_tiket()
            break
        elif pilih == "4":
            print("Hapus oMasih Update")
        elif pilih == "5":
            keluar_admin()
            break
        else:
            print("\nPilihan Anda Tidak Valid!")
            return pilihan_admin()

#Tambah Tiket Admin
def tambah_tiket():
    nomor_tiket = input("Masukkan nomor tiket baru: ")
    nama_konser = input("Masukkan nama konser: ")
    lokasi = input("Masukkan lokasi konser: ")
    tanggal = input("Masukkan tanggal konser: ")
    harga = int(input("Masukkan harga tiket: "))
    jumlah = int(input("Masukkan jumlah tiket tersedia: "))

    tiket[nomor_tiket] = {
        'nama_konser': nama_konser,
        'lokasi': lokasi,
        'tanggal': tanggal,
        'harga': harga,
        'jumlah': jumlah
    }
    print("Tiket berhasil ditambahkan!")
    tampil_tiket_a(tiket)

#tampil Tiket User
def tampil_tiket_u(tiket):
    print("Tiket yang tersedia:")
    for nomor, info in tiket.items():
        print(f"Nomor Tiket: {nomor}")
        print(f"Nama Konser: {info['nama_konser']}")
        print(f"Lokasi Konser: {info['lokasi']}")
        print(f"Tanggal Konser: {info['tanggal']}")
        print(f"Harga Tiket: {info['harga']}")
        print(f"Jumlah Tiket Tersedia: {info['jumlah']}")
        print("======================================")
    pilih_item()

#tampil Tiket Admin
def tampil_tiket_a(tiket):
    print("\nTiket yang tersedia:")
    for nomor, info in tiket.items():
        print(f"\nNomor Tiket: {nomor}")
        print(f"Nama Konser: {info['nama_konser']}")
        print(f"Lokasi Konser: {info['lokasi']}")
        print(f"Tanggal Konser: {info['tanggal']}")
        print(f"Harga Tiket: {info['harga']}")
        print(f"Jumlah Tiket Tersedia: {info['jumlah']}")
        print("======================================")
    pilihan_admin()

#User
def pesan_tiket(tiket):
    nomor_tiket = input("Masukkan nomor tiket yang ingin dipesan: ")
    if nomor_tiket.upper() in tiket:
        if tiket[nomor_tiket.upper()]['jumlah'] > 0:
            jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
            if jumlah_tiket <= tiket[nomor_tiket.upper()]['jumlah']:
                tiket[nomor_tiket.upper()]['jumlah'] -= jumlah_tiket
                nama = input("Masukkan nama Anda: ")
                data_pemesanan = {
                    'nomor_tiket': nomor_tiket.upper(),
                    'jumlah_tiket': jumlah_tiket,
                    'nama' : nama
                }
                pesanan.append(data_pemesanan)  # Menambahkan data pesanan ke array pesanan_tiket
                print("Pemesanan tiket berhasil!")
                pilih_item()
                return data_pemesanan
            else:
                print("Maaf, jumlah tiket yang diminta tidak tersedia.")
        else:
            print("Maaf, tiket yang Anda pilih telah habis. Silakan pilih nomor tiket lain.")
    else:
        print("Nomor tiket tidak valid. Silakan coba lagi.")

    return None

#Data tiket
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
        "jumlah": 20
    },
    "TKT003": {
        "nama_konser": "Yura Yunita Konser Tutur Batin",
        "lokasi": "Gor Satria Purwokerto",
        "harga": 1000000,
        "jumlah": 30,
        "tanggal": "20 Agustus 2023"
    }
}

#User
def lihat_pesanan_nama(pesanan):
    while True:
        nama = input("Masukkan nama untuk mencari pesanan: ")
        total_harga = 0
        pesanan_ditemukan = False

        print("Pesanan berdasarkan nama '", nama, "':")
        for data in pesanan:
            if data['nama'].lower() == nama.lower():
                pesanan_ditemukan = True
                nomor_tiket = data['nomor_tiket']
                jumlah_tiket = data['jumlah_tiket']
                harga_tiket = tiket[nomor_tiket]['harga']
                total_harga += harga_tiket * jumlah_tiket
                print("Nomor Tiket:", nomor_tiket)
                print("Jumlah Tiket:", jumlah_tiket)
                print("Harga Tiket:", harga_tiket)
                print("----------------------------")

        if pesanan_ditemukan:
            print("Total Harga:", total_harga)
            pilih_item()
            break
        else:
            pilihan = input("Pesanan tidak ditemukan. Apakah Anda ingin mencoba lagi? (iya/tidak): ")
            if pilihan.lower() != 'iya':
                pilih_item(tiket)
                break

#User
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

#User
def keluar():
    while True:
        terus = input("\nApakah Anda ingin melanjutkan? (iya/tidak) = ")
        if terus == "iya" or terus == "tidak":
            break
        else:
            print("Pilihan Anda Tidak Valid!")
    if terus == "tidak":
        print("Sampai jumpa dan Terima kasih!")
    elif terus == "iya":
        pilih_item()

#Admin
def keluar_admin():
    while True:
        terus = input("\nApakah Anda ingin melanjutkan? (iya/tidak) = ")
        if terus == "iya" or terus == "tidak":
            break
        else:
            print("Pilihan Anda Tidak Valid!")
    if terus == "tidak":
        print("Sampai jumpa dan Terima kasih!")
    elif terus == "iya":
        pilihan_admin()
pilih_login()