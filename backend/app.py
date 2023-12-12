from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

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

if __name__ == '__main__':
    app.run(debug=True)