# importeren van de benodigde modules

# als constant de paden van de csv bestanden definiëren.

# inlezen van de twee csv bestanden (products en transactions)

# samenvoegen van de twee bestanden met merge

# aggregeren van de data op basis van product_id
# en het berekenen van de totale omzet per product.

import pandas as pd


PATH_DATA = "/Users/maximdemey/Library/CloudStorage/OneDrive-AholdDelhaize.com/Documents/PycharmProjects/github-training-202608/data"


def read_data(data_path: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Read the products and transactions CSV files.

    Args:
        data_path: Directory containing the CSV files.

    Returns:
        A tuple of (products, transactions) DataFrames.
    """
    products = pd.read_csv(data_path + "/products.csv")
    transactions = pd.read_csv(data_path + "/transactions.csv")
    return products, transactions


def join_products_transactions(
    products: pd.DataFrame, transactions: pd.DataFrame
) -> pd.DataFrame:
    """Join transactions with products on product_id.

    Args:
        products: Product dimension data.
        transactions: Transaction fact data.

    Returns:
        The merged DataFrame.
    """
    merged_data = pd.merge(transactions, products, on="product_id", how="right")
    return merged_data


def aggregate_data(merged_data: pd.DataFrame) -> pd.DataFrame:
    """Aggregate merged data into total revenue per product.

    Args:
        merged_data: Output of join_products_transactions.

    Returns:
        DataFrame with product_id and total_revenue columns.
    """
    aggregated_data = (
        merged_data.groupby("product_id").agg({"quantity": "sum"}).reset_index()
    )
    aggregated_data.rename(columns={"quantity": "total_quantity"}, inplace=True)
    return aggregated_data


def process(data_path: str) -> pd.DataFrame:
    """Run the full pipeline: read, join, and aggregate the sales data.

    Args:
        data_path: Directory containing the CSV files.

    Returns:
        DataFrame with total quantity per product.
    """
    products, transactions = read_data(data_path)
    merged_data = join_products_transactions(products, transactions)
    processed_data = aggregate_data(merged_data)
    return processed_data


if __name__ == "__main__":
    processed_data = process(PATH_DATA)
    print(processed_data)
