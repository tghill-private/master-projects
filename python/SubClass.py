import colorsys

class colours(object):
    def __init__(self,hue,sat,lum):
        self.hue = hue
        self.sat = sat
        self.lum = lum

        r,g,b = colorsys.hls_to_rgb(hue,lum,sat)

        self.rgb = (r,g,b)
        r_hex = hex(int(255*r))[2:]
        g_hex = hex(int(255*g))[2:]
        b_hex = hex(int(255*b))[2:]

        self.cstr = r_hex + g_hex + b_hex
        self.hsl = (hue,sat,lum)

    def colourfunc(self):
        print "I come from the base class"

    def __repr__(self):
        return "colours({0}, {1}, {2})".format(self.hue, self.sat, self.lum)


class transparent_colours(colours):
    def __init__(self,colour,alpha):
        self.colour = colour
        hue,sat,lum = colour.hsl
        super(transparent_colours,self).__init__(hue,sat,lum)

        self.alpha = alpha
        self.castr = self.cstr + hex(int(255*alpha))[2:]

    def func(self):
        print "Here's another method of transparent_colours"

    def __repr__(self):
        return "transparent_colours({0},{1}".format(self.colour, self.alpha)

c = colours(0.87,0.91,0.98)
print c

t = transparent_colours(c,0.71)
print t

