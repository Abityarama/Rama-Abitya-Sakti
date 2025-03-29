# Daftar barang, stok, dan harga
toko = {
    "01": {"nama": "Buku", "stok": 10, "harga": 50000},
    "02": {"nama": "Pulpen", "stok": 20, "harga": 2000},
    "03": {"nama": "Penggaris", "stok": 15, "harga": 10000},
    "04": {"nama": "Kertas", "stok": 50, "harga": 3000},
}

# Untuk menyimpan total penjualan harian
total_penjualan_harian = 0

# Fungsi untuk menampilkan daftar barang yang tersedia
def tampilkan_barang():
    print("Daftar Barang:")
    # Menampilkan setiap barang dalam toko
    for kode, info in toko.items():
        print(f"Kode: {kode}, Nama: {info['nama']}, Stok: {info['stok']}, Harga: {info['harga']}")

# Fungsi untuk melakukan pembelian barang
def beli_barang():
    global total_penjualan_harian  # Mengakses variabel global total_penjualan_harian
    kode_barang = input("Masukkan kode barang yang ingin dibeli: ")  # Meminta input kode barang
    
    # Cek apakah kode barang valid
    if kode_barang in toko:
        jumlah = int(input("Masukkan jumlah pembelian: "))  # Meminta input jumlah barang yang ingin dibeli
        
        # Cek apakah stok mencukupi
        if jumlah <= toko[kode_barang]["stok"]:
            total_harga = jumlah * toko[kode_barang]["harga"]  # Menghitung total harga
            print(f"Total harga: {total_harga}")
            konfirmasi = input("Apakah Anda ingin melanjutkan pembayaran? (ya/tidak): ")  # Konfirmasi pembelian
            
            # Jika konfirmasi pembayaran "ya", lanjutkan transaksi
            if konfirmasi.lower() == "ya":
                toko[kode_barang]["stok"] -= jumlah  # Mengurangi stok barang
                total_penjualan_harian += total_harga  # Menambahkan total penjualan harian
                print("Pembayaran berhasil. Terima kasih!")  # Menampilkan pesan sukses
            else:
                print("Pembayaran dibatalkan.")  # Jika pembayaran dibatalkan
        else:
            print("Stok tidak cukup.")  # Jika jumlah yang dibeli melebihi stok
    else:
        print("Kode barang tidak valid.")  # Jika kode barang tidak ditemukan

# Fungsi untuk menampilkan laporan penjualan
def laporan_penjualan():
    print(f"Total penjualan harian: {total_penjualan_harian}")  # Menampilkan total penjualan harian

# Fungsi utama untuk menjalankan program
def main():
    while True:
        # Menampilkan menu pilihan
        print("\nMenu:")
        print("1. Tampilkan barang")
        print("2. Beli barang")
        print("3. Laporan penjualan")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")  # Meminta input menu pilihan
        
        # Menjalankan tindakan berdasarkan pilihan menu
        if pilihan == "1":
            tampilkan_barang()  # Menampilkan barang
        elif pilihan == "2":
            beli_barang()  # Membeli barang
        elif pilihan == "3":
            laporan_penjualan()  # Menampilkan laporan penjualan
        elif pilihan == "4":
            print("Terima kasih! Sampai jumpa.")  # Menampilkan pesan keluar dan berhenti
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")  # Jika input menu tidak valid

# Mengecek apakah program dijalankan sebagai program utama
if __name__ == "__main__":
    main()  # Memanggil fungsi utama untuk menjalankan program