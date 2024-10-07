loading_percentage = int(input())

def loading_bar(percentage):
    bar = '[' + '%' * (percentage // 10) + '.' * (10 - percentage // 10) + ']'
    if percentage == 100:
        return f"{percentage}% Complete!\n{bar}"
    else:
        return f"{percentage}% {bar}\nStill loading..."

print(loading_bar(loading_percentage))