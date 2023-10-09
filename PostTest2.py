# Import

import os
os.system('cls')
from prettytable import PrettyTable

# Data

dtBarang = {
    'Cort AD 810 OP': 1912000,
    'Yamaha FS400C': 1490000,
    'Yamaha FS-100C': 1349000,
    'PRS SE A50E':14500000
}

tabel = PrettyTable()
def tampilkan_tabel():
    global tabel
    tabel.field_names = ['Nama', 'Harga']
    tabel.clear_rows()

    for nama, harga in dtBarang.items():
        tabel.add_row([nama, f'Rp {harga}'])
    
    print(tabel)

saldo = 25000

# Menu Untuk Admin
def menuAdmin():
    while True:
        print('+' + '-'* 22 + '+')
        print('| Selamat Datang Admin |')
        print('+' + '-'* 22 + '+')
        
        print('1. Menambahkan Data')
        global dtBarang
        print('2. Membaca Data')
        print('3. Mengubah Data')
        print('4. Menghapus Data')
        print('5. Keluar')
        
        menuAdmin = int(input('Pilih Menu (1/2/3/4/5): '))
        if menuAdmin == 1:
            namaBarang = input('Masukkan nama barang: ')
            if namaBarang in dtBarang:
                print('Barang tersebut sudah ada di database!')
            else:
                hargaBarang = int(input('Masukkan harga barang: '))
                if hargaBarang > 0:
                    dtBarang[namaBarang] = hargaBarang
                    print(f'Barang dengan nama {namaBarang} dan dengan harga Rp {hargaBarang} berhasil di tambah!')
                else:
                    print('Harga barang tidak boleh minus!')
        
        elif menuAdmin == 2:
            tampilkan_tabel()

        elif menuAdmin == 3:
            namaBarang = input('Masukkan nama barang: ')
            if namaBarang not in dtBarang:
                print('Barang tersebut tidak ada di database, ketik dengan benar!')
            else:
                hargaBarang = int(input('Masukkan harga barang: '))
                if hargaBarang > 0:
                    dtBarang.update({namaBarang: hargaBarang})
                    print(f'Harga barang {namaBarang} berhasil diubah') 
                else:
                    print('Harga barang tidak boleh minus!')

        elif menuAdmin == 4:
            namaBarang = input('Masukkan nama barang: ')
            dtBarang.pop(namaBarang)
            print(f'Barang {namaBarang} berhasil dihapus')

        elif menuAdmin == 5:
            print('Selamat tinggal, sampai jumpa lagi!')
            return True
        
        else:
            print(f'Tidak ada menu untuk angka {menuAdmin}')

# Menu Untuk User
def menuUser():
    global saldo
    while True:
        welcome = f'| Selamat Datang Pembeli |'
        print('+' + '-'* (len(welcome) - 2) + '+')
        print(welcome)
        print('+' + '-'* (len(welcome) - 2) + '+')
        
        print('1. Tampilkan Barang')
        print('2. Beli Barang')
        print('3. Saldo')
        print('4. Keluar')
        
        menuUser = int(input('Pilih Menu (1/2/3/4): '))
        if menuUser == 1:
            tampilkan_tabel()
        elif menuUser == 2:
            namaBarang = input('Masukkan Nama Barang: ')
            if namaBarang in dtBarang:
                kuantitas = int(input('Masukkan Kuantitas Barang: '))
                hargaBarang = dtBarang[namaBarang]
                totalHarga = kuantitas * hargaBarang
                if totalHarga <= saldo:
                    saldo -= totalHarga
                    print(f'Selamat barang {namaBarang} berhasil dibeli!')
                    print(f'Sisa saldo anda adalah {saldo}')
                else:
                    print('Saldo kurang, silahkan isi saldo dulu!')
            else:
                print(f'Tidak ada barang dengan nama {namaBarang}')
        elif menuUser == 3:
            print('+' + '-'*7 + '+')
            print('| Saldo |')
            print('+' + '-'*7 + '+')
            print('1. Tampilkan Saldo')
            print('2. Isi Saldo')
            menuSaldo = int(input('Pilih menu (1/2): '))
            if menuSaldo == 1:
                print(f'Saldo anda adalah Rp {saldo}')
            elif menuSaldo == 2:
                tambahSaldo = int(input('Masukkan Nominal Saldo: '))
                if tambahSaldo > 0:
                    saldo += tambahSaldo
                    print(f'Saldo anda sekarang adalah: Rp {saldo}')
                else:
                    print('Saldo tidak boleh minus!')
            else:
                print(f'Tidak ada menu untuk angka {menuSaldo}')
        elif menuUser == 4:
            print('Selamat tinggal, sampai jumpa lagi!')
            return True
        else:
            print(f'Tidak ada menu untuk angka {menuUser}')

# Pilih Menu
while True:
    print('+' + '-' *21 + '+')
    print('|    Selamat Datang   |')
    print('| Silahkan Pilih Role |')
    print('+' + '-' *21 + '+')
    print('1. Admin')
    print('2. Pembeli')
    print('3. Keluar')
    menuAwal = int(input('Masukkan menu yang ingin dipilih (1/2/3): '))
    if menuAwal == 1:
        menuAdmin()
    elif menuAwal == 2:
        menuUser()
    elif menuAwal == 3:
        print('Terima kasih atas kunjungan Anda')
        break
    else:
        print(f'Tidak ada menu untuk angka {menuAwal}')