# test_sqlalchemy.py
try:
    from sqlalchemy import create_engine, Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    
    print("✅ SQLAlchemy imported successfully")
    
    # Test basic functionality
    Base = declarative_base()
    
    class TestModel(Base):
        __tablename__ = 'test_table'
        id = Column(Integer, primary_key=True)
        name = Column(String(50))
    
    print("✅ SQLAlchemy basic functionality works")
    
except ImportError as e:
    print(f"❌ SQLAlchemy import failed: {e}")