pointa_ll = (48.999192, -117.032352)
pointa_pix = (130, 18)

pointb_ll = (25.769568, -80.197209)
pointb_pix = (642, 428)



x_b = (pointb_pix[0] - pointa_pix[0])/(pointb_ll[1] - pointa_ll[1])
y_b = (pointb_pix[1] - pointa_pix[1])/(pointb_ll[0] - pointa_ll[0])

x_a = pointa_pix[0] - (x_b*pointa_ll[1])
y_a = pointa_pix[1] - (y_b*pointa_ll[0])

print("x_b: ", x_b)
print("y_b: ", y_b)
print("x_a: ", x_a)
print("y_a: ", y_a)
