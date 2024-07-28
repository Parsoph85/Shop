from typing import Optional, List

from eshop.businsess_logic.product import Product


def product_create(dto) -> Product:
    raise Exception('Not implemented yet')


def product_get_by_id(id: str) -> Optional[Product]:
    raise Exception('Not implemented yet')


def product_get_many(page: int, limit: int) -> List[Product]:
    raise Exception('Not implemented yet')