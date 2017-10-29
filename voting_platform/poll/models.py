from django.db import models


class Category(models.Model):
    type = models.CharField(max_length=100)
    entry_count = models.IntegerField()

    def __str__(self):
        return self.type


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    vote_count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['vote_count']

#  cat = Category()
#  Candidate.objects.filter(category=cat)
#  cat.candidate_set.all()
