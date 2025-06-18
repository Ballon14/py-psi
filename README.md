# Student Grading System

Sistem penilaian mahasiswa sederhana yang memungkinkan input data mahasiswa, menghitung grade berdasarkan skor, dan menampilkan visualisasi dalam bentuk grafik batang.

## Fitur

-   ✅ Input data mahasiswa (Nama, NIM, Skor)
-   ✅ Validasi input data
-   ✅ Perhitungan grade otomatis (A, B, C, D, E)
-   ✅ Penentuan predikat berdasarkan skor
-   ✅ Tampilan statistik grade
-   ✅ Visualisasi grafik batang dengan matplotlib
-   ✅ Penanganan error dan exception

## Sistem Penilaian

| Rentang Skor | Grade | Predikat         |
| ------------ | ----- | ---------------- |
| 90-100       | A     | Summa Cum Laude  |
| 80-89        | B     | Sangat Memuaskan |
| 70-79        | C     | Memuaskan        |
| 60-69        | D     | Cukup            |
| 0-59         | E     | Kurang           |

## Requirements

### Python Version

-   Python 3.6 atau lebih baru

### Dependencies

-   `matplotlib` - untuk membuat grafik visualisasi

## Instalasi

### 1. Clone atau Download

```bash
# Clone repository (jika menggunakan git)
git clone <https://github.com/Ballon14/py-psi.git
cd py-psi

# Atau download file main.py secara langsung
```

### 2. Install Python

Pastikan Python 3.6+ sudah terinstall di sistem Anda:

```bash
python --version
# atau
python3 --version
```

Jika belum terinstall, download dari [python.org](https://www.python.org/downloads/)

### 3. Install Dependencies

#### Menggunakan pip:

```bash
pip install matplotlib
```

#### Menggunakan pip3 (Linux/Mac):

```bash
pip3 install matplotlib
```

#### Menggunakan conda (jika menggunakan Anaconda):

```bash
conda install matplotlib
```

### 4. Verifikasi Instalasi

```bash
python -c "import matplotlib; print('matplotlib berhasil diinstall')"
```

## Cara Menjalankan

### 1. Jalankan Program

```bash
python main.py
```

### 2. Ikuti Instruksi

1. Masukkan jumlah mahasiswa
2. Input data untuk setiap mahasiswa:
    - Nama mahasiswa
    - NIM mahasiswa
    - Skor (0-100)
3. Program akan menampilkan:
    - Tabel hasil penilaian
    - Statistik distribusi grade
    - Grafik visualisasi

## Contoh Penggunaan

```
Masukkan jumlah mahasiswa: 3

--- Data mahasiswa ke-1 ---
Nama mahasiswa: Ahmad Rifai
NIM mahasiswa: 123456789
Skor (0-100): 95
✓ Data berhasil disimpan: Ahmad Rifai - Grade A

--- Data mahasiswa ke-2 ---
Nama mahasiswa: Siti Nurhaliza
NIM mahasiswa: 987654321
Skor (0-100): 85
✓ Data berhasil disimpan: Siti Nurhaliza - Grade B

--- Data mahasiswa ke-3 ---
Nama mahasiswa: Budi Santoso
NIM mahasiswa: 456789123
Skor (0-100): 75
✓ Data berhasil disimpan: Budi Santoso - Grade C

============================================================
           HASIL PENILAIAN MAHASISWA
============================================================
 1. Ahmad Rifai (123456789)
    Skor:  95 | Grade: A | Summa Cum Laude
 2. Siti Nurhaliza (987654321)
    Skor:  85 | Grade: B | Sangat Memuaskan
 3. Budi Santoso (456789123)
    Skor:  75 | Grade: C | Memuaskan

----------------------------------------
STATISTIK GRADE:
----------------------------------------
Grade A:  1 mahasiswa ( 33.3%)
Grade B:  1 mahasiswa ( 33.3%)
Grade C:  1 mahasiswa ( 33.3%)

✓ Grafik berhasil ditampilkan!
```

## Troubleshooting

### Error: ModuleNotFoundError: No module named 'matplotlib'

**Solusi:** Install matplotlib dengan perintah `pip install matplotlib`

### Error: Permission denied

**Solusi:** Gunakan `pip install --user matplotlib` atau jalankan sebagai administrator

### Grafik tidak muncul

**Solusi:**

-   Pastikan GUI backend tersedia
-   Coba install `python-tk`: `sudo apt-get install python3-tk` (Linux)
-   Untuk server tanpa GUI, matplotlib akan tetap berjalan tanpa menampilkan grafik

### Input tidak valid

Program sudah dilengkapi dengan validasi input:

-   Nama dan NIM tidak boleh kosong
-   Skor harus berupa angka 0-100
-   Jumlah mahasiswa harus lebih dari 0

## Struktur File

```
student-grading-system/
│
├── main.py          # File utama program
├── README.md        # Dokumentasi ini
└── requirements.txt # (opsional) daftar dependencies
```

## Requirements.txt (Opsional)

Untuk memudahkan instalasi, Anda bisa membuat file `requirements.txt`:

```
matplotlib>=3.0.0
```

Kemudian install dengan:

```bash
pip install -r requirements.txt
```

## Kontribusi

Jika ingin berkontribusi pada proyek ini:

1. Fork repository
2. Buat branch baru (`git checkout -b feature/improvement`)
3. Commit perubahan (`git commit -am 'Add some feature'`)
4. Push ke branch (`git push origin feature/improvement`)
5. Buat Pull Request

## Lisensi

Proyek ini menggunakan lisensi MIT. Silakan gunakan dan modifikasi sesuai kebutuhan.

## Kontak

Jika ada pertanyaan atau masalah, silakan buat issue di repository ini.
