from typing import List, NamedTuple
import asyncio
import random

# Exercice 1

def addToEach(n: int, lst: List[int]) -> List[int]:
    return [x + n for x in lst]

def removeDuplicates(lst: List[int]) -> List[int]:
    return list(set(lst))

# Exercice 2
class Personne(NamedTuple):
    nom: str
    age: int

def anniversaire(people: List[Personne]) -> List[Personne]:
    return [Personne(p.nom, p.age + 1) for p in people]

async def getRandomNumber() -> int:
    await asyncio.sleep(1)
    return random.randint(1, 100)

async def generateTwoRandomNumbers():
    num1, num2 = await asyncio.gather(getRandomNumber(), getRandomNumber())
    print(f"Random numbers: {num1}, {num2}")

# Exercice 3

class Article(NamedTuple):
    nom: str
    prix: float
    stock: int

def ajouter_article(inventaire: List[Article], article: Article) -> List[Article]:
    return inventaire + [article]

def mettre_a_jour_stock(inventaire: List[Article], nom: str, nouvelle_qte: int) -> List[Article]:
    return [Article(a.nom, a.prix, nouvelle_qte) if a.nom == nom else a for a in inventaire]

def supprimer_article(inventaire: List[Article], nom: str) -> List[Article]:
    return [a for a in inventaire if a.nom != nom]

# Exercice 6 (le dernier)

def detecter_stock_bas(inventaire: List[Article], seuil: int) -> List[str]:
    return [a.nom for a in inventaire if a.stock < seuil]

def passer_commande_reapprovisionnement(inventaire: List[Article], seuil: int, qte_reappro: int) -> List[Article]:
    return [Article(a.nom, a.prix, a.stock + qte_reappro) if a.stock < seuil else a for a in inventaire]


if __name__ == "__main__":
    print("Exercice 1 : Test ajouter a chaque")
    print(addToEach(5, [1, 2, 3]))  

    print("Exercice 1 : Test enelver doublon") 
    print(removeDuplicates([1, 2, 2, 3, 3, 3]))  

    print("Exercice 2 : Test anniversaire")
    personnes = [Personne("Alice", 30), Personne("Bob", 25)]
    print(anniversaire(personnes)) 

    print("Exercice 3 : Tester ajoute article")
    inventaire = [Article("Pomme", 0.5, 100)]
    nouvel_article = Article("Banane", 0.3, 50)
    print(ajouter_article(inventaire, nouvel_article))  

    print("Exercice 3 : Test stock bas")
    print(detecter_stock_bas(inventaire, seuil=80))  


    print("Tester reaprovisionnement")
    print(passer_commande_reapprovisionnement(inventaire, seuil=80, qte_reappro=50))  

    asyncio.run(generateTwoRandomNumbers()) 
