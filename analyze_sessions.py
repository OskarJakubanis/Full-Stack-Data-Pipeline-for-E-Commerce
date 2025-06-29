import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def analyze_sessions(sessions_path: str, output_dir: str):
    sessions = pd.read_csv(sessions_path, parse_dates=['session_start', 'session_end'])

    # Obliczanie czasu trwania sesji
    sessions['duration_sec'] = (sessions['session_end'] - sessions['session_start']).dt.total_seconds()

    # Wskaźnik porzucenia koszyka
    abandonment_rate = sessions['cart_abandoned'].mean() * 100

    # Średni czas sesji
    avg_duration = sessions['duration_sec'].mean()

    print(f"Cart abandonment rate: {abandonment_rate:.2f}%")
    print(f"Average session duration: {avg_duration:.2f} seconds")

    # Wykres: porzucenie koszyka wg kanału
    plt.figure(figsize=(8, 5))
    sessions.groupby('channel')['cart_abandoned'].mean().sort_values().plot(kind='bar', color='orange')
    plt.title("Cart Abandonment Rate by Channel")
    plt.ylabel("Abandonment Rate")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/abandonment_by_channel.png")
    plt.close()

    # Wykres: średni czas sesji wg kanału
    plt.figure(figsize=(8, 5))
    sessions.groupby('channel')['duration_sec'].mean().sort_values().plot(kind='bar', color='teal')
    plt.title("Average Session Duration by Channel")
    plt.ylabel("Avg. Duration (seconds)")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/avg_duration_by_channel.png")
    plt.close()

if __name__ == "__main__":
    analyze_sessions('data/sessions.csv', 'outputs')
