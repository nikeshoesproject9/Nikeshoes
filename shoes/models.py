from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shoes(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='movie/images/')
	quantity = models.IntegerField()
	price = models.FloatField()
	

	def __str__(self):
		return self.name


class ShoesSize(models.Model):
	shoes = models.ForeignKey(Shoes,on_delete=models.CASCADE)
	size = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.shoes}: {self.size}'

class ShoesColor(models.Model):
	shoes = models.ForeignKey(Shoes,on_delete=models.CASCADE)
	color = models.CharField(max_length=100) 

	def __str__(self):
		return f'{self.shoes.name}: {self.color}'


class ShoeCart(models.Model):    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    shoe_selected = models.ForeignKey(Shoes,on_delete=models.CASCADE)
    color_selected_id = models.ForeignKey(ShoesColor,on_delete=models.CASCADE)
    size_selected_id = models.ForeignKey(ShoesSize,on_delete=models.CASCADE)
    purchased_quantity = models.IntegerField()
    total_amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'{self.user.username} | {self.shoe_selected.name}'


# Create your models here.
