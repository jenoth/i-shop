from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.strip().casefold()
        self.last_name = self.last_name.strip().casefold()
        self.email = self.email.strip().casefold()
        self.address = self.address.strip().casefold()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
