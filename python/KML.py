default_keys = {
                'name',
                'description',
                'ExtendedData'
}

def defaults_dict(keys=default_keys, **kwargs):
    defaults = dict.fromkeys(keys, "")
    defaults.update(kwargs)
    return defaults




point_template = """\
    <Point id="{id}">
        <name>{name}</name>
        <description>{description}</description>
        <ExtendedData>{ExtendedData}</ExtendedData>
        <extrude>{extrude}</extrude>
        <altitudeMode>{altitudeMode}</altitudeMode>
        <coordinates>{coordinates}</coordinates>
    </Point>
"""

line_string = """\
    <Placemark>
    <LineString id="{id}">
        <name>{name}</name>
        <description>{description}</description>
        <ExtendedData>{ExtendedData}</ExtendedData>
        <extrude>{extrude}</extrude>
        <tessellate>{tessellate}</tessellate>
        <altitudeMode>{altitudeMode}</altitudeMode>
        <coordinates>{coordinates}</coordinates>
    </LineString>
    </Placemark>
"""

kml_template = """\
<kml>
<Document>
<name>{name}</name>
<description>{description}</description>
{contents}</Document>
</kml>"""

class KML(object):
    keys = [    'name',
                'description',
                'contents'  ]
    def __init__(self, name="", description="", **kwargs):
        self.contents = []
        self.name = name
        self.description = description
        string_format = dict.fromkeys(KML.keys,"")
        for (key,val) in kwargs:
            if key in KML.keys:
                string_format[key]=val
        self.string_format = string_format
        print string_format

    def write(self):
        contents = ''.join([obj.write() for obj in self.contents])
        self.string_format['contents']=contents
        return kml_template.format(**self.string_format)

    def write_to(self, save_name):
        with open(save_name, 'w') as output:
            output.write(self.write())

    def add_object(self, obj):
        self.contents.append(obj)


class LineString(object):
    line_keys = [   'id',
                    'name',
                    'description',
                    'ExtendedData',
                    'extrude',
                    'tessellate',
                    'altitudeMode',
                    'coordinates'   ]

    def __init__(self, lats, lons, alts=0, **kwargs):
        coordinates = Coord(lats, lons, alts)
        self.coordinates = coordinates
        string_formats = dict.fromkeys(LineString.line_keys,"")
        for (key,val) in kwargs.iteritems():
            if key in LineString.line_keys:
                string_formats[key]=val
        self.string_formats = string_formats

    def write(self):
        self.string_formats['coordinates']=self.coordinates.write()
        return line_string.format(**self.string_formats)


def iterable(obj):
    return hasattr(obj, "__iter__")

class Coord(object):
    def __init__(self, lats, lons, alts=0):
        if not iterable(lats):
            lats = [lats]
        if not iterable(lons):
            lons = [lons]
        if not iterable(alts):
            alts = [alts]
        if iterable(lats) and iterable(lons):
            if len(lats)!=len(lons):
                raise ValueError("Lat and Lon lengths not equal")
            if len(alts)>1:
                if len(alts)!=len(lats) or len(alts)!=len(lons):
                    raise ValueError("Altitude not equal length")
            else:
                alts = [alts[0] for lat in lats]

        self.lats = lats
        self.lons = lons
        self.alts = alts

    def write(self):
        coordinates = []
        for triple in zip(self.lons, self.lats, self.alts):
            coordinates.append(','.join(map(str,triple)))
        return ' '.join(coordinates)



class Point(object):
    point_keys = [  "id",
                    "name",
                    "description",
                    "ExtendedData",
                    "extrude",
                    "altitudeMode",
                    "coordinates",
                      ]
    def __init__(self, lat, lon, **kwargs):
        defaults = {'altitude':0}
        defaults.update(kwargs)
        coordinate = Coord(lat,lon,defaults['altitude'])
        self.coordinate = coordinate
        string_formats = dict.fromkeys(Point.point_keys,"")
        for (key,val) in kwargs.iteritems():
            if key in Point.point_keys:
                string_formats[key]=val
        self.string_formats = string_formats

    def write(self):
        self.string_formats["coordinates"] = self.coordinate.write()
        return point_template.format(**self.string_formats)

    def write_to(self, save_name):
        with open(save_name,"w") as output:
            output.write(self.write())

if __name__ == "__main__":
    # p = Point(-135.2,48.6, altitude=30, description="A point")
    # print p.write()
    # p.write_to("KML_point.kml")
    kml = KML()
    l = LineString([30,40],[50,60],name="Line String", description="Describes")
    kml.add_object(l)
    print kml.write()
    kml.write_to("KML_test.kml")
