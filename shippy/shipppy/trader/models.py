from django.db import models
# Create your models here.


 # may need to find the best django specific models to represent volumes/dollars

class trade_year (models.Model):

    year = models.IntegerField()
    total_ton = models.IntegerField(null= True, blank=True)
    total_value = models.IntegerField( null= True, blank=True)
    usport = models.CharField(max_length=155)

   
    def __str__(self):        
        return str(self.year) + ' ' + str(self.total_value) + ' ' + str(self.usport)

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
