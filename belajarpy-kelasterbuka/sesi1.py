# 1.coba pertama kali 1️⃣

# print("hello world")

# 2. BELAJAR VARIABLE 2️⃣

# a = 10 #angka 10 dimasukan ke varible a
# b = 20 #angka 20 dimasukan ke varible b

# #pemanggilan pertama
# print(a + b) #menampilkan hasil dari penjumlahan varible a dan b

# #penamaan variable

# nilai1 = 11 #untuk penamaan variable yg lebih dari 2 kata menggunakan underscore
# juta10 = 22 #penamaan varible tidak boleh menggunakan angka di depannya
# print(nilai1)

# #assignment indirect
# nilai1 = juta10
# print (nilai1)

# 3. TIPE DATA 3️⃣

# # TIPE DATA DASAR PY
# tipe data INTEGER adalah data yg berisikan angka satuan (tanpa koma) (INT)
# # data_integer = 10
# print("data ; ", data_integer, ", bertipe data : ", type(data_integer))

# # tipe data FLOAT adalah data yg berisikan angka dengan koma (FLOAT)
# data_float = 1.5
# print("data ; ", data_float, ", bertipe data : ", type(data_float))

# # tipe data STRING adalah data yg berisikan karakter (STR)
# data_string = "ini data string"
# print("data ; ", data_string, ", bertipe data : ", type(data_string))

# # tipe data BOOLEAN berisikan biner true/false (BOOL)
# # penggunaannya untuk menentukan suatu kondisi
# # penulisan untuk data boolean, tidak boleh menggunakan tanda petik, dan huruf awalnya harus besar
# data_boolean = True
# print("data ; ", data_boolean, ", bertipe data : ", type(data_boolean))

# # TIPE DATA KHUSUS DI PY
# tipe data COMPLEX adalah data yg berisikan bilangan kompleks (COMPLEX)
# data_complex = complex(5,6)
# print("data ; ", data_complex, ", bertipe data : ", type(data_complex))

# # tipe data dari bahasa C
# from ctypes import c_double

# data_c_double = c_double(10.5)
# print("data ; ", data_c_double, ", bertipe data : ", type(data_c_double))

# 4. CASTING (merubah dari satu tipe ke tipe lain) 4️⃣
# # INTEGER

# print("====INTEGER====")

# data_int = 0
# print("data = ", data_int, ", tipe = " ,type(data_int))

# data_float = float(data_int)
# data_str = str(data_int) 
# data_bool = bool(data_int) #data akan menjadi false jika data int = 0
# print("data = ", data_float, ", tipe = " ,type(data_float))
# print("data = ", data_str, ", tipe = " ,type(data_str))
# print("data = ", data_bool, ", tipe = " ,type(data_bool))

# # # FLOAT

# print("====FLOAT====")
# data_float = 10.9
# print("data = ", data_float, ", tipe = " ,type(data_float))

# data_int = int(data_float) #data ini akan dibulatkan ke bawah
# data_str = str(data_float) 
# data_bool = bool(data_float) #data akan menjadi false jika data float = 0

# print("data = ", data_int, ", tipe = " ,type(data_int))
# print("data = ", data_str, ", tipe = " ,type(data_str))
# print("data = ", data_bool, ", tipe = " ,type(data_bool))

# # # BOOLEAN

# print("====BOOLEAN====")
# data_bool = 0
# print("data = ", data_bool, ", tipe = " ,type(data_bool))

# data_int = int(data_bool) #data ini akan dibulatkan ke bawah
# data_str = str(data_bool) 
# data_float = float(data_bool) #data akan menjadi false jika data float = 0

# print("data = ", data_int, ", tipe = " ,type(data_int))
# print("data = ", data_str, ", tipe = " ,type(data_str))
# print("data = ", data_float, ", tipe = " ,type(data_float))

# # # STRING

# print("====STRING====")
# data_str = "10"
# print("data = ", data_bool, ", tipe = " ,type(data_bool))

# data_int = int(data_str) #data ini akan dibulatkan ke bawah #harus angka jika data string -> integer
# data_bool = str(data_bool) # jika ada nilainya, data boolean akan bernilai true # jika tidak, bernilai false
# data_float = float(data_str) #data akan menjadi false jika data float = 0

# print("data = ", data_int, ", tipe = " ,type(data_int))
# print("data = ", data_bool, ", tipe = " ,type(data_bool))
# print("data = ", data_float, ", tipe = " ,type(data_float))

# 5. INPUT USER

# coba_input = input("masukan nama : ")
# print("Hallo",coba_input, "!")
# print("bertipe data : ",type(coba_input)) #data yg dimasukan pasti STR

# # jika ingin mengambil data INT

# data_int = int(input("masukan angka : "))

# print("nilai anda : ", data_int)
# print("bertipe : ", type(data_int))

# # jika ingin mengambil nilai boolean

# data_boolean = bool(int(input("masukan angka : "))) # casting dari integer ke boolean

# print("nilai anda : ", data_boolean)
# print("bertipe : ", type(data_boolean))

# 6. OPERASI ARITMATIKA

# a = 2
# b = 3

# print("Berikut hasilnya")

# # operasi penjumlahan

# hasil_jumlah = a + b
# print("hasil penjumlahannya : ", hasil_jumlah, type(hasil_jumlah))

# # operasi pengurangan

# hasil_kurang = a - b
# print("hasil pengurangannya : ", hasil_kurang, type(hasil_kurang))

# # operasi perkalian

# hasil_kali = a * b
# print("hasil perkalianya : ", hasil_kali,type(hasil_kali))

# # operasi pembagian

# hasil_bagi = a / b
# print("hasil pembagian : ", hasil_bagi,type(hasil_bagi))

# # operasi eksponen (pangkat)

# hasil_pangkat = a ** b
# print("hasil pangkat : ", hasil_pangkat,type(hasil_pangkat))

# # operasi modulus (sisa bagi)

# hasil_modulus = a % b
# print("hasil modulus : ", hasil_modulus,type(hasil_modulus))

# # operasi floor division

# hasil_floor = a // b
# print("hasil floor division : ", hasil_floor,type(hasil_floor))

# # prioritas operasi, operasi precedence

# o = 2
# p = 3
# q = 4

# hasil_precedence = p + o * q - o * p # perhitungan akan dimulai dari operasi yg diprioritaskan seperti di matematika

# '''
# 1. ()
# 2. ekponen **
# 3. perkalian dan lainnya
# 4. tambah dan kurang
# '''
# print("hasil precedence : ", hasil_precedence,type(hasil_precedence))

# 7. KONVERSI SATUAN TEMPERATURE

# print("\nProgram CELCIUS")

# celcius = float(input("Masukan Suhu dalam celcius : "))
# print("Suhunya adalah", celcius, "derajat celcius")

# # konversi ke REAMUR
# reamur = (4 / 5) * celcius
# print("Suhunya adalah", reamur, "derajat reamur")

# # konversi ke FAHRENHEIT

# fahrenheit = ((9 / 5) * celcius) + 32
# print("Suhunya adalah", fahrenheit, "derajat fahrenheit")

# # konversi ke KELVIN

# kelvin = celcius + 273
# print("suhunya adalah", kelvin, "derajat kelvin")

# # konversi fahrenheit ke kelvin

# fahrenheit_kelvin = ((5 / 9) * (fahrenheit - 32)) + 273
# print("suhunya adalah", fahrenheit_kelvin, "derajat kelvin")

# # konversi kelvin ke fahrenheit

# kelvin_fahrenheit = ((9 / 5) * (kelvin - 273)) + 32
# print("suhunya adalah", kelvin_fahrenheit, "derajat fahrenheit")

# 8. operasi komparasi

# a = 6
# b = 1

# # lebih besar dari ( > )
# print("\n===LEBIH DARI===")
# hasil = a > 4
# print("a > 4 : ", hasil, type(hasil))
# hasil = b > 2
# print("b > 2 : ", hasil, type(hasil))

# # kurang dari ( < )
# print("\n===KURANG DARI===")
# hasil = a < 4
# print("a < 4 : ", hasil, type(hasil))
# hasil = b < 2
# print("b < 2 : ", hasil, type(hasil))

# # LEBIH DARI SAMA DENGAN
# print("\n===LEBIH DARI SAMA DENGAN===")
# hasil = a >= 4
# print("a >= 4 : ", hasil, type(hasil))
# hasil = b >= 2
# print("b >= 2 : ", hasil, type(hasil))

# # KURANG DARI SAMA DENGAN
# print("\n===KURANG DARI SAMA DENGAN===")
# hasil = a <= 4
# print("a <= 4 : ", hasil, type(hasil))
# hasil = b <= 2
# print("b <= 2 : ", hasil, type(hasil))

# # SAMA DENGAN
# print("\n===SAMA DENGAN===")
# hasil = a == 4
# print("a == 4 : ", hasil, type(hasil))
# hasil = b == 1
# print("a == 1 : ", hasil, type(hasil))

# # TIDAK SAMA DENGAN
# print("\n===TIDAK SAMA DENGAN===")
# hasil = a != 4
# print("a != 4 : ", hasil, type(hasil))
# hasil = b != 1
# print("a != 1 : ", hasil, type(hasil))

# # MEMBANDINGKAN MEMORY ATAU OBJECT DENGAN IS

# print("\n===MEMBANDINGKAN MEMORY ATAU OBJECT DENGAN IS===")

# print("a is b : ", a is b)
# print("a is not b : ", a is not b)

# # MEMBANDINGKAN MEMORY ATAU OBJECT DENGAN IS NOT

# print("\n===MEMBANDINGKAN MEMORY ATAU OBJECT DENGAN IS NOT===")

# print("a is 2 : ", a is 2)
# print("a is not 1 : ", a is not 1)

# 9. OPERASI LOGIKA ATAU BOOLEAN

# # NOT
# print("\n=== NOT ===")
# a = True
# c = not a

# print("data boolean : ", a)
# print("data C : ", c)

# # OR # jika salah satu ada yg true, maka hasilnya true
# print("\n=== OR ===")
# a = False
# b = False
# c = a or b

# print(a, " OR ", b, " = ", c)

# a = False
# b = True
# c = a or b

# print(a, " OR ", b, " = ", c)

# a = True
# b = False
# c = a or b

# print(a, " OR ", b, " = ", c)

# a = True
# b = True
# c = a or b

# print(a, " OR ", b, " = ", c)

# # AND # jika salah satu ada yg false, maka hasilnya true
# print("\n=== AND ===")
# a = False
# b = False
# c = a and b

# print(a, " and ", b, " = ", c)

# a = False
# b = True
# c = a and b

# print(a, " and ", b, " = ", c)

# a = True
# b = False
# c = a and b

# print(a, " and ", b, " = ", c)

# a = True
# b = True
# c = a and b

# print(a, " and ", b, " = ", c)

# # XOR # nilai akan true jika salah satu dari nilai bernilai true

# print("\n=== XOR ===")
# a = False
# b = False
# c = a ^ b

# print(a, " xor ", b, " = ", c)

# a = False
# b = True
# c = a ^ b

# print(a, " xor ", b, " = ", c)

# a = True
# b = False
# c = a ^ b

# print(a, " xor ", b, " = ", c)

# a = True
# b = True
# c = a ^ b

# print(a, " xor ", b, " = ", c)

# 10. LATIHAN LOGIKA DAN KOMPARASI
# MEMBUAT GABUNGAN AREA RENTANG DARI ANGKA

# # ++++ 3 ---- 10 ++++
# # kurang dari 3 lebih dari 10

# print("\n=== LATIHAN LOGIKA DAN KOMPARASI ===")

# input_user = float(input("Masukan angka \nkurang dari angka 3 \natau \nlebih besar dari angka 10 \n:"))

# # memeriksa angka kurang dari 3

# kurang_dari_3 = (input_user < 3)
# print("Kurang dari 3 = ", kurang_dari_3)

# # memeriksa angka lebih dari 10

# lebih_dari_10 = (input_user > 10)
# print("\nLebih dari 10 = ", lebih_dari_10)

# hasil = kurang_dari_3 or lebih_dari_10
# print("\nangka yg anda masukan = ", hasil)

# # kasus irisan

# input_user = float(input("\nMasukan angka \nLebih dari angka 3 \ndan \nKurang besar dari angka 10 \n:"))

# # memeriksa angka lebih dari 3

# lebih_dari_3 = (input_user > 3)
# print("\nlebih dari 3 = ", lebih_dari_3)

# # memeriksa angka kurang dari 10

# kurang_dari_10 = (input_user < 10)
# print("\nkurang dari 10 = ", kurang_dari_10)

# hasil = lebih_dari_3 and kurang_dari_10
# print("angka yg anda masukan = ", hasil)

# LATIHAN LOGIKA DAN KOMPARASI
# # soal no 1
# input_user = float(input("\nMasukan angka Lebih dari angka 0 dan Kurang dari angka 5 dan angka yg lebih dari 8 dan kurang dari 11 : "))

# # lebih dari 0
# lebih_dari_0 = (input_user > 0)
# print("lebih dari 0 : ", lebih_dari_0)

# # kurang dari 5
# kurang_dari_5 = (input_user < 5)
# print("kurang dari 5 : ", kurang_dari_5)

# # dan

# # lebih dari 8
# lebih_dari_8 = (input_user > 8)
# print("lebih dari 8 : ",lebih_dari_8)

# # kurang dari 11
# kurang_dari_11 = (input_user < 11)
# print("kurang dari 11 : ",kurang_dari_11)

# hasil = lebih_dari_0 and kurang_dari_5 and lebih_dari_8 and kurang_dari_11
# print("\nBernilai : ", hasil)


# # Soal no 2

# # Meminta input dari pengguna
# input_user = float(input("\nMasukan angka yg kurang dari 0 , lebih dari 5 dan kuran dari 8, lebih dari 11 : "))

# # Memeriksa kondisi
# kurang_dari_0 = (input_user < 0)
# lebih_dari_5 = (input_user > 5)
# kurang_dari_8 = (input_user < 8)
# lebih_dari_11 = (input_user > 11)

# # Menampilkan hasil
# print("Kurang dari 0:", kurang_dari_0)
# print("Lebih dari 5:", lebih_dari_5)
# print("Kurang dari 8:", kurang_dari_8)
# print("Lebih dari 11:", lebih_dari_11)

# # Menggunakan operator logika AND untuk memeriksa semua kondisi
# hasil = kurang_dari_0 and lebih_dari_5 and kurang_dari_8 and lebih_dari_11
# print("\nBernilai", hasil)

# 11. OPERATOR BITWISE, OPERASI BINER, BINARY

# a = 9
# b = 5

# # bitwise OR (|)

# c = a | b
# print("\n==== OR ====")
# print("nilai : ", a, ", binary : ", format(a, "08b"))
# print("nilai : ", b, ", binary : ", format(b, "08b"))
# print("---------------------------------------")
# print("\nnilai : ", c, ", binary : ", format(c, "08b"))

# # bitwise AND (&)

# c = a & b
# print("\n==== AND ====")
# print("nilai : ", a, ", binary : ", format(a, "08b"))
# print("nilai : ", b, ", binary : ", format(b, "08b"))
# print("---------------------------------------")
# print("\nnilai : ", c, ", binary : ", format(c, "08b"))

# # bitwise XOR (^)

# c = a ^ b
# print("\n==== XOR ====")
# print("nilai : ", a, ", binary : ", format(a, "08b"))
# print("nilai : ", b, ", binary : ", format(b, "08b"))
# print("---------------------------------------")
# print("\nnilai : ", c, ", binary : ", format(c, "08b"))

# # bitwise NOT (~)

# c = ~a
# print("\n==== NOT ====")
# print("nilai : ", a, ", binary : ", format(a, "08b"))
# print("---------------------------------------")
# print("\nnilai : ", c, ", binary : ", format(c, "08b"))

# # shifting

# # shift right (>>)
# c = a >> 3
# print("\n==== SHIFT RIGHT ====")
# print("nilai : ", a, ", binary : ", format(a, "08b"))
# print("---------------------------------------")
# print("\nnilai : ", c, ", binary : ", format(c, "08b"))

# # shift left (<<)
# c = a << 3
# print("\n==== SHIFT LEFT ====")
# print("nilai : ", a, ", binary : ", format(a, "08b"))
# print("---------------------------------------")
# print("\nnilai : ", c, ", binary : ", format(c, "08b"))

# 12. ASSIGNMENT
# operasi yg dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

# a = 5 # ini adalah assignment
# print("\nnilai a adalah ", a)

# # contoh penyingkatan 

# a += 5 # artinya a = a + 1 menggunakan operator tambah (+)
# print("\nnilai a += 5 adalah ", a)

# a -= 5 # artinya adalah a = a - 1, menggunakan operator kurang (-)
# print("\nnilai a -= 5 adalah ", a)

# a *= 5 # artinya adalah a = a * 5, menggunakan operator kali (*)
# print("\nnilai a *= 5 adalah ", a)

# a /= 5 # artinya adalah a = a / 5, menggunakan operator bagi (/)
# print("\nnilai a /= 5 adalah ", a)

# b = 10
# print("\nnilai b adalah ", b)
# b %= 3 # artinya adalah b = b % 3, menggunakan operator modulus (%)
# print("nilai b %= 3 adalah ", b)

# b = 10
# print("\nnilai b adalah ", b)
# b //= 3 # artinya adalah b = b // 3, menggunakan operator floor division
# print("nilai b //= 3 adalah ", b)

# b = 10
# print("\nnilai b adalah ", b)
# b **= 3 # artinya adalah b = b ** 3, menggunakan operator eksponen (**)
# print("nilai b **= 3 adalah ", b)

# operasi bitwise dengan assignment
# # OR
# print("\n==== OR ====")
# c = True
# print("\nnilai c adalah ", c)
# c |= False # artinya adalah c = c | True, menggunakan operator bitwise OR (|)
# print("nilai c |= False adalah ", c)

# # AND
# print("\n==== AND ====")
# c = True
# print("\nnilai c adalah ", c)
# c &= False # artinya adalah c = c & False, menggunakan operator bitwise AND (&)
# print("nilai c &= False adalah ", c)

# c = True
# print("\nnilai c adalah ", c)
# c &= True # artinya adalah c = c & True, menggunakan operator bitwise AND (&)
# print("nilai c &= True adalah ", c)

# # XOR 
# print("\n==== XOR ====")
# c = False
# print("\nnilai c adalah ", c)
# c ^= False # artinya adalah c = c ^ False, menggunakan operator bitwise XOR (^)
# print("nilai c ^= False adalah ", c)

# c = False
# print("\nnilai c adalah ", c)
# c ^= True # artinya adalah c = c ^ True, menggunakan operator bitwise XOR (^)
# print("nilai c ^= True adalah ", c)

# # geser geser

# d = 0b0100
# print("\nNilai D adalah ", d)
# d >>= 1 # artinya adalah d = d >> 1, menggunakan operator shift right (>>)
# print("nilai d >>= 1 adalah", format(d, "04b"))
# d <<= 2 # artinya d = d <<= 2, menggunakan operator shift left (<<)
# print("nilai d <<= 2 adalah", format(d, "04b"))

# 13. STRING

# # a. menggunakan string biasa
# data = "ini adalah string"
# print(data, type(data))

# # menggunakan single quote ('...')
# data = '\nini adalah string menggunakan single quote'
# print(data, type(data))

# # menggunakan double quote
# data = "\nini adalah string menggunakan double quote"
# print(data, type(data))

# # menggunakan triple quote
# data = '''\nini adalah string 
# menggunakan 
# triple quote'''
# print(data, type(data))

# # b. menggunakan tanda (\)

# # membuat tanda (') menjadi string
# print('ini adalah hari jum\'at') # menggunakan tanda (\) untuk menambahkan ' di kalimat
# print('g\'day isn\'t it?')

# # backslash \
# print('C:\\user\\fathih') # menggunakan double (\) untuk mencetak tanda \ sebagai string

# # tab
# print('ini adalah penggunaan\t tab') # menggunakan (\t) untuk tab

# # backspace
# print('ini adalah penggunaan\b backspace') # menghapus karakter di belakangnya menggunakan (\b)

# # newline
# print('baris pertama.\nbaris kedua.') # menggunakan (\n) untuk membuat baris baru
# print('baris pertama. \rbaris kedua.')
# print('baris pertama. \n\rbaris kedua.')

# # c. string literal
# # hati-hati
# print('C:\new folder') # akan salah dalam penulisannya

# # menggunakan raw string
# print(r'C:\new folder\folder baru') # akan mencetak semua yg ada di dalam quote sebagai string termasuk tandanya

# # multiline literal string
# print("""
#       ini
#       adalah
#       multiline
#       literal
#       string
#       """) # akan mencetak string diberbagai baris selama di dalam quote (""")

# # multiline literal dan raw
# print(r"""
#       contoh penggunaannya
#       www.contoh multiline dan raw.com/asik 
#       """) # menggabungkan multiline dan raw string

# 14. OPERASI DAN MANIPULASI STRING

# # a. menyambung string (concatenate)
# nama_pertama = "Fathih"
# nama_tengah = "Pradipta"
# nama_akhir = "Arya"

# # nama_lengkap = nama_pertama + nama_tengah + nama_akhir # menggabungkan string
# nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir # menambahkan string kosong sebagai spasi
# print(nama_lengkap)

# # b. menghitung panjang string
# panjang = (len(nama_lengkap)) # menghitung panjang string, spasi dan tanda baca pun jg dihitung
# print("panjang dari nama tersebut adalah " + str(panjang))

# # c. operator untuk string

# # cek komponen di string
# d = "d"
# status = d in nama_lengkap
# print("string "+ d + " ada di " + nama_lengkap + " = " +str(status)) # untuk mengecek ada komponen di string atau tidak

# d = "d"
# status = d not in nama_lengkap
# print("string "+ d + " tidak ada di " + nama_lengkap + " = " +str(status)) # untuk mengecek ada komponen di string atau tidak

# # mengulang string
# print("wk"*10) # menggunakan tanda (*) untuk mengulangkan string
# print(5*"wk") # penggunaannya bisa di depan atau di belakang string

# # indexing
# print("index ke-0 : " + nama_lengkap[0])
# print("index ke-1 : " + nama_lengkap[1])
# print("index ke-(-3) : " + nama_lengkap[-3]) # jika pengambilan index dari angka minus, maka di ambilnya dari belakang string
# print("index ke-0 sampai 6 : " + nama_lengkap[0:6]) # pengambilan range pada index menggunakan tanda (:) yg berarti index 0 "sampai" index 6
# print("index ke-0,2,4,6,8,10 : "+ nama_lengkap[0:6:2]) # ini adalah contoh pengambilan index dengan increment 2, tanda (:) kedua mengartikan "increment" atau kenaikan

# #item paling kecil
# print("paling kecil : " + min(nama_lengkap))
# print("paling besar : " + max(nama_lengkap)) # pengambilan berat atau kecil itu dari ASCII CODE

# ascii_code = ord("a")
# print("ASCII code untuk spasi adalah " + str(ascii_code)) # untuk ASCII CODE paling ringan ada spasi (" ")
# data = 121
# print("ASCII code untuk 121 adalah " + chr(data)) # dan ASCII CODE paling berat adalah huruf "y"

# 15. operator dalam bentuk method
# # menghitung panjang string

# data = "Fathih Pradipta Arya"
# jumlah = data.count("a") # .count adalah method yg menempel pada string. pada OOP string itu sebagai object # fungsi count untuk  menghitung panjang dari string
# print("jumlah a pada " + data + " adalah " + str(jumlah))

# # a. merubah case dalam string

# # UPPERCASE (merubah string menjadi huruf besar semua)
# print("\n==== UPPERCASE ====")
# uppercase = "test yaa" 
# print("sebelum = " + uppercase)
# uppercase = uppercase.upper()
# print("sesudah = " + uppercase)

# # LOWERCASE (merubah string menjadi huruf kecil semua)
# print("\n==== LOWERCASE ====")
# lowercase = "TEST YAA" 
# print("sebelum = " + lowercase)
# lowercase = lowercase.lower()
# print("sesudah = " + lowercase)

# # b. isX method

# # islower
# # untuk mengecek apakah string berisi huruf kecil semua
# print("\n==== isX ====")
# coba = "contoh yaa"
# cek_lower =coba.islower() # jika ditulis seperti ini, maka hasilnya akan menjadi boolean
# print(coba + " apakah lower?  " + str(cek_lower)) # untuk menampilkan harus dirubah dlu menjadi string dengan "str"

# # isupper
# # untuk mengecek apakah string berisi huruf besar semua
# cek_upper =coba.isupper() 
# print(coba + " apakah upper? " + str(cek_upper))

# # isaslpha()
# # untuk mengecek apakah string berisi huruf semua
# huruf = "ini"
# print(huruf + " apakah huruf semua? " + str(huruf.isalpha())) # penggunaannya hanya huruf, tidak termasuk spasi

# # isalnum()
# # untuk mengecek apakah string berisi huruf dan angka
# anghur = "fathih10"
# print(anghur + "apakah huruf dan angka? " + str(anghur.isalnum()))

# # isdecimal()
# # untuk mengecek apakah string berisi angka semua
# desimal = "34832942397"
# print(desimal + " apakah angka? " + str(desimal.isdecimal()))

# # isspace()
# # untuk mengecek apakah string tidak berisi (spasi, tab, newline)
# kosong = " "
# print(kosong + " apakah spasi? " + str(kosong.isspace()))

# # istitle()
# # untuk mengecek apakah string dimulai dari huruf besar
# judul = "Burung Kakatua"
# cek_judul = judul.istitle()
# print(judul + " apakah judul? " + str(cek_judul))

# # c. startswith() dan endswith()

# # startswith()
# # untuk mengcek apakah string dimulai dengan sesuatu yg sama
# cek_start = "Fathih Pradipta".startswith("Fathih")
# print("start = " + str(cek_start))

# cek_end = "Fathih Pradipta".endswith("Pradipta")
# print("end = " + str(cek_end))

# # d. join() dan split()

# # join()
# # untuk menggabungkan string
# print("\n==== JOIN ====")
# pisah = ["Fathih", "Pradipta", "Arya"]
# gabung = " ".join(pisah)
# print("sebelum = " , pisah)
# print("sesudah = " , gabung)

# # split
# # untuk memisahkan string
# print("\n==== SPLIT ====")
# gabung = "FathihehmPradiptaehmArya"
# pisah = gabung.split("ehm")
# print("sebelum = " ,gabung)
# print("sesudah = " ,pisah)

# # e. alokasi karakter rjust(), ljust(), center(), strip()

# # rjust()
# # untuk membuat rata kanan
# print("\n" + 4*"=" + " RJUST " + "="*4)
# kanan = " kanan ".rjust(10) # angka 10 memberikan jumlah karakter pada string
# print("-" + kanan + "-")

# # ljust()
# # untuk membuat rata kiri
# print("\n" + 4*"=" + " LJUST " + "="*4)
# kiri = " kiri ".ljust(10)
# print("-" + kiri + "-")

# # center()
# # untuk membuat rata tengah
# print("\n" + 4*"=" + " CENTER " + "="*4)
# tengah = " tengah ".center(20,"-") # jika ingin mengganti selain space kosong, bisa menambah argumen lagi setelah angka
# print("-" + tengah + "-")

# # strip()
# # menghilangkan argumen
# print("\n" + 4*"=" + " STRIP " + "="*4)
# tengah = tengah.strip(":") # bisa untuk rjust dan ljust juga
# print("-" + tengah + "-")
