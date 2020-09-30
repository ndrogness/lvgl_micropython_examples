import lvgl as lv


def lv_arc(screen):

    # Create the arc object on lv screen, ie a lv.scr() object
    arc = lv.arc(screen)


    # Setup Angles, from docs:
    #  Zero degree is at the middle right (3 o'clock) of the object and the degrees are increasing
    #  in a clockwise direction. The angles should be in [0;360] range.
    #
    # Get background angle start and end in degrees
    start = arc.get_bg_angle_start() # default is 135
    end = arc.get_bg_angle_end() # default is 45

    # Set background angles
    #arc.set_bg_angles(180,max)
    # Set start angle of the arc (0-360 degrees)
    #arc.set_start_angle(0)

    # Set arc size
    arc.set_size(150, 150)

    # Get current value of arc
    # print(arc.get_value()) # default is 0
    # print(arc.get_min_value()) # default is 0
    # print(arc.get_max_value()) # default is 100

    # Set the current value (0-100)
    # A percentage of the arc foreground that is filled
    # Note: This doesnt work on micropython?
    # Examples:
    #    50 is 50% filled
    #    100 is 100% filled
    # arc.set_value(5)
    #
    # Or set the value base on end angle (0-360) degrees
    # Set end angle of the arc (0-360 degrees)
    arc.set_end_angle(200)

if __name__ == '__main__':
    lv.init()
    scr = lv.obj()
    lv.scr_load(scr)
    lv_arc(scr)
