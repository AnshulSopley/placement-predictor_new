
from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('placement_predict.pkl','rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    age =int(request.form.get('age'))
    cgpa =float(request.form.get('cgpa'))
    iq = int(request.form.get('iq'))
#prediction
    result = model.predict(np.array([age,cgpa,iq]).reshape(1,3))
    print(result)
    if result[0] >= 1 :
        result = 'PLACED'
    else:
        result= 'NOT PLACED'
    
    
    
    return render_template('index.html',result=result)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080, debug=False)
