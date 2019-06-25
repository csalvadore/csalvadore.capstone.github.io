# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:55:56 2019

@author: tuc08826
"""

from math import pi

import pandas as pd

from bokeh.io import output_file, show, reset_output
from bokeh.palettes import Colorblind6
from bokeh.plotting import figure
from bokeh.transform import cumsum
reset_output()
output_file("ritisTOTAL.html")


x = {
     'Incidents': 32889,
     'Weather': 415,
     'Work Zones': 10545,
     'Special Events': 3445,
     'Bottlenecks': 8977,
     'Other': 504
}

data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Colorblind6

p = figure(plot_height=225, plot_width=275, toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data)

p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

p.legend.label_text_font_size = '6pt'

show(p)