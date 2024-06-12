# Proyek Mini OpenCV

Proyek ini adalah aplikasi pemrosesan gambar yang menggunakan OpenCV untuk mendeteksi warna merah secara real-time dari video yang diambil dari kamera. Latar belakang proyek ini adalah kebutuhan untuk mendeteksi objek berwarna merah dalam berbagai aplikasi seperti pelacakan objek, analisis video, dan pengenalan pola. Deteksi warna merah dilakukan dengan mengubah ruang warna dari BGR ke HSV, yang lebih efektif untuk segmentasi warna.

Walaupun aplikasi ini mampu mendeteksi warna merah dengan akurat, ada beberapa keterbatasan yang perlu diperhatikan. Pertama, kondisi pencahayaan yang berubah-ubah dapat mempengaruhi akurasi deteksi warna. Kedua, aplikasi ini hanya mendeteksi warna merah dalam rentang hue yang telah ditentukan dan mungkin tidak akurat untuk variasi warna merah yang sangat beragam. Terakhir, kecepatan pemrosesan tergantung pada perangkat keras yang digunakan, sehingga mungkin ada penurunan performa pada perangkat dengan spesifikasi rendah.

## Tujuan Proyek

Tujuan dari proyek ini adalah untuk mendeteksi warna merah dalam video real-time untuk aplikasi keamanan dan pemantauan. Deteksi warna merah dapat membantu dalam mengidentifikasi pakaian atau objek berwarna merah tertentu, seperti seragam petugas keamanan atau kendaraan darurat.

## Instalasi

1. Clone repository: `git clone https://github.com/your-username/mini-project-opencv.git`
2. Install dependensi yang diperlukan: `pip install -r requirements.txt`

## Penggunaan

1. Jalankan aplikasi: `RedMaskingMirror.py`
2. Sesuaikan pengaturan kamera dan pastikan kondisi pencahayaan yang baik untuk deteksi warna yang akurat.
3. Aplikasi akan menampilkan feed video real-time dengan warna merah yang disorot.

## Alat dan Software Yang Digunakan

- Webcam Camera JETE W7
- [OpenCV](https://opencv.org/) - Perpustakaan Komputer Visi Sumber Terbuka
- [Python](https://www.python.org/) - Bahasa Pemrograman
- [Visual Studio Code](https://code.visualstudio.com/) - Editor Teks