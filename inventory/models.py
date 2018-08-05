from django.db import models


class Building(models.Model):
    building_name = models.CharField(max_length=50)
    building_number = models.IntegerField()

    def __str__(self):
        return self.building_name


class House(models.Model):
    house_number = models.CharField(max_length=50)
    house_building = models.ForeignKey('inventory.Building', on_delete=models.CASCADE)

    def __str__(self):
        return "House Number is: {}".format(self.house_number)


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.FloatField()
    item_house = models.ForeignKey('inventory.House',on_delete=models.CASCADE)

    def __str__(self):
        return "The price of {} is: {}".format(self.item_name, self.item_price)