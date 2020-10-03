import lvgl as lv
import styles


def button_event_handler(obj, event):
    if event == lv.EVENT.CLICKED:
        print("Clicked")
    elif event == lv.EVENT.VALUE_CHANGED:
        print("Toggled")


def lv_button(screen):

    # Create button object on center screen
    button1 = lv.btn(screen)
    button1.align(screen, lv.ALIGN.CENTER, 0, 0)

    button1.set_event_cb(button_event_handler)
    button1.add_style(button1.PART.MAIN, styles.gstyle_shadow1)

    # Create a symbol as the text label
    label = lv.label(button1)
    label.set_text(lv.SYMBOL.PLAY)

    # Create text Label for button
    label1 = lv.label(button1)
    label1.set_text("Play")


if __name__ == '__main__':
    lv.init()
    scr = lv.obj()
    lv.scr_load(scr)
    lv_button(scr)
