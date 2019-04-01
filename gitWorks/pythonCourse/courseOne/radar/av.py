class Av:

    @classmethod
    def checkRadar(cls):
        return f"number of av in Zone is {cls.av_radar}"


    def __init__(self, nom, position, vitesse, palier):
        self._nom = nom 
        self.position= position 
        self.vitesse = 0 
        self.position = position 
        av_radar +=1

    def __repr__(self):
        return f"name  is {self._nom} "
    
    def ouOfCarte(self):
        av.radar -=1
        return f"{self.name} is out of Carte"

    def palier(self):
        return f"{self.palier}"

    def position(self):
        if self.position == 'haut':
            return f"{self.position}"
        elif self.position == 'bas':
            return f"{self.position}"
        elif self.position == 'gauche':
            return f"{self.position}"
        elif self.position == 'droite':
            return f"{self.position}"
        elif self.position == 'diaghautGauche':
            return f"{self.position}"
        elif self.position == 'diaghautDroite':
            return f"{self.position}"        
        elif self.position == 'diagbasGauche':
            return f"{self.position}"
        elif self.position == 'diagbasDroite':
            return f"{self.position}"
        else:
            return f"{self.position}"


    def vitesse(self):
        if self.name == 'low':
            vitesse +=2
            return f"{self.vitesse} /s"
        elif self.name == 'mid':
            vitesse +=3
            return f"{self.vitesse} /s"
        elif self.name == 'high':
            vitesse+= 1
        else:
            return f"Alert => {self.name} controle " 


n= Av("airbus")
print(n.name)