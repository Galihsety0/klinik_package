def daftar_pasien(nama, usia, keluhan):
    print("=====DATA PASIEN======")
    print(f"Nama : {nama}")
    print(f"Usia : {usia}")
    print(f"Keluhan : {keluhan}")

def cek_prioritas(usia):
    status = ""
    print(f"Status : {usia}")
    if usia <=  5 or usia >= 65:
        status = "PRIORITAS"
    else: 
        status = "REGULER"