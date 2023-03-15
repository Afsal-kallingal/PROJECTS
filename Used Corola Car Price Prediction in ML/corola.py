
from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
app=Flask(__name__)
model=pickle.load(open('corola.pkl','rb'))
@app.route('/')
def home():
    return render_template('a.html')


@app.route('/predict',methods=['POST'])
def predict():
    a=float(request.values['a1'])
    b=float(request.values['b1'])
    c=float(request.values['c1'])  
    d=float(request.values['d1']) 
    e=float(request.values['e1'])
    f=float(request.values['f1'])
    g=float(request.values['g1'])
    h=float(request.values['h1'])
    i=float(request.values['i1'])
    data=pd.DataFrame({'Age':[a],
                   'KM':[b],
                   'FuelType':[c],
                   'HP':[d],
                   'MetColor':[e],
                   'Automatic':[f],
                   'CC':[g],
                   'Doors':[h],
                   'Weight':[i]})


    print(data)
    pre=model.predict(data)   
    print(pre)
    
     
    return render_template('result.html',prediction_text='{}'.format(pre))

if __name__=='__main__':
    app.run(port=8000)