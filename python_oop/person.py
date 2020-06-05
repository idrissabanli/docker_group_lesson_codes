class Person():
    '''
    Bu shexs sinifidir. onun yasi ve full_name-i movcuddur
    '''
    _full_name = 'sklnflksnskns'
    
    def __init__(self):
        '''
        bu person class-inin initialize funksiyasidir
        '''
        self.__age = 0

    @property
    def age(self):
        '''
        bu age-in getter methodudur!
        '''
        return person.__age

    @age.setter
    def age(self, c_age):
        if 0<c_age<150 and self.__age < c_age:
            self.__age = c_age
        else:
            print(f'Yasi {c_age}-e deyise bilmezsiniz!!')

person = Person()
print(person._full_name)
person.age = 6
print('age=', person.age)
person.age = person.age +  5
print('age=', person.age)
print(help(person))
