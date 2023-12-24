'''
class methods 1 of 2
class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter +=1

    @classmethod
    def get_internal(cls):
        return '# of objects created: {}'.format(cls.__internal_counter)

print(Example.get_internal())

example1 = Example(10)
print(Example.get_internal())

example2 = Example(99)
print(Example.get_internal())
'''

'''
class methods 2 of 2
class Car:
    def __init__(self, vin):
        print('Ordinary __init__ was called for', vin)
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand):
        print('Class method was called')
        _car = cls(vin)
        _car.brand = brand
        return _car

car1 = Car('ABCD1234')
car2 = Car.including_brand('DEF567', 'NewBrand')

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)
'''

'''
static methods 1 of 2
class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban
            
    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False
'''

'''
static methods 2 of 2
class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban
            
    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False


account_numbers = ['8' * 20, '7' * 4, '2222']

for element in account_numbers:
    if Bank_Account.validate(element):
        print('We can use', element, ' to create a bank account')
    else:
        print('The account number', element, 'is invalid')
'''

'''
Using static and class methods - comparison
The time has come to compare the use of class and static methods:
* a class method requires 'cls' as the first parameter and a static method does
not;
* a class method has the ability to access the state or methods of the class,
and a static method does not;
* a class method is decorated by '@classmethod' and a static method by
'@staticmethod';
* a class method can be used as an alternative way to create objects, and a
static method is only a utility method.
'''

class Lux_Watch:
    __watches_created = 0

    def __init__(self) -> None:
        Lux_Watch.__watches_created += 1

    @classmethod
    def engrave(cls, engraving:str):
        _lux_watch = cls()
        _lux_watch.engraving = engraving

    @classmethod
    def get_number_of_watches_created(cls) -> str:
        return f'Watches created: {cls.__watches_created}'
    
    @staticmethod
    def validate(engraving:str) -> bool:
        if len(engraving) <= 40:
            if engraving.isalnum():
                return True
        return False
    
watches = []
watches.append(Lux_Watch())
print(Lux_Watch.get_number_of_watches_created())

tests = ["correcttext", "incorrect text", "foo@baz.com"]
for test in tests:
    if Lux_Watch.validate(test):
        watches.append(Lux_Watch.engrave(test))
    print(Lux_Watch.get_number_of_watches_created())

