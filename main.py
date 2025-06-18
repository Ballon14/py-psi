import matplotlib.pyplot as plt 

def get_grade_and_predicate(score):
    """
    Fungsi untuk menentukan grade dan predikat berdasarkan skor
    """
    if 90 <= score <= 100:
        return "A", "Summa Cum Laude"  # Perbaikan ejaan
    elif 80 <= score <= 89:
        return "B", "Sangat Memuaskan"
    elif 70 <= score <= 79:
        return "C", "Memuaskan"
    elif 60 <= score <= 69:
        return "D", "Cukup"
    elif 0 <= score <= 59:
        return "E", "Kurang"
    else:
        return None, "Tidak dapat diberikan predikat"

def main():
    try:
        # Input jumlah mahasiswa dengan validasi
        while True:
            try:
                n = int(input("Masukkan jumlah mahasiswa: "))
                if n <= 0:
                    print("Jumlah mahasiswa harus lebih dari 0!")
                    continue
                break
            except ValueError:
                print("Input harus berupa angka! Silakan coba lagi.")

        data_mahasiswa = []
        grade_counter = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

        # Input data mahasiswa
        for i in range(n):
            print(f"\n--- Data mahasiswa ke-{i+1} ---")
            
            # Input nama (tidak boleh kosong)
            while True:
                nama = input("Nama mahasiswa: ").strip()
                if nama:
                    break
                print("Nama tidak boleh kosong!")
            
            # Input NIM (tidak boleh kosong)
            while True:
                nim = input("NIM mahasiswa: ").strip()
                if nim:
                    break
                print("NIM tidak boleh kosong!")
            
            # Input skor dengan validasi
            while True:
                try:
                    skor = int(input("Skor (0-100): "))
                    if 0 <= skor <= 100:
                        break
                    else:
                        print("Skor harus dalam rentang 0-100!")
                except ValueError:
                    print("Skor harus berupa angka!")

            grade, predikat = get_grade_and_predicate(skor)

            if grade is not None:
                data_mahasiswa.append({
                    "Nama": nama,
                    "NIM": nim,
                    "Skor": skor,
                    "Grade": grade,
                    "Predikat": predikat
                })
                grade_counter[grade] += 1
                print(f"✓ Data berhasil disimpan: {nama} - Grade {grade}")

        # Tampilkan hasil
        if data_mahasiswa:
            print("\n" + "="*60)
            print("           HASIL PENILAIAN MAHASISWA")
            print("="*60)
            
            for i, mhs in enumerate(data_mahasiswa, 1):
                print(f"{i:2d}. {mhs['Nama']} ({mhs['NIM']})")
                print(f"    Skor: {mhs['Skor']:3d} | Grade: {mhs['Grade']} | {mhs['Predikat']}")
            
            # Tampilkan statistik
            print("\n" + "-"*40)
            print("STATISTIK GRADE:")
            print("-"*40)
            total_mahasiswa = len(data_mahasiswa)
            for grade, count in grade_counter.items():
                if count > 0:
                    percentage = (count / total_mahasiswa) * 100
                    print(f"Grade {grade}: {count:2d} mahasiswa ({percentage:5.1f}%)")
            
            # Buat grafik
            create_chart(data_mahasiswa)
        else:
            print("Tidak ada data mahasiswa yang valid untuk ditampilkan.")

    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh pengguna.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def create_chart(data_mahasiswa):
    """
    Fungsi untuk membuat grafik batang
    """
    try:
        # Persiapan data untuk grafik
        nama_labels = [f"{mhs['Nama']}\n({mhs['NIM']})" for mhs in data_mahasiswa]
        skor_values = [mhs['Skor'] for mhs in data_mahasiswa]

        # Warna untuk setiap grade
        colors = {
            "A": "#2E8B57",  # Sea Green
            "B": "#4169E1",  # Royal Blue
            "C": "#FF8C00",  # Dark Orange
            "D": "#DC143C",  # Crimson
            "E": "#8B008B"   # Dark Magenta
        }
        bar_colors = [colors[mhs['Grade']] for mhs in data_mahasiswa]

        # Buat grafik
        plt.figure(figsize=(max(12, len(data_mahasiswa) * 1.5), 8))
        bars = plt.bar(nama_labels, skor_values, color=bar_colors, alpha=0.8, edgecolor='black', linewidth=0.5)
        
        # Pengaturan grafik
        plt.title('Distribusi Skor Mahasiswa dan Predikatnya', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Nama Mahasiswa (NIM)', fontsize=12, fontweight='bold')
        plt.ylabel('Skor', fontsize=12, fontweight='bold')
        plt.ylim(0, 105)  # Set batas y-axis
        
        # Rotasi label x-axis
        plt.xticks(rotation=45, ha='right')
        
        # Tambahkan teks predikat di atas setiap bar
        for bar, mhs in zip(bars, data_mahasiswa):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, height + 1,
                     f"{mhs['Grade']}\n{mhs['Predikat']}", 
                     ha='center', va='bottom', fontsize=9, fontweight='bold')

        # Tambahkan grid dan legend
        plt.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Buat legend
        from matplotlib.patches import Patch
        legend_elements = [Patch(facecolor=colors[grade], label=f'Grade {grade}') 
                          for grade in colors.keys() 
                          if any(mhs['Grade'] == grade for mhs in data_mahasiswa)]
        plt.legend(handles=legend_elements, loc='upper right')
        
        plt.tight_layout()
        plt.show()
        
        print("\n✓ Grafik berhasil ditampilkan!")
        
    except Exception as e:
        print(f"Gagal membuat grafik: {e}")

# Jalankan program
if __name__ == "__main__":
    main()