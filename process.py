from data import Barang
from exceptions import ValidasiError, BarangTidakDitemukanError


class BarangProcess:
    def __init__(self):
        self.daftar_barang = []   # menyimpan objek-objek Barang
        self._counter_id = 1      # auto increment id

    # ---------- VALIDASI ----------
    def _validasi_nama(self, nama: str):
        if not nama or not nama.strip():
            raise ValidasiError("Nama barang tidak boleh kosong.")
        return nama.strip()

    def _validasi_harga(self, harga_str: str):
        try:
            harga = float(harga_str)
        except ValueError:
            raise ValidasiError("Harga harus berupa angka (contoh: 15000).")
        if harga < 0:
            raise ValidasiError("Harga tidak boleh negatif.")
        return harga

    def _validasi_stok(self, stok_str: str):
        try:
            stok = int(stok_str)
        except ValueError:
            raise ValidasiError("Stok harus berupa bilangan bulat (contoh: 10).")
        if stok < 0:
            raise ValidasiError("Stok tidak boleh negatif.")
        return stok

    # ---------- PROSES UTAMA ----------
    def tambah_barang(self, nama: str, harga_str: str, stok_str: str) -> Barang:
        nama_valid = self._validasi_nama(nama)
        harga_valid = self._validasi_harga(harga_str)
        stok_valid = self._validasi_stok(stok_str)

        barang = Barang(self._counter_id, nama_valid, harga_valid, stok_valid)
        self.daftar_barang.append(barang)
        self._counter_id += 1
        return barang

    def hapus_barang(self, id_str: str):
        try:
            id_barang = int(id_str)
        except ValueError:
            raise ValidasiError("ID harus berupa angka.")

        for b in self.daftar_barang:
            if b.id_barang == id_barang:
                self.daftar_barang.remove(b)
                return b
        raise BarangTidakDitemukanError(f"Barang dengan ID {id_barang} tidak ditemukan.")

    def cari_barang(self, keyword: str):
        keyword = keyword.strip().lower()
        hasil = [b for b in self.daftar_barang if keyword in b.nama.lower()]
        return hasil

    def get_semua_barang(self):
        return self.daftar_barang
