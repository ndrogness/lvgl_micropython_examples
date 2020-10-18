import lvgl as lv
import time


def draw_clock_digit(digit, digit_container=None, style=None, start_x=0, start_y=0, width=20, height=40):

    pts = []
    mid_width = int(width / 2)
    mid_height = int(height / 2)
    print('Building digit:', digit, 'at:', start_x, start_y)
    # Zero
    if digit == ':':
        half_mid = int(mid_height/2)
        pts.append(lv.point_t({'x': start_x+mid_width, 'y': start_y+half_mid}))
        pts.append(lv.point_t({'x': start_x+mid_width, 'y': start_y+mid_height+half_mid}))

    elif digit.isdigit():
        num = int(digit)

        if num == 0:
            pts.append(lv.point_t({'x': start_x, 'y': start_y}))
            # Top horizontal -
            pts.append(lv.point_t({'x': start_x+width, 'y': start_y}))

            # Right vertical |
            pts.append(lv.point_t({'x': start_x+width, 'y': start_y+height}))

            # Bottom horizontal _
            pts.append(lv.point_t({'x': start_x, 'y': start_y+height}))

            # Left Vertical |
            pts.append(lv.point_t({'x': start_x, 'y': start_y}))

        elif num == 1:
            pts.append(lv.point_t({'x': start_x+mid_width, 'y': start_y}))
            pts.append(lv.point_t({'x': start_x+mid_width, 'y': start_y+height}))

        elif num == 2:
            pts.append(lv.point_t({'x': start_x, 'y': start_y}))
            # Top horizontal -
            pts.append(lv.point_t({'x': start_x+width, 'y': start_y}))

            # Right upper vertical |
            pts.append(lv.point_t({'x': start_x+width, 'y': start_y+mid_height}))

            # Mid vertical -
            pts.append(lv.point_t({'x': start_x, 'y': start_y+mid_height}))

            # Left lower vertical |
            pts.append(lv.point_t({'x': start_x, 'y': start_y+height}))

            # Bottom horizontal _
            pts.append(lv.point_t({'x': start_x+width, 'y': start_y+height}))

        elif num >= 3:
            pts.append(lv.point_t({'x': start_x, 'y': start_y}))
            # Top horizontal left -
            pts.append(lv.point_t({'x': start_x + width, 'y': start_y}))

            # Right upper vertical down |
            pts.append(lv.point_t({'x': start_x + width, 'y': start_y + mid_height}))

            # Mid vertical left -
            pts.append(lv.point_t({'x': start_x, 'y': start_y + mid_height}))

            # Mid vertical right -
            pts.append(lv.point_t({'x': start_x+width, 'y': start_y + mid_height}))

            # Left lower vertical down |
            pts.append(lv.point_t({'x': start_x+width, 'y': start_y + height}))

            # Bottom horizontal left _
            pts.append(lv.point_t({'x': start_x, 'y': start_y + height}))

    if digit_container is not None:
        digit_line = lv.line(digit_container)
        digit_line.set_points(pts, len(pts))
        if style is not None:
            digit_line.add_style(digit_line.PART.MAIN, style)
        digit_line.align(None, lv.ALIGN.CENTER, 0, 0)

    return pts


class LvDigitLineClock:

    def __init__(self, lv_cont=None, size_x=0, size_y=0, digit_margin=10):
        self.cont_main = lv_cont
        self.size_x = size_x
        self.pos_x = 0
        self.size_y = size_y
        self.pos_y = 0
        self.digit_margin = digit_margin
        self.digit_width = int( (size_x-(digit_margin*9)) / 8 )
        self.digit_height = int( size_y-(digit_margin*2) )

        self.time = time.time()
        (self.year, self.month, self.mday, self.hour, self.minute, self.second, self.weekday,
         self.yearday) = time.localtime()

        # Line Style
        self.line_style = lv.style_t()
        self.line_style.init()
        self.line_style.set_line_width(lv.STATE.DEFAULT, 2)
        self.line_style.set_line_color(lv.STATE.DEFAULT, lv.color_hex(0x0000ff))
        self.line_style.set_line_rounded(lv.STATE.DEFAULT, True)
        self.line_style.set_pad_all(lv.STATE.DEFAULT, 0)
        self.line_style.set_margin_all(lv.STATE.DEFAULT, 0)

        # Container Style
        self.cont_style = lv.style_t()
        self.cont_style.init()
        self.cont_style.set_pad_all(lv.STATE.DEFAULT, 1)
        self.cont_style.set_margin_all(lv.STATE.DEFAULT, 1)
        # self.cont_style.set_border_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
        # self.cont_style.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
        # dont nedd -> cont_style.set_bg_color(lv.STATE.DEFAULT, styles.LV_COLOR_WATCH)

        # Digit Container Style
        self.cont_dstyle = lv.style_t()
        self.cont_dstyle.init()
        self.cont_dstyle.set_pad_all(lv.STATE.DEFAULT, 5)
        self.cont_dstyle.set_margin_all(lv.STATE.DEFAULT, 5)
        # self.cont_style.set_border_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
        # self.cont_style.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
        # dont nedd -> cont_style.set_bg_color(lv.STATE.DEFAULT, styles.LV_COLOR_WATCH)

        # Setup Main Parent container
        if self.cont_main is not None:
            #self.cont_main = lv.cont(lv_scr)
            # self.cont_main.set_auto_realign(True)
            self.cont_main.set_size(size_x, size_y)
            self.cont_main.set_fit(lv.FIT.NONE)
            #self.cont_main.set_layout(lv.LAYOUT.PRETTY_MID)
            self.cont_main.set_layout(lv.LAYOUT.ROW_MID)
            self.cont_main.add_style(self.cont_main.PART.MAIN, self.cont_style)

        # 12:34:56
        self.digit_pts = []

    def set_pos(self, x_pos, y_pos):
        if self.cont_main is None:
            self.pos_x = x_pos
            self.pos_y = y_pos
        else:
            self.cont_main.set_pos(x_pos, y_pos)

    def _build_digits(self):

        self.digit_pts.clear()

        d_txt = '{:02n}:{:02n}:{:02n}'.format(self.hour, self.minute, self.second)
        print('Digitizing:', d_txt)
        digit_count = 0
        d_start_x = self.pos_x
        d_start_y = self.pos_y

        for digit in d_txt:

            self.digit_pts.append(draw_clock_digit(digit=digit,
                                                   digit_container=self.cont_main,
                                                   style=self.line_style,
                                                   start_x=d_start_x,
                                                   start_y=d_start_y,
                                                   width=self.digit_width,
                                                   height=self.digit_height
                                                   )
                                  )

            digit_count += 1

            if self.cont_main is None:
                # No container so no auto layout, have to manually align digits
                d_start_x += self.digit_width + self.digit_margin

            '''
            # Old style - not used
            if digit_count < len(self.cont_digits):
                if self.cont_digits[digit_count] is None:
                    self.cont_digits[digit_count] = lv.cont(self.cont_main)
                self.cont_digits[digit_count].set_auto_realign(True)
                self.cont_digits[digit_count].set_fit(lv.FIT.TIGHT)
                self.cont_digits[digit_count].set_layout(lv.LAYOUT.CENTER)
                draw_clock_digit(digit=digit, digit_container=self.cont_digits[digit_count], style=self.line_style)
                #self.cont_digits[digit_count].align_origo(None, lv.ALIGN.CENTER, 0, 0)
                self.cont_digits[digit_count].add_style(self.cont_digits[digit_count].PART.MAIN, self.cont_dstyle)
            digit_count += 1

        for panel in panels:
            print("Trying:", panel)
            if panel['digits'] < 10:
                # First digit is zero
                d_txt = '0{0}'.format(panel['digits'])
            else:
                d_txt = '{0}'.format(panel['digits'])

            digit_count = 0
            for digit in d_txt:
                points = get_line_pts_from_num(int(digit), size=self.digit_size)
                if len(points) > 0 and digit_count < len(panel['lines']):
                    # Found a line points
                    print("Adding points:", points)
                    panel['lines'][digit_count].set_points(points, len(points))
                    panel['lines'][digit_count].add_style(panel['lines'][0].PART.MAIN, self.line_style)
                    if digit_count == 0:
                        panel['lines'][digit_count].align(None, lv.ALIGN.IN_LEFT_MID, 0, 0)
                    else:
                        panel['lines'][digit_count].align(None, lv.ALIGN.IN_RIGHT_MID, 0, 0)

                digit_count += 1
        '''

    def update(self):
        self.time = time.time()
        (self.year, self.month, self.mday, self.hour, self.minute, self.second, self.weekday, self.yearday) = time.localtime()
        self._build_digits()

    def deinit(self):
        pass
