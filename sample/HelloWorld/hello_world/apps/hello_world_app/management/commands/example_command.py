import os
import select
import sys
import traceback

from tusk.core.management import BaseCommand, CommandError
from tusk.utils.datastructures import OrderedSet


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass

    help = "Sample Command that do nothing"

    def add_arguments(self, parser):
        ...
