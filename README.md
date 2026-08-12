# Project UAS Bahasa Pemrograman — Sistem Manajemen Inventaris Toko

Program CLI (command line) sederhana untuk mengelola data barang inventaris toko,
dibuat dengan konsep **Modular** dan **OOP** (pemisahan class Data, View, dan Process).

## 📌 Deskripsi Program
Program ini memungkinkan pengguna untuk:
- Menambahkan data barang (nama, harga, stok)
- Melihat seluruh data barang dalam bentuk tabel
- Mencari barang berdasarkan nama
- Menghapus barang berdasarkan ID
- Validasi input menggunakan konsep exception (custom exception), sehingga
  program tidak crash ketika user salah memasukkan data (misalnya huruf pada kolom harga).

## 🧩 Struktur Modular (OOP)
| File            | Peran                                                            |
|-----------------|-------------------------------------------------------------------|
| `data.py`       | **Class Data** — struktur/model data `Barang`                     |
| `view.py`       | **Class View** — menampilkan menu, input, dan tabel hasil         |
| `process.py`    | **Class Process** — logika bisnis: validasi, tambah, hapus, cari  |
| `exceptions.py` | Custom exception untuk validasi input                             |
| `main.py`       | Entry point, menghubungkan Data–View–Process                      |

## ▶️ Cara Menjalankan
1. Pastikan Python 3 sudah terinstal.
2. Clone repository ini:
   ```
   git clone <URL_REPOSITORY_INI>
   cd <nama-folder>
   ```
3. Jalankan program:
   ```
   python main.py
   ```
4. Ikuti menu yang tampil di layar (1–5).

## 🎥 Dokumentasi & Video Demo
- Video penjelasan & proses pembuatan program (menampilkan wajah presenter): **[ISI LINK YOUTUBE DI SINI]**
- Video demo program berjalan: **[ISI LINK YOUTUBE / bisa digabung dengan video di atas]**

## 👤 Identitas
- Nama: [ISI NAMA KAMU]
- NIM: [ISI NIM KAMU]
- Mata Kuliah: Bahasa Pemrograman
