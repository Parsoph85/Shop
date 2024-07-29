from typing import Optional, List
import uuid

from eshop.businsess_logic.product import Product
from eshop.data_access.product_repo import get_by_id, get_many, save


def product_create(name:str, price:float) -> Product:
    product = Product(
        id=str(uuid.uuid4()),
        name=name,
        price=price,
    )
    save(product)
    return product


def product_get_by_id(id: str) -> Optional[Product]:
    return get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    return get_many(page=page, limit=limit)
