from tabulate import tabulate
def displaymenu(): # fungsi untuk menampilkan pilihan pada menu utama
    print('\n ----- SELAMAT DATANG DI APLIKASI DATA INDUK DAN NILAI SISWA -----'.center(60))
    print("""\n
        Navigasi menu aplikasi (1-4)
        1. Menampilkan data-data siswa
        2. Menambah data siswa baru
        3. Mengubah data-data siswa
        4. Menghapus data-data siswa
        5. Keluar dari aplikasi""")

def main():
    daftar_siswa = [
    {'id': '12a', 'nama_depan': 'Michael','nama_belakang':'Schumacher', 'kelas': 12, 'jenis_kelamin': 'L', 'tanggal_lahir': '05-03-2005'},
    {'id': '12b', 'nama_depan': 'Hayley','nama_belakang':'Williams', 'kelas': 12, 'jenis_kelamin': 'P', 'tanggal_lahir': '12-08-2004'},
    {'id': '12c', 'nama_depan': 'Ralf','nama_belakang':'Schumacher', 'kelas': 12, 'jenis_kelamin': 'L', 'tanggal_lahir': '22-11-2003'},
    {'id': '12d', 'nama_depan': 'Michael','nama_belakang':'Jordan', 'kelas': 12, 'jenis_kelamin': 'L', 'tanggal_lahir': '14-04-2005'},
    {'id': '12e', 'nama_depan': 'Jane','nama_belakang':'Foster', 'kelas': 12, 'jenis_kelamin': 'P', 'tanggal_lahir': '23-09-2005'},
    {'id': '12f', 'nama_depan': 'Susi','nama_belakang':'Susanti', 'kelas': 12, 'jenis_kelamin': 'P', 'tanggal_lahir': '30-07-2005'}
    ]
    # list daftar siswa berisi data induk siswa dengan id siswa sebagai primary key

    list_nilai = [
    {'id': '12a','wajib':{'Matematika':90,'Fisika':70},'pilihan':{'Geografi':75,'Kimia':80}}, 
    {'id': '12b','wajib':{'Matematika':86,'Fisika':90},'pilihan':{'Geografi':83,'Seni':97}},
    {'id': '12c','wajib':{'Matematika':67,'Fisika':70},'pilihan':{'English':80,'Olahraga':98}},
    {'id': '12d','wajib':{'Matematika':76,'Fisika':90},'pilihan':{'Seni':82,'Kimia':79}},
    {'id': '12e','wajib':{'Matematika':90,'Fisika':80},'pilihan':{'Elektro':97,'Olahraga':75}},  
    ] 
    # daftar nilai berisi nilai wajib dan pilihan dari masing-masing siswa dengan id siswa sebagai primary key
    
    while True:
        displaymenu()
        try:
            pilihan_user = int(input('Pilihan Menu: '))
            if pilihan_user == 1:
                read(daftar_siswa,list_nilai)
            elif pilihan_user == 2:
                create(daftar_siswa,list_nilai)
            elif pilihan_user == 3:
                update(daftar_siswa,list_nilai)
            elif pilihan_user == 4:
                delete(daftar_siswa,list_nilai)
            elif pilihan_user == 5:
                print('Terima kasih telah menggunakan aplikasi data siswa')
                break
            else:
                print('Pilihan tidak valid, silahkan coba lagi.')
        except ValueError:
            print('Input tidak valid, harap masukkan angka.')

def read(daftar_siswa,list_nilai): # Fungsi read
    while True:
        print('\n' + '---------------- MENU READ ----------------'.center(60))
        print("""
            Navigasi menu read (1-4)
            1. Menampilkan seluruh data induk siswa 
            2. Pencarian siswa 
            3. Menampilkan nilai siswa 
            4. Kembali ke Menu utama """)
        siswa_total = len(daftar_siswa) 
        nilai_masuk = len(list_nilai)
        try:
            pilihan_read = int(input('Pilihan anda: '))
            if pilihan_read == 1: # pilihan untuk menunjukkan seluruh data induk dari siswa
                if daftar_siswa:
                    print(tabulate(daftar_siswa, headers="keys", tablefmt="grid"))
                else:
                    print('Data siswa belum tersedia') # apa bila daftar siswa tidak ada maka akan memberikan pemberitahuan bahwa data belum tersedia

            elif pilihan_read == 2:
                if daftar_siswa: # pilihan untuk mencari siswa tertentu
                    print("""Pilih metode pencarian yang anda inginkan:
                        1. Berdasarkan ID 
                        2. Berdasarkan Nama""") # user dapat mencari siswa berdasarkan id ataupun namanya
                    try:
                        pilihan_pencarian_siswa = int(input('Metode pencarian yang digunakan adalah: '))
                        if pilihan_pencarian_siswa == 1: # pilihan 1 akan memanggil fungsi pencarian berdasarkan id
                            cari_id = input('Masukkan id siswa: ')
                            pencarian_siswa_id(cari_id,daftar_siswa)
                        elif pilihan_pencarian_siswa == 2: # pilihan 2 akan memanggil fungsi pencarian berdasarkan nama
                            nama_nama = input('Masukkan nama siswa yang ingin anda cari: ')
                            pencarian_siswa_nama(nama_nama,daftar_siswa)
                        else:
                            print('Tolong masukkan pilihan yang valid')
                    except ValueError:
                        print('Input tidak valid, harap masukkan angka')
                else:
                    print('Data siswa belum tersedia')
                

            elif pilihan_read == 3: # pilihan untuk memunculkan semua nilai siswa
                print(f'Jumlah seluruh siswa: {siswa_total}')
                print(f'Jumlah nilai yang sudah diinput: {nilai_masuk}')
                if list_nilai:
                    for siswa in daftar_siswa:
                        print('==========================================')
                        print(f'ID siswa: {siswa['id']}, Nama siswa: {siswa['nama_depan']} {siswa['nama_belakang']}')
                        print('==========================================')

                        nilai_siswa = {}
                        for nilai in list_nilai:
                            if nilai['id'] == siswa['id']:
                                nilai_siswa = nilai
                                break

                        if nilai_siswa:
                            print('Nilai Wajib')
                            print('---------------------------------------')
                            for matpel,hasil in nilai_siswa['wajib'].items():
                                print(f'Nilai mata pelajaran {matpel}: {hasil}')
                            print('---------------------------------------')
                            print('Nilai Pilihan')
                            print('---------------------------------------')
                            for matpel,hasil in nilai_siswa['pilihan'].items():
                                print(f'Nilai mata pelajaran {matpel}: {hasil}')
                        else:
                            print('Nilai untuk siswa ini belum tersedia')
                        print()
                else:
                    print('Data nilai belum tersedia')
                # Ini adalah kode untuk print hasil matpel sesuai dengan 'id' siswa

            elif pilihan_read == 4:
                break
            else:
                print('Tolong masukkan pilihan yang valid')
        except ValueError:
            print('Input tidak valid, harap masukkan angka')

def create(daftar_siswa,list_nilai): # Fungsi create
    while True:
        print('\n' + '---------------- MENU CREATE ----------------'.center(60))
        print("""
            Pilih menu update [0-3]
            1. Menambah siswa baru
            2. Memasukkan nilai siswa
            3. Kembali ke menu utama  """)
        try:
            pilihan_create = int(input('Pilihan anda: '))
            if pilihan_create == 1: # Pilihan untuk menambahkan siswa baru
                siswa_baru = {}
                id_baru = input('Masukkan ID siswa baru: ')
                id_terdaftar = False
                for cari_siswa in daftar_siswa:
                    if cari_siswa['id'] == id_baru:
                        print('\nID SISWA YANG ANDA MASUKKAN SUDAH TERDAFTAR, MOHON MASUKKAN ID LAIN')
                        id_terdaftar = True
                        break

                if not id_terdaftar: # Input siswa hanya dapat dilakukan apa bila id belum terdaftar sebelumnya
                    siswa_baru['id'] = id_baru
                    while True:
                        nama_depan_baru = input('Masukkan nama depan siswa baru yang ingin anda masukkan: ')
                        if nama_depan_baru.isalpha():
                            siswa_baru['nama_depan'] = nama_depan_baru
                            break
                        else:
                            print("Nama depan hanya boleh mengandung huruf. Silakan coba lagi.")
                    while True:
                        nama_belakang_baru = input('Masukkan nama belakang siswa baru yang ingin anda masukkan: ')
                        if nama_belakang_baru.isalpha():
                            siswa_baru['nama_belakang'] = nama_belakang_baru
                            break
                        else:
                            print("Nama belakang hanya boleh mengandung huruf. Silakan coba lagi.")
                    while True:
                        kelas_baru = input('Masukkan kelas dari siswa baru (11/12/13): ')
                        if kelas_baru in ['10', '11', '12']:
                            siswa_baru['kelas'] = kelas_baru
                            break
                        else:
                            print("Kelas harus diisi dengan 11, 12, atau 13. Silakan coba lagi.")
                    while True:
                        jk_baru = input('Masukkan jenis kelamin siswa baru (L/P): ')
                        if jk_baru.upper() in ['L', 'P']:
                            siswa_baru['jenis_kelamin'] = jk_baru.upper()
                            break
                        else:
                            print("Jenis kelamin harus 'L' atau 'P'. Silakan coba lagi.")
                    
                    tanggal_baru = input('Masukkan tanggal lahir dari siswa baru (format dd-mm-yyyy): ')
                    siswa_baru['tanggal_lahir'] = tanggal_baru
                    validasi_input = input(f'\nApakah anda yakin ingin memasukkan {nama_depan_baru} {nama_belakang_baru} dengan id {id_baru} pada data induk siswa? (YA/TIDAK): ')
                    if validasi_input.upper() == 'YA':
                        daftar_siswa.append(siswa_baru)  # Penambahan siswa baru ke data siswa
                        print('\nDAFTAR SISWA BERHASIL DISIMPAN')
                    else:
                        print('\nPENAMBAHAN DATA SISWA BARU DIBATALKAN')

            elif pilihan_create == 2: # Pilihan untuk menambah nilai siswa yang sudah terdaftar sebelumnya
                wajib_baru = {}
                pilihan_baru = {}
                new_id = input('Masukkan ID Siswa yang ingin ditambah nilai: ')
                siswa_ditemukan = False
                for cari_siswa in daftar_siswa:
                    if cari_siswa['id'] == new_id:
                        siswa_ditemukan = True # Siswa yang ingin ditambahkan nilainya harud terdaftar terlebih dahulu
                        print('\nDATA SISWA DITEMUKAN') 
                        nilai_exist = False

                        for cari_siswa_lagi in list_nilai:
                            if cari_siswa_lagi['id'] == new_id:
                                nilai_exist = True # Pengecekan apakah nilau sudah terinput sebelumnya 
                                print('\nNILAI SISWA SUDAH DIINPUT')
                                break

                        if not nilai_exist: # Nilai hanya bisa diinput apa bila siswa sudah terdaftar dan nilai belum diinput
                            try:
                                print('\nMasukkan nilai mata pelajaran wajib: ')  # Pengisian nilai wajib
                                while True:
                                    mat_baru = int(input('Masukkan nilai wajib matematika (0-100): '))
                                    if 0 <= mat_baru <= 100:
                                        wajib_baru['matematika'] = mat_baru
                                        break
                                    else:
                                        print("Nilai harus antara 0 dan 100. Silakan coba lagi.")

                                while True:
                                    fis_baru = int(input('Masukkan nilai wajib fisika (0-100): '))
                                    if 0 <= fis_baru <= 100:
                                        wajib_baru['fisika'] = fis_baru
                                        break
                                    else:
                                        print("Nilai harus antara 0 dan 100. Silakan coba lagi.")

                                print('\nMasukkan nilai mata pelajaran pilihan: ')
                                print('Mata pelajaran pilihan tersedia: ')
                                matpel_pilihan_tersedia = ['Geografi', 'Kimia', 'Seni', 'English', 'Olahraga', 'Elektro']
                                print(matpel_pilihan_tersedia)

                                while True:
                                    pilihan1 = input('Mata pelajaran pilihan 1 adalah: ')
                                    if pilihan1 in matpel_pilihan_tersedia:
                                        while True:
                                            nilai_pilihan1 = int(input(f'Masukkan nilai untuk mata pelajaran {pilihan1} (0-100): '))
                                            if 0 <= nilai_pilihan1 <= 100:
                                                pilihan_baru[pilihan1] = nilai_pilihan1
                                                break
                                            else:
                                                print("Nilai harus antara 0 dan 100. Silakan coba lagi.")
                                        break
                                    else:
                                        print('Pilihan mata pelajaran tidak tersedia, isi kembali')

                                matpel_pilihan_tersedia.remove(pilihan1)
                                print('Mata pelajaran pilihan tersedia: ')
                                print(matpel_pilihan_tersedia)

                                while True:
                                    pilihan2 = input('Mata pelajaran pilihan 2 adalah: ')
                                    if pilihan2 in matpel_pilihan_tersedia:
                                        while True:
                                            nilai_pilihan2 = int(input(f'Masukkan nilai untuk mata pelajaran {pilihan2} (0-100): '))
                                            if 0 <= nilai_pilihan2 <= 100:
                                                pilihan_baru[pilihan2] = nilai_pilihan2
                                                break
                                            else:
                                                print("Nilai harus antara 0 dan 100. Silakan coba lagi.")
                                        break
                                    else:
                                        print('Pilihan mata pelajaran tidak tersedia, isi kembali')

                                validasi_tambah_nilai = input('Apakah anda yakin menambahkan nilai? (YA/TIDAK): ')
                                if validasi_tambah_nilai.upper() == 'YA':
                                    nilai_baru = {
                                        'id': new_id,
                                        'wajib': wajib_baru,
                                        'pilihan': pilihan_baru
                                    }
                                    list_nilai.append(nilai_baru)  # Penyimpanan nilai ke list nilai
                                    print('\nDATA NILAI SISWA BERHASIL DISIMPAN')
                            except ValueError:
                                print('Input tidak valid, harap masukkan angka')
                        break  
                if not siswa_ditemukan:
                    print('\nID SISWA TIDAK DITEMUKAN')


            elif pilihan_create == 3:
                break
            else:
                print('Pilihan tidak valid, silahkan masukkan angka 1-5.')
        except ValueError:
            print('Input tidak valid, harap masukkan angka')

def update(daftar_siswa,list_nilai): # Fungsi update
    while True:
        print('\n' + '---------------- MENU UPDATE ----------------'.center(60))
        print("""
            Pilih menu update [0-4]
            1. Mengubah data siswa
            2. Mengubah nilai siswa
            3. Kembali ke menu utama  """)
        siswa_total = len(daftar_siswa) # Sebagai tracker berapa jumlah siswa dalam data induk siswa
        nilai_masuk = len(list_nilai) # Sebagai tracker berapa jumlah siswa yang nilainya sudah diinput
        print(f'Jumlah seluruh siswa: {siswa_total}')
        print(f'Jumlah nilai yang sudah diinput: {nilai_masuk}')

        try:
            pilihan_update = int(input('Pilihan anda: ')) # Pilihan untuk mengganti data induk siswa berdasarkan id
            if pilihan_update == 1:
                id_edit = input('Masukkan ID siswa yang ingin diubah data induknya: ')
                siswa_ditemukan = False
                for i in range(len(daftar_siswa)):
                    if daftar_siswa[i]['id'] == id_edit:
                            siswa_ditemukan = True
                            print('DATA SISWA DITEMUKAN')
                            print(daftar_siswa[i])
                            while True:
                                print("\nMenu Pengubahan Detail Siswa")
                                print("1. Ganti nama depan")
                                print("2. Ganti nama belakang")
                                print("3. Ganti kelas")
                                print("4. Ganti jenis kelamin")
                                print("5. Ganti tanggal lahir")
                                print("6. Selesai dan Kembali ke menu update")

                                pilihan_ubah = input('Masukkan pilihan (1-6): ')

                                if pilihan_ubah == '1':  # Update Nama Depan
                                    while True:
                                        nama_depan_update = input('Masukkan nama depan baru: ')
                                        if nama_depan_update.isalpha():
                                            break
                                        else:
                                            print("Nama depan hanya boleh mengandung huruf. Silakan coba lagi.")
                                    q1 = input(f'Apakah anda ingin mengganti nama depan menjadi {nama_depan_update}? (YA/TIDAK): ')
                                    if q1.upper() == 'YA':
                                        daftar_siswa[i]['nama_depan'] = nama_depan_update

                                elif pilihan_ubah == '2':  # Update Nama Belakang
                                    while True:
                                        nama_belakang_update = input('Masukkan nama belakang baru: ')
                                        if nama_belakang_update.isalpha():
                                            break
                                        else:
                                            print("Nama belakang hanya boleh mengandung huruf. Silakan coba lagi.")
                                    q2 = input(f'Apakah anda ingin mengganti nama belakang menjadi {nama_belakang_update}? (YA/TIDAK): ')
                                    if q2.upper() == 'YA':
                                        daftar_siswa[i]['nama_belakang'] = nama_belakang_update

                                elif pilihan_ubah == '3':  # Update Kelas
                                    while True:
                                        kelas_update = input('Masukkan kelas baru (11/12/13): ')
                                        if kelas_update in ['10', '11', '12']:
                                            break
                                        else:
                                            print("Kelas harus diisi dengan 11, 12, atau 13. Silakan coba lagi.")
                                    q3 = input(f'Apakah anda ingin mengganti kelas menjadi {kelas_update}? (YA/TIDAK): ')
                                    if q3.upper() == 'YA':
                                        daftar_siswa[i]['kelas'] = kelas_update

                                elif pilihan_ubah == '4':  # Update Jenis Kelamin
                                    while True:
                                        jk_update = input('Masukkan update jenis kelamin (L/P): ')
                                        if jk_update.upper() in ['L', 'P']:
                                            jk_update = jk_update.upper()
                                            break
                                        else:
                                            print("Jenis kelamin harus 'L' atau 'P'. Silakan coba lagi.")
                                    q4 = input(f'Apakah anda ingin mengganti jenis kelamin menjadi {jk_update}? (YA/TIDAK): ')
                                    if q4.upper() == 'YA':
                                        daftar_siswa[i]['jenis_kelamin'] = jk_update

                                elif pilihan_ubah == '5':  # Update Tanggal Lahir
                                    tgl_update = input('Masukkan update tanggal lahir (format dd-mm-yyyy): ')
                                    q5 = input(f'Apakah anda ingin mengganti tanggal lahir menjadi {tgl_update}? (YA/TIDAK): ')
                                    if q5.upper() == 'YA':
                                        daftar_siswa[i]['tanggal_lahir'] = tgl_update

                                elif pilihan_ubah == '6':  # Selesai dan Kembali ke Update
                                    print(f'Data untuk siswa dengan ID {daftar_siswa[i]["id"]} berhasil diupdate')
                                    break

                                else:
                                    print('Pilihan tidak valid, silakan masukkan angka 1-6.')

                            break 
                if not siswa_ditemukan:
                        print('\nID SISWA TIDAK DITEMUKAN')

            elif pilihan_update == 2: # Pilihan untuk mengganti nilai siswa
                id_edit = input('Masukkan ID siswa yang ingin diubah list nilainya: ')
                siswa_ditemukan = False
                for i in range(len(list_nilai)):
                    if list_nilai [i]['id'] == id_edit:
                        siswa_ditemukan = True
                        print('\nDATA SISWA DITEMUKAN')

                        while True:
                            print("\nMenu Pengubahan Nilai")
                            print("1. Ganti nilai wajib")
                            print("2. Ganti nilai pilihan")
                            print("3. Selesai dan kembali ke menu update")
                            
                            pilihan_ubah = input('Masukkan pilihan (1-3): ')

                            if pilihan_ubah == '1':  # Mengubah matpel wajib
                                q1a = input('Apakah anda ingin mengganti nilai Matematika? (YA/TIDAK): ')
                                if q1a.upper() == 'YA':
                                    while True:
                                        try:
                                            matematika_baru = int(input('Masukkan nilai update mata pelajaran matematika (0-100): '))
                                            if 0 <= matematika_baru <= 100:
                                                list_nilai[i]['wajib']['Matematika'] = matematika_baru
                                                break
                                            else:
                                                print("Nilai harus antara 0 dan 100. Silakan coba lagi.")
                                        except ValueError:
                                            print("Masukkan angka yang valid.")

                                q1b = input('Apakah anda ingin mengganti nilai Fisika? (YA/TIDAK): ')
                                if q1b.upper() == 'YA':
                                    while True:
                                        try:
                                            fisika_baru = int(input('Masukkan nilai update mata pelajaran fisika (0-100): '))
                                            if 0 <= fisika_baru <= 100:
                                                list_nilai[i]['wajib']['Fisika'] = fisika_baru
                                                break
                                            else:
                                                print("Nilai harus antara 0 dan 100. Silakan coba lagi.")
                                        except ValueError:
                                            print("Masukkan angka yang valid.")

                            elif pilihan_ubah == '2':  # Mengubah matpel pilihan
                                print(f'Siswa dengan id {list_nilai[i]["id"]} mengambil mata pelajaran pilihan:')
                                for matpel in list_nilai[i]['pilihan'].keys():
                                    print(f'Mata kuliah pilihan adalah {matpel}')
                                    q2a = input(f'Apakah anda ingin mengganti nilai untuk matpel pilihan {matpel}? (YA/TIDAK): ')
                                    if q2a.upper() == 'YA':
                                        while True:
                                            try:
                                                new_pilihan = int(input(f'Masukkan update nilai untuk matpel {matpel} (0-100): '))
                                                if 0 <= new_pilihan <= 100:
                                                    list_nilai[i]['pilihan'][matpel] = new_pilihan
                                                    break
                                                else:
                                                    print("Nilai harus antara 0 dan 100. Silakan coba lagi.")
                                            except ValueError:
                                                print("Masukkan angka yang valid.")

                            elif pilihan_ubah == '3':  # Kembali ke menu update
                                print(f'Data nilai untuk siswa dengan ID {id_edit} berhasil diupdate')
                                break

                            else:
                                print('Pilihan tidak valid, silakan masukkan angka 1-3.')

                        break 
                if not siswa_ditemukan:
                    print('\nNILAI YANG BELUM DIINPUT TIDAK BISA DIUBAH')

            elif pilihan_update == 3:
                break
            else:
                print('Pilihan tidak valid, silahkan masukkan angka 1-5.')
        except ValueError:
            print('Input tidak valid, harap masukkan angka')

def delete(daftar_siswa, list_nilai): # Fungsi delete
    while True:
        print('\n' + '---------------- MENU DELETE ----------------'.center(60))
        print("""
            Pilih menu update [0-4]
            1. Menghapus nilai siswa
            2. Menghapus daftar induk siswa
            3. Kembali ke menu utama  """)

        try:
            pilihan_delete = int(input('Pilihan anda: '))
            if pilihan_delete == 1: # Pilihan untuk menghapus nilai siswa berdasarkan id
                id_hapus = input('Masukkan ID siswa yang ingin dihapus data nilainya: ')
                siswa_ditemukan = False
                for i in range(len(list_nilai)):
                    if list_nilai[i]['id'] == id_hapus:
                        siswa_ditemukan = True
                        print('DATA SISWA DITEMUKAN')
                        validasi_del_nilai = input(f'Apakah anda yakin ingin menghapus nilai siswa dengan ID {id_hapus}? (YA/TIDAK ): ')
                        if validasi_del_nilai.upper() == 'YA':
                            del list_nilai[i]
                            print('Data berhasil dihapus')
                        break
                if not siswa_ditemukan:
                    print('\nID SISWA TIDAK DITEMUKAN')

            elif pilihan_delete == 2: # Pilihan untuk menghapus data induk
                id_hapus = input('Masukkan ID siswa yang ingin dihapus data induknya: ')
                siswa_ditemukan = False
                nilai_exist = False

                for i in range(len(daftar_siswa)):
                    if daftar_siswa[i]['id'] == id_hapus:
                        siswa_ditemukan = True
                        print('\nDATA SISWA INDUK DITEMUKAN')

                        for j in range(len(list_nilai)):
                            if list_nilai[j]['id'] == id_hapus:
                                nilai_exist = True
                                break

                        if nilai_exist: # Apabila nilai sudah diinput, penghapusan data induk akan juga menghapus nilai dari id
                            print('PERINGATAN: Menghapus data induk akan juga menghapus nilai siswa yang bersangkutan')
                            validasi_del_nilai = input(f'Apakah anda yakin ingin menghapus data induk siswa dengan id {id_hapus}? (YA/TIDAK): ')
                            if validasi_del_nilai.upper() == 'YA':
                                del daftar_siswa[i]
                                for j in range(len(list_nilai)):
                                    if list_nilai[j]['id'] == id_hapus:
                                        del list_nilai[j]
                                        break
                                print(f'Data induk dan nilai siswa dengan ID {id_hapus} berhasil dihapus')
                        else: # Apabila nilai belum diinput maka hanya akan menghapus data induk siswa
                            validasi_del_nilai = input(f'Apakah anda yakin ingin menghapus data induk siswa dengan id {id_hapus}? (YA/TIDAK): ')
                            if validasi_del_nilai.upper() == 'YA':
                                del daftar_siswa[i]
                                print(f'Data induk siswa dengan ID {id_hapus} berhasil dihapus, nilai belum diinput')
                        break 

                if not siswa_ditemukan:
                    print('\nID SISWA TIDAK DITEMUKAN')        

            elif pilihan_delete == 3:
                break
            else:
                print('Pilihan tidak valid, silahkan masukkan angka 1-3.')
        except ValueError:
            print('Input tidak valid, harap masukkan angka')

# Fungsi pencarian siswa berdasarkan id nya
def pencarian_siswa_id(cari_id,daftar_siswa):
    siswa_ditemukan = False
    for cari_siswa in daftar_siswa:
        if cari_siswa['id'] == cari_id:
            print(f'''
            Siswa dengan  ID {cari_siswa['id']} DITEMUKAN
            Nama: {cari_siswa['nama_depan']} {cari_siswa['nama_belakang']},
            Kelas: {cari_siswa['kelas']}, 
            Jenis kelamin: {cari_siswa['jenis_kelamin']}, 
            Tanggal Lahir: {cari_siswa['tanggal_lahir']}
            ''')
            siswa_ditemukan = True
            break
    if siswa_ditemukan == False:
        print('Siswa tidak ditemukan berdasarkan id yang anda masukkan')

# Fungsi pencarian siswa berdasarkan nama 
def pencarian_siswa_nama(nama_nama,daftar_siswa):
    siswa_ditemukan = False
    for cari_siswa in daftar_siswa:
        if cari_siswa['nama_depan'].capitalize() == nama_nama.capitalize() or cari_siswa['nama_belakang'].capitalize() == nama_nama.capitalize():
            print(f'''
            Siswa dengan nama {nama_nama} DITEMUKAN
            Nama depan: {cari_siswa['nama_depan']} 
            Nama belakang {cari_siswa['nama_belakang']}
            ID {cari_siswa['id']}
            Kelas: {cari_siswa['kelas']}
            Jenis kelamin: {cari_siswa['jenis_kelamin']}
            Tanggal Lahir: {cari_siswa['tanggal_lahir']}
            ''')
            siswa_ditemukan = True
    if siswa_ditemukan == False:
        print('Siswa tidak ditemukan berdasarkan nama yang anda masukkan')


main() # Fungsi untuk memanggil menu utama


