import cairo
width, height = (500,400)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
dataSet1=[
        ['dataSet 1', [[0,1], [1,3], [2,2.5]]],
        ['dataSet 2', [[0,2], [1,4], [2,3]]],
        ['dataSet 3', [[0,5], [1,1], [2,0.5]]],
]
dataSet2=[
        ['dataSet 1', [[0,1], [1,3], [2,2.5]]],
        ['dataSet 2', [[0,2], [1,4], [2,3]]],
        ['dataSet 3', [[0,5], [1,1], [2,0.5]]],
]
dataSet=[
        ['dataSet 1', [[0,1], [1,3], [2,2.5]]],
        ['dataSet 2', [[0,2], [1,4], [2,3]]],
        ['dataSet 3', [[0,5], [1,1], [2,0.5]]],
]

import pycha.bar
chart = pycha.bar.VerticalBarChart(surface)
chart.addDataset( dataSet )
chart.render()

surface.write_to_png('output.png')

