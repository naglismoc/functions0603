import random
def say_hi():#nieko nepriima, nieko negrazina
    print("sveikuciai")
say_hi()
def say_hi_to(name):#priima kintamaji, nieko negrazina
    print("hi", name)
say_hi_to("Jonas")
say_hi_to("Petras")

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



































