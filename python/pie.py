# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import pi

import pandas as pd

from bokeh.io import output_file, show, reset_output
from bokeh.palettes import Colorblind6
from bokeh.plotting import figure
from bokeh.transform import cumsum
reset_output()
output_file("ritis.html")


x = {
     'Incidents': 0,
     'Weather': 0,
     'Work Zones': 10,
     'Special Events': 0,
     'Bottlenecks': 1,
     'Other': 1
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