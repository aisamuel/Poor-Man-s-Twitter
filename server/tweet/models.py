from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """
    This is a base model class that contains some default fields for models on Poor man's Tweeter app
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
        
class Tweet(BaseModel):
    """_summary_
    This is the model that contains list of created tweets
    """
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['created']
    