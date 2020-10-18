import lvgl as lv
import ttgo
from axp_constants import *
from widgets.lv_arc import lv_arc
from widgets.lv_img import lv_img
from widgets.lv_canvas import lv_canvas
from widgets.lv_btn import lv_btn
from widgets.lv_tileview import lv_tileview
from widgets.lv_btnmatrix import lv_btnmatrix
from widgets.lv_line import lv_line
import lv_digitlineclock
import lv_watchface

# Globals
watch = ttgo.Watch()
tft = watch.tft
power = watch.pmu


def init():
    # power.adc1Enable(AXP202_VBUS_VOL_ADC1
    #                  | AXP202_VBUS_CUR_ADC1 |
    #                  AXP202_BATT_CUR_ADC1 | AXP202_BATT_VOL_ADC1, True)
    watch.lvgl_begin()


# initial the Watch
init()

# Grab a lv screen
scr = lv.obj()

# Turn on backlight
# watch.tft.backlight_fade(100)
watch.tft.backlight_fade(50)

# Show Canvas
# lv_canvas.lv_canvas(scr)

# Show Arc
# lv_arc.lv_arc(scr)

# Show Button
#lv_btn.lv_btn(scr)

# Show tileview
#lv_tileview.lv_tileview(scr)

# Show buttonmatrix
#lv_btnmatrix.lv_btnmatrix(scr)

#widget_page = lv.page(scr)
#widget_page.set_size(240, 960)


#Show Imgage
#lv_img.lv_img(scr)

#Show line
#lv_line.lv_line(scr)

#Digital Clock
# Setup Main Parent container
# cont_main = lv.cont(scr)

# self.cont_main.set_auto_realign(True)
# cont_main.set_size(size_x, size_y)
# cont_main.set_fit(lv.FIT.NONE)
# cont_main.add_style(self.cont_main.PART.MAIN, self.cont_style)
# cont.set_layout(lv.LAYOUT.PRETTY_MID)
# self.cont_main.set_layout(lv.LAYOUT.ROW_MID)

# dclock = lv_digitlineclock.LvDigitLineClock(cont_main, size_x=220, size_y=75)
# dclock.set_pos(10, 80)
# dclock.update()

watchface = lv_watchface.WatchFace(scr)
watchface.load()

# Load the screen
lv.scr_load(scr)
