from flask import Flask, request, render_template, jsonify


from src.pipeline.prediction_pipeline import CustomData, PredictPipeline


application = Flask(__name__)

app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Collect form data here
        data = request.form
        return f"Form submitted with data: {data}"

    # Fields configuration
    numeric_fields = [
        {'name': 'carat', 'label': 'Carat'},
        {'name': 'depth', 'label': 'Depth'},
        {'name': 'table', 'label': 'Table'},
        {'name': 'x', 'label': 'X'},
        {'name': 'y', 'label': 'Y'},
        {'name': 'z', 'label': 'Z'}
    ]

    select_fields = [
        {'name': 'cut', 'label': 'Cut', 'options': ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']},
        {'name': 'color', 'label': 'Color', 'options': ['D', 'E', 'F', 'G', 'H', 'I', 'J']},
        {'name': 'clarity', 'label': 'Clarity', 'options': ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']}
    ]

    return render_template('form.html', numeric_fields=numeric_fields, select_fields=select_fields)

    
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)