from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
# CREATE TABLE users (
#     id SERIAL,
#     username TEXT NOT NULL UNIQUE,
#     password TEXT NOT NULL,
#     first_name TEXT NOT NULL,
#     last_name TEXT NOT NULL,
#     account_id INT NOT NULL UNIQUE,
#     PRIMARY KEY(id)
# );
class Users(models.Model):
    username   = models.CharField(max_length=70, blank=False, default='')
    first_name = models.CharField(max_length=70, blank=False, default='')
    last_name  = models.CharField(max_length=70, blank=False, default='')

# CREATE TABLE accounts (
#     id SERIAL,
#     user_id INT NOT NULL UNIQUE,
#     PRIMARY KEY(id)
# );
class Accounts(models.Model):
    name        = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=70, blank=False, default='')
    user        = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True, default=NULL)

# CREATE TABLE assets (
#     id SERIAL,
#     name TEXT NOT NULL UNIQUE,
#     type TEXT NOT NULL,
#     rating NUMERIC,
#     current_price NUMERIC NOT NULL,
#     PRIMARY KEY (id)
# );    
class Assets(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    type = models.CharField(max_length=70, blank=False, default='')
    current_pirce = models.FloatField()

# CREATE TABLE portfolios (
#     id SERIAL,
#     name TEXT NOT NULL,
#     account_id INT NOT NULL UNIQUE,
#     description TEXT NOT NULL,
#     ytd_profit NUMERIC,
#     total_value numeric,
#     PRIMARY KEY (id)
# );
class Portfolios(models.Model):
    account      = models.OneToOneField(Accounts, on_delete=models.CASCADE)
    description  = models.CharField(max_length=70, blank=False, default='')
    # account      = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    asset        = models.ManyToManyField(Assets)

# CREATE TABLE portfolio_assets (
#     portfolio_id INT NOT NULL,
#     asset_id INT NOT NULL,
#     average_purchase_price NUMERIC NOT NULL,
#     quantity INT NOT NULL,
#     PRIMARY KEY(portfolio_id, asset_id)
# );
class PortfolioAssets(models.Model):
    avg_purchase_price = models.FloatField(default=0)
    quantity           = models.IntegerField(blank=False, default=0)
    portfolio          = models.ForeignKey(Portfolios, on_delete=models.CASCADE)
    asset              = models.ForeignKey(Assets, on_delete=models.CASCADE)
    

