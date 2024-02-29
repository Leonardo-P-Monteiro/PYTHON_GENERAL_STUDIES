import enum

class DayWeek(enum.Enum):
    SUNDAY = 'sunday'
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'


# for day in DayWeek:
#     print(f'Today is {day.name}')

# DayWeek.name > traz o "nome da chave".
# DayWeek.value > traz o "valor da chave".

def dayweek(enum: DayWeek):
    
    if not isinstance(enum, DayWeek):
        raise Exception('Day not found.')

    print(f'Today is {enum.value}')
    print(f'this is the name of the enum: {enum.name}')


dayweek(DayWeek.SATURDAY)
