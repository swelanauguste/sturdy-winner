from django.db import models

class Invoice(models.Model):
    part_type = models.CharField(max_length=100)
    vehicle = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100)
    price_ea = models.PositiveIntegerField(default=0)
    core_ea = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    shipping = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.vehicle +'-'+ self.part_number +'-'+ str(self.price_ea) +'EA'

    
    

    

    
