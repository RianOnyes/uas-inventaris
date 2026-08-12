class BarangView:
    def tampilkan_header(self):
        print("=" * 50)
        print("   SISTEM MANAJEMEN INVENTARIS TOKO")
        print("=" * 50)

    def tampilkan_menu(self):
        print("\nPilih menu:")
        print("1. Tambah Barang")
        print("2. Lihat Semua Barang")
        print("3. Cari Barang")
        print("4. Hapus Barang")
        print("5. Keluar")

    def input_menu(self):
        return input("Masukkan pilihan (1-5): ").strip()

    def input_data_barang(self):
        print("\n-- Tambah Barang Baru --")
        nama = input("Nama barang   : ")
        harga = input("Harga barang  : ")
        stok = input("Stok barang   : ")
        return nama, harga, stok

    def input_id_hapus(self):
        return input("Masukkan ID barang yang ingin dihapus: ")

    def input_kata_kunci_cari(self):
        return input("Masukkan kata kunci nama barang: ")

    def tampilkan_pesan(self, pesan: str):
        print(f">> {pesan}")

    def tampilkan_tabel(self, daftar_barang):
        if not daftar_barang:
            print(">> Tidak ada data barang untuk ditampilkan.")
            return

        header = ["ID", "Nama", "Harga", "Stok"]
        rows = [b.to_row() for b in daftar_barang]

        # hitung lebar kolom otomatis
        kolom = list(zip(header, *rows)) if rows else [[h] for h in header]
        lebar = [max(len(str(item)) for item in k) + 2 for k in zip(header, *rows)]

        def cetak_baris(items):
            baris = "|"
            for item, w in zip(items, lebar):
                baris += f" {str(item):<{w-1}}|"
            print(baris)

        garis = "+" + "+".join("-" * w for w in lebar) + "+"
        print(garis)
        cetak_baris(header)
        print(garis)
        for row in rows:
            cetak_baris(row)
        print(garis)
