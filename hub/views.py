from django.shortcuts import render
import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import gspread
import g.settings as settings
from oauth2client.service_account import ServiceAccountCredentials


@csrf_exempt
def home(request):

    dat = {}
    if request.method == "POST":
        ou = request.POST.get("outlet")
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.BASE_DIR + '/hub/outlet-ed311da57e3e.json', scope)
        gc = gspread.authorize(credentials)
        sht = gc.open_by_url('https://docs.google.com/spreadsheets/d/1aXW4Owz52XTTNMQXK_fEugL77qZNGtR0mkNU0fCtWPs')
        worksheet = sht.get_worksheet(0)
        cell_list = worksheet.range('A1:A5')
        cell_list[0] = ou.city
        cell_list[1] = ou.cluster
        cell_list[2] = ou.name
        cell_list[3] = ou.lat
        cell_list[4] = ou.lon
        worksheet.update_cells(cell_list)

    return render(request, 'hub/home.html', dat)