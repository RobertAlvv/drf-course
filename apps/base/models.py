from django.db import models
from simple_history.models import HistoricalRecords

class BaseModel(models.Model):
    
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de actualizacion', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)
    historical = HistoricalRecords(user_model = "users.User", inherit=True)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
        
        
    @property
    def _history_user(self):
        return self.change_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value