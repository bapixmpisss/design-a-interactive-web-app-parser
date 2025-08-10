# Import necessary libraries
import flask
from flask import request, jsonify
import json
import re

# Initialize Flask app
app = flask.Flask(__name__)

# Load parser configuration from a JSON file
with open('parser_config.json') as f:
    parser_config = json.load(f)

# Define a function to parse user input
def parse_input(user_input):
    for rule in parser_config['rules']:
        pattern = re.compile(rule['pattern'])
        if pattern.match(user_input):
            return rule['output']
    return "Error: Input not recognized"

# Define a route for the parser API
@app.route('/parse', methods=['POST'])
def parse_api():
    user_input = request.form['input']
    output = parse_input(user_input)
    return jsonify({'output': output})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)