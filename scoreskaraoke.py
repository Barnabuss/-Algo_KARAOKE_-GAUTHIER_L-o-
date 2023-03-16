class Karaoke:
    def __init__(self,Nummusique,Listemusique,Ajoutdemusqiue,Listeplayer):
        self.Nummusique = Nummusique
        self.Listemusique =Listemusique
        self.Ajoutdemusqiue = Ajoutdemusqiue
        self.Listeplayer = Listeplayer
        self.Listemusique = []
        self.Ajoutdemusqiue = []
        self.Listeplayer = []








class player:
    def __init__(self,pseudo,scorePlayer,scoremusique):
        self.pseudo=pseudo
        self.scorePlayer=scorePlayer
        self.scorePlayer= [0,0,0,0,0]
        self.scoremusique=scoremusique

    def affichepseudo(self):
        print ("Bonjour " + self.pseudo) 


    def Scores(self):
        print ("Ton score est de " + str(self.scoremusique))

    def Ajoutscore (self,musiques,newScore):
        if(newScore > self.scorePlayer [musiques] and newScore <= 50 and newScore >= 100):
            self.scorePlayer[musiques] = newScore

        if (newScore < 0 or newScore > 100):
            print("ce score est incorrect")

    
    def afficherTotal(self):
        scoretotal = 0
        for i in range(len(self.scorePlayer)):
            scoretotal = scoretotal + self.scorePlayer[i]
        print (scoretotal)

    def moyennescore (self):
        self.scoretotal = 0
        for i in range(len(self.scorePlayer)):
            self.scoretotal = self.scoretotal + self.scorePlayer[i]
        self.moyenne = (self.scoretotal/5)
        print (self.moyenne)



Player = player ("player",70,80)


Player.affichepseudo()
Player.Scores()
Player.Ajoutscore(1,85)
Player.Ajoutscore(2,95)
Player.Ajoutscore(3,65)
Player.Ajoutscore(4,55)
Player.afficherTotal()