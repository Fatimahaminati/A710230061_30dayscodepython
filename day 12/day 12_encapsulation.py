class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary


employee1 = Employee("Amfa", 25, 6000000)

print("Nama:", employee1.get_name())  
print("Usia:", employee1.get_age())   
print("Gaji:", employee1.get_salary())  

employee1.set_salary(8000000)
print("Gaji baru:", employee1.get_salary())  
