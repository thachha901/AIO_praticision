from abc import ABC, abstractmethod

class Ward:
    def __init__(self, name: str):
        self.name = name
        self.list_people = list()
    
    def add_Person(self, person):
        self.list_people.append(person)
        
    def describe(self):
        print(f"Name: {self.name}")
        for p in self.list_people:
            p.describe()
            
    def compute_Average_Age(self):
        total_age = sum(p.getAge() for p in self.list_people)
        return total_age / len(self.list_people) if self.list_people else 0
            
    def count_Doctors(self):
        return sum(1 for p in self.list_people if isinstance(p, Doctor))
    
    def sortAge(self):
        return self.list_people.sort(key=lambda p: p.getAge(), reverse=True)
    
    def printWard(self):
        print(f"Ward Name: {self.name}")
        for p in self.list_people:
            print(f"Name: {p.name}, Year of Birth: {p.yob}, Age: {p.getAge()}")
    
class Person(ABC):
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob
        
    def getAge(self):
        return 2025 - self.yob
        
    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
    
    def describe(self):
        print(f"Student {self.name} was born in {self.yob} and is in grade {self.grade}.")

class Doctor(Person):
    def __init__(self, name, yob, spe):
        super().__init__(name, yob)
        self.spe = spe
    
    def describe(self):
        print(f"Doctor {self.name} was born in {self.yob} and Specialist: {self.spe}.")
        
class Teacher(Person):
    def __init__(self, name, yob, sub):
        super().__init__(name, yob)
        self.sub = sub
    
    def describe(self):
        print(f"Teacher {self.name} was born in {self.yob} and teaches subject {self.sub}.")
        



if __name__ == "__main__":
    student1 = Student("Alice", 2005, 10)
    student1.describe()
    doctor1 = Doctor("Dr. Smith", 1980, "Cardiology")
    doctor1.describe()
    teacher1 = Teacher("Mr. Brown", 1990, "Mathematics")
    teacher1.describe()
    
    ward = Ward("General Ward")
    ward.add_Person(student1)
    ward.add_Person(doctor1)
    ward.add_Person(teacher1)
    ward.describe()
    
    result = ward.count_Doctors()
    print(result)
    ward.sortAge()
    ward.printWard()
    print(ward.compute_Average_Age())