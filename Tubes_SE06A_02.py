import time 
# PROYEK APLIKASI PEMESANAN TIKET KONSER AREA PURWOKERTO

def pilih_login():
    print("\n========== SELAMAT DATANG DI PurwoVibe ==========")
    print("Pilih opsi berikut!")
    print("1. Admin")
    print("2. User")
    print("3. Keluar")
    while True: 
        pilihan = (input("\nMasukkan Pilihan Anda : "))

        if pilihan == "1":
            login_admin()
            break
        elif pilihan == "2":
            pilih_item()
            break
        elif pilihan == "3":
            print("Terimakasih Telah Memakai Aplikasi ini!")
            break
        else:
            print("Pilihan yang Anda pilih tidak ada")
            continue

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
            print("Login tidak dapat diteruskan, Anda akan dikembalikan!")
            time.sleep(5)
            pilih_login()
            break
        else:
            print("Username dan Password yang Anda input ada yang salah, coba lagi!")
            login += 1

def pilih_item():
    print("\n========== SELAMAT DATANG DI PurwoVibe ==========")
    print("Pilih opsi berikut!")
    print("1. Lihat tiket")
    print("2. Pesan tiket")
    print("3. Lihat pesanan")
    print("4. Hapus pesanan")
    print("5. Pembayaran")
    print("6. Keluar")
    while True:
        pilih = (input("\nMasukkan Pilihan Anda : "))
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
            hapus_pesanan(pesanan)
            break
        elif pilih == "5":
            while True:
                nama = input("Masukkan nama Anda: ")
                if nama in [data['nama'] for data in pesanan]: 
                    pembayaran(nama, pesanan)
                    break
                elif nama not in [data['nama'] for data in pesanan]:
                    print("Nama tidak ditemukan dalam pesanan.")
                    pilih_item()
                    break
            break
        elif pilih == "6":
            keluar()
            break
        else:
            print("\nPilihan Anda Tidak Valid!")
            continue

def pilihan_admin():
    print("\n========== HALLO ADMIN! SELAMAT DATANG DI PurwoVibe ==========")
    print("Pilih opsi berikut!")
    print("1. Lihat tiket")
    print("2. Lihat tiket yang terjual")
    print("3. Tambah tiket")
    print("4. Hapus tiket")
    print("5. Keluar")
    pilih = (input("\nMasukkan Pilihan Anda : "))
    while True:
        if pilih == "1":
            tampil_tiket_a(tiket)
            break
        elif pilih == "2":
            tiket_terjual()
            break
        elif pilih == "3":
            tambah_tiket()
            break
        elif pilih == "4":
            hapus_tiket(tiket)
            break
        elif pilih == "5":
            keluar_admin()
            break
        else:
            print("\nPilihan Anda Tidak Valid!")
            return pilihan_admin()

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

#Tiket Terjual Admin
def tiket_terjual():
    if len(pesanan) == 0:
        print("Tiket belom ada yang terjual")
        pilihan_admin()
    else:
        print("Tiket yang terjual: ")
        for data in pesanan:
            nomor_tiket = data['nomor_tiket']
            jumlah_tiket = data['jumlah_tiket']
            print(f"Nomor tiket: {nomor_tiket}")
            print(f"Jumlah tiket: {jumlah_tiket}")
        pilihan_admin()

#Tambah Tiket Admin
def tambah_tiket():
    while True:
        nomor_tiket = input("Masukkan nomor tiket: ")
        if nomor_tiket.upper() in tiket:
            print("Nomor tiket sudah terpakai!")
            continue
        else:
            break
    nama_konser = input("Masukkan nama konser: ")
    lokasi = input("Masukkan lokasi konser: ")
    tanggal = input("Masukkan tanggal konser: ")
    while True:
        harga = input("Masukkan harga tiket: ")
        if harga.isdigit():
            harga = int(harga)
            break
        else:
            print("Harga tiket haruslah berupa angka!")
            continue
    while True:
        jumlah = input("Masukkan jumlah tiket tersedia: ")
        if jumlah.isdigit():
            jumlah = int(jumlah)
            break
        else:
            print("Jumlah tiket haruslah berupa angka!")
            continue
    tiket[nomor_tiket] = {
        'nama_konser': nama_konser,
        'lokasi': lokasi,
        'tanggal': tanggal,
        'harga': harga,
        'jumlah': jumlah
    }
    print("Tiket berhasil ditambahkan!")
    tampil_tiket_a(tiket)

#Hapus Tiket admin
def hapus_tiket(tiket):
    while True:
        nomor_tiket = input("Masukkan Nomor Tiket: ")
        if nomor_tiket in tiket:
            del tiket[nomor_tiket]
            print(f"Tiket dengan Nomor {nomor_tiket} telah dihapus")
            pilihan_admin()
            break
        else:
            print(f"Tiket dengan Nomor {nomor_tiket} tidak ditemukan")
            while True:
                pilih = input("Apakah anda ingin mengulangnya?(iya/tidak): ")
                if pilih == "iya" or pilih == "tidak":
                    break
                else:
                    print("Pilihan anda tidak valid!")
                    continue
            if pilih == "iya":
                continue
            elif pilih == "tidak":
                pilihan_admin()
                break

#Admin
def keluar_admin():
    while True:
        while True:
            terus = input("\nApakah Anda yakin ingin keluar? (iya/tidak) = ")
            if terus == "iya" or terus == "tidak":
                break
            else:
                print("Pilihan Anda Tidak Valid!")
        if terus == "iya":
            print("Sampai jumpa dan Terima kasih!")
            pilih_login()
            break
        elif terus == "tidak":
            pilihan_admin()
            break

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

#User
def pesan_tiket(tiket):
    while True:
        nomor_tiket = input("\nMasukkan nomor tiket yang ingin dipesan: ")
        if nomor_tiket.upper() in tiket:
            if tiket[nomor_tiket.upper()]['jumlah'] > 0:
                while True:
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
                        pembayaran(nama, pesanan)
                        return data_pemesanan
                    else:
                        print("Maaf, jumlah tiket yang diminta tidak tersedia.")
                        while True:
                            pilih2 = input("Apakah anda ingin memesan dengan jumlah lain?(iya/tidak): ")
                            if pilih2 == "iya" or pilih2 == "tidak":
                                break
                            else:
                                print("Pilihan anda tidak valid!")
                                continue
                        if pilih2 == "tidak":
                            pilih_item()
                            break
                        elif pilih2 == "iya":
                            continue
            else:
                print("Maaf, tiket yang Anda pilih telah habis. Silakan pilih nomor tiket lain.")
                continue
        else:
            print("Nomor tiket tidak valid. Silakan coba lagi.")
            while True:
                pilih1 = input("Apakah anda ingin memasukkan nomor tiket lagi?(iya/tidak): ")
                if pilih1 == "iya" or pilih1 == 'tidak':
                    break
                else:
                    print("Pilihan anda tidak valid!")
                    continue
            if pilih1 == "iya":
                continue
            elif pilih1 == "tidak":
                pilih_item()
                break

        return None

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
                print(f"Nomor Tiket: {nomor_tiket}")
                print(f"Jumlah Tiket: {jumlah_tiket}")
                print(f"Harga Tiket: {harga_tiket}")
                print("----------------------------")

        if pesanan_ditemukan:
            print("Total Harga:", total_harga)
            pilih_item()
            break
        else:
            pilihan = input("Pesanan tidak ditemukan. Apakah Anda ingin mencoba lagi? (iya/tidak): ")
            while True:
                if pilihan.lower() == 'iya' or pilihan.lower() == 'tidak':
                    break
                else:
                    print("Pilihan anda tidak valid!")
                    continue
            if pilihan.lower() == 'iya':
                continue
            elif pilihan.lower() == 'tidak':
                pilih_item()
                break

#Hapus User
def hapus_pesanan(pesanan):
    if len(pesanan) == 0:
        print("\nBelum ada pesanan!")
        pilih_item()
    nama = input("Masukkan nama Anda: ")
    pesanan_ditemukan = False
    for i in range(len(pesanan)):
        if pesanan[i]['nama'].lower() == nama.lower():
            print(f"List pesanan atas nama {nama}: ")
            for data in pesanan:
                nomor_tiket = data['nomor_tiket']
                jumlah_tiket = data['jumlah_tiket']
                print(f"Nomor tiket: {nomor_tiket}")
                print(f"Jumlah: {jumlah_tiket}")
                print("===========================")
            no_tiket = input("Masukkan nomor tiket yang ingin anda hapus: ")
            if pesanan[i]['nomor_tiket'] == no_tiket:
                pesanan_ditemukan = True
                nomor_tiket = pesanan[i]['nomor_tiket']
                jumlah_tiket = pesanan[i]['jumlah_tiket']
                tiket[nomor_tiket]['jumlah'] += jumlah_tiket
                pesanan.pop(i)
                print(f"\nPesanan dengan nama '{nama}' dan nomor tiket '{no_tiket}' telah dihapus.")
                pilih_item()
                break
            if not pesanan_ditemukan:
                print(f"\nPesanan dengan nama '{nama}' dan nomor tiket '{no_tiket}' tidak ditemukan.")
                pilih_item()
        else:
            print(f"\nPesanan atas nama {nama} tidak ditemukan!")
            pilih_item()

#User
def pembayaran(nama, pesanan):
    total_harga = 0
    for data in pesanan:
        if data['nama'].lower() == nama.lower():
            nomor_tiket = data['nomor_tiket']
            jumlah_tiket = data['jumlah_tiket']
            harga_tiket = tiket[nomor_tiket]['harga']
            total_harga += harga_tiket * jumlah_tiket
            print(f"Nomor Tiket: {nomor_tiket}")
            print(f"Jumlah Tiket: {jumlah_tiket}")
            print(f"Harga Tiket: {harga_tiket}")
            print("----------------------------")
    print(f"\nTotal harga yang harus dibayar: {total_harga}")
    while True:
        pilihan = input("Apakah anda ingin melanjutkan pembayaran?(iya/tidak): ")
        if pilihan.lower() == "iya":
            print("----------------------------")
            print("Silahkan melakukan pembayaran melalui VA: 123xxxxxxx(Mandiri)")
            while True:
                pilih = input("Apakah anda ingin memesan tiket lagi?"
                        "\nJika tidak maka anda akan kembali!(iya/tidak): ")
                print("----------------------------")
                if pilih.lower() == "iya":
                    pesan_tiket(tiket)
                    break
                elif pilih.lower() == "tidak":
                    pilih_item()
                    break
                else:
                    print("Pilihan anda tidak valid! Silahkan coba lagi")
                    continue
            break
        elif pilihan.lower() == "tidak":
            print("Terima kasih, silahkan datang kembali!")
            pilih_item()
            break
        else:
            print("Pilihan anda tidak valid! Silahkan coba lagi")
            continue

#User
def keluar():
    while True:
        while True:
            terus = input("\nApakah Anda yakin ingin keluar? (iya/tidak) = ")
            if terus == "iya" or terus == "tidak":
                break
            else:
                print("Pilihan Anda Tidak Valid!")
        if terus == "iya":
            print("Sampai jumpa dan Terima kasih!")
            pilih_login()
            break
        elif terus == "tidak":
            pilih_item()
            break

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
pesanan = []
pilih_login()