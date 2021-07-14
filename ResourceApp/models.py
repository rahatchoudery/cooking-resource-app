"""from django.db import models


class Resources(models.Model):
    Knife_Skills = 'Knife_Skills'
    Culinary_Terms = 'Culinary_Terms'
    Recipes = 'Recipes'

    Beginner = 'Beginner'
    Intermediate = 'Intermediate'
    Advanced = 'Advanced'

    Article = 'Article'
    Book = 'Book'
    Video = 'Video'

    Subject_Choices = [
        (Knife_Skills, 'Knife Skills'),
        (Culinary_Terms, 'Culinary Terms'),
        (Recipes, 'Recipes')
    ]

    Level_Choices = [
        (Beginner, 'Beginner'),
        (Intermediate, 'Intermediate'),
        (Advanced, 'Advanced')
    ]

    Medium_Choices = [
        (Article, 'Article'),
        (Book, 'Book'),
        (Video, 'Video')
    ]

    subject = models.CharField(max_length=1, choice=Subject_Choices, default=Knife_Skills)
    level = models.CharField(max_length=1, choice=Level_Choices)
    medium = models.CharField(max_length=1, choice=Medium_Choices)
    link = models.URLField(max_length=200)
"""