import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    grouped = activities.groupby('sell_date')['product'].unique()
    sorted_products = grouped.apply(sorted).apply(','.join)
    num_sold = grouped.apply(len)
    result = pd.DataFrame({
        'sell_date': num_sold.index,
        'num_sold': num_sold.values,
        'products': sorted_products.values
        })
    result = result.sort_values(by='sell_date')
    return result