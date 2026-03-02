# 🛒 Grocery Delivery GraphQL API

A production-ready GraphQL API for grocery delivery built with FastAPI, Graphene, and SQLAlchemy.

## 🚀 Features

- ✅ Complete GraphQL API with queries and mutations
- ✅ Inventory tracking per store
- ✅ Automatic stock deduction on orders
- ✅ Order status management (pending → preparing → on_the_way → delivered)
- ✅ Customer order history
- ✅ Category-based product filtering
- ✅ Automatic delivery time calculation
- ✅ Input validation and error handling

## 🛠️ Tech Stack

- **FastAPI** - Modern web framework
- **Graphene** - GraphQL implementation
- **SQLAlchemy 2.0** - ORM
- **Uvicorn** - ASGI server
- **SQLite** - Database (easily switchable to PostgreSQL)
- **starlette-graphene3** - GraphQL Playground

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/aadarshrdeshmukh/graphql.git
cd graphql
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Seed the database
```bash
python seed_data.py
```

### 5. Run the server
```bash
uvicorn grocery_api.main:app --reload
```

The API will be available at:
- **API:** http://127.0.0.1:8000
- **GraphQL Playground:** http://127.0.0.1:8000/graphql

## 📖 Documentation

- **ALL_WORKING_QUERIES.md** - Complete collection of all working queries
- **QUERY_CORRECTIONS.md** - Common mistakes and corrections

## 🎯 Quick Start

### Open GraphQL Playground
Navigate to http://127.0.0.1:8000/graphql in your browser

### Example Query - Get Store Products
```graphql
query {
  store(id: 1) {
    name
    address
    inStockProducts {
      product {
        name
        price
      }
      inStock
    }
  }
}
```

### Example Mutation - Create Order
```graphql
mutation {
  createOrder(
    customerId: 1
    storeId: 1
    items: [
      { productId: 1, quantity: 2 }
      { productId: 6, quantity: 1 }
    ]
  ) {
    success
    message
    order {
      id
      total
      status
      deliveryTime
    }
  }
}
```

## 📊 Database Schema

### Tables
- **stores** - Store information
- **categories** - Product categories
- **products** - Product catalog
- **inventory** - Stock levels per store
- **customers** - Customer information
- **orders** - Order records
- **order_items** - Order line items

### Sample Data
- 2 Stores
- 4 Categories (Fruits, Vegetables, Dairy, Bakery)
- 8 Products
- 2 Customers
- All products have 100 units in stock initially

## 🔥 Key Features

### Inventory Management
- Track stock per store
- Automatic deduction on order creation
- Prevent orders when stock insufficient

### Order Processing
- Validate customer, store, and products
- Calculate total automatically
- Assign delivery time (current + 1 hour)
- Create order items with price snapshot
- Set initial status to "pending"

### GraphQL Queries
- `store(id)` - Get store with in-stock products
- `customer(id)` - Get customer with order history
- `orders(status)` - Filter orders by status
- `productsByCategory(categoryId)` - Get products by category

### GraphQL Mutations
- `createOrder` - Create new order with validation
- `updateOrderStatus` - Update order status

## 🧪 Testing

All queries are documented in **ALL_WORKING_QUERIES.md**

### Test Workflow
1. Check initial inventory
2. Create an order
3. Verify inventory decreased
4. Update order status
5. Check customer order history
6. Filter products by category

## 📁 Project Structure

```
grocery_api/
├── database.py              # Database configuration
├── main.py                  # FastAPI app & GraphQL setup
├── models/                  # SQLAlchemy models
│   ├── store.py
│   ├── product.py
│   ├── category.py
│   ├── inventory.py
│   ├── customer.py
│   ├── order.py
│   └── order_item.py
├── types/                   # GraphQL types
│   ├── store.py
│   ├── product.py
│   ├── category.py
│   ├── customer.py
│   ├── order.py
│   └── order_item.py
├── queries/                 # GraphQL queries
│   └── root.py
└── mutations/               # GraphQL mutations
    ├── store.py
    ├── product.py
    ├── customer.py
    └── order.py
```

## 🔄 Switch to PostgreSQL

Update `grocery_api/database.py`:
```python
DATABASE_URL = "postgresql://user:password@localhost/dbname"
```

## 📝 License

MIT

## 👤 Author

Aadarsh Deshmukh
- GitHub: [@aadarshrdeshmukh](https://github.com/aadarshrdeshmukh)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show your support

Give a ⭐️ if this project helped you!
