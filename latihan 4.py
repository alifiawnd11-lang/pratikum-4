# 1. Buat sebuah list sebanyak 5 elemen dengan nilai bebas
A = [10, 20, 30, 40, 50]

# --- akses list ---
# tampilkan elemen ke 3
print("Elemen ke-3:", A[2])

# ambil nilai elemen ke 2 sampai elemen ke 4
print("Elemen 2 sampai 4:", A[1:4])

# ambil elemen terakhir
print("Elemen terakhir:", A[-1])

# --- ubah elemen list ---
# ubah elemen ke 4 dengan nilai lainnya
A[3] = 99
print("Ubah elemen ke-4:", A)

# ubah elemen ke 4 sampai dengan elemen terakhir
A[3:] = [77, 88]
print("Ubah elemen 4 sampai akhir:", A)

# --- tambah elemen list ---
# ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
B = A[:2]
print("List B:", B)

# tambah list B dengan nilai string
B.append("halo")
print("B tambah string:", B)

# tambah list B dengan 3 nilai
B.extend([100, 200, 300])
print("B tambah 3 nilai:", B)

# gabungkan list B dengan list A
gabung = B + A
print("Gabungan B dan A:", gabung)