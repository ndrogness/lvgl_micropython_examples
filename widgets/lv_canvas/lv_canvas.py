import lvgl as lv
import styles

def lv_canvas(screen):
    cbuff = bytearray(240*240*4)
    canvas = lv.canvas(screen)
    canvas.set_buffer(cbuff, 240, 240, lv.img.CF.TRUE_COLOR)
    canvas.fill_bg(styles.LV_COLOR_GREY, lv.OPA.COVER)

    rect_dsc = lv.draw_rect_dsc_t()
    rect_dsc.init()
    rect_dsc.radius = 10
    rect_dsc.bg_opa = lv.OPA.COVER
    rect_dsc.bg_grad_dir = lv.GRAD_DIR.HOR
    rect_dsc.bg_color = styles.LV_COLOR_RED
    rect_dsc.bg_grad_color = styles.LV_COLOR_BLUE
    rect_dsc.border_width = 2
    rect_dsc.border_opa = lv.OPA._90
    rect_dsc.border_color = styles.LV_COLOR_WHITE
    rect_dsc.shadow_width = 5
    rect_dsc.shadow_ofs_x = 5
    rect_dsc.shadow_ofs_y = 5

    canvas.draw_rect(70, 60, 100, 70, rect_dsc)

    label1 = lv.label(canvas)
    label1.add_style(label1.PART.MAIN, styles.gstyle_font1)
    label1.set_text("test font")

if __name__ == '__main__':
    lv.init()
    scr = lv.obj()
    lv.scr_load(scr)
    lv_canvas(scr)
