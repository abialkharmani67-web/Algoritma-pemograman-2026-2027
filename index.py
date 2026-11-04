
nama = input("Nama mahasiswa       : ")
tugas = float(input("Nilai tugas (0-100)  : "))
uts = float(input("Nilai UTS (0-100)    : "))
uas = float(input("Nilai UAS (0-100)    : "))
kehadiran = float(input("Kehadiran % (0-100)  : "))

nilai_akhir = (tugas * 0.2) + (uts * 0.3) + (uas * 0.3) + (kehadiran * 0.2)

if nilai_akhir >= 85:
    nilai_huruf = "A"
    keterangan = "Sangat Baik"
elif nilai_akhir >= 75:
    nilai_huruf = "B"
    keterangan = "Baik"
elif nilai_akhir >= 65:
    nilai_huruf = "C"
    keterangan = "Cukup"
elif nilai_akhir >= 50:
    nilai_huruf = "D"
    keterangan = "Kurang"
else:
    nilai_huruf = "E"
    keterangan = "Sangat Kurang"

if nilai_akhir >= 60:
    status = "Lulus"
else:
    status = "Tidak Lulus"

print()
print("Nama:", nama)
print("Tugas:", tugas, "| UTS:", uts, "| UAS:", uas, "| Kehadiran:", kehadiran)
print("------------------------------")
print("Nilai Akhir :", nilai_akhir)
print("Nilai Huruf :", nilai_huruf, "(" + keterangan + ")")
print("Status      :", status)
