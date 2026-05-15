from django.db import models
from django.contrib.auth.models import User


# Extends the base User to include profile information (FR1, FR2)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.name


# Stores detailed information about sellers (UC-03)
class Seller(models.Model):
    SELLER_TYPES = [
        ('Individual', 'Individual'),
        ('Gallery', 'Gallery'),
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=SELLER_TYPES)
    bio = models.TextField()
    logo = models.ImageField(upload_to='sellers/logos/')
    cover_image = models.ImageField(upload_to='sellers/covers/')
    # Address logic: Only required/displayed for Galleries
    street_name = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


# The main artwork object for the marketplace (UC-02)
class Artwork(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Bidding', 'Bidding'),
        ('Sold', 'Sold'),
        ('Expired', 'Expired'),
    ]
    title = models.CharField(max_length=255)
    medium = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    starting_bid_price = models.DecimalField(max_digits=12, decimal_places=2)
    listing_date = models.DateTimeField(auto_now_add=True)
    dimensions = models.CharField(max_length=50)
    year_of_creation = models.IntegerField()
    edition = models.CharField(max_length=100)
    provenance = models.TextField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='artworks')
    thumbnail = models.ImageField(upload_to='artworks/thumbs/')
    sold_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return self.title


# Bidding logic (UC-04)
class Bid(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Contingent', 'Contingent'),
    ]
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_price = models.DecimalField(max_digits=12, decimal_places=2)
    bid_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.artwork.title}"


# Purchase finalization data (UC-05)
class Finalization(models.Model):
    bid = models.OneToOneField(Bid, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    national_id = models.CharField(max_length=50)


