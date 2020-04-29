# 1) Returns all customers from customer table
customers = Customer.objects.all()

# 2) Returns first customer in customers list
firstCustomer = Customer.objects.first()

# 3) Returns last customer in customers list
lastCustomer = Customer.objects.last()

# 4) Returns single customer by name
customerByName = Customer.objects.get(name='Joseph Boadi')

# 5) Returns single customer by name
customerById = Customer.objects.get(id=2)

# 6) Returns all orders related to a customer (firstCustomer variable set above)
firstCustomer.order_set.all()

# 7) Returns orders customer name (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

# 8) Returns products from products table with value of "Out Door" in categories attribute
products = Product.objects.filter(category="Out Door")

# 9) Order/sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# 10) Returns all products with tag of "Sports": (Query Many to Many Fields)
productsFiltered = Product.objects.filter(tags__name="Sports")

# Returns the total count for number of talls a "Ball" was ordered by firstCustomer
ballOrders = firstCustomer.order_set.filter(product_name="Ball").count()

# Returns total count for each product ordered
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

# Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


# RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)


class ChildModel(models.Model):
    parent = models.ForeignKey('TargetModel', on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, blank=True, null=True)

parent = ParentModel.objects.first()
# Returns all child models related to parent
parent.childmodel_set.all()




