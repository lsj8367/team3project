from django.db import models

# Create your models here.
class Tuser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=10, blank=True, null=True)
    user_pwd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tuser'

class Travel(models.Model):
    tourid = models.IntegerField(db_column='tourId', primary_key=True)  # Field name made lowercase.
    city = models.CharField(max_length=10, blank=True, null=True)
    town = models.CharField(max_length=20, blank=True, null=True)
    tourname = models.CharField(db_column='tourName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    genre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel'

class Treview(models.Model):
    treview_no = models.IntegerField(primary_key=True)
    treview = models.ForeignKey('Tuser', models.DO_NOTHING, blank=True, null=True)
    tourid = models.ForeignKey(Travel, models.DO_NOTHING, db_column='tourId', blank=True, null=True)  # Field name made lowercase.
    rating = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treview'