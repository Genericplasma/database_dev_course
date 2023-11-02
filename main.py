import panadas as pd

file_name = "MOCK_FILE.csv"

df = pd.read_csv(file_name)

print(df.head())