from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://u508qr7czvn9efud:6a1NmvGOTY0q3MoJeSjw@b24a0ybxg1uqiep6ko1s-mysql.services.clever-cloud.com:3306/b24a0ybxg1uqiep6ko1s', echo=True)

Session = sessionmaker(bind=engine)
