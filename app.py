from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load color data from CSV file
colors_df = pd.read_csv('colors.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_color_info', methods=['POST'])
def get_color_info():
    data = request.get_json()
    r, g, b = data['r'], data['g'], data['b']

    # Find the closest matching color in the CSV data
    closest_color = colors_df.iloc[(colors_df[['R', 'G', 'B']] - [r, g, b]).abs().sum(axis=1).idxmin()]
    color_name = closest_color['color_name']

    return jsonify({'colorName': color_name, 'r': r, 'g': g, 'b': b})

if __name__ == '__main__':
    app.run(debug=True)
