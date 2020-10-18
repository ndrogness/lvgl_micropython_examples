import lvgl as lv
import styles


def lv_line(screen):
    line_points = [[5,5], [70,70]]
    valid_pos = [lv.point_t(), lv.point_t(), lv.point_t(), lv.point_t(), lv.point_t(), lv.point_t(), lv.point_t()]
    valid_pos[0].x = 0
    valid_pos[0].y = 0
    valid_pos[1].x = 10
    valid_pos[1].y = 0
    valid_pos[2].x = 10
    valid_pos[2].y = 10
    valid_pos[3].x = 0
    valid_pos[3].y = 10
    valid_pos[4].x = 10
    valid_pos[4].y = 10
    valid_pos[5].x = 10
    valid_pos[5].y = 20
    valid_pos[6].x = 0
    valid_pos[6].y = 20

    line_style2 = lv.style_t()
    line_style2.init()
    line_style2.set_line_width(lv.STATE.DEFAULT, 8)
    line_style2.set_line_color(lv.STATE.DEFAULT, styles.LV_COLOR_BLUE)
    line_style2.set_line_rounded(lv.STATE.DEFAULT, True)

    cont_style = lv.style_t()
    cont_style.init()
    cont_style.set_border_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    cont_style.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    # cont_style.set_bg_color(lv.STATE.DEFAULT, styles.LV_COLOR_WATCH)

    cont = lv.cont(screen)
    #cont.add_style(cont.PART.MAIN, cont_style)
    cont.set_auto_realign(True)
    cont.set_size(200,65)
    cont.set_pos(20,85)
    #cont.align_origo(None, lv.ALIGN.CENTER, 0, 0)
    cont.set_fit(lv.FIT.NONE)
    # cont.set_layout(lv.LAYOUT.PRETTY_MID)
    cont.set_layout(lv.LAYOUT.ROW_MID)

    line = lv.line(cont)
    points = styles.get_line_pts_from_num(1, size=40)
    line.set_points(points, len(points))
    line.add_style(line.PART.MAIN, line_style2)
    line.align(None, lv.ALIGN.CENTER, 0, 0)

    line2 = lv.line(cont)
    points = styles.get_line_pts_from_num(2, size=40)
    line2.set_points(points, len(points))
    line2.add_style(line2.PART.MAIN, line_style2)
    line2.align(None, lv.ALIGN.CENTER, 0, 0)


if __name__ == '__main__':
    lv.init()
    scr = lv.obj()
    lv_line(scr)
    lv.scr_load(scr)
