from django.db import models

# Create your models here.
'''
Each Store should have a store name, 
a store location
and a contact email address for the store.
'''
class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name
'''Each Tub should contain information on the flavour of the tub,
the size of the tub (in litres), 
whether or not the tub is vegan, 
whether or not the tub is gluten free 
and which store the tub is assigned to.
'''
class Tub(models.Model):
    # use tuple for flavors
    FLAVOR_CHOICES = [
        ('Blueberry', 'Blueberry'),
        ('Vanilla', 'Vanilla'),
        ('Chocolate', 'Chocolate'),
        ('Strawberry', 'Strawberry'),
        ('Banana', 'Banana'),
        ('Mango', 'Mango')
    ]
    flavor = models.CharField(max_length=50, choices=FLAVOR_CHOICES)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    is_vegan = models.BooleanField()
    is_gluten_free = models.BooleanField()
    # store - tube, one to many relationship
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['flavor', 'size', 'is_vegan', 'is_gluten_free', 'store']
    
    def __str__(self):
        return f"{self.size}L {self.flavor} Tube from {self.store.name}"