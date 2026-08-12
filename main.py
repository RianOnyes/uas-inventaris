from process import BarangProcess
from view import BarangView
from exceptions import ValidasiError, BarangTidakDitemukanError


def main():
    process = BarangProcess()
    view = BarangView()

    view.tampilkan_header()

    while True:
        view.tampilkan_menu()
        pilihan = view.input_menu()

        try:
            if pilihan == "1":
                nama, harga, stok = view.input_data_barang()
                barang = process.tambah_barang(nama, harga, stok)
                view.tampilkan_pesan(
                    f"Barang '{barang.nama}' berhasil ditambahkan dengan ID {barang.id_barang}."
                )

            elif pilihan == "2":
                daftar = process.get_semua_barang()
                view.tampilkan_tabel(daftar)

            elif pilihan == "3":
                keyword = view.input_kata_kunci_cari()
                hasil = process.cari_barang(keyword)
                view.tampilkan_tabel(hasil)

            elif pilihan == "4":
                id_str = view.input_id_hapus()
                barang = process.hapus_barang(id_str)
                view.tampilkan_pesan(f"Barang '{barang.nama}' (ID {barang.id_barang}) berhasil dihapus.")

            elif pilihan == "5":
                view.tampilkan_pesan("Terima kasih telah menggunakan program ini. Sampai jumpa!")
                break

            else:
                view.tampilkan_pesan("Pilihan tidak valid. Silakan pilih angka 1-5.")

        # --- Validasi / penanganan exception ---
        except ValidasiError as e:
            view.tampilkan_pesan(f"[Input tidak valid] {e}")
        except BarangTidakDitemukanError as e:
            view.tampilkan_pesan(f"[Data tidak ditemukan] {e}")
        except Exception as e:
            view.tampilkan_pesan(f"[Terjadi kesalahan tak terduga] {e}")


if __name__ == "__main__":
    main()
