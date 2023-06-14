num = 1
while num <= 10:
    print(num)
    num += 1
    
#for -> iterable es un obj que se puede recorrer 
my_str = "Hola"
for letter in my_str:
    print (letter, end=' ')
print()

my_lista = ["a", "b", "c", 12]
for item in my_lista:
    print(item, end=' ')
print()

# function range()
# rangel (fin)
for i in range(3):
    print(i, end=' ')
print()

#range(ini:fin)
for i in range(3, 6):
    print(i, end=' ');
print()

#range(ini:fin:step)
for i in range(1, 11, 2):
    print(i, end=' ');