from django.db import models

# Create your models here.
class SearchDetails(models.Model):
    Search_Item=models.CharField(max_length=100,help_text="Enter your Required News")
    def __str__(self):
        return self.Search_Item

class FeedBackDetailsModel(models.Model):
    Person_Name=models.CharField(max_length=100,help_text='Enter person Name')
    Suggested_Name=models.CharField(max_length=100,help_text='Enter your Suggested news')
    Feedback_Text=models.TextField(max_length=900,help_text='please give your suggestions to improve')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Person_Name