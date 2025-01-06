"""
Class Basic
"""
class Person:
    def __init__(self,name,age,address,wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet #private class attribute

    def pay(self,amount):
        if amount > self.__wallet:
            print('Not Enough')
            return
        self.__wallet -= amount
        print('You has {0} left'.format(self.__wallet))

maria = Person('Maria',20,'Seoul',1000)
maria.pay(500)


"""
Class Attribute
"""
class Person:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.bag.append("Book")

maria = Person()
maria.bag.append("Key")

print(james.bag)
print(maria.bag)


'''
Static Method

1) 메서드를 사용할시에 인스턴스를 통하지 않고 클래스에서 바로 호출
2) 인스턴서의 상태를 변화시키지 않는 메서드를 만들때 사용
3) 메서드 위에 @staticmethod 사용, 정적 메서드는 매개변수에 self 미지정
'''

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def mul(a,b):
        print(a*b)

Calc.add(10,20)
Calc.mul(10,20)


'''
Class Method

@classmethod 사용
클래스 메소드는 첫 번째 매개벼수에 cls 사용
'''

class Person:
    count = 0

    def __init__(self):
        Person.count += 1 #인스턴스가 만들어질때 카운트 추가

    @classmethod
    def print_count(cls): #cls 매개변수를 통하여 클래스 속성에 접근 가능
        print('{0}명 생성되었습니다.'.format(cls.count))

james = Person()
maria = Person()
Kim = Person()

Person.print_count()

'''
Class 상속 (inheritance)
'''

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'Hello'

    def greeting(self):
        print("Hello")

class PersonList:
    def __init__(self):
        self.person_list = []

    def append_person(self,person):
        self.person_list.append(person)

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__() #super()로 기반클래스의 __init__ 메서드호출
        self.school = 'Python'

    def study(self):
        print('Study')


james = Student()
james.greeting()
james.study()
print(james.school)
print(james.hello)


'''
Class Overriding

어떤 이름이 같은 메서드 이름으로 계속 사용되어야 할때 메서드 오버라이딩 활용
'''

class Person:
    def greeting(self):
        print('Hello')

class Student(Person):
    def greeting(self):
        #super().greeting()
        print('Hello WOrld')

james = Student()
james.greeting()

"""
Class 다중상속
"""

class A:
    def greeting(self):
        print('This is A')

class B(A):
    def greeting(self):
        print('This is B')

class C(A):
    def greeting(self):
        print('This is C')

class D(B,C):
    pass

x = D()
x.greeting() #--> "This is B"
print(D.mro()) #Method 탐색 순서 확인하기, 다중상속을 한다면 클래스의 목록 중 왼쪽에서 오른쪽 순서


"""
Abstract Class

메서드의 목록만 가진 클래스, 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용

import abc 모듈 필요 및 metaclass = ABCMeta 지정, @abstractmethod
"""
from abc import * 

class StudentBase(metaclass=ABCMeta):
    #추상클래스는 인스턴스를 만들수 없으므로 pass를 통해 빈 메서드로 만들어 놓을 것
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('Study')

    def go_to_school(self):
        print('Go to School')

lee = Student()

# go_to_school 메소드 미 생성시 
# TypeError: Can't instantiate abstract class Student with abstract method go_to_schol
lee.study()
