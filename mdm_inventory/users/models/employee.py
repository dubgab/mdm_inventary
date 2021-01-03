"""Employee Model"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from mdm_inventory.utils.models import BasicModel


class Employee(BasicModel , models.Model):
    """
        Model of Employee in to app
    """
    #dates
    date_of_birth = models.DateField(_("Fecha De Nacimiento"), auto_now=False, auto_now_add=False)
    entry_date = models.DateField(_("Fecha de entrada"), auto_now=False, auto_now_add=False)

    user = models.ForeignKey("users.User", verbose_name=_("user_employee"), on_delete=models.CASCADE)
    salary = models.FloatField(_("Sueldo"))

    #permissions
    is_manager = models.BooleanField(_("Gerente") , default=False)
    is_cashier = models.BooleanField(_("Cajero") , default=False)
    is_supervisor = models.BooleanField(_("Supervisor") , default=False)
    
    def __str__(self):
        """Return username and email"""
        return f'{self.user.email} - {self.salary}'
