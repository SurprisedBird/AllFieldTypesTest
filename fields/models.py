from django.db import models
from datetime import timedelta
from PIL import Image
import uuid

# Create your models here.
class AllFieldsTypes(models.Model):
	big_int = models.BigIntegerField()
	binary = models.BinaryField()
	boolean = models.BooleanField()
	char = models.CharField(max_length=50)
	date = models.DateField(auto_now=False, auto_now_add=False)
	date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	decimal = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	duration = models.DurationField(default=timedelta(days=1))
	email = models.EmailField(blank=True, unique=True)
	file = models.FileField(default=None, max_length=100, null=True)
	path_field=models.FilePathField(path=None, match=None, recursive=False, max_length=100, null=True)
	float_field = models.FloatField(default=3.0)
	intg = models.IntegerField()
	IP = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, default='127.0.0.1')
	null_bul = models.NullBooleanField()
	pos_int = models.PositiveIntegerField(default=0)
	pos_smal_int = models.SmallIntegerField(default=0)
	slug = models.SlugField(max_length=50, null=True)
	text = models.TextField(default=0)
	time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
	URL = models.URLField(max_length=30, null=True)
	uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 

#	require Pillow installed
	image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=40, null=True)
