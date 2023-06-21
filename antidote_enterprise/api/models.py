from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid

class Provider(models.Model):
    name = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class ProviderUser(models.Model):
    api_key = models.CharField(max_length=50, unique=True)
    secret_key = models.CharField(max_length=50, unique=True)
    provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_amount = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_id} - {self.provider_id}"


class Configuration(models.Model):
    provider_user_id = models.ForeignKey(ProviderUser, on_delete=models.CASCADE, unique=True)
    leverage = models.IntegerField(default=10)
    interval = models.CharField(max_length=10, default="15m")
    margin_type = models.CharField(max_length=10, default="CROSSED")
    volume_usdt = models.IntegerField(null=True)
    amount_usdt = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    candle_change_ratio = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    profit_percentage = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    max_position_count = models.IntegerField(null=True)
    is_bollinger_active = models.BooleanField(default=False)
    check_position_mode = models.BooleanField(default=False)
    blacklist = models.JSONField()
    roes = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Configuration of {self.provider_user_id}"


class License(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    email = models.CharField(max_length=50, unique=True)
    license_key = models.CharField(max_length=50, unique=True, default=uuid.uuid4())
    expire_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"License of {self.user_id}"


