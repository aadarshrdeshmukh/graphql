"""Seed database with sample data for testing"""
from grocery_api.database import SessionLocal, init_db
from grocery_api.models import Store, Category, Product, Inventory, Customer

def seed_database():
    init_db()
    db = SessionLocal()
    
    try:
        # Create categories
        categories = [
            Category(name="Fruits", description="Fresh fruits"),
            Category(name="Vegetables", description="Fresh vegetables"),
            Category(name="Dairy", description="Dairy products"),
            Category(name="Bakery", description="Bread and baked goods"),
        ]
        db.add_all(categories)
        db.commit()
        
        # Create stores
        stores = [
            Store(name="Downtown Grocery", address="123 Main St", opening_hours="8AM-10PM"),
            Store(name="Uptown Market", address="456 Oak Ave", opening_hours="7AM-11PM"),
        ]
        db.add_all(stores)
        db.commit()
        
        # Create products
        products = [
            Product(name="Apple", category_id=1, price=1.99, unit="lb"),
            Product(name="Banana", category_id=1, price=0.99, unit="lb"),
            Product(name="Orange", category_id=1, price=2.49, unit="lb"),
            Product(name="Carrot", category_id=2, price=1.49, unit="lb"),
            Product(name="Broccoli", category_id=2, price=2.99, unit="lb"),
            Product(name="Milk", category_id=3, price=3.99, unit="gallon"),
            Product(name="Cheese", category_id=3, price=5.99, unit="lb"),
            Product(name="Bread", category_id=4, price=2.49, unit="loaf"),
        ]
        db.add_all(products)
        db.commit()
        
        # Create inventory for stores
        inventory_items = []
        for store in stores:
            for product in products:
                inventory_items.append(
                    Inventory(store_id=store.id, product_id=product.id, quantity=100)
                )
        db.add_all(inventory_items)
        db.commit()
        
        # Create customers
        customers = [
            Customer(name="John Doe", address="789 Elm St", phone="555-0101"),
            Customer(name="Jane Smith", address="321 Pine St", phone="555-0102"),
        ]
        db.add_all(customers)
        db.commit()
        
        print("✅ Database seeded successfully!")
        print(f"Created {len(categories)} categories")
        print(f"Created {len(stores)} stores")
        print(f"Created {len(products)} products")
        print(f"Created {len(inventory_items)} inventory items")
        print(f"Created {len(customers)} customers")
        
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
