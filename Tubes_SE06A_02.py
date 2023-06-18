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
            tampil_tiket_1(tiket)
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
    print("========== SELAMAT DATANG DI PurwoVibe ==========")
    print("Pilih opsi berikut!")
    print("1. Lihat Tiket")
    print("2. Lihat Tiket yang terjual")
    print("3. Tambah Tiket")
    print("4. Hapus Tiket")
    print("5. Keluar")
    pilih = (input("\nMasukkan Pilihan Anda : "))
    while True:
        if pilih == "1":
            tampil_tiket_2(tiket)
            break
        elif pilih == "2":
            print("\nTiket Terjual Update ")
        elif pilih == "3":
            tambah_tiket(tiket)
            break
        elif pilih == "4":
            print("Hapus oMasih Update")
        elif pilih == "5":
            keluar_admin()
            break
        else:
            print("\nPilihan Anda Tidak Valid!")
            return pilihan_admin()

#tampil Tiket User
def tampil_tiket_1(tiket):
    print("Tiket yang tersedia:")
    for nomor, info in tiket.items():

        print(f"Nomor Tiket: {nomor['TKT001']}")
        print(f"Nama Artis: {info['Coldplay']}")
        print(f"Tanggal Konser: {info['15 November 2023']}")
        print(f"Harga Tiket: {info['']}")
        print(f"Jumlah Tiket Tersedia: {info['jumlah']}")
        print("======================================")
        
        print("======================================")
        print(f"Nomor Tiket: {'TKT001'}")
        print(f"Artis: {info['Artis A']}")
        print(f"Tanggal: {info['25 Juni 2023']}")
        print(f"Jam: {info['15.00 WIB']}")
        print(f"Harga Tiket: {info['100000']}")
        print(f"Jumlah Tiket Tersedia: {info['2']}")
        print("======================================")
        
        print("======================================")
        print(f"Nomor Tiket: {'TKT002'}")
        print(f"Artis: {info['Artis B']}")
        print(f"Tanggal: {info['25 Juni 2023']}")
        print(f"Jam: {info['19.00 WIB']}")
        print(f"Harga Tiket: {info['120000']}")
        print(f"Jumlah Tiket Tersedia: {info['5']}")
        print("======================================")
        
        print("======================================")
        print(f"Nomor Tiket: {'TKT003'}")
        print(f"Artis: {info['Artis C']}")
        print(f"Tanggal: {info['26 Juni 2023']}")
        print(f"Jam: {info['16.00 WIB']}")
        print(f"Harga Tiket: {info['120000']}")
        print(f"Jumlah Tiket Tersedia: {info['4']}")
        print("======================================")
        
        print("======================================")
        print(f"Nomor Tiket: {'TKT004'}")
        print(f"Artis: {info['Artis D']}")
        print(f"Tanggal: {info['26 Juni 2023']}")
        print(f"Jam: {info['20 .00 WIB']}")
        print(f"Harga Tiket: {info['150000']}")
        print(f"Jumlah Tiket Tersedia: {info['7']}")
        print("======================================")
        
        print("======================================")
        print(f"Nomor Tiket: {'TKT005'}")
        print(f"Artis: {info['Artis E']}")
        print(f"Tanggal: {info['27 Juni 2023']}")
        print(f"Jam: {info['19.00 WIB']}")
        print(f"Harga Tiket: {info['135000']}")
        print(f"Jumlah Tiket Tersedia: {info['5']}")
        print("======================================")
        
        print("======================================")
        print(f"Nomor Tiket: {'TKT006'}")
        print(f"Artis: {info['Artis F']}")
        print(f"Tanggal: {info['27 Juni 2023']}")
        print(f"Jam: {info['21.00 WIB']}")
        print(f"Harga Tiket: {info['100000']}")
        print(f"Jumlah Tiket Tersedia: {info['6']}")
        print("======================================")
        
        print("======================================")
        print(f"Nomor Tiket: {'TKT007'}")
        print(f"Artis: {info['Artis G']}")
        print(f"Tanggal: {info['28 Juni 2023']}")
        print(f"Jam: {info['15.00 WIB']}")
        print(f"Harga Tiket: {info['145000']}")
        print(f"Jumlah Tiket Tersedia: {info['8']}")
        print("======================================")
        
        print("======================================")
        print(f"Nomor Tiket: {'TKT008'}")
        print(f"Artis: {info['Artis H']}")
        print(f"Tanggal: {info['28 Juni 2023']}")
        print(f"Jam: {info['19.00 WIB']}")
        print(f"Harga Tiket: {info['90000']}")
        print(f"Jumlah Tiket Tersedia: {info['1']}")
        print("======================================")

        print(f"Nomor Tiket: {nomor}")
        print(f"Nama Konser: {info['nama_konser']}")
        print(f"Lokasi Konser: {info['lokasi']}")
        print(f"Tanggal Konser: {info['tanggal']}")
        print(f"Harga Tiket: {info['harga']}")
        print(f"Jumlah Tiket Tersedia: {info['jumlah']}")
        print("======================================")
    pilih_item()

#tampil Tiket Admin
def tampil_tiket_2(tiket):
    print("Tiket yang tersedia:")
    for nomor, info in tiket.items():
        print(f"Nomor Tiket: {nomor}")
        print(f"Nama Konser: {info['nama_konser']}")
        print(f"Lokasi Konser: {info['lokasi']}")
        print(f"Tanggal Konser: {info['tanggal']}")
        print(f"Harga Tiket: {info['harga']}")
        print(f"Jumlah Tiket Tersedia: {info['jumlah']}")
        print("======================================")
    pilihan_admin()
    
#Tambah Tiket Admin
daftar_tiket = []  # Definisikan daftar_tiket sebagai list kosong di luar fungsi
def tambah_tiket(nomor, nama_konser, lokasi, tanggal, harga, jumlah):
    tiket = {
        'Nomor Tiket': nomor,
        'Nama Konser': nama_konser,
        'Lokasi Konser': lokasi,
        'Tanggal Konser': tanggal,
        'Harga Tiket': harga,
        'Jumlah Tiket Tersedia': jumlah
    }
    daftar_tiket.append(tiket)
    print("Tiket berhasil ditambahkan!")



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
            pilih_item(tiket)
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