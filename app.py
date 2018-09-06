'''
Challenge:
- Create a class named `Person` with suitable attributes and methods
- Create a class named `User` that will represent the user from the previous challenges.
- Class `User` must extend class `Person` and include new attributes and methods for a User
- Using a data structures approach, create a class called `GuestList' that will add, retrieve and handle deleting of users.

NOTE: These classes should work with your API on a new branch called ModularApi
'''
from module import Person, User, GuestList, AppUsers

Person = Person("Haruna","+256775185123","har.mullah@gmail.com","Engineer")

print(Person.description())

user = User("Logan","+211775111223","logan1@gmail.com","Engineer", "Male",45)

print("The user is called {},a {} with age {} years and {} by professional.\
 Contact {} on {} or by email: {}".format(user.name, user.gender, user.age,\
  user.professional, user.name,user.phone,user.email))

guesslist = GuestList()

guesslist.add_user(AppUsers(1, "ibn yusuf", "user@email.com"))
# guesslist.add_user(AppUsers("Doreen", "doreen@email.com"))
# guesslist.add_user(AppUsers("mark", "markn@email.com"))

added_user = guesslist.find_user_by_email(1)
print(added_user)
# klassap = StudentsClass()

# klass.add_student(Student(1, "student", 21))

# addedstudent = klass.find_student_by_id(1)

# print(addedstudent.name)