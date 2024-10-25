from flask import Flask, render_template, request
import pickle
import pandas as pd

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
        department_IT = int(request.form["department_IT"])
        department_RandD = int(request.form["department_RandD"])
        department_accounting = int(request.form["department_accounting"])
        department_hr = int(request.form["department_hr"])
        department_management = int(request.form["department_management"])
        department_marketing = int(request.form["department_marketing"])
        department_product_mng = int(request.form["department_product_mng"])
        department_sales = int(request.form["department_sales"])
        department_support = int(request.form["department_support"])
        department_technical = int(request.form["department_technical"])

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
            'department_IT': [department_IT],
            'department_RandD': [department_RandD],
            'department_accounting': [department_accounting],
            'department_hr': [department_hr],
            'department_management': [department_management],
            'department_marketing': [department_marketing],
            'department_product_mng': [department_product_mng],
            'department_sales': [department_sales],
            'department_support': [department_support],
            'department_technical': [department_technical]
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