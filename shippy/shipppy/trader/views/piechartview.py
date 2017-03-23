from django.shortcuts import render
from django.http import HttpResponse
from trader.models import *




xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
chartdata = {'x': xdata, 'y': ydata}
charttype = "pieChart"
chartcontainer = 'piechart_container'
data = {
    'charttype': charttype,
    'chartdata': chartdata,
    'chartcontainer': chartcontainer,
    'extra': {
        'x_is_date': False,
        'x_axis_format': '',
        'tag_script_js': True,
        'jquery_on_ready': False,
    }
}
return render_to_response('piechart.html', data) 

