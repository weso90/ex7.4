import random

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
        return f"Tytuł: {self.title} ({self.year}), S{self.season:02d}E{self.episode:02d}, Liczba odtworzeń: {self.played}"

def get_movies(library):
    library = sorted(library, key=lambda movie: movie.title.lower())
    for i in library:
        if isinstance(i, Movie):
            print(i)
        else:
            continue
    return library

def get_series(library):
    library = sorted(library, key=lambda series: series.title.lower())
    for i in library:
        if isinstance(i, Series):
            print(i)
        else:
            continue
    return library

def search(title, library):
    for i in library:
        if title.lower() in i.title.lower():
            print(f"Film/serial {title} znajduje się w bibliotece")
            return True
    print(f"brak filmu/serialu {title} w bibliotece")
    return False

def generate_views(library):
    random_production = random.choice(library)
    play = random.randint(1,100)
    random_production.played =+ play

def generate_views_x10(library):
    for i in range(10):
        generate_views(library)

def top_titles(library, content_type):
    library = sorted(library, key=lambda production: production.played, reverse=True)

    if content_type == "filmy":
        top = [i for i in library if isinstance(i, Movie)]
        print("Najpopularniejsze filmy:")
        for movie in top[:3]:
            print(f"{movie.title} Ilość odtworzeń {movie.played}" )
        return top
    elif content_type == "seriale":
        top = [i for i in library if isinstance(i, Series)]
        print("Najpopularniejsze seriale:")
        for series in top[:3]:
            print(f"{series.title} Ilość odtworzeń {series.played}")


library = []

movie1 = Movie(title="Pulp Fiction", year=1994, genre="Crime")
movie2 = Movie(title="Django", year=2012, genre="western")
movie3 = Movie(title="Gwiezdne wojny nowa nadzieja",year=1977, genre="Science fiction")
movie4 = Movie(title="Chłopaki nie płaczą", year=2000, genre="comedy")
series1 = Series(title="Californication", year=2007, genre="drama", episode=1, season=1)
series2 = Series(title="Dexter", year=2006, genre="drama", episode=2, season=3)
library.append(movie1)
library.append(series1)
library.append(movie2)
library.append(series2)
library.append(movie3)
library.append(movie4)

generate_views_x10(library)
get_movies(library)
get_series(library)
search("deaxter", library)

top_titles(library, "filmy")