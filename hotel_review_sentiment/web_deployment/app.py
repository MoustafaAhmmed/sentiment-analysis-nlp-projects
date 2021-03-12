from flask import Flask, render_template, request
import pickle
import numpy as np
import csv
model = pickle.load(open('hotel_review.pkl', 'rb'))

app = Flask(__name__ , template_folder ='templates')


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    pred = model.predict([data1])
    myfile = open("review.csv", "a", encoding='utf-8')
    wr = csv.writer(myfile)
    wr.writerow([data1,pred])
    myfile.close()


    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)



