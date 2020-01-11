# class MyClass:
#     nama = "BabaStudio"
class Person:
    def __init__(obj, name, age):
        obj.name = name
        obj.age = age

    def myfunc(abc):
        print("Hello My Name is" + abc.name)
        print("My age is" + str(abc.age))

# p1 = MyClass()
p1 = Person("John", 36)

p1.myfunc()
# print(p1.nama)