import lvgl as lv
import ustruct as struct
import lodepng as png
from widgets.lv_img.imagetools import get_png_info, open_png


def lv_img(screen):

    # Image descriptor
    img_dsc = lv.img_dsc_t()
    # img_dsc.data_size = len(buff)
    # img_dsc.data = buff
    # img_dsc.header.always_zero = 0
    # img_dsc.header.w = 153
    # img_dsc.header.h = 154
    # img_dsc.header.cf = lv.img.CF.TRUE_COLOR
    # img_dsc.header.cf = lv.img.CF.RAW

    # Image from Lvgl bin builder (doesnt work)
    #with open('widgets/lv_img/wf565.bin', 'rb') as f:
    # with open('widgets/lv_img/wf888.bin', 'rb') as f:
    #     h = lv.img_header_t()
    #     h = f.read(4)
    #     lv.img.decoder_get_info(h, img_dsc.header)
    #     img_dsc.data_size = img_dsc.header.w * img_dsc.header.h * 4
    #     img_dsc.data = f.read()

    # Use PNG from imagetools
    # Register new image decoder
    decoder = lv.img.decoder_create()
    decoder.info_cb = get_png_info
    decoder.open_cb = open_png

    # with open('widgets/lv_img/png_decoder_test.png', 'rb') as f:
    with open('widgets/lv_img/wface2_240x240.png', 'rb') as f:
        buff = f.read()
        img_dsc.data = buff
        img_dsc.data_size = len(buff)

    print('buff size:', img_dsc.data_size)
    img = lv.img(screen)
    img.set_src(img_dsc)


    # lv.img.cache_set_size(2)

    # img2 = lv.img(screen)
    # img2.set_auto_size(True)
    # raw_dsc = lv.img_dsc_t()
    # get_png_info(None, png_img_dsc, raw_dsc.header)
    # dsc = lv.img_decoder_dsc_t({'src': png_img_dsc})
    # if open_png(None, dsc) == lv.RES.OK:
    #     raw_dsc.data = dsc.img_data
    #     raw_dsc.data_size = raw_dsc.header.w * raw_dsc.header.h * lv.color_t.SIZE
    #     img2.set_src(raw_dsc)
    #     img2.set_drag(True)


if __name__ == '__main__':
    lv.init()
    scr = lv.obj()
    lv.scr_load(scr)
    lv_img(scr)
