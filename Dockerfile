# Langkah 1: Gunakan base image Python yang ringan sebagai fondasi.
FROM python:3.9-slim

# Langkah 2: Atur direktori kerja di dalam container.
WORKDIR /app

# Langkah 3: Salin file daftar dependensi dan install library-nya.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Langkah 4: Salin semua sisa kode aplikasi ke dalam container.
COPY . .

# Langkah 5: Beri tahu Docker bahwa aplikasi kita akan berjalan di port 5000.
EXPOSE 5000

# Langkah 6: Perintah default untuk menjalankan aplikasi saat container dimulai.
CMD ["python", "app.py"]