from flask import Flask, render_template,Response, jsonify,request
import csv
import requests
from faker import Faker

app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/requirements/')
def requirements():
    with open('requirements.txt', 'r') as file:
        content = file.read()
        content_with_newline = content + '\n'
        return Response(content_with_newline, mimetype='text/plain')


@app.route('/mean/')
def mean():
    # Read the CSV file
    filename = 'hw.csv'
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            if len(row) == 0:
                continue  # Skip empty rows

            rows.append(row)

    # Extract height and weight values
    heights = [float(row[1]) for row in rows]
    weights = [float(row[2]) for row in rows]

    # Calculate the average height and weight
    avg_height_cm = sum(heights) / len(heights) * 2.54
    avg_weight_kg = sum(weights) / len(weights) * 0.453592

    # Return the result as JSON
    result = {
        'average_height_cm': avg_height_cm,
        'average_weight_kg': avg_weight_kg
    }
    return jsonify(result)


@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return "People in space: "+ str(r.json()["number"])

@app.route('/generate-users/')
def generate_users():
    count = request.args.get('count', default=10, type=int)
    users = []
    for _ in range(count):
        name = fake.name()
        email = fake.email()
        user = f"{name} {email}"
        users.append(user)
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)