class ClassFather:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def greet(self):
        return f'Hi! My name is {self._name} and i have {self._age} years old!'

class ClassDaughter(ClassFather):
    def greet(self):
        return super().greet()
        


father  = ClassFather('Leonardo', 27)
print(father.greet())
daugther = ClassDaughter('Esmeralda', 15)
print(daugther.greet())
print(ClassDaughter.mro())
help()