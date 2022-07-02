import pandas as pd

def read_data(data_file: str) -> pd.DataFrame:
    return pd.read_csv(data_file, sep='\n', delimiter=',')

def write_data(data_file: str, data: pd.DataFrame):
    pd_data = read_data(data_file)
    pd_data = pd_data.append(data)
    pd_data.to_csv(data_file,sep='\n')