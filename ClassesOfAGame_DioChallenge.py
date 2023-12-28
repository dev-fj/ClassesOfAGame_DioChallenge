#%%

#1: Gerando classe 

class Character():
    
    def __init__(self, name, age, kind1, act1):
        self.name = name
        self.age = age
        self.kind1 = kind1
        self.act1 = act1

    def act(self):
        self.act1 = self.act1.upper()
        print(f"The {self.kind1} {name} used {self.act1}!!\n")


    
#2: Gerando variáveis que serão atribuídas as classes


input("Welcome to Anolya! A world of Magic and Adventure!\n Are you ready to ENTER this world?\n")

while True:
    name = input("Alright, so how would you want to be known?\n").upper()
    if name.strip():
        break
    else:
        print("Hurry up, tell me your name before we get shot by an arrow! \n")

input(f"I see, nice to meet you {name}! My name is Fahon! And I'll be your guide... \n")

while True:

    age = input(f"And how old are you {name}?\n")
    try:
        age = int(age)
        break
    except ValueError:
        print("Here in Anolya we count age with numbers, gimme numbers lad!\n")
input(f"ohh boi! I remember when I was {age}, it was when I defeated my first dragon, but that's another story, we need to focus... \n")

#%%



def kind_p(kind):
    

    while kind == None:
        kind_str = input("Last but not least, tell me, what do you like more: swords(1), magic(2), healing powers(3) or shurikens(4) ? \n")
        

        try:    
            kind = int(kind_str)


            if  1 <= kind <= 4:

                if kind == 1:
                    kind = {"kind":"Warrior",
                    "act":"Sacred sword"}
                    
                elif kind == 2:
                    kind = {"kind":"Mage",
                    "act":"Fire balls"}
                   

                elif kind == 3:
                    kind = {"kind":"Monk",
                    "act":"Source of life on allies"}


                elif kind == 4:
                    kind = {"kind":"Ninja",
                    "act":"Attack from the shadows"}
                   

                    
            else:
                kind = None
                print("No no no, you need to choose a number between 1 and 4\n")
        
        except ValueError:
                print("No no no, you need to choose a number between 1 and 4\n")
    return kind



kind = None

resultk = kind_p(kind)
kind1 = resultk['kind']     
act1 = resultk['act']

print(f"Ohhh ! {resultk['kind']} it is a kind of fighter that I really respect!\n")
input("Get ready! There is a challange up ahead! Do something quick! \n")

# dic = {"kind":"warrior","act":"sacred sword" }

#%%
#3: Gerando objetos

hero = Character(name, age, kind1, act1)

#4: Utilizando os métodos
part1 = hero.act()


