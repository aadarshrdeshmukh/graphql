# 🎯 ALL WORKING QUERIES - Copy & Paste Ready

## ✅ TEST QUERIES (READ DATA)

### 1. Get Store with Products and Stock
```graphql
query {
  store(id: 1) {
    id
    name
    address
    openingHours
    inStockProducts {
      product {
        id
        name
        price
        unit
        category {
          name
          description
        }
      }
      inStock
    }
  }
}
```

### 2. Get Customer with Order History
```graphql
query {
  customer(id: 1) {
    id
    name
    address
    phone
    orders {
      edges {
        node {
          id
          status
          total
          deliveryTime
          store {
            name
          }
          items {
            edges {
              node {
                product {
                  name
                }
                quantity
                price
              }
            }
          }
        }
      }
    }
  }
}
```

### 3. Get All Orders (No Filter)
```graphql
query {
  orders {
    id
    customer {
      name
      address
    }
    store {
      name
    }
    status
    total
    deliveryTime
  }
}
```

### 4. Get Orders by Status - Pending
```graphql
query {
  orders(status: "pending") {
    id
    customer {
      name
    }
    store {
      name
    }
    status
    total
    deliveryTime
  }
}
```

### 5. Get Orders by Status - Preparing
```graphql
query {
  orders(status: "preparing") {
    id
    customer {
      name
    }
    status
    total
    deliveryTime
  }
}
```

### 6. Get Orders by Status - On The Way
```graphql
query {
  orders(status: "on_the_way") {
    id
    customer {
      name
    }
    status
    total
    deliveryTime
  }
}
```

### 7. Get Orders by Status - Delivered
```graphql
query {
  orders(status: "delivered") {
    id
    customer {
      name
    }
    status
    total
    deliveryTime
  }
}
```

### 8. Get Products by Category - Fruits (Category 1)
```graphql
query {
  productsByCategory(categoryId: 1) {
    id
    name
    price
    unit
    category {
      name
      description
    }
  }
}
```

### 9. Get Products by Category - Vegetables (Category 2)
```graphql
query {
  productsByCategory(categoryId: 2) {
    id
    name
    price
    unit
    category {
      name
    }
  }
}
```

### 10. Get Products by Category - Dairy (Category 3)
```graphql
query {
  productsByCategory(categoryId: 3) {
    id
    name
    price
    unit
    category {
      name
    }
  }
}
```

### 11. Get Products by Category - Bakery (Category 4)
```graphql
query {
  productsByCategory(categoryId: 4) {
    id
    name
    price
    unit
    category {
      name
    }
  }
}
```

### 12. Get Store 2 Products
```graphql
query {
  store(id: 2) {
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

### 13. Get Customer 2 Details
```graphql
query {
  customer(id: 2) {
    name
    address
    phone
  }
}
```

---

## ✅ TEST MUTATIONS (WRITE DATA)

### 1. Create Order - Basic
```graphql
mutation {
  createOrder(
    customerId: 1
    storeId: 1
    items: [
      { productId: 1, quantity: 2 }
      { productId: 3, quantity: 1 }
    ]
  ) {
    success
    message
    order {
      id
      total
      status
      deliveryTime
      customer {
        name
      }
      store {
        name
      }
      items {
        edges {
          node {
            product {
              name
            }
            quantity
            price
          }
        }
      }
    }
  }
}
```

### 2. Create Order - Multiple Items
```graphql
mutation {
  createOrder(
    customerId: 1
    storeId: 1
    items: [
      { productId: 1, quantity: 5 }
      { productId: 2, quantity: 3 }
      { productId: 6, quantity: 2 }
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

### 3. Create Order - Customer 2, Store 2
```graphql
mutation {
  createOrder(
    customerId: 2
    storeId: 2
    items: [
      { productId: 4, quantity: 2 }
      { productId: 8, quantity: 1 }
    ]
  ) {
    success
    message
    order {
      id
      total
      status
    }
  }
}
```

### 4. Update Order Status - To Preparing
```graphql
mutation {
  updateOrderStatus(orderId: 1, status: preparing) {
    success
    message
    order {
      id
      status
    }
  }
}
```

### 5. Update Order Status - To On The Way
```graphql
mutation {
  updateOrderStatus(orderId: 1, status: on_the_way) {
    success
    message
    order {
      id
      status
      deliveryTime
    }
  }
}
```

### 6. Update Order Status - To Delivered
```graphql
mutation {
  updateOrderStatus(orderId: 1, status: delivered) {
    success
    message
    order {
      id
      status
    }
  }
}
```

---

## 🧪 VALIDATION TEST QUERIES (Error Cases)

### 1. Test Insufficient Stock
```graphql
mutation {
  createOrder(
    customerId: 1
    storeId: 1
    items: [
      { productId: 1, quantity: 200 }
    ]
  ) {
    success
    message
  }
}
```
**Expected Result:** `"success": false, "message": "Insufficient stock..."`

### 2. Test Invalid Customer
```graphql
mutation {
  createOrder(
    customerId: 999
    storeId: 1
    items: [
      { productId: 1, quantity: 1 }
    ]
  ) {
    success
    message
  }
}
```
**Expected Result:** `"message": "Customer with id 999 not found"`

### 3. Test Invalid Store
```graphql
mutation {
  createOrder(
    customerId: 1
    storeId: 999
    items: [
      { productId: 1, quantity: 1 }
    ]
  ) {
    success
    message
  }
}
```
**Expected Result:** `"message": "Store with id 999 not found"`

### 4. Test Invalid Product
```graphql
mutation {
  createOrder(
    customerId: 1
    storeId: 1
    items: [
      { productId: 999, quantity: 1 }
    ]
  ) {
    success
    message
  }
}
```
**Expected Result:** `"message": "Product with id 999 not found"`

### 5. Test Invalid Order ID for Status Update
```graphql
mutation {
  updateOrderStatus(orderId: 999, status: delivered) {
    success
    message
  }
}
```
**Expected Result:** `"message": "Order with id 999 not found"`

---

## 🎯 COMPLETE TEST WORKFLOW

### Step 1: Check Initial Inventory
```graphql
query {
  store(id: 1) {
    name
    inStockProducts {
      product { name }
      inStock
    }
  }
}
```
**Expected:** All products have 100 units in stock

### Step 2: Create an Order
```graphql
mutation {
  createOrder(
    customerId: 1
    storeId: 1
    items: [
      { productId: 1, quantity: 5 }
    ]
  ) {
    success
    message
    order {
      id
      total
      status
    }
  }
}
```
**Expected:** Order created, total = 5 × $1.99 = $9.95, status = "pending"

### Step 3: Verify Inventory Decreased
```graphql
query {
  store(id: 1) {
    inStockProducts {
      product { name }
      inStock
    }
  }
}
```
**Expected:** Apple stock decreased from 100 to 95 ✅

### Step 4: Update Order Status
```graphql
mutation {
  updateOrderStatus(orderId: 1, status: preparing) {
    success
    order { status }
  }
}
```
**Expected:** Status changed to "preparing" ✅

### Step 5: Check Order Status
```graphql
query {
  orders(status: "preparing") {
    id
    customer { name }
    total
  }
}
```
**Expected:** Shows the order with status "preparing" ✅

### Step 6: Check Customer Order History
```graphql
query {
  customer(id: 1) {
    name
    orders {
      edges {
        node {
          status
          total
        }
      }
    }
  }
}
```
**Expected:** Shows customer's order history ✅

### Step 7: Filter Products by Category
```graphql
query {
  productsByCategory(categoryId: 1) {
    name
    price
  }
}
```
**Expected:** Shows only Fruits (Apple, Banana, Orange) ✅

---

## 📊 AVAILABLE DATA

### Stores
- **Store 1:** Downtown Grocery (123 Main St)
- **Store 2:** Uptown Market (456 Oak Ave)

### Categories
1. Fruits
2. Vegetables
3. Dairy
4. Bakery

### Products
1. Apple - $1.99/lb (Fruits)
2. Banana - $0.99/lb (Fruits)
3. Orange - $2.49/lb (Fruits)
4. Carrot - $1.49/lb (Vegetables)
5. Broccoli - $2.99/lb (Vegetables)
6. Milk - $3.99/gallon (Dairy)
7. Cheese - $5.99/lb (Dairy)
8. Bread - $2.49/loaf (Bakery)

### Customers
- **Customer 1:** John Doe (789 Elm St, 555-0101)
- **Customer 2:** Jane Smith (321 Pine St, 555-0102)

### Order Statuses
- `pending`
- `preparing`
- `on_the_way`
- `delivered`

---

## ✅ ALL TEST CASES VERIFIED

1. ✅ **Store inventory tracked** - Query store to see stock levels
2. ✅ **Order totals calculated** - Automatic calculation on order creation
3. ✅ **Status updates work** - Update order status mutation
4. ✅ **Delivery time assigned** - Automatically set to current time + 1 hour
5. ✅ **Customer history complete** - Query customer to see all orders
6. ✅ **Category filtering works** - productsByCategory query
7. ✅ **Stock levels updated** - Inventory decreases after order creation

---

## 🚀 HOW TO USE

1. Open: http://127.0.0.1:8000/graphql
2. Copy any query from above
3. Paste in left panel
4. Click ▶️ Play
5. See results!

**Pro Tip:** Run the "Complete Test Workflow" section step by step to see all features in action!
