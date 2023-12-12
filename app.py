from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debug mode

# Set your RapidAPI key and host
RAPIDAPI_KEY = 'YOUR-RAPIDAPI-KEY'
RAPIDAPI_HOST = 'food-recipes-with-images.p.rapidapi.com'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    # Assuming you have updated the HTML form to use 'ingredient' as the name attribute
    ingredients = request.form.get('ingredient')
    
    # Process ingredients and fetch recipes (you'll implement this)

    # For now, a simple example response
    recipes = ["Recipe 1", "Recipe 2", "Recipe 3"]

    return jsonify({'recipes': recipes})

@app.route('/search_recipes', methods=['POST'])
def search_recipes():
    try:
        # Get the search query from the form
        search_query = request.form.get('q')

        # Make a request to the external API
        url = 'https://food-recipes-with-images.p.rapidapi.com/'
        headers = {
            'X-RapidAPI-Key': RAPIDAPI_KEY,
            'X-RapidAPI-Host': RAPIDAPI_HOST
        }
        params = {'q': search_query}

        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()

        # Extract relevant information from the response_data (modify as per API response structure)
        recipes = response_data.get('recipes', [])

        return jsonify({'recipes': recipes})

    except Exception as e:
        # Log the exception for debugging
        print(f"Error: {str(e)}")
        return "An error occurred."

if __name__ == '__main__':
    app.run(debug=True)