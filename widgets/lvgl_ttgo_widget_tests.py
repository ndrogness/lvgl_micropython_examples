import lvgl as lv
import ttgo
from axp_constants import *
from widgets.lv_arc import lv_arc
from widgets.lv_img import lv_img
from widgets.lv_canvas import lv_canvas
from widgets.lv_button import lv_button
from widgets.lv_tileview import lv_tileview

# Globals
watch = ttgo.Watch()
tft = watch.tft
power = watch.pmu


def init():
    power.adc1Enable(AXP202_VBUS_VOL_ADC1
                     | AXP202_VBUS_CUR_ADC1 |
                     AXP202_BATT_CUR_ADC1 | AXP202_BATT_VOL_ADC1, True)
    watch.lvgl_begin()


# initial the Watch
init()

# Grab a lv screen
scr = lv.obj()

# Load the screen & turn on backlight
lv.scr_load(scr)
# watch.tft.backlight_fade(100)
watch.tft.backlight_fade(50)

# Show Canvas
#lv_canvas.lv_canvas(scr)

# Show Arc
# lv_arc.lv_arc(scr)

# Show Button
#lv_button.lv_button(scr)

# Show tileview
lv_tileview.lv_tileview(scr)

#widget_page = lv.page(scr)
#widget_page.set_size(240, 960)


#Show Imgage
#lv_img.lv_img(scr)


