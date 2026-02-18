##Limpar terminal
import os
def limpar():
    os.system('cls' if os.name=='nt' else 'clear')
limpar()

##Simulador de batalha
my_life=10
class Enemy:
    def __init__(self, name, life, atk, res, sor):
        self.name = name
        self.life = life
        self.atk = atk
        self.res = res
        self.sor = sor

enemy_list = {
    "enemy1": Enemy("Renan", 10, 6, 1, 1),
    "enemy2": Enemy("Fernando", 20, 2, 4, 4),
    "enemy3": Enemy("Andrey", 15, 4, 3, 2)
}

poss_enemies=[enemy_list["enemy1"], enemy_list["enemy2"], enemy_list["enemy3"]]
import random
number = random.randint(0, 2)
now_enemy = poss_enemies[number]

print(f"O {now_enemy.name} quer batalhar!")
fim=0
while fim==0 :
    import random

    number = random.randint(0, 4)
    if number<3:
        dmg= random.randint(6, 10)-now_enemy.res
        now_enemy.life-=dmg
        print(f"O {now_enemy.name} tomou {dmg} de dano")
    else:
        luck=random.randint(0, 10)
        multi=1
        if luck<=now_enemy.sor:
            multi=1.2
       
        dmg= (now_enemy.atk)*multi
        my_life-=dmg
        text=(f"O {now_enemy.name} desviou do golpe! Você tomou {dmg} de dano")
        if luck<=now_enemy.sor:
           text+= ", Foi bem no coração!"


        print(text)

    if now_enemy.life<=0:
        print(f"{now_enemy.name} morreu lol")
        fim=1
   
    if my_life<=0:
        print(f"Você morreu lol")
        fim=1