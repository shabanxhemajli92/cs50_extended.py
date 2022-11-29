import datetime
class User:
    def __init__(self,full_name, last_name,birthday):
        self.name = full_name
        self.last_name = last_name
        self.birthday=birthday
        
        
        name_pieces=full_name.split(" ")
        self.first_name=name_pieces[0]
        self.last_name=name_pieces[-1]



    def age(self):
        today=datetime.date(2001, 5 , 12)
        yyyy=int(self.birthday[0:4])
        mm=int(self.birthday[4:6])
        dd=int(self.birthday[6:8])
        date_of_birth=datetime.date(yyyy,mm,dd)
        age_in_days=(today - date_of_birth).days
        age_in_years= age_in_days/365
        return int(age_in_years)
user=User("Dave Bowman","19710715") 
print(user.age()) 
