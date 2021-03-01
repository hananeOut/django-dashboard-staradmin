from django.db import models
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.models import User

procedure_CHOICES = [('nouvelle procédure', 'Nouvelle procédure'),
                     ('relance procédure', 'Relance procédure')]

operation_CHOICES = [('consultation', 'Consultation'),
                     ('gré à gré', 'Gré à Gré')]

evaluation_CHOICES = [('système de notation', 'Système de notation'),
                      ('le moins Disant', 'Le moins Disant')]

class Consultation(models.Model):
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    Nouvelle_Relance = models.CharField(choices = procedure_CHOICES, max_length=30)
    N_Dossier = models.CharField(max_length=10)
    A_N_Dossier = models.CharField(max_length=10, blank="false")
    Designation = models.TextField(max_length=60)
    Type_Operation = models.CharField(choices=operation_CHOICES, max_length=60)
    Nom_Agent_Tech = models.TextField(max_length=60)
    date_Fich_Tech = models.DateTimeField()
    Fich_Tech_valid = models.FileField(upload_to="Fiche/")
    date_Lance = models.DateTimeField()
    date_Ouvert = models.DateTimeField()
    PV_Eval = models.FileField(upload_to="Evaluation/")
    PV_Ouvert = models.FileField(upload_to="Ouverture/")
    System_Eval = models.CharField(choices=evaluation_CHOICES, max_length=30)

class Soumission(models.Model):
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    Iden_Ope = models.TextField(max_length=200, blank="false")
    Raison_Soci = models.TextField(max_length=200, blank="false")
    Statut_Juri = models.TextField(max_length=200, blank="false")
    N_Tele = models.CharField(max_length=12, blank="false")
    N_Fax = models.CharField(max_length=12, blank="false")
    Email = models.EmailField(max_length = 254, blank="false")
    Con_id = models.ForeignKey(Consultation, on_delete=models.SET_NULL, null=True, blank=True)









