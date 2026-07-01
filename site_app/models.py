from django.db import models

class Inscription(models.Model):  # Nom du modèle
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'inscription'  # Nom réel de la table en base de données

    def __str__(self):
        return self.email
