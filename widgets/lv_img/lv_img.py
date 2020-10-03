import lvgl as lv


def lv_img(screen):
    img_var = lv.img_dsc_t()
    img = lv.img(screen)
    img.set_src("/widgets/lv_img/wf565.bin")
    #with open('widgets/lv_img/wf565.bin', 'rb') as f:
    #    buff = f.read()
    #img.set_src(buff)
    # img.set_auto_size(True)


if __name__ == '__main__':
    lv.init()
    scr = lv.obj()
    lv.scr_load(scr)
    lv_img(scr)
