# Proyek Mini OpenCV

Proyek ini adalah aplikasi pemrosesan gambar yang menggunakan OpenCV untuk mendeteksi warna merah secara real-time dari video yang diambil dari kamera. Latar belakang proyek ini adalah kebutuhan untuk mendeteksi objek berwarna merah dalam berbagai aplikasi seperti pelacakan objek, analisis video, dan pengenalan pola. Deteksi warna merah dilakukan dengan mengubah ruang warna dari BGR ke HSV, yang lebih efektif untuk segmentasi warna.

Walaupun aplikasi ini mampu mendeteksi warna merah dengan akurat, ada beberapa keterbatasan yang perlu diperhatikan. Pertama, kondisi pencahayaan yang berubah-ubah dapat mempengaruhi akurasi deteksi warna. Kedua, aplikasi ini hanya mendeteksi warna merah dalam rentang hue yang telah ditentukan dan mungkin tidak akurat untuk variasi warna merah yang sangat beragam. Terakhir, kecepatan pemrosesan tergantung pada perangkat keras yang digunakan, sehingga mungkin ada penurunan performa pada perangkat dengan spesifikasi rendah.

## Tujuan Proyek

Tujuan dari proyek ini adalah untuk mendeteksi warna merah dalam video real-time untuk aplikasi keamanan dan pemantauan. Deteksi warna merah dapat membantu dalam mengidentifikasi pakaian atau objek berwarna merah tertentu, seperti seragam petugas keamanan atau kendaraan darurat.

## Instalasi

1. Clone repository: `git clone https://github.com/cyberlument/OpenCV-ColorMasking-RED-.git`
2. Install dependensi yang diperlukan: `pip install -r requirements.txt`

## Library Yang Digunakan

1. numpy: Library untuk komputasi numerical .
2. opencv-python: Library untuk computer vision.

## Penggunaan

1. Jalankan aplikasi: `RedMaskingMirror.py`
2. Sesuaikan pengaturan kamera dan pastikan kondisi pencahayaan yang baik untuk deteksi warna yang akurat.
3. Aplikasi akan menampilkan feed video real-time dengan warna merah yang disorot.

## Output Yang Dihasilkan
![PengujianMiniProjectOpenCVRedMasking1](https://github.com/Cyberlument/OpenCV-ColorMasking-RED-/assets/101156094/10dce2f1-8940-496a-9804-6c3d258e39e9)

![PengujianMiniProjectOpenCVRedMasking2](https://github.com/Cyberlument/OpenCV-ColorMasking-RED-/assets/101156094/196a72d7-c6d1-490c-9094-53b5e05d977c)

## Alat dan Software Yang Digunakan

- [Webcam JETE W7](https://jete.id/product/webcam-jete-w7-full-hd-1080px/) - Webcam Yang Digunakan Untuk Mini Proyek Ini.
- [OpenCV](https://opencv.org/) - Perpustakaan Komputer Visi Sumber Terbuka
- [Python](https://www.python.org/) - Bahasa Pemrograman
- [Visual Studio Code](https://code.visualstudio.com/) - Editor Teks
