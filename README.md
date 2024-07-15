<font color="indianred">

# Notes, concepts and observations

</font>

## Domain and business concepts

When dealing with business projects, we can come across specific jargons. From this, we have the ubiquitous language

> **Ubiquitous language for this case**

- SKU (stock-keeping-unit): identification of a product (in practice, the product name)

- Customers: place *orders*

- Order: identified by an *order reference*; comprises multiple *order lines* {src\model.py}

- &nbsp;&nbsp;&nbsp;&nbsp;Order line: has a SKU and a *quantity*

- Batch: related to stock. Has a unique ID, a SKU and a quantity

**Here, we start projecting how the entities will work, paying attention in some business rules**

- Order lines must be allocated to batches
- We must deal with *available quantity*: addition and deletion of elements according to orders
- It's not possible to allocate a order whose quantity is higher than the available in batch (business test-case)
- We can't allocate the same line twice (test-case)
- We will face scenarios like - batches have an *ETA* if they are currently shipping, or they may be in *warehouse*

![UML Model ](image.png)


> So, from the gathered basic functional requisits of 
>
> our business, we start writing our tests that assures 
>
> this requisits will be respected. Having the test, we 
>
> write the underlying code responsible for doing the 
>
> task.

**Value Objects and Entities**

An order line is uniquely identified by its order ID, SKU, and quantity; if we change one of those values, we now have a new line. That’s the definition of a value object: any object that is identified only by its data and doesn’t have a long-lived identity. What about a batch, though? That is identified by a reference.

We use the term entity to describe a domain object that has long-lived identity. On the previous page, we introduced a Name class as a value object. If we take the name Harry Percival and change one letter, we have the ne


<p>
(at first glance, looks kinda crazy and contraintuituve the ideia of developing the test before the underlying code, but when applied, we have to admit: it's a very clever approach)🤪
</p>

### Conceptual explanations

#### using_property_decorator
<details>
    <summary>What's @property decorator</summary>
    
    The @property decorator is a built-in construct in Python that provides a concise way to define properties in classes. It essentially creates a getter method that behaves like an attribute when accessed. Here's a breakdown of its functionality:

    Functionality:

    Transforms a Method into an Attribute: When you apply @property to a method within a class, it alters how that method is invoked. Instead of calling it like a regular method with parentheses, you can access it directly using dot notation, just like an attribute.

    Getters and Setters (Optional): The @property decorator can also be used in conjunction with the @setter.setter and @deleter.deleter decorators to define setter and deleter methods for the property. These methods control how the property's value can be set and deleted, respectively.

</details>

#### idempotence_definition
<details>
    <summary>Idempotence</summary>
    Idempotence is a property of certain operations or actions that ensures they can be applied multiple times without changing the outcome, beyond the initial application. In simpler terms, performing an idempotent operation multiple times has the same effect as performing it just once.
</details>

#### using_dataclasses
<details>
    <summary>Dataclasses</summary>
    Whenever we have a business concept that has data but no identity, we often choose to represent it using the *Value Object* pattern. A value object is any domain objet that is uniquely identified by the data it holds; we usually make them immutable:

<code>
    @dataclass(frozen=True)
    class OrderLine:
        orderid: OrderReference
        sku: ProductReference
        qty: Quantity
</code>
</details>
<br>

>
>**Value Object**<br>
>Any object is identified only by its data and doesn't have a long-lived identity (ex: order lines)
>
>**Entity**<br>
> A domain object that has long-lived identity (ex: individual (people) identity)
>
> Entities, unlike values, have *identity equality*. We can change their values, but they still recognizable


<div class="admonitionblock warning">
<table>
<tr>
<td class="icon">
<div class="title">Warning</div>
</td>
<td class="content">
    DO NOT MODIFY <code>__hash__</code>
    WITHOUT ALSO MODIFYING <code>__eq__</code>.     
</td>
</tr>
</table>
</div>
</div>
</div>

**Not everything has to be an Object (here we go): DOMAIN SERVICE**

Domain Service operations don't have a natural home in an entity or value object.
A "thing" that allocates and *order line*, given a set of *batches*, sounds like a function.<br>
:sparkles: Let's make a function! :sparkles:

NEXT and SORTED works together to find the first suitable batch, instead of listing and search between all of them<br>
:elephant: *memory efficiency* :elephant:

**Domain Modeling Recap (in my words)**

- Domain modeling:
  - Is the closest part to the business. More likely to change. Make it easy to understand and modify
  
- Distinguish entities from value objects
  - Value object: defined by its attributes. Best when immutable (different attribute = different object)
  - Entity: attributes may vary, but still being the same entity (usually has a name or reference)

- Not everything has to be an object
  - Let the verbs be functions! (Instead of a BarBuilder, what about a build_bar()?)

- Time to apply your best OO design principles
  - HA HA HA HA HA HA :joy:
  - SOLID *e os caramba*

**Chapter 2: Repository Pattern**

Sits between our domain model and the database

Layered architecture

Presentation Layer -> Business Logic -> Database Layer

Onion architecture

Presentation Layer -> Domain Model <- Database Layer

:sparkles: Boil down to the dependency inversion principle: high-lever modules (the domain) should not depend on low-level ones (the infrastructure) :sparkles:

We are not going to make a "declarative" code for ORM use.
We will use "classical mapping", where ORM depends on model
  - Declare an explicit *mapper*

With SQLAlchemy we can use *alembic* https://alembic.sqlalchemy.org/en/latest/

About repository pattern: even though our objects are in memory, we need to put them somewhere so we can find them again.
The core methods are **add()** and **get()**. We can define them in our abstract base class

:pushpin: We will have to write in our repository class each time we add a new domain object that we want to retrieve

:bulb: **The repository pattern would make it easy to make fundamental changes to the way we store things**