import pandas as pd
import numpy as np
import io
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency

def read_multi_csv(filepath: str) -> dict[str, pd.DataFrame]:
    dataframes = {}
    current_rows = []

    with open(filepath, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped in ('', ','):
                if current_rows:
                   df = pd.read_csv(io.StringIO('\n'.join(current_rows)))
                   df = df.rename(columns={df.columns[1]: f"{df.columns[0].replace('_id','')}_{df.columns[1]}"})
                   dataframes[df.columns[0]] = df
                   current_rows = []
            else:
                current_rows.append(stripped)

    if current_rows:
        df = pd.read_csv(io.StringIO('\n'.join(current_rows)))
        df = df.rename(columns={df.columns[1]: f"{df.columns[0].replace('_id','')}_{df.columns[1]}"})
        dataframes[df.columns[0]] = df

    return dataframes

def recover_feature(data: pd.DataFrame, missing_feature: str, index_feature:str, empty_value="?") -> pd.DataFrame:
    records_without_field = set(data[data[missing_feature] == empty_value][index_feature])
    records_with_field = set(data[data[missing_feature] != empty_value][index_feature])
    records_to_impute = records_without_field.intersection(records_with_field)
    recovered_mapping = data[
        (data[index_feature].isin(records_to_impute)) & (data[missing_feature] != empty_value)
    ].drop_duplicates(index_feature).set_index(index_feature)[missing_feature]

    mask = (data[index_feature].isin(records_to_impute)) & (data[missing_feature] == empty_value)
    data.loc[mask, missing_feature] = data.loc[mask, index_feature].map(recovered_mapping)

    return data

def group_by_condition(df, grouping_cols, target_col, condition=pd.isnull):
    grouped_data = (
        df.groupby(grouping_cols, observed=True)[target_col]
        .apply(lambda x: condition(x).mean() * 100)
        .reset_index(name=f'percentage_of_{target_col}')
    )
    return grouped_data


def eta_squared(continuous, categorical):
    mask       = continuous.notna() & categorical.notna()
    y, grp     = continuous[mask], categorical[mask]
    groups     = [g.values for _, g in y.groupby(grp, observed=True)]
    F, p       = f_oneway(*groups)
    grand_mean = y.mean()
    ss_total   = ((y - grand_mean) ** 2).sum()
    ss_between = sum(len(g) * (g.mean() - grand_mean) ** 2 for g in groups)
    return ss_between / ss_total, p, F

def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    r, k = confusion_matrix.shape
    return np.sqrt(chi2 / (n * min(k - 1, r - 1)))