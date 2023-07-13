from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        categories_data = [
            {'name': 'Овощи'},
            {'name': 'Фрукты'},
            {'name': 'Мясо'},
            {'name': 'Молочная продукция'},
            {'name': 'Ликеро-водочная продукция'},
        ]

        category_for_create = []
        for data in categories_data:
            category_for_create.append(Category(**data))

        Category.objects.bulk_create(category_for_create)
