from django.shortcuts import render
from .models import MpanCores


def home(request):
    return render(request, 'home.html', {'results': ""})


def search(request):
    an_mpan = request.GET.get('an_mpan', '')
    meter_serial_number = request.GET.get('meter_serial_number', '')

    if an_mpan == "":
        results = MpanCores.objects.filter(
            meter_serial_number=meter_serial_number)
    elif meter_serial_number == "":
        results = MpanCores.objects.filter(an_mpan=an_mpan)
    elif an_mpan == "" and meter_serial_number == "":
        results = []
    else:
        results = MpanCores.objects.filter(
            an_mpan=an_mpan, meter_serial_number=meter_serial_number)

    if not results.exists():
        results = False

    # print("results: ", {'results': results})

    return render(request, 'home.html', {'results': results})
