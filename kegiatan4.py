>>> Nama = 'Imawan Luthfi Pambudi'
>>> NIM = 168
>>> Tinggi = 1.70
>>> Berat = 55
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # data "Aku" merupakan type data "tuple"
>>> Aku[0]
2000
>>> # objek pertama dalam data "Aku" adalah tahunlahir.nilai tahunlahir adalah 2000
>>> a = NIM % 4; Aku[a]
2000
>>> # sisa hasil bagi "NIM" dengan "4" adalah 0.jadi hasil aku adalah objek pertama data "Aku" yaitu "TahunLahir" yang nilainya 2000
>>> type(Aku[a])
<class 'int'>
>>> # merupakan type data integer
>>> Aku[a:4]
(2000, 55, 1.7, 168)
>>> # 4 objek data "aku" adalah "TahunLahir", "Berat", "Tinggi", dan "NIM"
>>> type(Aku[4])
<class 'str'>
>>> #merupakan type data string
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # terjadi kesalahan/data error
>>> type(Data)
<class 'list'>
>>> # Data yang berisi ("TahunLahir", "Berat", "Tinggi", "NIM", dan "Nama").merupakan type data list
>>> type(Data[4])
<class 'str'>
>>> #data ke 4 yaitu "NIM" merupakan type data string
>>> Data[4][5]
'n'
>>> # menampilkan data ke 4 dan ke 5 yang muncul adalah "n"
>>> Data[4][a:6]
'Imawan'
>>> # data menampilkan objek ke 4 dalam data yaitu nama dari urutan pertama hingga ke 6 yaitu "Imawan"
>>> Data[0] = 'ok';Data
['ok', 55, 1.7, 168, 'Imawan Luthfi Pambudi']
>>> # data menampilkan objek data.data pertama diganti dengan 'ok' 
>>> Data[-a]
'ok'
>>> # data yang tersimpan pada data"-a" adalah 'ok'
>>> range(a)
range(0, 0)
>>> # data range "a" memiliki nilai "0, dan 0"
>>> 