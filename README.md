# Praktikum-Post-Test-2
# Profil
Nama : Muhammad Aryaputra Wirawan\
NIM : 2309116027\
Kelas : A\
Tema : Toko Gitar
# Daftar Isi
- [Profil](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/edit/main/README.md#profil)
- [Daftar Isi](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/edit/main/README.md#daftar-isi)
- [Flowchart](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/edit/main/README.md#flowchart)
- [Output]()


# Flowchart

![Posttest2 drawio](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/f91ddd6c-e560-4d60-bfcf-bf6504eb404b)

Gambar di atas adalah flowchart dari program yang saya buat

# Output

## Menu Awal

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/fcf38e0d-2439-4216-86e9-b983d83b8b46)

Gambar di atas adalah menu awal dari program jika pertama kali dijalankan. Terdapat 3 menu yang dapat dipilih

### Penjelasan Menu

**1. Admin**\
Jika angka 1 dipilih maka user akan masuk ke menu admin. Menu untuk role admin dapat melakukan CRUD (Create, Read, Update dan Delete).

**2. Pembeli**\
Jika angka 2 dipilih maka user akan masuk ke menu pembeli. Menu untuk role pembeli dapat melakukan menapilkan data barang yang dijual, membeli barang, melihat saldo dan isi saldo.

**3. Keluar**\
Jika angka 3 dipilih maka user akan keluar dari program.

**4. Angka Selain 1-3**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/4cf1f06f-8d84-4d40-aa55-4a569b28f09f)

Jika angka yang dimasukkan selain 1, 2 dan 3 maka akan muncul pesan "Tidak ada menu untuk angka {angka yang dimasukkan}," sebagai contoh saya memasukkan angka 4.

## Menu Admin

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/f260072c-2aa8-4265-927f-de7fd09533b5)

Menu admin akan muncul jika angka 1 dipilih di menu awal.

### Penjelasan Menu

**1. Menambahkan Data**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/458ca232-0f4e-446c-9385-fb24bf4f3287)

Menambahkan data dapat dilakukan dengan cara memilih angka 1 di menu admin. Menu yang muncul pertama adalah masukkan nama barang. Disini dapat diisi nama barang yang ingin ditambahkan ke database sebagai contoh saya memasukkan PRS SE Angelus.

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/0f05f080-1192-4eb3-be13-f2e7e74a204f)

Menu kedua yang muncul adalah masukkan harga barang. Disini dapat diisi harga barang dari barang yang ingin ditambahkan sebagai contoh saya memasukkan Rp. 750.000.

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/92c7379d-d626-4596-975d-469c3dec9d82)

Lalu akan muncul pesan "Barang dengan nama {nama barang} dan dengan harga Rp {harga barang} berhasil di tambah!"

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/c127dffe-bdca-420e-a6f9-d72d1fe6757a)

Jika nama barang yang dimasukkan sudah ada di database maka akan muncul pesan "Barang tersebut sudah ada di database!."

**2. Membaca Data**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/8e1bac93-6c61-408e-8fdc-da73e98ebcdf)

Membaca data yang ada di databse dapat dilakukan dengan cara memilih angka 2 di menu admin.

**3. Mengubah Data**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/3a28aa11-3e92-4aad-a467-197a033f371e)

Mengubah data seperti harga dapat dilakukan dengan cara memilih angka 3 di menu admin. Menu yang muncul pertama adalah masukkan nama barang. Disini dapat diisi nama barang yang datanya ingin diubah sebagai contoh saya ingin mengubah harga Cort AD 810 OP.

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/bd462abe-a5fe-45fd-9469-359022e5122f)

Menu kedua yang muncul adalah masukkan harga barang. Disini dapat diisi dengan harga baru dari barang yang ingin diubah harganya sebagai contoh saya memasukkan Rp. 250.000

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/d17a83a6-4c9a-4f75-998a-03854d1e3458)

Lalu akan muncul pesan "Harga barang {nama barang} berhasil diubah."

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/d73aee5e-8da6-45a0-9c2f-2ea10448bb23)

Jika nama barang yang ingin diubah tidak ada di database maka akan muncul pesan "Barang tersebut tidak ada di database, ketik dengan benar!"

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/ae4a7a0a-3635-420d-a009-3b9385c9f4d0)

Jika harga barang yang ingin diubah minus maka akan muncul pesan "Harga barang tidak boleh minus!"

**4. Menghapus Data**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/3039d1c7-8fc7-4f88-9964-5526f829ad26)

Menghapus data dapat dilakukan dengan cara memilih angka 4 di menu admin. Menu yang muncul adalah masukkan nama barang. Disini dapat diisi nama barang yang ingin dihapus dari database sebagai contoh saya akan menghapus Cort AD 810 OP.

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/d7786b01-eb1c-4c5a-8f7e-dfc82fe29214)

Lalu akan muncul pesan "Barang {nama barang} berhasil dihapus."

**5. Keluar**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/df256c15-c47a-4ada-bc68-96e8314e7c7c)

Keluar dari menu admin dapat dilakukan dengan cara memilih angka 5. Program akan keluar dari menu admin dan akan kembali ke menu awal.


**6. Angka Selain 1-5**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/cfbfd942-1697-40b7-9c95-a7908b8f7862)

Jika angka yang dimasukkan selain angka 1 sampai 5 maka akan muncul pesan "Tidak ada menu untuk angka {angka yang dimasukkan}."

## Menu Pembeli

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/11a8a718-55a3-4aad-b9e8-c65920c61a50)


Menu pembeli akan muncul jika angka 2 dipilih di menu awal.

### Penjelasan Menu 

**1. Tampilkan Barang**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/c3e9f3e8-bed3-40c9-8eb9-814a1035f2aa)

Menampilkan barang yang dijual dapat dilakukan dengan cara memilih angka 1 di menu pembeli.

**2. Beli Barang**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/e4ac04c1-6465-4126-afbd-c34cc942c2b5)

Membeli barang dapat dilakukan dengan cara memilih angka 2 di menu pembeli. Menu yang muncul pertama adalah masukkan nama barang yang ingin dibeli nama barang harus ada di database sebagai contoh saya memasukkan PRS SE Angelus.

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/9a94fdba-ac6f-4d37-92ef-693096aafa06)

Menu kedua yang muncul adalah masukkan kuantitas barang. Disini dapat diisi dengan berapa banyak kuantitas dari barang yang ingin dibeli sebagai contoh saya isi 2.  

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/6cb19fc0-e6f8-4358-992d-5f074313b51a)

Jika berhasil maka akan ada pesan barang berhasil dibeli dan menampilkan sisa saldo.

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/41a95e63-d2df-4edd-957b-ddb9e9e31522)

Jika barang yang ingin dibeli tidak ada di database maka akan muncul pesan "Tidak ada barang dengan nama {nama barang}."

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/5988b097-946f-4129-8998-8f400c30dde7)

Jika total harga melebihi saldo maka akan muncul pesan "Saldo kurang, silahkan isi saldo dulu!"

**3. Saldo**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/235529cb-bfa7-4e16-96fa-93054fce730c)

Untuk masuk ke menu saldo dapat dilakukan dengan cara memilih angka 3 di menu pembeli. Di dalam menu ini terdapat 2 pilihan untuk menampilkan saldo dan mengisi saldo.

**a. Tampilkan Saldo**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/3aeb9267-a417-4dce-adb1-9850d3f8f35d)

Jika memilih angka 1 maka akan langsung muncul saldo yang pembeli miliki sekarang dan kembali ke menu pembeli.

**b. Isi Saldo**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/4b54cab7-283d-4a39-a9f9-22136aa0ec2b)

Jika memilih angka 2 maka akan langsung muncul masukkan nominal saldo sebagai contoh saya akan memasukkan Rp. 250.000.

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/3a763baf-823c-43aa-bfa1-0d0bd7365ad5)

Setelah itu akan muncul saldo setelah ditambah.

**4. Keluar**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/6ddde68c-e387-46d0-a732-ef7ed0c24c91)

Keluar dari menu admin dapat dilakukan dengan cara memilih angka 4. Program akan keluar dari menu pembeli dan akan kembali ke menu awal.

**5. Angka Selain 1-4**

![image](https://github.com/AryaWirawwn/Praktikum-Post-Test-2/assets/143393183/a8c2ece8-fbfe-4633-a5d1-41b77d1a0237)

Jika angka yang dimasukkan selain angka 1 sampai 4 maka akan muncul pesan "Tidak ada menu untuk angka {angka yang dimasukkan}."
