from django.db import models


class MpanCores(models.Model):
    # J0003
    # MPAN Core
    # eg, 1200023305967 of 026|1200023305967|V|
    an_mpan = models.CharField(max_length=30, db_index=True)  # index
    # J0004
    # Meter Id (Serial Number)
    # eg, S76A 13884 of 028|S76A 13884|C|
    meter_serial_number = models.CharField(max_length=30, db_index=True)  # index
    # J0022
    # BSC Validation Status状态
    # eg, V of 026|1200023305967|V|
    state = models.CharField(max_length=20)
    # J0171
    # Reading Type
    # eg, C of 028|S76A 13884|C|
    reading_type = models.CharField(max_length=20)
    # J0010
    # Meter Register Id
    # eg, S of 030|S|20160226000000|17393.011|||T|N|
    meter_register_id = models.CharField(max_length=30)
    # J0016
    # Reading Date & Time
    # eg, 20160226000000 of 030|S|20160226000000|17393.011|||T|N|
    reading_date_time = models.DateTimeField()
    # J0040
    # Register Reading
    # eg, 17393.011 of 030|S|20160226000000|17393.011|||T|N|
    register_reading = models.CharField(max_length=20)
    # J0045
    # Meter Reading Flag
    # eg, T of 030|S|20160226000000|17393.011|||T|N|
    meter_reading_flag = models.CharField(max_length=20)
    # J1888
    # Reading Method
    # eg, N of 030|S|20160226000000|17393.011|||T|N|
    reading_method = models.CharField(max_length=20)
    # Files Name
    files_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'my_mpan_cores'  # table name


class Files(models.Model):
    files_name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'files'  # table name
