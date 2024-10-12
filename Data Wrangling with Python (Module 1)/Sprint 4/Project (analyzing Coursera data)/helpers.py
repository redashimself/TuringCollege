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


def convert_metric_prefix_to_numeric(column):
    def convert_value(value):
        if isinstance(value, str):
            value = value.replace('k', '')
        return pd.to_numeric(value, errors='coerce') * 1000

    return column.apply(convert_value)
