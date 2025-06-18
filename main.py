import random
def say_hi():#nieko nepriima, nieko negrazina
    print("sveikuciai")
say_hi()
def say_hi_to(name):#priima kintamaji, nieko negrazina
    print("hi", name)
say_hi_to("Jonas")
say_hi_to("Petras")
vardas = "Klemensas"
say_hi_to(vardas)

def sim_pi():#nieko nepriima, grazina reiksme
    return 3.14
print(sim_pi())
sp = sim_pi()
print(sp)

def sumavimas(a,b):#priima du kintamuosius, grazina reiksme
    return a + b

res = sumavimas(4651,6135)
print(res)

def make_initials(name,surname):
    return (name[0] + surname[0]).upper()

print( make_initials("Naglis","Mockevicius") )

print( make_initials("naglis","mockevicius") )

def make_initials_v2(txt):
    parts = txt.split()
    init = ""
    for pt in parts:
        init += pt[0]
    return init.upper()
print(make_initials_v2("Naglis Mockevicius"))
print(make_initials_v2("Naglis Jonas Mockevicius"))


def calc_age(birth_year=2025):
    return 2025 - birth_year

age = calc_age()
print(age)
age = calc_age(1914)
print(age)

def print_info(name = "", surname = "", birth_year = 0):
    print("mano vardas",name,"pavarde",surname,"gimimo metai",birth_year)


print_info()
print_info("Naglis")
print_info(35)
print_info(surname="Mockevicius",birth_year = 1999)



def generate_rnd_str(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text



txt = generate_rnd_str(10)
print(txt)
for i in txt:
    print(i)





















