from django.db import models
# Create your models here.
import datetime

class us_port(models.Model):

    """
    The us_port table refernces the city and states of maritime ports in relation to the 
    metric tons and value totals
    """

    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    year = models.ForeignKey('trade_year')
        
    def __str__(self):         
        return (self.city, self.state)

    class Meta:
        ordering = ['state']

 # may need to find the best django specific models to represent volumes/dollars

class trade_year (models.Model):

    year = models.DateField()
    total_ton = models.IntegerField()
    total_value = models.DecimalField(max_digits=6, decimal_places=2)
   
    def __str__(self):        
        return (self.year, self.total_ton)

    class Meta: 
        ordering = ['year']

    """

    #solution found to allow a list of years rolling backwards starting at 2013
    

    def yearlist:
    YEAR_CHOICES = []
    for r in range (2013, (datetime.datetime.now().year+1)):
            YEAR_CHOICES.append((r,r))

    year = models.IntegerField(_('year'), max_length=4, choices= YEAR_CHOICES, default=).year)

    """


    """
class capital_import (models.Model):

    # will i pass in the values such as  metric tons and dollar amount as parameters inside integerfields? ()
    import_ton = models.IntegerField()
    import_value = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):        
        return self.name

class capital_export (models.Model): 
    
    export_value = models.DecimalField(max_digits=6, decimal_places=2) 
    export_ton = models.IntegerField()

    def __str__(self):        
        return self.name


"""
# map of global borders from GeoDJango tut.

"""
class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    #mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):              
        return self.name

"""
