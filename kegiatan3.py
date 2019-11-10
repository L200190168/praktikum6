>>> Nama = 'Imawan Luthfi Pambudi'
>>> NIM = 'L200190168'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # data "x" merupakan type data integer
>>> type(b)
<class 'int'>
>>> # data "Nama" memiliki instruksi "len"
>>> a / b
55.61904761904762
>>> # data "a" dibagi dengan data "b"
>>> a // b
55
>>> # data "a" dibagi data "b" dengan pembulatan hasil
>>> 10 * (a - 999)
1690
>>> # data a dikurangi 999,kemudian dikalikan 10
>>> b ** 2
441
>>> # data b dipangkatkan 2
>>> a % b
13
>>> #sisa hasil bagi data "a" dengan data "b"
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # data "c" merupakan type data float
>>> a / c
93.44
>>> # data "a" dibagi dengan data "c"
>>> a // c
93.0
>>> # data "a" dibagi data "c" dengan pembulatan hasil
>>> a % c
5.5
>>> #sisa hasil bagi data "a" dengan data "c"
>>> c > b
False
>>> # data "c" lebih besar dari data "b",maka hasilnya adalah "salah/false"
>>> type(c > b)
<class 'bool'>
>>> # merupakan type data boolean,jadi memiliki dua kemungkinan nilai,yaitu "True" atau "False"
>>> a > b and b > c
True
>>> # data "a" lebih besar dari data "b" dan data "b" lebih besar dari data "c",maka hasilnya adalah "Benar/True"
>>> a > 1100 or b < 10
True
>>> # data "a" lebih besar dari 1100 atau data "b" lebih kecil dari 10,maka hasilnya adalah "Benar/True"