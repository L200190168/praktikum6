## Program Akun
## Dibuat oleh Luthfi L200190168
import random
angka = random.randint(0,1000)

Nama = 'Imawan Luthfi Pambudi'
TanggalLahir = '31 Mei 2000'
NamaSingkat = Nama[0] + '. ' + Nama[7] + '. ' + Nama[14:21]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[7:11]
Password = Nama[0:4] + str(angka)
