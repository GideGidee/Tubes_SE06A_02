import time 
# PROYEK APLIKASI PEMESANAN TIKET KONSER AREA PURWOKERTO

def pilih_login():
    print("===========SELAMAT DATANG DI KONSER==============")
    print("Pilih opsi berikut!")
    print("1. Admin")
    print("2. User")

    pilihan = (input("\nMasukkan Pilihan Anda : "))

    if pilihan == "1":
        login_admin()
    elif pilihan == "2":
        pilih_item()
    else:
        print("Pilihan yang anda pilih tidak")
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
            print("Username dan Password yang anda input ada yang salah, coba lagi!")
            time.sleep(5)
            pilih_login()
            break
        else:
            print("Login tidak dapat diteruskan, Anda akan dikembalikan!")
            login += 1

def pilih_item():
    print("===========SELAMAT DATANG DI ==============")
    print("Pilih opsi berikut!")
    print("1. Lihat tiket")
    print("2. Pesan tiket")
    print("3. Lihat pesanan")
    print("4. Pembayaran")
    print("5. Keluar")

    pilih = (input("\nMasukkan Pilihan Anda : "))
    while True:
        if pilih == "1":
            tampil_tiket(tiket)
            break
        elif pilih == "2":
            pesan_tiket(tiket)
            break
        elif pilih == "3":
            lihat_pesanan_nama(pesanan)
            break
        elif pilih == "4":
            print("\nHasil Pengurangan : ")
        elif pilih == "5":
            keluar()
            break
        else:
            print("\nPilihan anda Tidak Valid!")
            return pilih_item()

def pilihan_admin():
    print("===========SELAMAT DATANG DI ==============")
    print("Pilih opsi berikut!")
    print("1. Lihat tiket")
    print("2. Lihat pesanan")
    print("3. Tambah tiket")
    print("4. Hapus tiket")
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
            keluar()
            break
        else:
            print("\nPilihan anda Tidak Valid!")
            return pilihan_admin()

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

def tampil_tiket(tiket):
    print("Tiket yang tersedia:")
    for nomor, info in tiket.items():
        print("======================================")
        print(f"Nomor Tiket: {'PWT-BKS001'}")
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
                pesanan_tiket.append(data_pemesanan)  # Menambahkan data pesanan ke array pesanan_tiket
                print("Pemesanan tiket berhasil!")
                return data_pemesanan
            else:
                print("Maaf, jumlah tiket yang diminta tidak tersedia.")
        else:
            print("Maaf, tiket yang Anda pilih telah habis. Silakan pilih nomor tiket lain.")
    else:
        print("Nomor tiket tidak valid. Silakan coba lagi.")

    return None

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

pilih_login()