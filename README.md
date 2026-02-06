# DevSecOps App – Repository Guidelines and Guardrails

Repository ini digunakan sebagai contoh implementasi DevSecOps dalam pengembangan aplikasi berbasis tim.

Fokus utama repository ini meliputi:

- menjaga kualitas kode,
- memastikan keamanan sejak tahap awal pengembangan,
- menerapkan proses CI/CD yang konsisten dan terkontrol.

Repository ini tidak berfokus pada pengembangan fitur, melainkan pada proses, tata kelola, dan kontrol kualitas pengembangan perangkat lunak.

## Struktur Tim

- Frontend Web: React.js
- Frontend Mobile: React Native
- Backend API: Python
- System Analyst
- Product Owner
- DevSecOps (Process and Security Owner)

## Aturan Dasar Repository

### Larangan Push Langsung ke Branch Main

Branch `main` merepresentasikan kondisi kode yang stabil dan siap digunakan.

Ketentuan yang berlaku:

- Push langsung ke branch `main` tidak diperbolehkan.
- Seluruh perubahan harus dilakukan melalui Pull Request.
- Pull Request hanya dapat digabungkan setelah seluruh pemeriksaan otomatis dinyatakan lulus.

## Aturan Branching

Pengembangan dilakukan menggunakan branch terpisah dengan ketentuan penamaan sebagai berikut:

- feature/nama-fitur
- bugfix/nama-bug
- hotfix/nama-perbaikan

Contoh penggunaan:

```
feature/login-page
bugfix/login-validation
```

## Pull Request

Setiap Pull Request wajib memenuhi ketentuan berikut:

- menjelaskan perubahan yang dilakukan secara jelas,
- tidak mengandung credential atau secret dalam bentuk apa pun,
- seluruh pipeline CI/CD harus berjalan dengan status lulus.

Pull Request akan ditolak secara otomatis apabila:

- proses build gagal,
- pengujian tidak berhasil,
- pemeriksaan keamanan tidak memenuhi standar.

Keputusan penggabungan kode sepenuhnya ditentukan oleh sistem CI/CD.

## CI/CD Pipeline

Pipeline CI/CD dijalankan secara otomatis pada setiap push dan Pull Request dengan tahapan sebagai berikut:

1. Pengambilan source code
2. Proses build aplikasi
3. Eksekusi unit test
4. Pemeriksaan keamanan dasar

Apabila salah satu tahapan gagal, proses penggabungan kode akan dihentikan.

## Aturan Keamanan

Ketentuan keamanan yang berlaku:

- tidak diperbolehkan menyimpan password, API key, atau token di dalam source code,
- file konfigurasi sensitif seperti `.env` tidak boleh di-commit ke repository,
- credential tidak boleh ditulis secara hardcoded.

Contoh kode yang tidak diperbolehkan:

```javascript
const password = "admin123";
```

Pipeline akan melakukan deteksi otomatis dan memblokir pelanggaran terhadap ketentuan keamanan.

## Prinsip DevSecOps

Peran DevSecOps dalam repository ini meliputi:

- penetapan standar kualitas kode,
- penerapan kontrol keamanan,
- pengawasan konsistensi proses pengembangan.

DevSecOps tidak berperan sebagai pengembang fitur, melainkan sebagai penanggung jawab mekanisme kontrol agar setiap perubahan yang masuk memenuhi standar yang telah ditetapkan.

## Tujuan Repository

Repository ini bertujuan sebagai:

- media pembelajaran DevSecOps berbasis praktik,
- simulasi alur kerja tim pengembangan perangkat lunak,
- contoh penerapan CI/CD dan security gate bagi pemula.

## Catatan

Apabila pipeline gagal:

- lakukan pemeriksaan pada log CI/CD,
- perbaiki permasalahan yang ditemukan,
- lakukan push ulang setelah perbaikan selesai.

Permintaan pengecualian terhadap aturan yang telah ditetapkan tidak akan diproses.
