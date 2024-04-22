import pandas as pd
import sys

def fill_na_with_mean(df):
    for col in df.columns:
        if df[col].dtype != 'object': 
            df[col].fillna(df[col].mean(), inplace=True)


def outlier_thresholds(dataframe, col_name, q1=0.25, q3=0.75):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range

    return low_limit, up_limit


def remove_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    new_df = dataframe[~((dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit))]

    return new_df
    

if __name__ == "__main__":
        csv = sys.argv[1]
        
        df = pd.read_csv(csv)

        fill_na_with_mean(df)
        for col in df.select_dtypes(include=['float64', 'int64']).columns:
            df = remove_outlier(df, col)
            
        sys.stdout.write(df.to_csv(index=False))