class Barang:
    """Class data yang merepresentasikan satu barang di inventaris."""

    def __init__(self, id_barang: int, nama: str, harga: float, stok: int):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def to_row(self):
        """Mengubah data barang menjadi list, untuk kebutuhan tampilan tabel."""
        return [self.id_barang, self.nama, f"Rp{self.harga:,.0f}", self.stok]

    def __repr__(self):
        return f"Barang(id={self.id_barang}, nama={self.nama}, harga={self.harga}, stok={self.stok})"
