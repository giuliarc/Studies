# Following the business rules specified, let's build the code that will be used by the test.
# When specifying business features, entities and it's attibutes were defined.
# Here, we structure these entities, respecting the specifications

#order_atrib_BU

from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set

@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int

class Batch:
    def __init__(self, ref: str, sku:str, qty: int, eta: Optional[date]):
      self.reference = ref
      self.sku = sku
      self.eta = eta
      self.available_quantity = qty
      # Batch have two more attributes: purchase_quantity and allocations
      # From this, more methods where included, considering allocation possibilities
      self._purchased_quantity = qty
      self._allocations = set() #type Set[OrderLine]

    def allocate(self, line:OrderLine):
       if self.can_allocate(line):
          self._allocations.add(line)

    def deallocate(self, line:OrderLine):
       if line in self.allocations

    @property
    def allocated_quantity(self) -> int:
        """ Notes about @property decorator (:doc:docs/source/notes.md#using_property_decorator)"""
        return sum(line.qty for line in self._allocations)

    def can_allocate(self, line:OrderLine) -> bool:
       return self.sku == line.sku and self.available_quantity >= line.qty