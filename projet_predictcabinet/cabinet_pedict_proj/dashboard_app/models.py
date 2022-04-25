from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

GENDER = (
			(0, 'F'),
			(1, 'M'),
		)

class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], null=True)
    sexe = models.PositiveBigIntegerField(choices=GENDER, null=True)
    cas = models.PositiveBigIntegerField(null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/ml_cabinet_model.joblib')
        self.predictions = ml_model.predict([[self.sexe, self.cas]])
        return super().save(*args, **kwargs)
        
        class Meta:
            ordering = ['-date']
        
        def __str__(self):
            return self.name
				
		