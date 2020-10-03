import lvgl as lv

# Some lvgl C to python shortcuts
LV_OPA_COVER = lv.OPA.COVER
LV_STATE_DEFAULT = lv.STATE.DEFAULT

LV_COLOR_RED = lv.color_hex(0xff0000)
LV_COLOR_BLUE = lv.color_hex(0x0000ff)
LV_COLOR_LIGHT_GREY = lv.color_hex(0xd3d3d3)
LV_COLOR_GREY = lv.color_hex(0x808080)
LV_COLOR_SILVER = lv.color_hex(0xc0c0c0)

# Background style - color blue
gstyle_bg1 = lv.style_t()
gstyle_bg1.init()
gstyle_bg1.set_bg_color(lv.STATE.DEFAULT, LV_COLOR_BLUE)
gstyle_bg1.set_border_color(lv.STATE.DEFAULT, LV_COLOR_BLUE)

# Line style - color red
gstyle_line1 = lv.style_t()
gstyle_line1.init()
gstyle_line1.set_line_color(lv.STATE.DEFAULT, LV_COLOR_RED)

# Shadow Style - grey with blue shadow
gstyle_shadow1 = lv.style_t()
gstyle_shadow1.init()
#  Add background color and a radius
gstyle_shadow1.set_radius(lv.STATE.DEFAULT, 5)
gstyle_shadow1.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
gstyle_shadow1.set_bg_color(lv.STATE.DEFAULT, LV_COLOR_SILVER)
#  Add Shadow
gstyle_shadow1.set_shadow_width(lv.STATE.DEFAULT, 8)
gstyle_shadow1.set_shadow_color(lv.STATE.DEFAULT, LV_COLOR_BLUE)
gstyle_shadow1.set_shadow_ofs_x(lv.STATE.DEFAULT, 10)
gstyle_shadow1.set_shadow_ofs_y(lv.STATE.DEFAULT, 20)



