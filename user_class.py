class User:
    pass

user1=User()
user1.first_name="Dave"
user1.last_name="Bowman"
user2=User()
user2.first_name="John"
user2.last_name="Doe"
print(user1.first_name, user1.last_name)
print(user2.first_name, user2.last_name)

user1.age=45
user2.favourite_sports_team="New England Patriots"

print(user2.favourite_sports_team)
print(user1.first_name, user1.last_name,"is " ,user1.age,"years old")