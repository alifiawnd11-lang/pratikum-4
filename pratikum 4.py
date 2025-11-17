# Program Data Nilai Mahasiswa Sederhana

data_mahasiswa = []


def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung nilai akhir dengan bobot 20% Tugas, 35% UTS, 45% UAS."""
    # Bobot: Tugas (20%), UTS (35%), UAS (45%)
    nilai_akhir = (tugas * 0.20) + (uts * 0.35) + (uas * 0.45)
    return nilai_akhir


def input_data_mahasiswa():
    """Mengambil input data Nama, NIM, dan Nilai."""
    while True:
        # Tampilan Input


        nama = input("Nama : ")
        # Input NIM dan pastikan berupa angka
        while True:
            nim_input = input("NIM : ")
            if nim_input.isdigit():
                nim = nim_input
                break
            else:
                print("NIM harus berupa angka. Silakan coba lagi.")

        # Input Nilai Tugas
        while True:
            try:
                nilai_tugas = int(input("Nilai Tugas : "))
                break
            except ValueError:
                print("Nilai harus berupa angka. Silakan coba lagi.")

        # Input Nilai UTS
        while True:
            try:
                nilai_uts = int(input("Nilai UTS : "))
                break
            except ValueError:
                print("Nilai harus berupa angka. Silakan coba lagi.")

        # Input Nilai UAS
        while True:
            try:
                nilai_uas = int(input("Nilai UAS : "))
                break
            except ValueError:
                print("Nilai harus berupa angka. Silakan coba lagi.")

        # Hitung Nilai Akhir
        nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

        # Simpan data ke dalam list
        data_mahasiswa.append({
            'nama': nama,
            'nim': nim,
            'tugas': nilai_tugas,
            'uts': nilai_uts,
            'uas': nilai_uas,
            'akhir': round(nilai_akhir, 2)  # Bulatkan 2 angka di belakang koma
        })

        # Konfirmasi untuk tambah data
        tambah_lagi = input("Tambah data(y/t)?").lower()
        if tambah_lagi != 'y':
            break


def tampilkan_tabel_hasil():
    """Menampilkan data yang sudah diinput dalam format tabel."""

    # Header Tabel
    print("\n| No |Nama\t\t\t        |NIM\t\t   |Tugas  | UTS |  UAS | Akhir |")
    print("======================================================================")

    # Isi Tabel
    if not data_mahasiswa:
        print("| Tidak ada data.                                                     |")
    else:
        for i, data in enumerate(data_mahasiswa, 1):
            # Format output agar rata dan rapi
            print(
                f"| {i:<2} | {data['nama']:<20} | {data['nim']:<12} | {data['tugas']:<5} | {data['uts']:<3} | {data['uas']:<3} | {data['akhir']:<5} |")

    # Penutup Tabel
    print("=======================================================================")


# --- Eksekusi Program ---

print("Tampilan Program")
input_data_mahasiswa()
tampilkan_tabel_hasil()