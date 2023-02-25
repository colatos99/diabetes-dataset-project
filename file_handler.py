import pandas as pd
def get_diabetes_cvs():
    diabetes_data = pd.read_csv("diabetes.csv")
    return diabetes_data
    