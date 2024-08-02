from django.db import models

class JobPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    mission = models.TextField()
    context = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    experience = models.TextField()
    qualities = models.TextField()
    additional_assets = models.TextField()
    contact_email = models.EmailField()
    reference_code = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    publication_date = models.DateField()
    sector = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=255)

    def __str__(self):
        return self.title
