<font color="indianred">

# Notes, concepts and observations

</font>

## Domain and business concepts

When dealing with business projects, we can "depare" with specific jargons. From this, we have the ubiquitous language

> Ubiquitous language for this case

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


> So, from the gathered basic functional requisits of 
>
> our business, we start writing our tests that assures 
>
> this requisits will be respected. Having the test, we 
>
> write the underlying code responsible for doing the 
>
> task.



<p>

>(at firsy glance, looks kinda crazy and contraintuituve the ideia of developing the test before the underlying code, but when applied, we have to admit: it's a very clever approach)🤪


### Conceptual explanations

#### using_property_decorator
<details>
    <summary>What's @property decorator</summary>
    The @property decorator is a built-in construct in Python that provides a concise way to define properties in classes. It essentially creates a getter method that behaves like an attribute when accessed. Here's a breakdown of its functionality:

    Functionality:

    Transforms a Method into an Attribute: When you apply @property to a method within a class, it alters how that method is invoked. Instead of calling it like a regular method with parentheses, you can access it directly using dot notation, just like an attribute.

    Getters and Setters (Optional): The @property decorator can also be used in conjunction with the @setter.setter and @deleter.deleter decorators to define setter and deleter methods for the property. These methods control how the property's value can be set and deleted, respectively.

</details>