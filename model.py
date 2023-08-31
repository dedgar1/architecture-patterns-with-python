from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass(frozen=True)
class Orderline:
    orderid: str
    sku: str
    qty: int

class Batch: 
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        self.reference = reference = ref
        self.sku = sku
        self.eta = eta
        self.available_quantity = qty

    def allocate(self, line: Orderline):
        self.available_quantity -= line.qty