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