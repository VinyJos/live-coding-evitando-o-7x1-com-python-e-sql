import random
import pandas as pd


class Team:
    BEST_SCORE = 1837.6  # BRASIL (BRA)

    def __init__(self, content):
        self.teamData = content.split('|')
        self.name = self.teamData[0]
        self.score = float(self.teamData[1])

    def motivate(self):
        """
           A pior seleção da copa (GAN, segundo a FIFA) têm 1393.5 de score, o qual equivale a 75% do melhor score (BRA).
           Sendo assim, para que a aleatoriedade não seja tão determinante, podemos definir um intervalo inicial próximo de 75.

           Por exemplo, GAN poderia ter valores entre 70~75 (aproximadamente). Por outro lado, BRA teria 70~100 (maior chance de vitória).
           1837.6 (BRA) ----- 100
           1393.5 (GAN) -----  X
           """
        self.lastMotivation = random.uniform(70, (self.score * 100) / Team.BEST_SCORE)

        return self.lastMotivation


df = pd.read_csv('data.csv')

bestTeamsByGroup = {}
# fazendo a leitura do csv e separando
for label, content in df.items():
    team1 = Team(content[0])
    team2 = Team(content[1])
    team3 = Team(content[2])
    team4 = Team(content[3])
    # Vai pegar os 4 times da lista, e passar pela função motivate, e o reverse é para deixar o maior para o menor
    bestTeamsByGroup[label] = sorted([team1, team2, team3, team4], key=Team.motivate, reverse=True)


for group, motivatedTeams in bestTeamsByGroup.items():
    print(f'Grupo {group}: ', end="") # end é para não pular linhas
    for team in motivatedTeams:
        print(f"{team.name} ({team.lastMotivation:.2f}) | ", end="") # não precisa colocar o self
    print()
