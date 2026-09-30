from json import dumps

# 1. Store customer orders
# Create a list of customer names
# Store each customer's order details (customer name, product, price, category) as tuples inside a list
# Use a dictionary where keys are customer names and values are lists of ordered products

# Assignment: "Create a list of customer names"
customer_names = [
    "Alice Johnson",
    "Brian Smith",
    "Carla Davis",
    "David Wilson",
    "Emma Brown",
    "Frank Miller",
    "Grace Taylor",
]

# Assignment: "Store each customer's order details as tuples inside a list"
# Tuple format: (customer name, product, price, category)
orders = [
    ("Alice Johnson", "Laptop", 850.00, "Electronics"),
    ("Alice Johnson", "T-Shirt", 25.00, "Clothing"),
    ("Alice Johnson", "Coffee Maker", 75.00, "Home Essentials"),

    ("Brian Smith", "Headphones", 120.00, "Electronics"),
    ("Brian Smith", "Jeans", 60.00, "Clothing"),

    ("Carla Davis", "Desk Lamp", 35.00, "Home Essentials"),
    ("Carla Davis", "T-Shirt", 25.00, "Clothing"),

    ("David Wilson", "Smartphone", 700.00, "Electronics"),
    ("David Wilson", "Sneakers", 90.00, "Clothing"),
    ("David Wilson", "Desk Lamp", 35.00, "Home Essentials"),

    ("Emma Brown", "Coffee Maker", 75.00, "Home Essentials"),
    ("Emma Brown", "Jeans", 60.00, "Clothing"),
    ("Emma Brown", "Headphones", 120.00, "Electronics"),

    ("Frank Miller", "T-Shirt", 25.00, "Clothing"),
    ("Frank Miller", "Desk Lamp", 35.00, "Home Essentials"),

    ("Grace Taylor", "Laptop", 850.00, "Electronics"),
    ("Grace Taylor", "Sneakers", 90.00, "Clothing"),
]

# Assignment: "Use a dictionary where keys are customer names
# and values are lists of ordered products"
customer_orders = {}

for customer, product, price, category in orders:
    customer_orders.setdefault(customer, []).append(product)

# 2. Classify products by category 
# Use a dictionary to map each product to its respective category 
# Create a set of unique product categories 
# Display all available product categories

# Assignment: "Use a dictionary to map each product to its respective category"
product_categories = {
    "Laptop": "Electronics",
    "Headphones": "Electronics",
    "Smartphone": "Electronics",
    "T-Shirt": "Clothing",
    "Jeans": "Clothing",
    "Sneakers": "Clothing",
    "Coffee Maker": "Home Essentials",
    "Desk Lamp": "Home Essentials",
}

# Assignment: "Create a set of unique product categories"
unique_categories = set(product_categories.values())

# 3. Analyze customer orders 
# Use a loop to calculate the total amount each customer spends 
# If the total purchase value is above $100, classify the customer as a high-value buyer 
# If it is between $50 and $100, classify the customer as a moderate buyer 
# If it is below $50, classify them as a low-value buyer 

# Assignment: "Use a loop to calculate the total amount each customer spends"
customer_totals = {}

for customer in customer_names:
    total = 0.0

    for order_customer, product, price, category in orders:
        if order_customer == customer:
            total += price

    customer_totals[customer] = total

# Assignment:
# Above $100 -> high-value
# $50-$100 -> moderate
# Below $50 -> low-value
customer_classification = {}

for customer, total in customer_totals.items():
    if total > 100:
        customer_classification[customer] = "High-value buyer"
    elif 50 <= total <= 100:
        customer_classification[customer] = "Moderate buyer"
    else:
        customer_classification[customer] = "Low-value buyer"

# 4. Generate business insights 
# Calculate the total revenue per product category and store it in a dictionary 
# Extract unique products from all orders using a set 
# Use a list comprehension to find all customers who purchased electronics 
# Identify the top three highest-spending customers using sorting

# Assignment: "Calculate the total revenue per product category
# and store it in a dictionary"
category_revenue = {}

for customer, product, price, category in orders:
    category_revenue[category] = category_revenue.get(category, 0) + price

# Assignment: "Extract unique products from all orders using a set"
unique_products = {
    product
    for customer, product, price, category
    in orders
}

# Assignment: "Use a list comprehension to find all customers
# who purchased electronics"
electronics_customers = [
    customer
    for customer, product, price, category in orders
    if category == "Electronics"
]

# Remove duplicates
electronics_customers = list(set(electronics_customers))

# Assignment: "Identify the top three highest-spending customers using sorting"
top_three_customers = sorted(
    customer_totals.items(),
    key=lambda item: item[1],
    reverse=True,
)[:3]

# Assignment: "Extract most frequently purchased products"
product_frequency = {}

for customer, product, price, category in orders:
    if product in product_frequency:
        product_frequency[product] += 1
    else:
        product_frequency[product] = 1

most_frequent_products = sorted(
    product_frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

# 5. Organize and display data 
# Print a summary of each customer’s total spending and their classification 
# Use set operations to find customers who purchased from multiple categories 
# Identify common customers who bought both electronics and clothing

# Pretty-print categories
print("Categories")
for category in sorted(unique_categories):
    print(f"- {category}")

print("\nRevenue by category")
for category, revenue in sorted(
    category_revenue.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(f"{category}: ${revenue:,.2f}")

# Assignment: "Print a summary of each customer's total spending
# and their classification"
print()
for customer in customer_names:
    print(
        f"{customer}: "
        f"${customer_totals[customer]:,.2f} | "
        f"{customer_classification[customer]}"
    )

# Assignment: "Identify common customers who bought both
# electronics and clothing"

# Build a set of customers for each category
category_customers = {}

for customer, product, price, category in orders:
    category_customers.setdefault(category, set()).add(customer)

electronics_customers_set = category_customers.get("Electronics", set())
clothing_customers_set = category_customers.get("Clothing", set())

electronics_and_clothing = electronics_customers_set & clothing_customers_set

print("\nPurchased both electronics and clothing:")
for customer in sorted(electronics_and_clothing):
    print(f"- {customer}")
