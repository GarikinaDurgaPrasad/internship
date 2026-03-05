from flask import Flask, render_template, request
from model import predict_feature, predict_house

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    area = float(request.form['area'])
    rooms = float(request.form['rooms'])
    age = float(request.form['age'])

    price = predict_house(area, rooms, age)

    f1 = float(request.form['f1'])
    f2 = float(request.form['f2'])
    f3 = float(request.form['f3'])
    f4 = float(request.form['f4'])

    feature = predict_feature([f1,f2,f3,f4])

    return render_template('index.html',
                           price=price,
                           feature=feature)

if __name__ == '__main__':

    app.run(debug=True)
