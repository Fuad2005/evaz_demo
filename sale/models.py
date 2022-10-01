from django.db import models

# Create your models here.
class City(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class PropertyType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class PurchaseType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Property(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    info = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=100)
    kmetr = models.IntegerField()
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, null=True, blank=True)
    purchase_type = models.ForeignKey(PurchaseType, on_delete=models.CASCADE, null=True, blank=True)
    new = models.BooleanField(default=False)
    repaired = models.BooleanField(default=False)
    longitude = models.CharField(max_length=100)
    lattitude = models.CharField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class PropertyFeature(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to = 'property-image/')
    main = models.BooleanField(default=False) 

    def save(self):
        if self.main:
            self.property.images.all().update(main=False)
        super().save()


    def delete(self):
        other = self.property.images.exclude(pk=self.pk).first()
        if other:
            other.main = True
            other.save()
        super().delete()