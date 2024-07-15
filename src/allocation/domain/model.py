# Following the business rules specified, let's build the code that will be used by the test.
# When specifying business features, entities and it's attibutes were defined.
# Here, we structure these entities, respecting the specifications

#order_atrib_BU

from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set

class OutOfStock(Exception):
   pass

# Defined after Domain Services concept was introduced
def allocate(line: OrderLine, batches: List[Batch]) -> str:
   # NEXT and SORTED works together to find the first suitable batch, instead of listing and search between all of them
   try:
      batch = next(b for b in sorted(batches) if b.can_allocate(line))
      batch.allocate(line)
      return batch.reference
   except StopIteration:
      raise OutOfStock(f"Out of stock for sku {line.sku}")
             

@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int


# Applying identity equality
class Batch:
    def __init__(self, ref: str, sku:str, qty: int, eta: Optional[date]):
      self.reference = ref
      self.sku = sku
      self.eta = eta
      #self.available_quantity = qty
      # Batch have two more attributes: purchase_quantity and allocations
      # From this, more methods where included, considering allocation possibilities
      self._purchased_quantity = qty
      self._allocations = set() #type Set[OrderLine]
    
    def __eq__(self, other):
       # Defines the behavior of the class for the == operator
       if not isinstance(other, Batch):
          return False
       return other.reference == self.reference
    
    def __hash__(self):
       # Control behavior of objects added to sets or used as dicts
       return hash(self.reference)
    
    def __gt__(self, other):
      # Here, the gt is for greater than
      if self.eta is None:
         return False # Other is greater
      if other.eta is None:
         return True # Self is greater
      return self.eta > other.eta # Actual comparison

    
    def allocate(self, line:OrderLine):
       if self.can_allocate(line):
          self._allocations.add(line)

    def deallocate(self, line:OrderLine):
       if line in self._allocations:
          self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        """Notes about @property decorator
        :doc:docs/source/notes.md#using_property_decorator
        """ 
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
       return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line:OrderLine) -> bool:
       return self.sku == line.sku and self.available_quantity >= line.qty