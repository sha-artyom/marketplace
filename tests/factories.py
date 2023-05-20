import factory

from market.core.models import User


class UserFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = User

	username = factory.Faker('name')
	first_name = 'First name'
	last_name = 'Last name'
	email = 'email@mail.ru'
	password = 'Password8956'
