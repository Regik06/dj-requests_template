from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    station_list = []
    with open('data-398-2018-08-30.csv') as f:
        file_obj = csv.DictReader(f)
        for row in file_obj:
            station_dict = {
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            }
            station_list.append(station_dict)

        paginator = Paginator(station_list, 10)
        page_number = int(request.GET.get("page", 1))
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': station_list,
            'page': page,
        }
    return render(request, 'stations/index.html', context)
