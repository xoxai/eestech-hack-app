import pandas as pd
from sedan.models import Data_stor

def get_attr(file_name: str):

    if file_name.endswith('.txt'):
        data = pd.read_table(file_name)
    elif file_name.endswith('.csv'):
        data = pd.read_csv(file_name, sep=';', skiprows=1, header=0)
        print(data.head())

    elif file_name.endswith(('.xls', '.xlsx,')):
        data = pd.read_excel(file_name,sheet_name=None)
        print(data.head())
        attr = list(data)
        print(attr)
    return attr