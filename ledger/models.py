from django.db import models
from datetime import date

# Model for Rubber Types
class RubberType(models.Model):
    name = models.CharField(max_length=100)
    bag_weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight per bag in kg")
    price_per_kg = models.DecimalField(max_digits=7, decimal_places=2, help_text="Selling price per kg")
    stock_bags = models.PositiveIntegerField(default=0, help_text="Number of bags in stock")

    def __str__(self):
        return f"{self.name} ({self.stock_bags} bags, {self.bag_weight} kg/bag)"

# Model for Purchases
class Purchase(models.Model):
    rubber_type = models.ForeignKey(RubberType, on_delete=models.CASCADE)
    order_date = models.DateField(default=date.today)
    arrival_date = models.DateField(null=True, blank=True, help_text="Date goods arrive at warehouse")
    bags_received = models.PositiveIntegerField(default=0, help_text="Number of bags received")
    customs_cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Customs and import charges")
    transport_cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Logistics cost")
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total cost of shipment", null=True, blank=True)
    cost_per_kg = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, help_text="Calculated cost per kg")

    def calculate_cost_per_kg(self):
        total_weight = self.bags_received * self.rubber_type.bag_weight
        self.total_cost = self.customs_cost + self.transport_cost
        self.cost_per_kg = self.total_cost / total_weight if total_weight > 0 else 0

    def save(self, *args, **kwargs):
        self.calculate_cost_per_kg()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.rubber_type.name} Purchase ({self.bags_received} bags)"

# Model for Sales
class Sale(models.Model):
    rubber_type = models.ForeignKey(RubberType, on_delete=models.CASCADE)
    sale_date = models.DateField(default=date.today)
    bags_sold = models.PositiveIntegerField(default=0)
    selling_price_per_kg = models.DecimalField(max_digits=7, decimal_places=2, help_text="Selling price per kg")
    revenue = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def calculate_revenue(self):
        total_weight = self.bags_sold * self.rubber_type.bag_weight
        self.revenue = total_weight * self.selling_price_per_kg

    def save(self, *args, **kwargs):
        self.calculate_revenue()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.bags_sold} bags of {self.rubber_type.name} sold"
