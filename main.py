from flask import Flask,render_template,request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

data = pd.read_csv('data/Bengaluru_House_Data.csv')

pipe = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    locations = sorted(data['location'].dropna().astype(str).unique())
    return render_template('index.html', locations=locations)

@app.route('/predict',methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')
    try:
        bhk = int(bhk)
        bath = int(bath)
        sqft = float(sqft)

        # Basic realistic range checks
        if bhk <= 0 or bhk > 6:
            return "Please enter a BHK value between 1 and 6."
        if bath <= 0 or bath > 6:
            return "Please enter a bathroom count between 1 and 6."
        if sqft < 300 or sqft > 10000:
            return "Please enter total square feet between 300 and 10,000."

        # Ratio check: ensure minimum 300 sqft per BHK
        if sqft / bhk < 300:
            return "Square footage is too low for the number of BHKs."

    except ValueError:
        return "Invalid input. Please enter numeric values."
    
    input = pd.DataFrame([{
        'location': location,
        'BHK': bhk,
        'bath': bath,
        'total_sqft': sqft
    }])
    
    prediction = pipe.predict(input)[0]*1e5

    if prediction < 0:
        return "Please give a valid input."
    return f"₹{np.round(prediction / 1e5, 2)} Lakhs"

if __name__ == "__main__":
    app.run(debug=True)