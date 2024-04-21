from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Latte(models.Model):
    FLAVOR_CHOICES = [
        ('Caramel', 'Caramel'),
        ('Vanilla', 'Vanilla'),
        ('Hazelnut', 'Hazelnut'),
        ('Cinnamon', 'Cinnamon'),
    ]

    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='latte_images/')

    @property
    def price(self):
        size_price_map = {
            'small': 3.25,
            'medium': 4.25,
            'large': 5.25,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name
    
class Macchiato(models.Model):
    FLAVOR_CHOICES = [
        ('Caramel', 'Caramel'),
        ('Vanilla', 'Vanilla'),
        ('Hazelnut', 'Hazelnut'),
        ('Cinnamon', 'Cinnamon'),
    ]

    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='macchiato_images/')

    @property
    def price(self):
        size_price_map = {
            'small': 3.50,
            'medium': 4.50,
            'large': 5.50,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name
    
class Cappuccino(models.Model):
    FLAVOR_CHOICES = [
        ('Caramel', 'Caramel'),
        ('Vanilla', 'Vanilla'),
        ('Hazelnut', 'Hazelnut'),
        ('Cinnamon', 'Cinnamon'),
    ]

    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='cappuccino_images/')

    @property
    def price(self):
        size_price_map = {
            'small': 3.75,
            'medium': 4.75,
            'large': 5.75,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name 

class Espresso(models.Model):
    FLAVOR_CHOICES = [
        ('Original', 'Original'),
    ]

    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='espresso_images/')

    @property
    def price(self):
        size_price_map = {
            'small': 2.00,
            'medium': 3.00,
            'large': 4.00,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name 
    
class OriginalGlaze(models.Model):
    FLAVOR_CHOICES = [
        ('Original', 'Original'),
        ('Vegan' , 'Vegan'),
        ('Gluten Free' , 'Gluten Free')
    ]

    SIZE_CHOICES = [
        ('Regular', 'Regular'),
        ('Donut Hole', 'Donut Hole'),
    ]
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='original_images/')
    
    @property
    def price(self):
        size_price_map = {
            'Regular': 2.50,
            'Donut Hole': 0.50,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name

class Strawberry(models.Model):
    FLAVOR_CHOICES = [
        ('Strawberry', 'Strawberry'),
        ('Vegan' , 'Vegan'),
        ('Gluten Free' , 'Gluten Free'),
    ]

    SIZE_CHOICES = [
        ('Regular', 'Regular'),
        ('Donut Hole', 'Donut Hole'),
    ]
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='Strawberry_images/')
    
    @property
    def price(self):
        size_price_map = {
            'Regular': 2.50,
            'Donut Hole': 0.50,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name
    
class Vanilla(models.Model):
    FLAVOR_CHOICES = [
        ('Vanilla', 'Vanilla'),
        ('Vegan' , 'Vegan'),
        ('Gluten Free' , 'Gluten Free'),
    ]

    SIZE_CHOICES = [
        ('Regular', 'Regular'),
        ('Donut Hole', 'Donut Hole'),
    ]
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='Vanilla_images/')
    
    @property
    def price(self):
        size_price_map = {
            'Regular': 2.50,
            'Donut Hole': 0.50,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name
from django.db import models

class Chocolate(models.Model):
    FLAVOR_CHOICES = [
        ('Chocolate', 'Chocolate'),
        ('Vegan' , 'Vegan'),
        ('Gluten Free' , 'Gluten Free'),
    ]

    SIZE_CHOICES = [
        ('Regular', 'Regular'),
        ('Donut Hole', 'Donut Hole'),
    ]
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='Chocolate_images/')
    
    @property
    def price(self):
        size_price_map = {
            'Regular': 2.50,
            'Donut Hole': 0.50,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name

from django.db import models

class BostonCream(models.Model):
    FLAVOR_CHOICES = [
        ('Boston Cream', 'Boston Cream'),
        ('Vegan' , 'Vegan'),
        ('Gluten Free' , 'Gluten Free'),
    ]

    SIZE_CHOICES = [
        ('Regular', 'Regular'),
        ('Donut Hole', 'Donut Hole'),
    ]
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='BostonCream_images/')
    
    @property
    def price(self):
        size_price_map = {
            'Regular': 3.50,
            'Donut Hole': 1.00,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name

class JellyDonut(models.Model):
    FLAVOR_CHOICES = [
        ('Jelly', 'Jelly'),
        ('Vegan' , 'Vegan'),
        ('Gluten Free' , 'Gluten Free'),
    ]

    SIZE_CHOICES = [
        ('Regular', 'Regular'),
        ('Donut Hole', 'Donut Hole'),
    ]
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='JellyDonut_images/')
    
    @property
    def price(self):
        size_price_map = {
            'Regular': 3.50,
            'Donut Hole': 1.00,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name
    
class MapleBacon(models.Model):
    FLAVOR_CHOICES = [
        ('Maple Bacon', 'Maple Bacon'),
        ('Vegan' , 'Vegan'),
        ('Gluten Free' , 'Gluten Free'),
    ]

    SIZE_CHOICES = [
        ('Regular', 'Regular'),
        ('Donut Hole', 'Donut Hole'),
    ]
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='MapleBacon_images/')
    
    @property
    def price(self):
        size_price_map = {
            'Regular': 4.00,
            'Donut Hole': 2.25,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name
class Smore(models.Model):
    FLAVOR_CHOICES = [
        ('Smore', 'Smore'),
        ('Vegan' , 'Vegan'),
        ('Gluten Free' , 'Gluten Free'),
    ]

    SIZE_CHOICES = [
        ('Regular', 'Regular'),
        ('Donut Hole', 'Donut Hole'),
    ]
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='Smore_images/')
    
    @property
    def price(self):
        size_price_map = {
            'Regular': 3.75,
            'Donut Hole': 1.25,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name
    
class Cruller(models.Model):
    FLAVOR_CHOICES = [
        ('Cruller', 'Cruller'),
        ('Vegan' , 'Vegan'),
        ('Gluten Free' , 'Gluten Free'),
    ]

    SIZE_CHOICES = [
        ('Regular', 'Regular'),
        ('Donut Hole', 'Donut Hole'),
    ]
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='Cruller_images/')
    
    @property
    def price(self):
        size_price_map = {
            'Regular': 3.00,
            'Donut Hole': 1.00,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name
    
class PBNJ(models.Model):
    FLAVOR_CHOICES = [
        ('PBNJ', 'PBNJ'),
        ('Vegan' , 'Vegan'),
        ('Gluten Free' , 'Gluten Free'),
    ]

    SIZE_CHOICES = [
        ('Regular', 'Regular'),
        ('Donut Hole', 'Donut Hole'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='PBNJ_images/')
    
    @property
    def price(self):
        size_price_map = {
            'Regular': 3.50,
            'Donut Hole': 1.25,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name


class BlueberryCake(models.Model):
    FLAVOR_CHOICES = [
        ('Blueberry Cake', 'Blueberry Cake'),
        ('Vegan' , 'Vegan'),
        ('Gluten Free' , 'Gluten Free'),
    ]

    SIZE_CHOICES = [
        ('Regular', 'Regular'),
        ('Donut Hole', 'Donut Hole'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    image = models.ImageField(upload_to='BlueberryCake_images/')
    
    @property
    def price(self):
        size_price_map = {
            'Regular': 4.00,
            'Donut Hole': 1.50,
        }
        return size_price_map.get(self.size, 0)

    def __str__(self):
        return self.name
