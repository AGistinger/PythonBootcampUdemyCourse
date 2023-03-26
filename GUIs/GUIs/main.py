# Introduction to GUIs
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import interact, interactive, fixed


# Define a function to explore
def func(x):
    return x


# Pass interact(function, default value)
# Integer will create a slider
interact(func, x=10)
# Boolean will create a checkbox
# interact(func, x=True)
# String will create a textbox
# interact(func, x="Hello")


# Use a Decorator
# If a parameter is marked as fixed it cannot be changed
# by the user
@interact(x=True, y=fixed(1.0))
def g(x, y):
    return (x, y)


# Widget Abbreviations
# Change min/max, step size, starting value
interact(func, x=widgets.IntSlider(min=-100, max=100, step=1, value=0))
interact(func, x=(-100, 100, 1))

# Create drop down menu
interact(func, x=["hello", "option 2", "option 3"])

# Dictionary has drop down but returns the value
interact(func, x={'one': 10, 'two': 20})


# Interactive
# Allows you to reuse widgets
# Return value of function will not display automatically
def f(a, b):
    display(a + b)
    return a + b


w = interactive(f, a=10, b=20)
print(type(w))
print(w.children)
display(w)

# GUI Widget Basics
w1 = widgets.IntSlider()  # Shows default int slider
display(w1)  # To display widget later

print(w1.value)  # Show current value
w1.value = 50  # change value
print(w1.keys)

w1.close()  # Close widget

# Link two similar widgets
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a, b)
my_link = widgets.jslink((a, "value"), (b, "value"))

# Unlink
my_link.unlink()

# List of Possible Widgets
# (DEPRECATED)
# for item in widgets.Widget.widget_types.items():
#    print(item[0])

widgets.IntSlider()
widgets.FloatSlider()
widgets.IntRangeSlider()
widgets.FloatRangeSlider()
widgets.IntProgress()
widgets.FloatProgress()
widgets.BoundedIntText()
widgets.BoundedFloatText()
widgets.IntText()
widgets.FloatText()
widgets.ToggleButton()
widgets.Checkbox()
widgets.Valid()
widgets.Dropdown()
widgets.RadioButtons()
widgets.Select()
# widgets.SelectionSlider()
# widgets.SelectionRangeSlider()
widgets.ToggleButtons()
widgets.SelectMultiple()
widgets.Text()
widgets.Textarea()
widgets.HBox()
widgets.HTML()
widgets.HTMLMath()
widgets.Image()
widgets.Button()

# Widget Styling and Layouts
# Based on CSS
wig = widgets.IntSlider()
display(wig)
wig.layout.margin = "auto"
wig.layout.height = "75px"
x = widgets.IntSlider(value=15, description="New Slider")
display(x)
x.layout = wig.layout

# Style, based on Bootstrap code
widgets.Button(description="Ordinary Button", button_sytle="info")

# Custom colors
b1 = widgets.Button(description="Custom Color")
b1.style.button_color = "lightgreen"  # uses string codes
display(b1)
print(b1.style.keys)

b2 = widgets.Button(description="New")
b2.style = b1.style  # match style

s1 = widgets.IntSlider(description="My Handle")
s1.style.handle_color = "blue"
display(s1)
