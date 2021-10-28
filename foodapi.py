import requests, json
import urllib3
urllib3.disable_warnings()

def getRecipe(id):
    cache = {}
    if id not in cache.keys():
        url = "https://tasty.p.rapidapi.com/recipes/detail"
        querystring = {"id":id}
        headers = {
            'x-rapidapi-host': "tasty.p.rapidapi.com",
            'x-rapidapi-key': "498beeb34fmsh7558841455add94p17d283jsn987de2c3f201"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        cache[id] = dict(json.loads(response.text)) 
    return cache[id]
    
    