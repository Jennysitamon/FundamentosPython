#function input  -> retorna string
name =input('Cómo te llamas? ')
age= int(input('Cuantos años tienes? '))
future= int(input('Cuantos años más? '))

print("Hola "+ name)
print("En " + str(future) + " años tendras " +str( age +future))

#format String
"""
    Hola Jenysita, en tres años tendras 22
"""
text_complete= "Hola {}, en {} años tendras {} años"
print(text_complete.format(name, future, age + future))

print(f"Hola { name }, en { future } años tendras { age + future } años")



