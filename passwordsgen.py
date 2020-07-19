import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8

#random.sample(list/tuple/string, Value)
#Join = assemble les list/tuple en charactére

p = "".join(random.sample(s, passlen))
print(p)