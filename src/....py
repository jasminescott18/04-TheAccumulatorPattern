import rosegraphics as rg
window = rg.RoseWindow(500, 500)


point2 = rg.Point(50, 50)
point3 = rg.Point((50 + 100), 50)

for k in range(5):
    line = rg.Line(point2, point3)
    y = ((-100 + 200) / 5


    line.attach_to(window)

window.render()
window.close_on_mouse_click()