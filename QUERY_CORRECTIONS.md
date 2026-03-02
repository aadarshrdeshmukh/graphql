# ❌ vs ✅ Query Corrections

## Your Original Queries vs Working Queries

---

## Query 1: Get Store Products

### ❌ What You Tried (Doesn't Work):
```graphql
query {
  store(id: 1) {
    name
    products {           # ← Field doesn't exist
      name
      price
      inStock
    }
  }
}
```

### ✅ Correct Query:
```graphql
query {
  store(id: 1) {
    name
    inStockProducts {    # ← Correct field name
      product {          # ← Need to access product object
        name
        price
      }
      inStock            # ← Stock is separate from product
    }
  }
}
```

**Why:** The store doesn't have a direct `products` field. It has `inStockProducts` which returns products WITH their stock levels.

---

## Query 2: Get Customer Orders

### ❌ What You Tried (Doesn't Work):
```graphql
query {
  customer(id: 1) {
    name
    orders {             # ← This is a Relay connection
      status
      total
      items { 
        product { name } 
      }
    }
  }
}
```

### ✅ Correct Query:
```graphql
query {
  customer(id: 1) {
    name
    orders {
      edges {            # ← Need edges/node for Relay
        node {
          status
          total
          items {
            edges {      # ← Items also use Relay
              node {
                product { name }
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

**Why:** The schema uses Relay connections (edges/node pattern) for relationships.

---

## Mutation 1: Create Order

### ❌ What You Tried (Doesn't Work):
```graphql
mutation {
  createOrder(input: {   # ← No "input" wrapper
    customerId: 1
    storeId: 1
    items: [
      { productId: 1, quantity: 2 }
    ]
  }) {
    order {
      id
      total
    }
  }
}
```

### ✅ Correct Mutation:
```graphql
mutation {
  createOrder(          # ← Direct arguments, no "input"
    customerId: 1
    storeId: 1
    items: [
      { productId: 1, quantity: 2 }
    ]
  ) {
    success            # ← Returns success/message/order
    message
    order {
      id
      total
      status
    }
  }
}
```

**Why:** The mutation doesn't use an `input` wrapper. Arguments are passed directly.

---

## Mutation 2: Update Order Status

### ❌ What You Tried (Doesn't Work):
```graphql
mutation {
  updateOrderStatus(input: {  # ← No "input" wrapper
    orderId: 1
    status: "delivered"       # ← String doesn't work
  }) {
    order {
      id
      status
    }
  }
}
```

### ✅ Correct Mutation:
```graphql
mutation {
  updateOrderStatus(          # ← Direct arguments
    orderId: 1
    status: delivered         # ← Enum value (no quotes)
  ) {
    success                   # ← Returns success/message/order
    message
    order {
      id
      status
    }
  }
}
```

**Why:** 
1. No `input` wrapper needed
2. Status is an enum, not a string (use `delivered` not `"delivered"`)
3. Returns `success`, `message`, and `order`

---

## Query 3: Get Orders by Status

### ❌ What You Tried (Doesn't Work):
```graphql
query {
  orders(status: "on_the_way") {  # ← String works here!
    customer { name }
    deliveryTime
  }
}
```

### ✅ This Actually Works! But Better Version:
```graphql
query {
  orders(status: "on_the_way") {  # ← String is correct for query
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

**Why:** For queries, status can be a string. For mutations, it must be an enum.

---

## 🎯 Key Differences Summary

| Feature | Your Version | Correct Version |
|---------|-------------|-----------------|
| Store products | `products` | `inStockProducts { product { ... } inStock }` |
| Customer orders | Direct access | `edges { node { ... } }` (Relay) |
| Order items | Direct access | `edges { node { ... } }` (Relay) |
| Create order | `input: { ... }` | Direct arguments |
| Update status | `input: { ... }` | Direct arguments |
| Status in mutation | `"delivered"` (string) | `delivered` (enum, no quotes) |
| Status in query | `"pending"` (string) | `"pending"` (string) ✅ |

---

## 📚 Quick Reference

### All Available Queries:
1. `store(id: Int!)` - Get store details
2. `customer(id: Int!)` - Get customer details
3. `orders(status: String)` - Get orders (optional filter)
4. `productsByCategory(categoryId: Int!)` - Get products by category

### All Available Mutations:
1. `createOrder(customerId, storeId, items)` - Create new order
2. `updateOrderStatus(orderId, status)` - Update order status

### Order Status Enum Values:
- `pending`
- `preparing`
- `on_the_way`
- `delivered`

---

## 🚀 Use This File

Open **ALL_WORKING_QUERIES.md** for complete, tested, copy-paste ready queries!
