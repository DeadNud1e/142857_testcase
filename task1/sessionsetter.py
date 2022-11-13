import pandas as pd

def setSession(df):
    """
    Adding session id for each user that have difference between views more that 3 minutes

    input: df - pandas dataframe

    output: pandas dataframe with session_id column
    """
    df.dropna()
    if not pd.core.dtypes.common.is_datetime64_ns_dtype(df['timestamp']):
        df['timestamp'] = pd.to_datetime(df['timestamp'])

    df = df.sort_values(['customer_id', 'timestamp'])
    diff_timestamp = df.groupby('customer_id')['timestamp'].diff()

    new_session = (diff_timestamp.isnull()) | (diff_timestamp.dt.seconds > 180)

    df['session_id'] = df.loc[new_session, ['customer_id', 'timestamp']] \
        .groupby('customer_id').rank(method='first').astype(int)
    df['session_id'] = df['session_id'].fillna(method='ffill').astype(int)

    return df


if __name__ == '__main__':
    path_to_df = 'task1/data.csv'
    df = pd.read_csv(path_to_df, names=['customer_id', 'product_id', 'timestamp'])
    out = setSession(df)
    print(out.head())