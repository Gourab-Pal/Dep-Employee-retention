from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

#import salary

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello() :
    prediction = None
    response = None
    if request.method == "POST":
        satisfaction_level = float(request.form["satisfaction_level"])
        last_evaluation = float(request.form["last_evaluation"])
        number_project = int(request.form["number_project"])
        average_monthly_hours = int(request.form["average_monthly_hours"])
        tenure = int(request.form["tenure"])
        work_accident = int(request.form["work_accident"])
        promotion_last_5years = int(request.form["promotion_last_5years"])
        salary = int(request.form["salary"])
        department = request.form["department"]

        department_list = np.zeros(10)

        if(department=="department_IT"):
            department_list = np.zeros(10)
            department_list[0] = 1
        if(department=="department_RandD"):
            department_list = np.zeros(10)
            department_list[1] = 1
        if(department=="department_accounting"):
            department_list = np.zeros(10)
            department_list[2] = 1
        if(department=="department_hr"):
            department_list = np.zeros(10)
            department_list[3] = 1
        if(department=="department_management"):
            department_list = np.zeros(10)
            department_list[4] = 1
        if(department=="department_marketing"):
            department_list = np.zeros(10)
            department_list[5] = 1
        if(department=="department_product_mng"):
            department_list = np.zeros(10)
            department_list[6] = 1
        if(department=="department_sales"):
            department_list = np.zeros(10)
            department_list[7] = 1
        if(department=="department_support"):
            department_list = np.zeros(10)
            department_list[8] = 1
        if(department=="department_technical"):
            department_list = np.zeros(10)
            department_list[9] = 1


        model = pickle.load(open('model.pkl','rb'))
        data = {
            'satisfaction_level': [satisfaction_level],
            'last_evaluation': [last_evaluation],
            'number_project': [number_project],
            'average_monthly_hours': [average_monthly_hours],
            'tenure': [tenure],
            'work_accident': [work_accident],
            'promotion_last_5years': [promotion_last_5years],
            'salary': [salary],
            'department_IT': [department_list[0]],
            'department_RandD': [department_list[1]],
            'department_accounting': [department_list[2]],
            'department_hr': [department_list[3]],
            'department_management': [department_list[4]],
            'department_marketing': [department_list[5]],
            'department_product_mng': [department_list[6]],
            'department_sales': [department_list[7]],
            'department_support': [department_list[8]],
            'department_technical': [department_list[9]]
        }
        prediction = model.predict(pd.DataFrame(data))
        prediction = int(prediction)
        if(prediction==0):
            response = "Stayed"
        else:
            response = "Exited"
    return render_template("index.html", my_pred = response)


if __name__ == "__main__":
    app.run(debug=True)