import lvgl as lv
import ttgo
from axp_constants import *
from widgets.lv_arc import lv_arc

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
watch.tft.backlight_fade(100)

# Show Arc
lv_arc.lv_arc(scr)


