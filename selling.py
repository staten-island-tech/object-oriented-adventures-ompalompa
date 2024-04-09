import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

class Movies:
    def __init__(self, data_path):
        with open(data_path, encoding="utf8") as file:
            self.data = json.load(file)

    def title_print(self):
        for movie in self.data:
            print(movie['title'])

    def after_year(self):
        year = int(input("Enter a year: "))
        for movie in self.data:
            if year < movie['year']:
                print(movie['title'])

    def between_years(self):
        year1 = int(input("Enter the lowest year: "))
        year2 = int(input("Enter the highest year: "))

        for movie in self.data:
            if year1 < movie['year'] < year2:
                print(movie['title'])

    def during_year(self):
        year = int(input("Enter a year: "))
        for movie in self.data:
            if year == movie['year']:
                print(movie['title'])

    def movie_search(self):
        title = input("Enter a title: ").lower()
        for movie in self.data:
            if title in movie['title'].lower():
                print(movie['title'])

    def genre_search(self):
        genre = input("Enter a genre: ").lower()
        for movie in self.data:
            if genre in [g.lower() for g in movie['genres']]:
                print(movie['title'])

player = Movies()
player.genre_search()