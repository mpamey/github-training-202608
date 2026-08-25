# Mock Sales Data

Synthetic datasets for practicing joins, data cleaning, and aggregated reporting.

## Files

- `transactions.csv` — order-level sales facts
  `order_id, order_date, customer_id, store_id, product_id, quantity, unit_price, discount_pct, payment_method`
- `products.csv` — product dimension
  `product_id, product_name, category, unit_cost`
- `stores.csv` — store dimension
  `store_id, store_name, region, city`
- `customers.csv` — customer dimension
  `customer_id, customer_name, signup_date, segment`

## Known data quality issues (intentional)

Use these as cleaning exercises before aggregating:

- **Inconsistent date formats**: mixed `YYYY-MM-DD` and `MM/DD/YYYY` in `order_date` and `signup_date`.
- **Inconsistent text casing**: `category`, `region`, and `payment_method` have mixed case values (e.g. `Beverages` / `beverages` / `BEVERAGES`).
- **Missing values**: some `unit_price`, `unit_cost`, `city`, and `segment` cells are blank.
- **Negative quantities**: a few `transactions.csv` rows have negative `quantity` (simulated returns/entry errors).
- **Duplicate rows**: exact duplicate rows in `transactions.csv`, and a duplicate `product_id` in `products.csv`.
- **Orphan foreign keys**: some `customer_id`/`product_id` values in `transactions.csv` don't exist in the corresponding dimension table (broken joins).
- **Stray whitespace**: leading/trailing spaces in some ID and name fields.

## Suggested exercises

1. Clean and standardize dates, casing, and whitespace across all files.
2. Deduplicate records and decide how to handle orphan keys.
3. Join `transactions` with `products`, `stores`, and `customers`.
4. Compute revenue (`quantity * unit_price * (1 - discount_pct/100)`) and margin (using `unit_cost`).
5. Build aggregated reports: revenue by region, by category, by month, and top customers.
