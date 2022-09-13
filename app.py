from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/flowers", methods=["GET"])
def flowers():

    flowers = [
    {'id': 1, 'name': 'rose', 'color': 'white', 'water': True},
    {'id': 2, 'name': 'orchid', 'color': 'purple', 'water': False},
    {'id': 3, 'name': 'tulip', 'color': 'red', 'water': True},
    {'id': 4, 'name': 'cactus', 'color': 'green', 'water': False},
    {'id': 5, 'name': 'bluebell', 'color': 'blue', 'water': True},
    {'id': 6, 'name': 'sunflower', 'color': 'yellow', 'water': True},
    {'id': 7, 'name': 'marigold', 'color': 'gold', 'water': True}
]
    return render_template("flowers.html", page_title="Flowers List" , flowers=flowers)

@app.route("/flowers/new", methods=["GET", "POST"])
def new_flower():
    if request.method == "GET":
        return "This route only really works for POST request"
    else:
        data = request.get_json()
        if data["color"] != "invisible":
            return "Yes, that seems like a flower", 201
        else: 
            return "Not a flower", 400


if __name__ == "__main__":
    app.run(debug=True) # pragma: no cover
