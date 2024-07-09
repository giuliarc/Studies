# Following the business rules specified, let's build the code that will be used by the test.
# When specifying business features, entities and it's attibutes were defined.
# Here, we structure these entities, respecting the specifications

#order_atrib_BU
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

    def allocate(self, line:OrderLine)
       self.available_quantity -= line.qty