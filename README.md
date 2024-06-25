# Capstone Project Modul 1: Student Information Sistem (Sistem Informasi Siswa)
## Overview
Project pada modul 1 ini mengimplementasikan konsep-konsep dasar dalam Python seperti *variable*, *looping*, *collection data types* dan *function* untuk membuat sebuah aplikasi manajemen sistem informasi data siswa. Aplikasi ini dirancang untuk memudahkan pengelolaan data induk dan nilai siswa, termasuk fungsi-fungsi untuk menambahkan data baru, mengubah data yang sudah ada, dan menghapus data yang tidak relevan.

## Data Description
Terdapat dua data yang menjadi struktur utama dari aplikasi ini antara lain adalalah daftar siswa dan list nilai.
### Struktur Data Daftar SIswa
|No|Nama Kolom|Tipe Data|Constraint|Keterangan|
| ------ | ------ | ------ | ------ | ------ |
|1|id|`str`|-|ID siswa sebagai primary key|
|2|nama_depan|`str`|alphabet| nama depan siswa|
|3|nama_belakang|`str`|alphabet| nama belakang siswa|
|4|kelas|`str`|(10-12)| kelas siswa|
|5|jenis_kelamin|`str`|(j/k)|jenis kelamin siswa|
|6|tanggal_lahir|`str`| -| tanggal lahir siswa|

### Struktur Data List Nilai
| No | Nama Kolom | Tipe Data | Constraints | Description |
|----|-------|------|-------------|-------------|
| 1  | id    | `str`| -           | ID siswa sebagai primary key |
| 2  | wajib | `dict` | `int` (0-100)       | Dictionary untuk nilai mata pelajaran wajib |
|    |       |       |            |   Matematika dan Fisika|
| 3  | pilihan | `dict` | `int` (0-100)     | Dictionary untuk nilai mata pelajaran pilihan |
|    |       |       |            |   Geografi, Kimia, Seni, English, Olahraga, Elektro|

## Fitur Utama
### Read
Fungsi read memungkinkan untuk memunculkan seluruh data induk dan data nilai dari seluruh siswa, serta mencari siswa tertentu.
1. Menampilkan seluruh data induk siswa
2. Pencarian data induk siswa
    + Berdasarkan ID
    + Berdasarkan Nama
3. Menampilkan seluruh data nilai siswa

### Create
Fungsi read berfungsi untuk menambah siswa dengan primary key baru yang belum terdaftar sebelumnya. Siswa yang sudah memiliki id dapat ditambah nilainya.
1. Menambah siswa baru
2. Memasukkan nilai siswa

### Update
Data induk dan nilai yang sudah diinput sebelumnya dapat diubah dengan menggunakan fitur update yang disediakan. Hal ini memungkinkan user untuk mengubah data induk ataupun nilai yang mengalami perubahan atau kesalahan inputan
1. Mengubah data siswa
2. Mengubah nilai siswa

### Delete
Fungsi delete berfungsi untuk menghapus data yang sudah tidak relevan lagi berdasarkan id siswa yang diinput. Penghapusan data induk akan sekaligus menghapus nilai dari siswa tersebut apabila sudah diinput. Penghapusan nilai tidak akan mempengaruhi data induk dari siswa tersebut.
1. Menghapus nilai siswa
2. Menghapus data induk dan nilai siswa

### Keterbatasan
Beberapa keterbatasan dari program ini sebagai acuan untuk pengembangan berikutnya antara lain
1. Belum dapat mengurutkan data baik berdasarkan id ataupun nama
2. Format tanggal lahir belum dibuat constraint pada inputannya
