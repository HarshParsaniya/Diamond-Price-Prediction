from flask import Flask, request, render_template, jsonify


from src.pipeline.prediction_pipeline import CustomData, PredictPipeline


application = Flask(__name__)

app = application

@app.route('/')
def home_page():
    return render_template('index.html')    

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
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
    
    else:
        data=CustomData(
            carat=float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('results.html',final_result=results)
    

    
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)