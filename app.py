from flask import Flask
import urllib.request, json
app = Flask(__name__)

@app.route('/')
def get_list_elements():
    
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)
    
    characters = []
    
    for character in dict ["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        }
        
        characters.append(character)
        
    return {"charecters": characters}