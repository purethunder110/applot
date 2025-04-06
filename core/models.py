from django.db import models

# Create your models here.


class ConfigurationSettings(models.Model):
    key = models.TextField()
    value = models.JSONField()
    previous_value = models.JSONField()

    def save(self, *args, **kwargs):
        self.previous_value = self.value
        super(ConfigurationSettings, self).save(*args, **kwargs)


class ActionPerformed(models.Model):
    action_performed = models.TextField()
    date_performed = models.DateField(null=False, auto_created=True)
