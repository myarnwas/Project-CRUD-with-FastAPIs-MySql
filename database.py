from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# عدّل بيانات الاتصال حسب إعدادات MySQL عندك
DATABASE_URL = "mysql+mysqlconnector://username:password@localhost:3306/testdb"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
