import pandas as pd

def enrich_customers(customers_path: str, orders_path: str, output_path: str):
    customers = pd.read_csv(customers_path)
    orders = pd.read_csv(orders_path)

    # Liczba zamówień na klienta
    order_counts = orders.groupby('user_id').size().reset_index(name='order_count')
    
    # Łączymy z danymi klientów
    enriched = pd.merge(customers, order_counts, how='left', left_on='customer_id', right_on='user_id')
    enriched['order_count'] = enriched['order_count'].fillna(0).astype(int)
    
    # Segmentacja klientów
    def segment(row):
        if row['order_count'] >= 5:
            return 'Loyal'
        elif row['order_count'] >= 2:
            return 'Engaged'
        else:
            return 'New'

    enriched['segment'] = enriched.apply(segment, axis=1)

    enriched.to_csv(output_path, index=False)
    print(f"Customers enriched and saved to {output_path}")

if __name__ == "__main__":
    enrich_customers('data/customers.csv', 'data/orders.csv', 'data/enriched_customers.csv')
