import os
import pandas as pd

# class Kelas_Pertanyaan:
#     def __init__(self, pertanyaan):
#         self.pertanyaan = pertanyaan

class Kelas_Jawaban:
    counter1 = 0
    counter2 = 0

    def __init__(self, answers):
        self.ans = answers
        for x in self.ans:
            if x == "1":
                Kelas_Jawaban.counter1 += 1
            else:
                Kelas_Jawaban.counter2 += 1
    
    def calculate(self):
        if Kelas_Jawaban.counter1 == 1 and Kelas_Jawaban.counter2 == 4:
            return("1 = 1 && 2 = 4")
        elif Kelas_Jawaban.counter1 == 2 and Kelas_Jawaban.counter2 == 3:
            return("1 = 2 && 2 = 3")
        elif Kelas_Jawaban.counter1 == 3 and Kelas_Jawaban.counter2 == 2:
            return("1 = 3 && 2 = 2")
        elif Kelas_Jawaban.counter1 == 4 and Kelas_Jawaban.counter2 == 1:
            return("1 = 4 && 2 = 1")
        elif Kelas_Jawaban.counter1 == 5 and Kelas_Jawaban.counter2 == 0:
            return("1 = 5 && 2 = 0")
        elif Kelas_Jawaban.counter1 == 0 and Kelas_Jawaban.counter2 == 5:
            return("1 = 0 && 2 = 5")

        
class identitas:
    jawaban = []
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

# CLEAR SCREEN
_ = os.system('cls')

# JUDUL
print("-= INVESTASI PROFIL RESIKO INDIKATOR =-\n")

# DATA DIRI
print("-= MASUKKAN DATA DIRI =-")

nama = input("NAMA : ")
umur = input("UMUR : ")

# INISIASI
person = identitas(nama, umur);

# PERTANYAAN

for nomor in range(5):
    _ = os.system('cls')
    print("-= PERTANYAAN =-")
    if nomor == 0:
        print("STATUS?")
        print("1. MARRIED || 2. SINGLE")
        jawaban = input("Jawaban (1 atau 2) : ")
        person.jawaban.append(jawaban)
    elif nomor == 1:
        print("PAHAM INVESTASI?")
        print("1. TIDAK || 2. PAHAM")
        jawaban = input("Jawaban (1 atau 2) : ")
        person.jawaban.append(jawaban)
    elif nomor == 2:
        print("INVESTASI BUAT APA?")
        print("1. NIKAH || 2. MASA DEPAN")
        jawaban = input("Jawaban (1 atau 2) : ")
        person.jawaban.append(jawaban)
    elif nomor == 3:
        print("JANGKA WAKTU INVESTASI?")
        print("1. <5 TAHUN || 2. >5 TAHUN")
        jawaban = input("Jawaban (1 atau 2) : ")
        person.jawaban.append(jawaban)
    elif nomor == 4:
        print("JIKA NILAI INVESTASI -15%, BAGAIMANA?")
        print("1. JUAL || 2. TAMBAH")
        jawaban = input("Jawaban (1 atau 2) : ")
        person.jawaban.append(jawaban)

# CALCULATE
out = Kelas_Jawaban(person.jawaban)


# CLEAR SCREEN
_ = os.system('cls')

# OUTPUT
print("-= HASIL =-")
print("NAMA : " + person.nama)
print("UMUR : " + person.umur)
hasil = out.calculate()
print("\nPROFIL RESIKO : " + hasil)

# DEBUGGING
# for i in person.jawaban:
#     print(i)
