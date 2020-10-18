import lvgl as lv
import styles


def lv_btnmatrix(screen):

    # Button matrix map
    btnm_map = ["1", "2", "3", "\n", "4", "5", "6", ""]

    # Create button matrix
    btnmatrix = lv.btnmatrix(screen)

    # Set the map (map must end with empty element of core dump!)
    btnmatrix.set_map(btnm_map)


if __name__ == '__main__':
    lv.init()
    scr = lv.obj()
    lv.scr_load(scr)
    lv_btnmatrix(scr)
