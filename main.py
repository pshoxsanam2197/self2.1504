# 1-m
class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif

kitob1 = Kitob("O‘tkan kunlar", "Abdulla Qodiriy")
kitob2 = Kitob("Mehrobdan chayon", "Abdulla Qodiriy")

print(f"Kitob nomi: {kitob1.nomi}")
print(f"Muallif: {kitob2.muallif}")


# 2-m
class Talaba():
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

talaba1 = Talaba("Ali", "20")
talaba2 = Talaba("Vali", "22")

print(f"1-talabaning ismi: {talaba1.ism} yoshi: {talaba1.yosh}")
print(f"2-talabaning ismi: {talaba2.ism} yoshi: {talaba2.yosh}")

# 3-m
class Telefon():
    def __init__(self, model, narx):
        self.model = model
        self.narx = narx

tel1 = Telefon("iPhone 13", "1200")
tel2 = Telefon("Samsung","900")

print(f"tel1 ning modeli: {tel1.model}, narxi: {tel1.narx}")
print(f"tel2 ning modeli: {tel2.model}, narxi: {tel2.narx}")

# 4-m
class Shahar():
    def __init__(self, nomi, aholisi):
        self.nomi = nomi
        self.aholisi = aholisi

shahar1 = Shahar("Toshkent", "3000000")
shahar2 = Shahar("Samarqand", "600000")

print(f"1-shaharning nomi: {shahar1.nomi} aholisi {shahar1.aholisi}")
print(f"2-shaharning nomi: {shahar2.nomi} aholisi {shahar2.aholisi}")

# 5-m
class Mashina():
    def __init__(self, marka, rang):
        self.m = marka
        self.r = rang

m1 = Mashina("Cobalt", "oq")
m2 = Mashina("Malibu", "qora")
m3 = Mashina("Nexia", "kulrang")

print(f"1-mashinaning markasi: {m1.m} rangi: {m1.r}")
print(f"2-mashinaning markasi: {m2.m} rangi: {m2.r}")
print(f"3-mashinaning markasi: {m3.m} rangi: {m3.r}")

# 6-m
class Talaba():
    def __init__(self, ism, yosh, kurs):
        self.i = ism
        self.y = yosh
        self.k = kurs

ism1 = Talaba("Ali", "20", "2-kurs")
ism2 = Talaba("Vali", "22", "3-kurs")

print(f"1-Talabaning ismi: {ism1.i} yoshi: {ism1.y} kursi: {ism1.k}")
print(f"2-Talabaning ismi: {ism2.i} yoshi: {ism2.y} kursi: {ism2.k}")

# 7-m
class Kitob():
    def __init__(self, nomi, muallif, sahifa_soni):
        self.nomi = nomi
        self.muallif = muallif
        self.sahifa_nomi = sahifa_soni

kitob1 = Kitob("O'tgan kunlar", "Abdulla Qodiriy", "300")
kitob2 = Kitob("Alkimyogar", "Paulo Coelho", "200")

print(f"1-kitobning nomi: {kitob1.nomi} muallifi: {kitob1.muallif} sahoifasi: {kitob1.sahifa_nomi}")
print(f"2-kitobning nomi: {kitob2.nomi} muallifi: {kitob2.muallif} sahoifasi: {kitob2.sahifa_nomi}")

# 8-m
class Telefon():
    def __init__(self, model, rang, narx):
        self.model = model
        self.rang = rang
        self.narx = narx

tel1 = Telefon("iPhone 13", "qora", "1200")
tel2 = Telefon("S21", "oq", "900")

print(f"1 - telefonning modeli: {tel1.model} rangi: {tel1.rang} narxi: {tel1.narx} ")
print(f"2 - telefonning modeli: {tel2.model} rangi: {tel2.rang} narxi: {tel2.narx} ")

# 9-m
class Mashina():
    def __init__(self, marka, rang, yili):
        self.marka = marka
        self.rang = rang
        self.yili = yili

m1 = Mashina("Cobalt", "oq", "2022")
m2 = Mashina("Malibu", "qora", "2023")

print(f"1 - mashinaning markasi: {m1.marka} rangi: {m1.rang} yili: {m1.yili}")
print(f"2 - mashinaning markasi: {m2.marka} rangi: {m2.rang} yili: {m2.yili}")


# 10-m
class Xodim():
    def __init__(self, ism, lavozim, maosh):
        self.ism = ism
        self.lavozim = lavozim
        self.maosh = maosh

x1 = Xodim("Ali", "Dasturchi", "1000")
x2 = Xodim("Vali", "Manager", "1500")
x3 = Xodim("Hasan", "Dizayner", "1200")

print(f"1 - xodimning ismi: {x1.ism} lavozimi :{x1.lavozim} maoshi: {x1.maosh}")
print(f"2 - xodimning ismi: {x2.ism} lavozimi :{x2.lavozim} maoshi: {x2.maosh}")
print(f"3 - xodimning ismi: {x3.ism} lavozimi :{x3.lavozim} maoshi: {x3.maosh}")



# 11-m
class Talaba():
    def __init__(self, ism, yosh, kurs, fakultet):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs
        self.fakultet = fakultet

t1 = Talaba("Ali", "20", "2", "IT")
t2 = Talaba("Vali", "22", "3","Iqtisod")

print(f"1 - talabaning ismi: {t1.ism}, yoshi: {t1.yosh} kursi: {t1.kurs} fakulteti: {t1.fakultet}")
print(f"2 - talabaning ismi: {t2.ism}, yoshi: {t2.yosh} kursi: {t2.kurs} fakulteti: {t2.fakultet}")

# 12-m
class Kitob():
    def __init__(self, nomi, muallif, janr, narx):
        self.nomi = nomi
        self.muallif = muallif
        self.janr = janr
        self.narx = narx

kitob1 = Kitob("O'tgan kunlar", "Abdulla Qodiriy", "roman", "50000")
kitob2 = Kitob("Alkimyogar", "Paulo Coelho", "fantastik", "40000")

print(f"1-kitobning nomi: {kitob1.nomi} muallifi: {kitob1.muallif} janri: {kitob1.janr} narxi: {kitob1.narx}")
print(f"2-kitobning nomi: {kitob2.nomi} muallifi: {kitob2.muallif} janri: {kitob2.janr} narxi: {kitob2.narx}")

# 13-m
class Telefon():
    def __init__(self, model, rang, narx, xotira):
        self.model = model
        self.rang = rang
        self.narx = narx
        self.xotira = xotira

tel1 = Telefon("iPhone 13", "qora", "1200", "128GB")
tel2 = Telefon("S21", "oq", "900", "256GB")

print(f"1 - telefonning modeli: {tel1.model} rangi: {tel1.rang} narxi: {tel1.narx} xotirasi: {tel1.xotira} ")
print(f"2 - telefonning modeli: {tel2.model} rangi: {tel2.rang} narxi: {tel2.narx} xotirasi: {tel2.xotira} ")
