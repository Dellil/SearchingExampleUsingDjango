import csv
from django.core.management.base import BaseCommand
from product.models import Product


class Command(BaseCommand):
    help = "This command creates product from csv file"

    def handle(self, *args, **options):
        with open("product_all_df.csv", encoding='UTF8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                product = Product(title=row[1], low_price=row[2], n_review=row[3], category=row[4])
                product.save()
        self.stdout.write(self.style.SUCCESS("Products Created"))