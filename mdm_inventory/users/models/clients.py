""" Client Model """

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from mdm_inventory.utils.models import BasicModel
from mdm_inventory.address.models import Address

class Client(BasicModel,models.Model):
    first_name = models.CharField(_("Primer nombre"), max_length=50)
    last_name = models.CharField(_("Apellido"), max_length=50)
    dni = models.CharField(_("DNI"), max_length=50 , unique=True)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    full_name = models.CharField(_("Nombre completo"), max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE , null=True , blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.dni}'
    