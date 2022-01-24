from os import lstat
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
@cross_origin()

def homepage():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()

def index():
    if request.method == 'POST':
        try:
            rm = float(request.form.get('rm'))
            # print(rm)
            ptratio = float(request.form.get('ptratio'))
            lstat = float(request.form.get('lstat'))
            rad = float(request.form.get('rad'))
            chas = float(request.form.get('chas'))
            print(rm, ptratio, lstat, rad, chas)
            

            data_list = [rm, ptratio, lstat, rad, chas]
            model = pickle.load(open("boston_house_one.pickle", "rb"))
            result = model.predict([data_list])

            return render_template('result.html', data=round(result[0], 2))

        except Exception as e:
            print("Exception is ", e)
    
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
        