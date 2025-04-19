class Production:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        self.played = 0

    def play(self):
        self.played += 1

class Movie(Production):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"Tytuł: {self.title} ({self.year}), Liczba odtworzeń: {self.played}"
    
class Series(Production):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
    
    def __str__(self):
        return f"Tytuł: {self.title} ({self.year}), S{self.season:02d}E{self.episode:02d}, Gatunek: {self.genre}"

library = []

movie1 = Movie(title="Pulp Fiction", year=1994, genre="Crime")
movie2 = Movie(title="Django", year=2012, genre="western")
series1 = Series(title="Californication", year=2007, genre="drama", episode=1, season=1)
library.append(movie1)
library.append(movie2)
library.append(series1)

movie1.play()
movie2.play()
movie2.play()
for i in library:
    print(i)