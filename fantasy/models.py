from django.db import models

class ItemType (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        

class Item(models.Model):
    name = models.CharField(max_length=255)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="static/images/")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
