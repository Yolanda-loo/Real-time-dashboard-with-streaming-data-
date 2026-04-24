import time
import random
import pandas as pd
from datetime import datetime

# Step 1: Define product and region pools
products = ["SUV", "Sedan", "Truck", "Motorbike", "Accessories"]
regions = ["North", "South", "East", "West"]

# Step 2: Simulate streaming transactions
def generate_transaction(transaction_id):
    return {
        "TransactionID": transaction_id,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Product": random.choice(products),
        "Region": random.choice(regions),
        "Revenue": round(random.uniform(100, 5000), 2)
    }

# Step 3: Stream transactions
def stream_transactions(n=20, delay=1):
    transactions = []
    for i in range(n):
        tx = generate_transaction(i+1)
        transactions.append(tx)
        print(tx)
        time.sleep(delay)  # simulate real-time delay
    return pd.DataFrame(transactions)

# Run simulation
if __name__ == "__main__":
    df = stream_transactions(n=50, delay=0.5)
    df.to_csv("data/streamed_sales.csv", index=False)
    print("Streaming complete. Data saved to data/streamed_sales.csv")
