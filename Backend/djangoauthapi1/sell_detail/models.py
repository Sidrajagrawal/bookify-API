from django.db import models
from django.utils.timezone import now
from account.models import User
import uuid

class ActiveSellDetailManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class SellDetail(models.Model):
    class ConditionChoices(models.TextChoices):
       BAD = 'bad', 'Bad'
       AVERAGE = 'average', 'Average'
       GOOD = 'good', 'Good'

    book_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sell_details')
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=50)
    book_quantity = models.PositiveIntegerField()
    book_expected_price = models.PositiveIntegerField()
    book_AI_price = models.PositiveIntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0)
    sale_count = models.PositiveIntegerField(default=0)
    book_edition = models.CharField(max_length=50, null=True, blank=True)
    book_isbn = models.CharField(max_length=13, unique=True, null=True)
    condition = models.CharField(
        max_length=10, choices=ConditionChoices.choices, default=ConditionChoices.GOOD
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = ActiveSellDetailManager() 
    all_objects = models.Manager()  

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = now()
        self.save()

    def __str__(self):
        return f"{self.book_title} by {self.book_author}"

class BookPhoto(models.Model):
    sell_detail = models.ForeignKey(SellDetail, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.sell_detail.book_title}"