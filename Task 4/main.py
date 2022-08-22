# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 
class Movie():
    def __init__(self, title,director,budget):
        self.title = title
        self.director = director
        self.budget = budget    
    def wasExpensive(self):
        return self.budget > 100000000

movies_list = []

movie = [Movie("Krikštatėvis", "F. F. Copolla", 6000000), Movie("Krikštatėvis 2", "F. F. Copolla", 13000000), Movie("Krikštatėvis 3", "F. F. Copolla", 54000000)]

for x in movie:
    if x.title == "Krikštatėvis 2": is_best = True
    else: is_best = False
    print(x.title, "\nAr brangus:", x.wasExpensive(),"\nAr vis tiek pats geriausias?:",is_best)