class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name= first_name
        self.last_name= last_name
        self.email=email
        self.age=age
        self.is_rewards_member =False
        self.gold_card_points = 0

    def display_info(self):
        print(f"user first name:{self.first_name}")
        print(f"user last name:{self.last_name}")
        print(f"user email:{self.email}")
        print(f"user age:{self.age}")
        print(f"is_rewards_member:{self.is_rewards_member}")
        print(f"gold_card_points:{self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member == True:
            print(f"ERROR : {self.first_name} is member" )
        else:
            self.is_rewards_member =True
            self.gold_card_points =200
        return(self)
    def decrease_points(self,amount):
        if amount <=self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("not enough points")
        return(self)
         
omar = User("omar","daly","omardaly@gmail.fr",21)
ali = User("ali","doudi","alidoudiy@gmail.fr",40)
sbou3i = User("sbou3i","labyeth","sbou3ilabith@gmail.fr",30)
omar.display_info()
ali.display_info()
sbou3i.display_info()
omar.enroll()
ali.enroll()
ali.enroll()
omar.decrease_points(50)
ali.decrease_points(80)
sbou3i.decrease_points(40)
omar.display_info()