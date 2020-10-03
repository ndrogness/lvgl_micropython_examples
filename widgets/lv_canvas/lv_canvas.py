import lvgl as lv
import styles

def lv_canvas(screen):
    cbuff = bytearray(240*240*4)
    canvas = lv.canvas(screen)
    canvas.set_buffer(cbuff, 240, 240, lv.img.CF.TRUE_COLOR)
    canvas.fill_bg(styles.LV_COLOR_GREY, lv.OPA.COVER)

if __name__ == '__main__':
    lv.init()
    scr = lv.obj()
    lv.scr_load(scr)
    lv_canvas(scr)
