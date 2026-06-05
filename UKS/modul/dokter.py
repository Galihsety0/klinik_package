def tampilkan_dokter(nama_dokter, spesialis, waktu_praktek):
    print("\n=====DATA DOKTER======")
    print(f"Nama : {nama_dokter}")
    print(f"Spesialisasi : {spesialis}")
    print(f"Jam : {waktu_praktek}")


def cek_tersedia(jam_sekarang, waktu_praktek):
    return jam_sekarang in waktu_praktek
    