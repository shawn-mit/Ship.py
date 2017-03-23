from django.shortcuts import render
from django.shortcuts import render_to_response

from models import trade_year
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

def index(request):
    miami_data = trade_year.objects.filter(usport = 'Miami, FL')
    newyork_data  = trade_year.objects.filter(usport = 'New York City, NY')
    los_angeles_data  = trade_year.objects.filter(usport = 'Los Angeles, CA')
    seattle_data  = trade_year.objects.filter(usport = 'Seattle, WA')
    detroit_data  = trade_year.objects.filter(usport = 'Detroit, MI')


    xdata = ["2003", "2004", "2005", "2007", "2008", "2009", "2010","2011","2012","2013"]
    ydata = []
    for  row in miami_data:

        ydata.append(int(row.total_value))
    ydata2 = []
    for  row in newyork_data:

        ydata2.append(int(row.total_value))

    chartdata = {'x': xdata, 'name1': 'miami', 'y': ydata, 'name2': 'newyork', 'y2':ydata2}
    charttype = "lineChart"
    chartcontainer = 'linechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            #'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    
    """
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
    """
    
    #return render(request, 'piechart.html', {'data':data})
    return render_to_response('piechart.html', data)
