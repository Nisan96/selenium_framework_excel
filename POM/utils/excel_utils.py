import pandas as pd

# Functions extract data from different rows of Excel file
def read_RegisterPage_validtest_data(Excel_file, Sheet_name):
    test_data = pd.read_excel(Excel_file, sheet_name=Sheet_name)
    data = test_data.iloc[0]
    return data


def read_RegisterPage_invalidtest_data(Excel_file, Sheet_name):
    test_data = pd.read_excel(Excel_file, sheet_name=Sheet_name)
    data = test_data.iloc[1]
    return data
