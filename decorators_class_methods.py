# Decorador para inserir o dundermethod nas classes.
def my__repr__(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def add_repr(cls):
    cls.__repr__ = my__repr__
    return cls

# Decorador de método da classe Team.
def biggest_fans(method): 
    def func_intern(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        
        if 'Flamengo' in result:
            return f'{self.name} tem a maior torcida do mundo!'
        return f'{result} tem uma torcida qualquer.'
    
    return func_intern

def planet_name(method):
    def inter_func(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        
        if result == 'Terra':
            return 'Você está em casa!'
        return f'O planeta é {result}'
    return inter_func
    

# Usando decorador na classe para definir o __repr__
@add_repr
class Team:
    def __init__(self, team_name):
        self.name = team_name
    @biggest_fans # Usando decorador no método.
    def speak_name_team(self):
        return f'{self.name}'


# Definido internamente o __repr__
class Planet:
    def __init__(self, planet_name:str):
        self.planet_name = planet_name.capitalize()

    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}{class_dict}'
        return class_repr
    @planet_name
    def speak_name_planet(self):
        return f'{self.planet_name}'

flamengo = Team('Flamengo')
vasco = Team('Vasco')
terra = Planet('Terra')
saturno = Planet('Saturno')

print(terra)
print(saturno)
print(flamengo)
print(vasco)
print(flamengo.speak_name_team())
print(vasco.speak_name_team())
print(terra.speak_name_planet())
print(saturno.speak_name_planet())
