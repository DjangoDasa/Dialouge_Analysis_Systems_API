
# Create your views here.

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import render, render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components



def home_view(request):
    return render(request, 'base/input.html')


def index(request):
    x= [1,3,5,7,9,11,13]
    y= [1,2,3,4,5,6,7]
    title = 'y = f(x)'

    plot = figure(title= title ,
        x_axis_label= 'X-Axis',
        y_axis_label= 'Y-Axis',
        plot_width =400,
        plot_height =400)

    plot.line(x, y, legend= 'f(x)', line_width = 2)
    #Store components
    script, div = components(plot)

    #Feed them to the Django template.
    return render_to_response( 'base/bokeh.html',
            {'script' : script , 'div' : div} )

class AnalysisApiView(generics.RetrieveAPIView):
    permission_classes = ''

    def get_queryset(self):

        return User.objects.filter(id=self.kwargs['pk'])
