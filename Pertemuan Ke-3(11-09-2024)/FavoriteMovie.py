movie_count = 0
max_ascii = 0
best_movie = ""

for i in range(7):
    movie = input()
    if movie == 'STOP':
        break

    movie_count += 1
    current_ascii = 0
    length_of_movie = len(movie)

    for char in movie:
        if char.isupper():
            current_ascii += ord(char) - length_of_movie
        elif char.islower():
            current_ascii += ord(char) - (2 * length_of_movie)
        else:
            current_ascii += ord(char)

    if current_ascii > max_ascii:
        max_ascii = current_ascii
        best_movie = movie

if movie_count >= 7:
    print("The limit is reached.")

print(f"The best movie for you is {best_movie} with {max_ascii} ASCII sum.")