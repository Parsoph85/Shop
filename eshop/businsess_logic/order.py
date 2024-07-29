from dataclasses import dataclass
from typing import List

from eshop.businsess_logic.product import Product


@dataclass
class Order:
    id: str
    product_ids: List[str]
    total: int
