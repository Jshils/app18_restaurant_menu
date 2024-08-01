from django.db import models
from django.contrib.auth.models import User

# Create a tuple of tuples of stings
MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("deserts", "Deserts")
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available')
)

# Note this class inherits from the Model class in the models library
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    # Create a relationship between the Item table and the User table
    # The on_delete parameter makes is so if a user is deleted then all the meals that the user created are deleted
    # CASCADE = delete user and all items associated with that user
    # PROTECT - makes it so you cannot delete users
    # SET_NULL - sets the User (data item) to null but all the data associated with that user will still be there -
        # i.e. the author name will not be assocaited with those particular records.
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal