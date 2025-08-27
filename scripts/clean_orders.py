import pandas as pd

def clean_orders(input_path: str, output_path: str):
    orders = pd.read_csv(input_path)
    
    # Usuwamy duplikaty
    orders = orders.drop_duplicates()
    
    # Konwersja dat do formatu datetime
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    orders['delivery_date'] = pd.to_datetime(orders['delivery_date'], errors='coerce')
    
    # Usuwamy zamówienia bez daty zamówienia
    orders = orders.dropna(subset=['order_date'])
    
    # Uzupełniamy brakujące daty dostawy wartością null
    orders['delivery_date'] = orders['delivery_date'].fillna(pd.NaT)
    
    # Filtrujemy zamówienia z negatywną ilością (jeśli takie są)
    orders = orders[orders['quantity'] > 0]
    
    # Zapisujemy wyczyszczony plik
    orders.to_csv(output_path, index=False)
    print(f"Orders cleaned and saved to {output_path}")

if __name__ == "__main__":
    clean_orders('data/orders.csv', 'data/clean_orders.csv')
