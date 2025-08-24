# test_imports.py
try:
    import models
    print("✅ Models imported successfully")
except ImportError as e:
    print(f"❌ Error importing models: {e}")

try:
    from database import engine, Base
    print("✅ Database imported successfully")
except ImportError as e:
    print(f"❌ Error importing database: {e}")

# Try to create tables
try:
    from database import engine, Base
    import models
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully")
except Exception as e:
    print(f"❌ Error creating tables: {e}")