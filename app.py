import pandas as pd
from flask import Flask,render_template,request
import Broker as bk
import numpy as np
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sendData')
def signupForm():
    name = request.args.get('fname')
    W = float(request.args.get('Weight'))
    H = float(request.args.get('Height'))
    BMI = round(W / np.power((H / 100),2),2)
    Smoking = request.args.get('Smoking')
    AlcoholDrinking = request.args.get('AlcoholDrinking')
    Stroke = request.args.get('Stroke')
    PhysicalHealth = float(request.args.get('PhysicalHealth'))
    MentalHealth = float(request.args.get('MentalHealth'))
    DiffWalking = request.args.get('DiffWalking')
    Sex = request.args.get('Sex')
    AgeCategory = request.args.get('AgeCategory')
    Race = "Asian"
    Diabetic = request.args.get('Diabetic')
    PhysicalActivity = request.args.get('PhysicalActivity')
    GenHealth = request.args.get('health')
    SleepTime = float(request.args.get('SleepTime'))
    Asthma = request.args.get('Asthma')
    KidneyDisease = request.args.get('KidneyDisease')
    SkinCancer = request.args.get('SkinCancer')

    data = {"BMI": BMI, "Smoking": Smoking, "AlcoholDrinking": AlcoholDrinking,
          "Stroke": Stroke, "PhysicalHealth": PhysicalHealth, "MentalHealth": MentalHealth,
          "DiffWalking": DiffWalking, "Sex": Sex, "AgeCategory": AgeCategory, "Race": Race,
          "Diabetic": Diabetic, "PhysicalActivity": PhysicalActivity, "GenHealth": GenHealth,
          "SleepTime": SleepTime, "Asthma": Asthma, "KidneyDisease": KidneyDisease, "SkinCancer": SkinCancer}
    df = bk.fillData(data)
    df = bk.clean(df)
    result = bk.predict(df)
    predNN = pd.DataFrame(result)
    y_predNN = predNN.idxmax(axis=1)

    if y_predNN[0] == 0:
        out = 'ไม่มีแนวโน้มเป็นโรคหัวใจ'
    else:
        out = 'มีแนวโน้มเป็นโรคหัวใจ'
    outList = {"result":out,"name":name}
    return render_template('result.html',data=outList)

if __name__ == '__main__':
    app.run()