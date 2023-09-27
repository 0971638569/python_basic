class Person:
    #thuộc tính
    def __init__(self, name, age, gender):
        print("Class Person được khởi tạo!")
        print("Name: %s - Age: %d - Male: %s" %(name, age, gender))
        self.name, self.age, self.gender = name, age, gender

    #phương thức
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setGender(self, gender):
        self.gender = gender

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def __del__(self):
        print('Class Person được hủy')
        del self.name, self.age, self.gender

class Rank(Person):
    def __init__(self, name, age, gender, rank):
        print("Class Rank được khởi tạo!")
        self.name, self.age, self.gender, self.rank = name, age, gender, rank
    
    def setRank(self, rank):
        self.rank = rank
    
    def getRank(self):
        print('super', super().getName())
        return self.rank
    
    def __del__(self):
        print('Class Rank được hủy')
        del self.name, self.age, self.gender, self.rank

class First:
    def getClass(self):
        print("Class Fist")
        
class Second(First):
    def getClass(self):
        print("Class Second")
        super().getClass()
         
person1 = Person('Nguyen Van A', 22, 'male');
person2 = Person('Nguyen Thi B', 26, 'female');
person3 = Rank('Nguyen Van K', 33, 'male', 'top1')
third = Second()
third.getClass()

print("Name: ", person1.getName())
print("Age: ", person1.getAge())
print("Gender: ", person1.getGender())
print('--------------------------------------------------')
print("Name: ", person2.getName())
print("Age: ", person2.getAge())
print("Gender: ", person2.getGender())
print('--------------------------------------------------')
print("Name: ", person3.getName())
print("Age: ", person3.getAge())
print("Gender: ", person3.getGender())
print("Rank: ", person3.getRank())
print('--------------------------------------------------')

person1.setName('Nguyen Thi H')
person1.setAge(33)
person1.setGender('female')
person2.setName('Nguyen Thi T')
person2.setAge(44)
person2.setGender('female')

print("Name: ", person1.getName())
print("Age: ", person1.getAge())
print("Gender: ", person1.getGender())
print('--------------------------------------------------')
print("Name: ", person2.getName())
print("Age: ", person2.getAge())
print("Gender: ", person2.getGender())

