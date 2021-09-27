"""
==================================================
|| -= INVESTASI PROFIL RISIKO INDIKATOR =-      ||
|| EXPERT SYSTEM SEDERHANA                      ||
||                                              ||
|| OLEH :                                       ||
|| KELOMPOK 4 - REKAYASA PENGETAHUAN A          ||                                      
|| 1. DAFFA MUHAMAD AZHAR      05111940000037   ||
|| 2. SATRIO HANIF WICAKSONO   05111940000103   ||
||                                              ||
|| TAHUN 2021                                   ||
==================================================
"""

import os

# KELAS PERTANYAAN
class pertanyaan:
    question = {}
    
    def __init__(self):
        pertanyaan.question.update({"STATUS?\n":"1. MARRIED\t||\t2. SINGLE"})
        pertanyaan.question.update({"PAHAM INVESTASI?\n":"1. TIDAK\t||\t2. PAHAM"})
        pertanyaan.question.update({"INVESTASI BUAT APA?\n":"1. KONSUMTIF (MOBIL/MOTOR)\t||\t2. MASA DEPAN"})
        pertanyaan.question.update({"JANGKA WAKTU INVESTASI?\n":"1. <5 TAHUN\t||\t2. >5 TAHUN"})
        pertanyaan.question.update({"JIKA NILAI INVESTASI -15%, BAGAIMANA?\n":"1. JUAL\t\t||\t2. TAMBAH"})
        
    
# KELAS JAWABAN
class Kelas_Jawaban:
    counter1 = 0
    counter2 = 0

    def __init__(self, answers):
        self.ans = answers
        for x in self.ans:
            if x == 1:
                Kelas_Jawaban.counter1 += 1
            elif x == 2:
                Kelas_Jawaban.counter2 += 1
    
    def calculate(self):
        if Kelas_Jawaban.counter1 == 0 and Kelas_Jawaban.counter2 == 5:
            return("AGGRESIVE")
        elif Kelas_Jawaban.counter1 == 1 and Kelas_Jawaban.counter2 == 4:
            return("MODERAT - AGGRESIVE")
        elif Kelas_Jawaban.counter1 == 2 and Kelas_Jawaban.counter2 == 3:
            return("MODERAT")
        elif Kelas_Jawaban.counter1 == 3 and Kelas_Jawaban.counter2 == 2:
            return("MODERAT")
        elif Kelas_Jawaban.counter1 == 4 and Kelas_Jawaban.counter2 == 1:
            return("KONSERVATIF - MODERAT")
        elif Kelas_Jawaban.counter1 == 5 and Kelas_Jawaban.counter2 == 0:
            return("KONSERVATIF")

# KELAS REKOMENDASI
class rekomen:
    tempatInvest = []

    def __init__(self):
        rekomen.tempatInvest.append("RD PASAR UANG, EMAS, USD")
        rekomen.tempatInvest.append("DEPOSITO")
        rekomen.tempatInvest.append("RD PENDAPATAN TETAP, OBLIGASI (SBR, ORI, dkk.)")
        rekomen.tempatInvest.append("PROPERTI, TANAH")
        rekomen.tempatInvest.append("RD SAHAM, RD CAMPURAN, P2P LENDING")
        rekomen.tempatInvest.append("SAHAM")

    def printRec(self, hasil):
        self.hasil = hasil
        if self.hasil == "KONSERVATIF":
            print("1. " + rekomen.tempatInvest[0])
            print("2. " + rekomen.tempatInvest[1])
            print("3. " + rekomen.tempatInvest[2])
        elif self.hasil == "KONSERVATIF - MODERAT":
            print("1. " + rekomen.tempatInvest[0])
            print("2. " + rekomen.tempatInvest[1])
            print("3. " + rekomen.tempatInvest[2])
        elif self.hasil == "MODERAT":
            print("1. " + rekomen.tempatInvest[0])
            print("2. " + rekomen.tempatInvest[2])
            print("3. " + rekomen.tempatInvest[3])
            print("4. " + rekomen.tempatInvest[4])
        elif self.hasil == "MODERAT - AGGRESIVE":
            print("1. " + rekomen.tempatInvest[0])
            print("2. " + rekomen.tempatInvest[3])
            print("3. " + rekomen.tempatInvest[4])
            print("4. " + rekomen.tempatInvest[5])
        elif self.hasil == "AGGRESIVE":
            print("1. " + rekomen.tempatInvest[0])
            print("2. " + rekomen.tempatInvest[4])
            print("3. " + rekomen.tempatInvest[5])
        
# KELAS IDENTITAS
class identitas:
    jawaban = []
    profileRisk = str

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

# MAIN FUNCTION

# DATA DIRI
eror = ""
while True:
    _ = os.system('cls')
    print("-= INVESTASI PROFIL RISIKO INDIKATOR =-")
    print(eror)
    print("\n-= MASUKKAN DATA DIRI =-")
    try:
        nama = str(input("NAMA : "))
        umur = int(input("UMUR : "))
    except ValueError:
        eror = "INPUT ERROR, UMUR HARUS BERUPA ANGKA"
        continue
    else:
        break
    
person = identitas(nama, umur);

# PERTANYAAN
q = pertanyaan()
for soal, pilihan in q.question.items():
    eror = ""
    while True:
        _ = os.system('cls')
        print("-= INVESTASI PROFIL RISIKO INDIKATOR =-")
        print(eror)
        print("\n-= PERTANYAAN =-")
        
        # q = pertanyaan()
        print(soal)
        print(pilihan)
        # question = q.callout(nomor)

        try:
            jawaban = int(input("Jawaban (1 atau 2) : "))
        except ValueError:
            eror = "MAAF, INPUT HARUS BERUPA ANGKA 1 ATAU 2"
            continue
        if jawaban > 2 or jawaban < 1:
            eror = "MAAF, INPUT HARUS BERUPA ANGKA 1 ATAU 2"
            continue
        else:
            break
            
    person.jawaban.append(jawaban)

# CALCULATE
out = Kelas_Jawaban(person.jawaban)

# OUTPUT
_ = os.system('cls')
print("-= INVESTASI PROFIL RISIKO INDIKATOR =-\n")
print("-= HASIL =-")
print("NAMA : " + person.nama)
print("UMUR :", person.umur)
person.profileRisk = out.calculate()
print("\nPROFIL RISIKO : " + person.profileRisk)

print("\nREKOMENDASI TEMPAT INVESTASI : ")
rec = rekomen()
rec.printRec(person.profileRisk)