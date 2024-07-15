from sqlalchemy.orm import mapper, relatioship

import allocation.domain.model as model #The ORM imports (knows about) the Domain, not the other way

metadata = MetaData()

order_lines = Table(
    "order_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(255)),
    Column("qty", Integer, nullable=False)
    Column("orderid", String(255))
)

def start_mappers():
    lines_mapper = mapper(model.OrderLine, order_lines)