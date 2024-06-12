import cv2
import numpy as np

# Tentukan batas bawah dan atas warna merah dalam ruang warna HSV
# lower_red = np.array([0, 100, 100])
# upper_red = np.array([10, 255, 255])
lower_red = np.array([136, 87, 111])
upper_red = np.array([180, 255, 255])

# Inisialisasi pengambilan video
cap = cv2.VideoCapture(1)

while True:
    # Baca frame dari video capture
    ret, frame = cap.read()

    if not ret:
        break

    # Balik frame secara horizontal (efek cermin)
    frame = cv2.flip(frame, 1)

    # Konversi frame dari BGR ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Buat mask untuk warna merah
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Terapkan mask ke frame
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Tampilkan frame asli dan hasil
    cv2.imshow('Original', frame)
    cv2.imshow('Result', res)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Hentikan pengambilan video dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()
