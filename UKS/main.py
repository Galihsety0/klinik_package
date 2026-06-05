from modul.pasien import daftar_pasien
from modul.pasien import cek_prioritas
from modul.dokter import tampilkan_dokter
from modul.dokter import cek_tersedia
from modul.pembayaran import hitung_tagihan
from modul.pembayaran import cetak_struk


#pasien
nama = "Budi Santoso"
usia = 65
keluhan = "Batuk & Demam"

daftar_pasien(nama, usia, keluhan)
cek_prioritas(usia)


#dokter
nama_dokter ="dr. Rina"
spesialis = "umum"
waktu_praktek = (8,9,10,11,13,15)

tampilkan_dokter(nama_dokter, spesialis, waktu_praktek)


#ketersediaan dokter
jam_sekarang = 10

cek_tersedia(jam_sekarang, waktu_praktek)
if cek_tersedia(jam_sekarang, waktu_praktek):
    print(f"\nDokter tersedia pada jam {jam_sekarang}")
else:
    print(f"\nDokter tidak tersedia pada jam {jam_sekarang}")


#pembayaran
biaya_konsultasi = 150000
biaya_obat = 75000

total = hitung_tagihan(biaya_konsultasi, biaya_obat)

cetak_struk(nama, nama_dokter, total)