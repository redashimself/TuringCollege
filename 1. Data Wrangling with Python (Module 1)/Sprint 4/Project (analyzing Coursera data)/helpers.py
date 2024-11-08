import pandas as pd


def strip_spaces(data):
    for column in data.select_dtypes(include=['object']):
        data[column] = data[column].str.strip()
    return data


def lowercase_data(data):
    data.columns = data.columns.str.lower()

    if data.index.dtype == 'object':
        data.index = data.index.str.lower()

    for column in data.select_dtypes(include=['object']):
        data[column] = data[column].str.lower()

    return data


import pandas as pd

def convert_metric_prefix_to_numeric(column):
    def convert_value(value):
        if not isinstance(value, str):
            return pd.to_numeric(value, errors='coerce')
        
        value = value.lower()
        if 'k' in value:
            value = value.replace('k', '')
            factor = 1000
        elif 'm' in value:
            value = value.replace('m', '')
            factor = 1000000
        else:
            factor = 1

        return pd.to_numeric(value, errors='coerce') * factor

    return column.apply(convert_value)
