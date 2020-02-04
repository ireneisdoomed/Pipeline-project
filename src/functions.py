from justwatch import JustWatch
from bs4 import BeautifulSoup
import requests

# APIs related functions

def netflix(title):
    just_watch = JustWatch(country='US')
    try:
        request = just_watch.search_for_item(query=title)
        offers = request["items"][0]["offers"]
        for e in offers:
            if e["monetization_type"] == "flatrate" and e["provider_id"] == 8:
                return True
        return False
    except Exception as e:
        return None

def hbo(title):
    just_watch = JustWatch(country='US')
    try:
        request = just_watch.search_for_item(query=title)
        offers = request["items"][0]["offers"]
        for e in offers:
            if e["monetization_type"] == "flatrate":
                if e["provider_id"] == 118 | 27:
                    return True
        return False
    except Exception as e:
        return None

def amazon(title):
    just_watch = JustWatch(country='US')
    try:
        request = just_watch.search_for_item(query=title)
        offers = request["items"][0]["offers"]
        for e in offers:
            if e["monetization_type"] == "flatrate":
                if e["provider_id"] == 9 | 194:
                    return True
        return False
    except Exception as e:
        return None

# Web Scraping of Rotten Tomatoes to obtain de Users Ratings

def rating(title):
    baseUrl = "https://www.rottentomatoes.com/m/"
    title = title.replace("The ", "")
    title = title.replace(" ", "_")    
    title = title.replace("'", "")
    res = requests.get(baseUrl+title).text
    soup = BeautifulSoup(res, 'html.parser')
    try:
        rating = soup.select('.mop-ratings-wrap__percentage')[1].text.strip()[:-1]
        normRating = round(int(rating) * 0.01 * 5)
    except Exception as e:
        return None
    return normRating


# Data Analysis functions

def whichGenre(genre):
    df[df["Genre"].str.contains(genre)]

def whereisit(title):
    if df[(df["Title"] == title) & (df["Netflix"] == True)].iloc[0].get("Netflix"):
        return "You can stream this movie on Netflix."
    
    if df[(df["Title"] == title) & (df["Netflix"] == True)].iloc[0].get("HBO"):
        return "You can stream this movie on HBO."
    
    if df[(df["Title"] == title) & (df["Netflix"] == True)].iloc[0].get("Amazon Prime"):
        return "You can stream this movie on Amazon Prime."

def theRating(title):
    try:
        return df[(df["Title"] == title) & (df["Netflix"] == True)].iloc[0].get("Rating")
    except Exception as e:
        return "There is no available rating for this movie."

def recommendation(genre):
    availableMovies = (df[df["Netflix"] | df["HBO"] | df["Amazon Prime"] == True])
    genreFilter = availableMovies[availableMovies["Genre"].str.contains(genre)]
    bestMovies = (genreFilter[genreFilter["Rating"] == 5])["Title"].tolist()
    return "Another good movie you may enjoy is: {}.".format(random.choice(bestMovies))

