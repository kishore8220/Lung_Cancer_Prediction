# Lung Cancer Prediction Web Application

This project is a web-based application built using Flask that predicts whether a person has lung cancer based on various health-related factors. It uses a machine learning model (Logistic Regression) to predict the likelihood of lung cancer from a set of user-provided input features.

## Features
- **Prediction of Lung Cancer**: Based on the user's input, the model predicts if the person has lung cancer or not.
- **Model Accuracy**: The application provides the accuracy of the model on the test data set.
- **Data Preprocessing**: The application preprocesses the data, handles categorical features, and uses logistic regression for prediction.

## Technologies Used
- **Flask**: Web framework to create the web application.
- **pandas**: For data manipulation and processing.
- **scikit-learn**: For machine learning, specifically Logistic Regression and data preprocessing techniques like Label Encoding.
- **HTML/CSS**: For creating the frontend user interface.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Kishore8220/lung-cancer-prediction.git
    cd lung-cancer-prediction
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On Mac/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Download the dataset `lung_cancer_survey.csv` and place it in the root directory of the project.

6. Run the Flask application:
    ```bash
    python app.py
    ```

7. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

## Application Overview

### 1. **Home Page**
   - The home page contains a simple form where the user can input their health-related information. The inputs include gender, age, smoking status, yellow fingers, anxiety, peer pressure, allergy, wheezing, alcohol consumption, coughing, shortness of breath, swallowing difficulty, and chest pain.
   
### 2. **Prediction Page**
   - When the form is submitted, the application processes the data and makes a prediction using the logistic regression model.
   - The prediction is displayed on a results page, which tells the user whether they are predicted to have lung cancer (`Cancer`) or not (`Not Cancer`).
   - The model’s accuracy on the test dataset is also shown on the results page.

## Code Explanation

- **Data Loading & Preprocessing**:
    - The dataset `lung_cancer_survey.csv` is loaded using `pandas`. The columns `CHRONIC DISEASE` and `FATIGUE` are dropped, and categorical columns like `GENDER` and `LUNG_CANCER` are encoded using `LabelEncoder`.
    
- **Model Training**:
    - The data is split into training and testing sets using `train_test_split` from `sklearn`. The logistic regression model is trained on the training data.
    
- **Prediction**:
    - When the user submits their information, the data is passed to the trained logistic regression model for prediction. The result is returned as `Cancer` or `Not Cancer` based on the model's output.

### Flask Routes:
- **`/` (Home Route)**: Displays the input form for the user to enter their health-related data.
- **`/predict` (Prediction Route)**: Processes the form data, makes a prediction using the logistic regression model, and displays the result along with the model's accuracy.

## Files in the Project

- **app.py**: The main Python script that contains the Flask application logic and the machine learning model.
- **lung_cancer_survey.csv**: The dataset used to train the model (this should be placed in the root directory).
- **templates/**:
    - **index.html**: The form page where users input their data.
    - **result.html**: The results page displaying the prediction and accuracy.
- **static/**: Folder for static files like CSS, images, or JavaScript (optional for styling).

## Dataset Information
The dataset `lung_cancer_survey.csv` includes health-related survey data used to predict lung cancer. Each row represents a person’s health information, with columns representing various health attributes such as age, gender, smoking status, and symptoms. The target variable is `LUNG_CANCER`, which is binary (0 for no cancer, 1 for cancer).

## Contributing
Feel free to fork this project and make improvements or modifications. If you would like to contribute, please create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact
For any questions or feedback, please open an issue in the repository or reach out to [kdkishore91@gmail.com].
