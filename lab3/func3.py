from functions2 import Movies

def score_5_5(movie_name):
    for m in Movies:
        if m['name'] == movie_name:
            if m['imdb'] > 5.5:
                return True
    return False

print(score_5_5('Love'))


def sublist_5_5():
    score_above_5_5 = []
    for m in Movies:
        if m['imdb'] > 5.5:
            score_above_5_5.append(m['name'])
    return score_above_5_5

print(sublist_5_5())


def category_list(category):
    category_movie = []
    for m in Movies:
        if m['category'] == category:
            category_movie.append(m['name'])
    return category_movie

print(category_list('Romance'))


def computes_average():
    sum = 0
    count = len(Movies)
    for m in Movies:
        sum += m['imdb']
    return sum/count

print(round(computes_average(), 2))


def category_computes_average(category):
    sum_category_movie = 0
    for m in Movies:
        if m['category'] == category:
            sum_category_movie += m['imdb']
    return sum_category_movie/len(category_list(category))

print(category_computes_average('Romance'))