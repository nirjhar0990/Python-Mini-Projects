import numpy as np
from datetime import datetime


# ============================================================
# 1. Load Dataset
# ============================================================

file_path = "data/messy_sales_data.csv"

data = np.genfromtxt(
    file_path,
    delimiter=",",
    dtype=str,
    encoding="utf-8",
    skip_header=0
)


# ============================================================
# 2. Extract Numeric Data
# ============================================================

# Numeric columns:
# Quantity, Unit_Price, Discount, Customer_Age
numeric_data = data[1:, 4:8]

# Create a floating-point array and initialize missing values as NaN
numeric_float = np.full(numeric_data.shape, np.nan)

missing_mask = (
    (numeric_data == "") |
    (numeric_data == "N/A") |
    (numeric_data == "Unknown")
)

numeric_float[~missing_mask] = numeric_data[~missing_mask].astype(float)


# ============================================================
# 3. Normalize Categorical Data
# ============================================================

category = np.char.title(data[1:, 3])

store_location = data[1:, 9]
# ============================================================
# 3. Normalize Categorical Data
# ============================================================

category = np.char.title(data[1:, 3])

store_location = np.char.title(data[1:, 9])

payment_method = data[1:, 8]


# ============================================================
# 4. Handle Missing Numeric Values
# ============================================================

# Calculate the median of each numeric column.
median_values = np.nanmedian(numeric_float, axis=0)

# Replace missing numeric values with the corresponding median.
for i in range(4):
    numeric_float[np.isnan(numeric_float[:, i]), i] = median_values[i]


# ============================================================
# 5. Validate and Clean Numeric Values
# ============================================================

# Quantity must be greater than zero.
invalid_quantity = numeric_float[:, 0] <= 0
numeric_float[invalid_quantity, 0] = median_values[0]


# Unit price must be greater than zero and within a reasonable range.
invalid_price = (
    (numeric_float[:, 1] <= 0) |
    (numeric_float[:, 1] > 500)
)

numeric_float[invalid_price, 1] = median_values[1]


# Customer age must be between 18 and 100.
invalid_age = (
    (numeric_float[:, 3] < 18) |
    (numeric_float[:, 3] > 100)
)

numeric_float[invalid_age, 3] = median_values[3]


# ============================================================
# 6. Prepare Date Data
# ============================================================

dates = data[1:, 1]
# ============================================================
# 6. Clean Date Values
# ============================================================

converted_dates = []

for date in dates:
    try:
        converted_date = datetime.strptime(date, "%m/%d/%Y")
        converted_dates.append(converted_date)
    except ValueError:
        converted_dates.append(None)


# Convert valid dates back to the original CSV format.
# Invalid dates are stored as blank values.
cleaned_dates = np.array([
    date.strftime("%m/%d/%Y") if date is not None else ""
    for date in converted_dates
])


# ============================================================
# 7. Clean Payment Method
# ============================================================

payment_method = data[1:, 8]

payment_method = np.char.title(payment_method)
payment_method[payment_method == "Paypal"] = "PayPal"
payment_method[payment_method == ""] = "Unknown"


# ============================================================
# 8. Convert Numeric Data to Strings
# ============================================================

quantity = numeric_float[:, 0].astype(str)
unit_price = numeric_float[:, 1].astype(str)
discount = numeric_float[:, 2].astype(str)
customer_age = numeric_float[:, 3].astype(str)


# ============================================================
# 9. Create Cleaned Dataset
# ============================================================

cleaned_columns = [
    data[1:, 0],       # Order_ID
    cleaned_dates,     # Date
    data[1:, 2],       # Product
    category,          # Category
    quantity,          # Quantity
    unit_price,        # Unit_Price
    discount,          # Discount
    customer_age,      # Customer_Age
    payment_method,    # Payment_Method
    store_location     # Store_Location
]

cleaned_data = np.column_stack(cleaned_columns)


# ============================================================
# 10. Sales Calculations
# ============================================================

# Revenue after applying the discount.
total_sales = (
    numeric_float[:, 0]
    * numeric_float[:, 1]
    * (1 - numeric_float[:, 2])
)

# Revenue before applying the discount.
subtotal = numeric_float[:, 0] * numeric_float[:, 1]

# Total discount amount.
discount_amount = subtotal * numeric_float[:, 2]

# Overall sales metrics.
average_order_value = np.mean(total_sales)
total_revenue = np.sum(total_sales)
total_quantity = np.sum(numeric_float[:, 0])
# ============================================================
# 11. Sales Analysis by Product
# ============================================================

products = data[1:, 2]
unique_products = np.unique(products)

product_quantity = []

for product in unique_products:
    total = np.sum(numeric_float[products == product, 0])
    product_quantity.append(total)

product_quantity = np.array(product_quantity)

best_product_index = np.argmax(product_quantity)


# ============================================================
# 12. Sales Analysis by Category
# ============================================================

unique_categories = np.unique(category)

category_quantity = []

for cat in unique_categories:
    total = np.sum(numeric_float[category == cat, 0])
    category_quantity.append(total)

category_quantity = np.array(category_quantity)

best_category_index = np.argmax(category_quantity)


# ============================================================
# 13. Sales Analysis by Store Location
# ============================================================

unique_locations = np.unique(store_location)

location_quantity = []

for location in unique_locations:
    total = np.sum(numeric_float[store_location == location, 0])
    location_quantity.append(total)

location_quantity = np.array(location_quantity)

best_location_index = np.argmax(location_quantity)

# ============================================================
# 14. Export Cleaned Dataset
# ============================================================

output_file = "data/cleaned_sales_data_retest.csv"

np.savetxt(
    output_file,
    cleaned_data,
    delimiter=",",
    fmt="%s",
    header="Order_ID,Date,Product,Category,Quantity,Unit_Price,Discount,Customer_Age,Payment_Method,Store_Location",
    comments=""
)

print(f"Cleaned dataset saved to: {output_file}")
