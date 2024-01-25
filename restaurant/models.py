from django.db import models


class Booking(models.Model):
    """Model definition for Booking."""

    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Booking."""

        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        """Unicode representation of Booking."""
        return self.name


class Menu(models.Model):
    """Model definition for Menu."""

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    class Meta:
        """Meta definition for Menu."""

        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        ordering = ["id"]

    def __str__(self):
        return f"{self.title} : {str(self.price)}"
