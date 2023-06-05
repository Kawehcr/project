from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    company_id = models.IntegerField(null=False, blank=False, verbose_name="Id da Empresa", db_column="company_id")
    name_project = models.CharField(max_length=100, verbose_name="Nome do projeto", null=False, blank=False, db_column="name_project")
    enabled = models.CharField(max_length=3, null=False, blank=False, verbose_name="Ativo", db_column="enabled")

    class Meta:
        db_table = "project"