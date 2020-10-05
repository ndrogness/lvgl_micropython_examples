import lvgl as lv
import styles

valid_pos = [lv.point_t(), lv.point_t(), lv.point_t(), lv.point_t()]
valid_pos[0].x = 0
valid_pos[0].y = 0
valid_pos[1].x = 0
valid_pos[1].y = 1
valid_pos[2].x = 1
valid_pos[2].y = 0
valid_pos[3].x = 1
valid_pos[3].y = 1


def lv_tileview(screen):


    # Create Tileview object
    tileview = lv.tileview(screen)
    tileview.set_valid_positions(valid_pos, 4)
    # tileview.set_edge_flash(True)

    tile1 = lv.obj(tileview)
    tile1.set_size(240, 240)
    tileview.add_element(tile1)
    tile1_label = lv.label(tile1)
    tile1_label.set_text("Tile 1")
    tile1_label.align(None, lv.ALIGN.CENTER, 0, 0)

    tile2 = lv.obj(tileview)
    tile2.set_size(240, 240)
    tileview.add_element(tile2)
    tile2_label = lv.label(tile2)
    tile2_label.set_text("Tile 2")
    tile2_label.align(None, lv.ALIGN.CENTER, 0, 0)

    tile3 = lv.obj(tileview)
    tile3.set_size(240, 240)
    tileview.add_element(tile3)
    tile3_label = lv.label(tile3)
    tile3_label.set_text("Tile 3")
    tile3_label.align(None, lv.ALIGN.CENTER, 0, 0)

    # tileview.set_tile_act(0, 0, lv.ANIM.ON)


if __name__ == '__main__':
    lv.init()
    scr = lv.obj()
    lv.scr_load(scr)
    lv_tileview(scr)
