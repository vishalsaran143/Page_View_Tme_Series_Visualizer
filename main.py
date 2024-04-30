from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot
import unittest
from test_module import TestTimeSeriesVisualizer

# Run the functions
draw_line_plot()
draw_bar_plot()
draw_box_plot()

# Import and run the unit tests
unittest.main(argv=[''], verbosity=2, exit=False)
