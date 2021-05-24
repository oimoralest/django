from django.db import models


class Pet(models.Model):
    '''Defines a Pet Schema'''
    SEX_CHOICE = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, blank=True)
    submission_date = models.DateField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

    class Meta:
        '''Defines Metadata for Pet'''
        db_table = 'pets'


class Vaccine(models.Model):
    '''Defines a Vaccine Schema'''
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
