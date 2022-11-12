import json
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import create_tables, del_tables, Book, Publisher, Stock, Shop, Sale
from db_auth import USER, PASSWORD


def upload_to_db(session):
    with open('fixtures.json', encoding='utf-8') as f:
        data = json.load(f)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]

        session.add(model(id=record.get('pk'), **record.get('fields')))
        session.commit()


DSN = f'postgresql://{USER}:{PASSWORD}@localhost:5432/book_catalog'
engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # del_tables(engine)

    create_tables(engine)
    upload_to_db(session)

    publisher = input('Введите имя издателя: ')
    result = session.query(Publisher.name, Book.title, Shop.name, Sale.price * Sale.count, Sale.date_sale). \
        join(Book).join(Stock).join(Sale).join(Shop).filter(Publisher.name == publisher).all()

    for row in result:
        print(*row, sep=' | ')
