import pandas as pd

def clean_missing_values(df):

    df_dropped = df.dropna()

    df_filled = df.copy()
    for col in df_filled.select_dtypes(include=['float64', 'int64']).columns:
        df_filled[col].fillna(df_filled[col].mean(), inplace=True)

    return df_dropped, df_filled


if __name__ == "__main__":
    data = {
        'Name': ['Alia', 'Eman', 'Fatima', 'Iqra', None],
        'Age': [25, None, 30, 22, 28],
        'Score': [85, 90, None, 88, 92]
    }

    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)

    df_dropped, df_filled = clean_missing_values(df)

    print("\nDataFrame after dropping missing values:\n", df_dropped)
    print("\nDataFrame after filling missing values:\n", df_filled)
