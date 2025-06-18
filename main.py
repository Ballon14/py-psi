import matplotlib.pyplot as plt 

def get_grade_and_predicate(score):
    if 90 <= score <= 100:
        return "A", "Summa Cumlaude"
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

try:
    n = int(input("Masukkan jumlah mahasiswa: "))

    data_mahasiswa = []

    grade_counter = {"A":0, "B":0, "C":0, "D":0, "E":0}

    for i in range(n):
        print(f"\nData mahasiswa ke-{i+1}")
        nama = input("Nama mahasiswa: ")
        nim = input("NIM mahasiswa: ")
        try:
            skor = int(input("Skor (0-100): ")) 

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
            else:
                print("Skor di luar jangkauan. Tidak dapat diberikan predikat.")
        except ValueError:
            print("Skor harus berupa angka!")

    print("\n--- Hasil Penilaian Mahasiswa ---")
    for mhs in data_mahasiswa:
        print(f"{mhs['Nama']} ({mhs['NIM']}): Skor = {mhs['Skor']}, Grade = {mhs['Grade']}, Predikat = {mhs['Predikat']}")

    nama_labels = [f"{mhs['Nama']}\n({mhs['NIM']})" for mhs in data_mahasiswa]

    skor_values = [mhs['Skor'] for mhs in data_mahasiswa]

    colors = {
        "A": "green",
        "B": "blue",
        "C": "orange",
        "D": "red",
        "E": "purple"
    }
    bar_colors = [colors[mhs['Grade']] for mhs in data_mahasiswa]

    plt.figure(figsize=(12, 6))
    bars = plt.bar(nama_labels, skor_values, color=bar_colors)
    plt.title('Skor Mahasiswa dan Predikatnya')
    plt.xlabel('Nama Mahasiswa (NIM)')
    plt.ylabel('Skor')
    plt.xticks(rotation=45, ha='right') 

    for bar, mhs in zip(bars, data_mahasiswa):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 mhs['Predikat'], ha='center', fontsize=8)

    plt.tight_layout() 
    plt.grid(axis='y') 
    plt.show()

except ValueError:
    print("Input jumlah mahasiswa harus berupa angka.")