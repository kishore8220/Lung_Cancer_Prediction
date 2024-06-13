from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load and prepare data
df = pd.read_csv("lung_cancer_survey.csv")
df.drop(['CHRONIC DISEASE','FATIGUE '], axis='columns', inplace=True)

obj = LabelEncoder()
df['GENDER'] = obj.fit_transform(df['GENDER'])
df['LUNG_CANCER'] = obj.fit_transform(df['LUNG_CANCER'])

x = df.drop(['LUNG_CANCER'], axis='columns')
y = df['LUNG_CANCER']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

model = LogisticRegression(random_state=0)
model.fit(x_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    GENDER = int(request.form['GENDER'])
    age = int(request.form['age'])
    SMOKING = int(request.form['SMOKING'])
    YELLOW_FINGERS = int(request.form['YELLOW_FINGERS'])
    ANXIETY = int(request.form['ANXIETY'])
    PEER_PRESSURE = int(request.form['PEER_PRESSURE'])
    ALLERGY = int(request.form['ALLERGY'])
    WHEEZING = int(request.form['WHEEZING'])
    ALCOHOL_CONSUMING = int(request.form['ALCOHOL_CONSUMING'])
    COUGHING = int(request.form['COUGHING'])
    SHORTNESS_OF_BREATH = int(request.form['SHORTNESS_OF_BREATH'])
    SWALLOWING_DIFFICULTY = int(request.form['SWALLOWING_DIFFICULTY'])
    CHEST_PAIN = int(request.form['CHEST_PAIN'])

    new_data = [[GENDER, age, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]]
    result = model.predict(new_data)

    if result == 1:
        prediction = 'Cancer'
    else:
        prediction = 'Not Cancer'

    accuracy = model.score(x_test, y_test) * 100

    return render_template('result.html', prediction=prediction, accuracy=accuracy)

if __name__ == '__main__':
    app.run(debug=True)
