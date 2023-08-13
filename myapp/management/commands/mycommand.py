from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
from myapp.models import MpanCores
from myapp.models import Files
from tools.read_files import read_file
import os


class Command(BaseCommand):
    help = 'My custom command'

    def add_arguments(self, parser):
        parser.add_argument('args', nargs='+', type=str, help='Arguments')

    def handle(self, *args, **options):
        # Get the file path
        for path in args:
            files_name = os.path.basename(path)
            # Firstly check if the file was read
            if not Files.objects.filter(files_name=files_name).exists():
                datas = read_file(path)
                for data in datas:
                    mpanCores = MpanCores(
                        an_mpan=data["an_mpan"],
                        meter_serial_number=data["meter_serial_number"],
                        state=data["state"],
                        reading_type=data["reading_type"],
                        meter_register_id=data["meter_register_id"],
                        reading_date_time=timezone.make_aware(datetime.strptime(data["reading_date_time"], "%Y%m%d%H%M%S")),
                        register_reading=data["register_reading"],
                        meter_reading_flag=data["meter_reading_flag"],
                        reading_method=data["reading_method"],
                        files_name=files_name,
                    )
                    mpanCores.save()
                # Save into read db
                file = Files(files_name=files_name)
                file.save()
            else:
                print("The file has already been loaded and does not need to be reloaded.")
