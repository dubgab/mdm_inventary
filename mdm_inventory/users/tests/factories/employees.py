from faker import Faker
import factory
import factory.fuzzy

# Models
from mdm_inventory.users.models import Employee

#factories
from .users import UserFactory

class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee
        #django_get_or_create = ('email', 'username',)

    user = factory.SubFactory(UserFactory)
    salary = factory.Sequence(lambda n: "1456%d" % n)
    date_of_birth  = factory.Faker('date')
    entry_date  = factory.Faker('date')
    is_manager  = False
    is_cashier  = True
    is_supervisor = False

    def __str__(self):
        return f'{self.user.email} - {self.salary}'