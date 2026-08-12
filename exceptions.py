class ValidasiError(Exception):
    """Dilempar ketika input dari user tidak memenuhi aturan validasi."""
    pass


class BarangTidakDitemukanError(Exception):
    """Dilempar ketika barang dengan id/keyword tertentu tidak ditemukan."""
    pass
