import random

class Media:
    def __init__(self, title, release_year, genre, views=0):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = views

    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Movie(Media):
    pass


class Series(Media):
    def __init__(self, title, release_year, genre, episode_number, season_number, views=0):
        super().__init__(title, release_year, genre, views)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02}E{self.episode_number:02}"


library = []


def get_movies():
    movies = [media for media in library if isinstance(media, Movie)]
    return sorted(movies, key=lambda x: x.title)


def get_series():
    series = [media for media in library if isinstance(media, Series)]
    return sorted(series, key=lambda x: x.title)


def search(title):
    results = [media for media in library if title.lower() in media.title.lower()]
    return results


def generate_views(item):
    views = random.randint(1, 100)
    item.views += views


def generate_views_multiple(index, times=10):
    for _ in range(times):
        generate_views(library[index])


def top_titles(content_type, limit=5):
    if content_type == "movies":
        items = get_movies()
    elif content_type == "series":
        items = get_series()
    else:
        return "Wpisz 'movies' lub 'series'."

    sorted_items = sorted(items, key=lambda x: x.views, reverse=True)
    return sorted_items[:limit]


# biblioteka filmów
library.append(Movie("Chłopaki nie płaczą", 2000, "Comedy"))
library.append(Movie("Kiler", 1997, "Comedy"))
library.append(Movie("Kiler-ów 2-óch", 1997, "Comedy"))
library.append(Movie("Poranek kojota", 2001, "Comedy"))
library.append(Movie("E=mc2", 2002, "Comedy"))
library.append(Movie("Trzy Billboardy za Ebbing, Missouri", 2017, "Thriller"))
library.append(Movie("Joker", 2019, "Thriller"))
library.append(Movie("Bad Boys: Ride or Die", 2024, "Action"))

# biblioteka seriali
library.append(Series("Ranczo", 2006, "Comedy", 1, 1))
library.append(Series("Ranczo", 2006, "Comedy", 1, 2))
library.append(Series("Ranczo", 2006, "Comedy", 1, 3))
library.append(Series("Ranczo", 2006, "Comedy", 1, 4))
library.append(Series("Ranczo", 2006, "Comedy", 2, 1))
library.append(Series("Ranczo", 2006, "Comedy", 2, 2))
library.append(Series("Ranczo", 2006, "Comedy", 2, 3))
library.append(Series("Ranczo", 2006, "Comedy", 2, 4))
library.append(Series("Ranczo", 2006, "Comedy", 2, 5))
library.append(Series("Ranczo", 2006, "Comedy", 2, 6))
library.append(Series("Top Gear", 2011, "automotive program", 1, 1))
library.append(Series("Top Gear", 2011, "automotive program", 1, 2))
library.append(Series("Top Gear", 2011, "automotive program", 1, 3))
library.append(Series("Top Gear", 2011, "automotive program", 1, 4))
library.append(Series("Top Gear", 2011, "automotive program", 2, 1))
library.append(Series("Top Gear", 2011, "automotive program", 2, 2))
library.append(Series("Top Gear", 2011, "automotive program", 2, 3))
library.append(Series("Top Gear", 2011, "automotive program", 2, 4))
library.append(Series("Top Gear", 2011, "automotive program", 3, 1))
library.append(Series("Top Gear", 2011, "automotive program", 3, 2))
library.append(Series("Top Gear", 2011, "automotive program", 3, 3))
library.append(Series("Top Gear", 2011, "automotive program", 3, 4))
library.append(Series("Rojst", 2018, "thriller", 1, 1))
library.append(Series("Rojst", 2018, "thriller", 1, 2))
library.append(Series("Rojst", 2018, "thriller", 1, 3))
library.append(Series("Rojst", 2018, "thriller", 2, 1))
library.append(Series("Rojst", 2018, "thriller", 2, 2))
library.append(Series("Rojst", 2018, "thriller", 2, 3))

# play
generate_views_multiple(0)
generate_views_multiple(3)

# wyszukiwarka
search_results = search("Kiler")
for result in search_results:
    print(result)

# najpopularniejsze
top_movies = top_titles("movies", 2)
top_series = top_titles("series", 2)

print("\nTop Movies:")
for movie in top_movies:
    print(movie)

print("\nTop Series:")
for series in top_series:
    print(series)