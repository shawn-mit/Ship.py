from django.shortcuts import render
from django.shortcuts import render_to_response
from models import trade_year
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

def index(request):
    all_port_data = trade_year.objects.filter(usport = 'Total All Ports')
    #miami_data  = trade_year.objects.filter(usport = 'Miami, FL')
    #newyork_data  = trade_year.objects.filter(usport = 'New York City, NY')
    #los_angeles_data  = trade_year.objects.filter(usport = 'Los Angeles, CA')
    #seattle_data  = trade_year.objects.filter(usport = 'Seattle, WA')
    #edetroit_data  = trade_year.objects.filter(usport = 'Detroit, MI')


    xdata = ["2003", "2004", "2005", "2007", "2008", "2009", "2010","2011","2012","2013"]
    ydata = []
    for  row in all_port_data:

        ydata.append(int(row.total_value))
    #ydata2 = []
    #for  row in newyork_data:

        #ydata2.append(int(row.total_value))

    chartdata = {'x': xdata, 'name1': 'all_port', 'y': ydata}
    charttype = 'discreteBarChart'
    chartcontainer = 'discreteBarChart_container'
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
    
    
    #return render(request, 'piechart.html', {'data':data})
    return render_to_response('discretebarchart.html', data)


"""
def index2(request):

    all_port_data = trade_year.objects.filter(usport = 'Total All Ports')
    #miami_data  = trade_year.objects.filter(usport = 'Miami, FL')
    #newyork_data  = trade_year.objects.filter(usport = 'New York City, NY')
    #los_angeles_data  = trade_year.objects.filter(usport = 'Los Angeles, CA')
    #seattle_data  = trade_year.objects.filter(usport = 'Seattle, WA')
    #detroit_data  = trade_year.objects.filter(usport = 'Detroit, MI')


    xdata = ["2003", "2004", "2005", "2007", "2008", "2009", "2010","2011","2012","2013"]
    ydata = []
    for row in all_port_data:

        ydata.append(int(row.total_value))

    """
    #iterate over the second set of data for us ports.
    """

    #ydata2 = []
    #for  row in newyork_data:

        #ydata2.append(int(row.total_value))

    chartdata = {'x': xdata, 'name1': 'all_port', 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'pieChart_container'
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


    #return render(request, 'piechart.html', {'data':data})
    return render_to_response('piechart.html', data)
    #def helper_data_view(request) 
"""