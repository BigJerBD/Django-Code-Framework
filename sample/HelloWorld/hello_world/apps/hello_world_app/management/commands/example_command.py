import os
import select
import sys
import traceback

from django_code_framework.core.management import BaseCommand, CommandError
from django_code_framework.utils.datastructures import OrderedSet


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass

    help = "Sample Command that do nothing"

    def add_arguments(self, parser):
        ...
