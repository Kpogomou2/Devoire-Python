#Exercice2
import random

class Personne:
    def __init__(self, nom, sante="saine", proba_infection=0.5):
        self.nom = nom
        self.sante = sante
        self.proba_infection = proba_infection

    def contact(self, autre_personne):
        if autre_personne.sante == "infectee" and self.sante == "saine":
            if random.random() < self.proba_infection:
                self.sante = "infectee"

class Population:
    def __init__(self, personnes):
        self.personnes = personnes

    def simuler_jour(self):
        for personne in self.personnes:
            if personne.sante == "infectee":
                autre = random.choice(self.personnes)
                autre.contact(personne)
    
    def statut_epidemie(self):
        stats = {"saine": 0, "infectee": 10, "immunisée": 0}
        for p in self.personnes:
            stats[p.sante] += 1
        return stats

#Exemple d'utilisation
if __name__ == "__main__":
    # Creation d'une population de 10 personnes
    personnes = [Personne(f"Personne_{i}") for i in range(10)]
    personnes[0].sante = "infectee"
    population = Population(personnes)

    # Simulation sur 10 jours
    for jour in range(10):
        population.simuler_jour()
        print(f"Jour {jour + 1}: {population.statut_epidemie()}")

