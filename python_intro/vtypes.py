i = 100
f = 3.14
c = 5+4j # 5 + 4 * kok(-1) || kok(-16) = 4*kok(-1)
print(type(i))
print(type(f))
print(type(c))

s = "salam" 
# 'salam' 
s1 = """
salam 
necesen?
"""
print(type(s))
print(type(s1))

b = True # False

print(type(b))

l = [1,2, s, s1, b, ["a", "b"]]
print(type(l))

t = (1,2, s, s1, b, ["a", "b"])
print(type(t))

se = {"Idris", "Aqil", "Tural", "Samir", "Amil"}
print(se)
print(type(se))

d = {
    "name": "Idris",
    "surname": "Shabanli"
}

print(d)
print(type(d))