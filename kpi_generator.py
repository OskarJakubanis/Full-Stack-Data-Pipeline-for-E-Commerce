import pandas as pd

def generate_kpis(customers_path, orders_path, returns_path, sessions_path, support_path, output_path):
    customers = pd.read_csv(customers_path)
    orders = pd.read_csv(orders_path)
    returns = pd.read_csv(returns_path)
    sessions = pd.read_csv(sessions_path)
    support = pd.read_csv(support_path)

    # Łączna sprzedaż
    total_sales = orders['order_value'].sum()

    # Średnia wartość zamówienia
    avg_order_value = orders['order_value'].mean()

    # Wskaźnik zwrotów
    return_rate = len(returns) / len(orders) * 100

    # Porzucenie koszyka
    abandonment_rate = sessions['cart_abandoned'].mean() * 100

    # Średni czas obsługi zgłoszenia
    avg_resolution_time = support['resolution_time_min'].mean()

    # Liczba unikalnych klientów
    unique_customers = customers['customer_id'].nunique()

    # KPI jako DataFrame
    kpis = pd.DataFrame({
        'Metric': [
            'Total Sales',
            'Average Order Value',
            'Return Rate (%)',
            'Cart Abandonment Rate (%)',
            'Avg. Resolution Time (min)',
            'Unique Customers'
        ],
        'Value': [
            f"${total_sales:,.2f}",
            f"${avg_order_value:,.2f}",
            f"{return_rate:.2f}",
            f"{abandonment_rate:.2f}",
            f"{avg_resolution_time:.2f}",
            f"{unique_customers}"
        ]
    })

    kpis.to_csv(output_path, index=False)
    print(f"KPI report saved to {output_path}")

if __name__ == "__main__":
    generate_kpis(
        'data/customers.csv',
        'data/orders.csv',
        'data/returns.csv',
        'data/sessions.csv',
        'data/support_tickets.csv',
        'outputs/kpis.csv'
    )
