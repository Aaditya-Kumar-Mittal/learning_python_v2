movies = []

num = int(input("How many movies do you want to enter? "))

for i in range(num):
    movie = input(f"Enter the name of movie {i+1}: ")
    movies.append(movie)

print("\nYou have entered the following movies:")
for movie in movies:
    print(movie)