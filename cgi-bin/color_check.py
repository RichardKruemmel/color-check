#!/usr/bin/env python3

import cgi

form = cgi.FieldStorage()

v_color = str(form.getvalue('color'))
with open('/Users/richardkruemmel/foundation_project/color_check/cgi-bin/colors.txt', 'r') as f:
    color_list=f.read()

if v_color in color_list:
    print("""
    <html>
    <body style="background-color: %s;">
    <h1>
    %s is a color.
    </h1>
    </body>
    </html>
    """ % (v_color, v_color))
else:
    print("""
    <html>
    <body>
    <h1>
    %s is a not a color.
    </h1>
    </body>
    </html>
    """ % v_color)