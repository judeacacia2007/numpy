import numpy as np
np.random.seed(42)
sales = np.random.randint(500, 2000, size=(5, 7))
print("sales dataset")
print(sales)

print("dataset information")
print("shape :", sales.shape)
print("Dimensions :", sales.ndim)
print("Size :", sales.size)
print("Data Type :", sales.dtype)
print("sales analysis")

store_total = sales.mean(axis=1)
print("total sales of each month:")
print(store_total)

month_total = sales.sum(axis=0)
print("Total Sales of Each Month:")
print(month_total)

month_average = sales.mean(axis=0)
print("Average Sales of Each Month:")
print(month_average)

print("buisness insights")
best_store = np.argmax(store_total)
worst_store = np.argmin(store_total)

print("Best Performing Store :", best_store + 1)
print("Worst Performing Store :", worst_store + 1)
best_month = np.argmax(month_total)
worst_month = np.argmin(month_total)

months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]

print("Best Performing Month :", months[best_month])
print("Worst Performing Month :", months[worst_month])

print("\nHighest Sale :", np.max(sales))
print("Lowest Sale :", np.min(sales))

print("filtering")

high_sales = sales[sales > 150000]
print("Sales greater than 150000:")
print(high_sales)

print("\nNumber of sales greater than 180000:")
print(np.sum(sales > 180000))
print("\nNumber of sales less than 75000:")
print(np.sum(sales < 75000))

print("top and bottom stores")

top3 = np.argsort(store_total)[-3:][::-1]
bottom3 = np.argsort(store_total)[:3]

print("Top 3 Stores:")
print(top3 + 1)

print("Bottom 3 Stores:")
print(bottom3 + 1)

print("Overall Sales :", np.sum(sales))
print("Overall Average Sale :", np.mean(sales))
print("Highest Sale :", np.max(sales))
print("Lowest Sale :", np.min(sales))
