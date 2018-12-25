# -*- coding:utf-8 -*-
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()


#9-4 就餐人数
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("Restaurant's name is " + self.name.title() )
        print("Cuisine type is " + self.type.title())
        print('How many people have dinner in the restaurant?  ' + str(self.number_served))
    def open_restaurant(self):
        print('In operation')
    def set_number_served(self,people):
        self.number_served = people
    def increment_number_served(self,people):
        self.number_served += people

restaurant = Restaurant('金拱门','快餐')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(10)
restaurant.describe_restaurant()
restaurant.increment_number_served(3)
restaurant.describe_restaurant()

#9-5 尝试登录次数
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print("First name is " + self.first_name.title() )
        print("Last name is " + self.last_name.title())

    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print('Hello ' + full_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
user1 = User('ergou','yang')

user1.describe_user()
user1.increment_login_attempts()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)


#9-6 冰淇淋小店
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("Restaurant's name is " + self.name.title() )
        print("Cuisine type is " + self.type.title())
        print('How many people have dinner in the restaurant?  ' + str(self.number_served))
    def open_restaurant(self):
        print('In operation')
    def set_number_served(self,people):
        self.number_served = people
    def increment_number_served(self,people):
        self.number_served += people

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        Restaurant.__init__(self,restaurant_name,cuisine_type)
        self.flavors = ['apple','milk']
    def show(self):
        print(self.flavors)

restaurant1 = IceCreamStand('金拱门','快餐')
restaurant1.describe_restaurant()
restaurant1.show()



#9-7 管理员
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print("First name is " + self.first_name.title() )
        print("Last name is " + self.last_name.title())

    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print('Hello ' + full_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self,first_name,last_name):
        User.__init__(self,first_name,last_name)
        self.privileges = ["can add post" ,"can delete post" ,"can ban user"]
    def show_privileges(self):
        print(self.privileges)

user = Admin('ergou','yang')
user.show_privileges()
'''

#9-8 权限
class Privileges():
    def __init__(self):
        self.privileges = ["can add post" ,"can delete post" ,"can ban user"]
    def show_privileges(self):
        print(self.privileges)

class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print("First name is " + self.first_name.title() )
        print("Last name is " + self.last_name.title())

    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print('Hello ' + full_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self,first_name,last_name):
        User.__init__(self,first_name,last_name)
        self.privileges = Privileges()


user = Admin('ergou','yang')
user.privileges.show_privileges()

#9-14 骰子
from random import randint

class Die():
    def __init__(self):
        self.sides = 6
    def roll_die(self):
        x = randint(1, self.sides)
        print(str(x))

die = Die()
for x in range(0,10):
    die.roll_die()

die.sides = 10
for x in range(0,10):
    die.roll_die()

die.sides = 20
for x in range(0,10):
    die.roll_die()




from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
      print(name.title() + "'s favorite language is " +
          language.title() + ".")


print("\033[1;33;44m需要变颜色的字符串\033[0m")








