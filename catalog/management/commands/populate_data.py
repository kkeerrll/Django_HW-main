from sqlite3 import ProgrammingError, IntegrityError

from django.core.management import BaseCommand, call_command
from ...models import Category, Product
import json

class Command(BaseCommand):
    requires_migrations_checks = True

    def handle(self, *args, **options) -> None:
        try:
            call_command('loaddata', 'fixtures.json')
        except ProgrammingError:
            pass
        except IntegrityError as e:
            self.stdout.write(self.style.NOTICE(f'Invalid fixtures: {e}'))
        else:
            self.stdout.write(self.style.SUCCESS(
                'Command have been completed successfully'
            ))
