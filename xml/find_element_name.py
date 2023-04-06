
# Dictionary of keywords for each element type
element_keywords = {
        "point": ["point", "points", "pts", "pt"],
        "line": ["line", "lines", "segment", "segments"],
        "triangle": ["triangle", "triangles", "tria", "tri"],
        "circle": ["circle", "circles", "circ", "c"],
        "angle": ["angle", "angles", "ang"],
        "rectangle": ["rectangle", "rectangles", "rect"],
        "diagonal": ["diagonal", "diagonals", "diag"],
        "quadrilateral": ["quadrilateral", "quadrilaterals", "quad"],
        "polygon": ["polygon", "polygons", "poly"],
        "arc": ["arc", "arcs"],
        "tangent": ["tangent", "tangents"],
        "perpendicular": ["perpendicular", "perpendiculars"],
        "midpoint": ["midpoint", "midpoints"],
        "bisector": ["bisector", "bisectors"],
        "chord": ["chord", "chords"],
        "sector": ["sector", "sectors"],
        "apex": ["apex", "apices"],
        "base": ["base", "bases"],
        "height": ["height", "heights"],
        "hypotenuse": ["hypotenuse", "hypotenuses"],
        "radius": ["radius", "radii"],
        "center": ["center", "centers", "centre", "centres"],
        "vertex": ["vertex", "vertices"],
        "side": ["side", "sides"],
        "opposite": ["opposite", "opposites"],
        "adjacent": ["adjacent", "adjacents"],
        "complement": ["complement", "complements"],
        "supplement": ["supplement", "supplements"]
    }


# Function to get the element type for an emph tag in a line
def get_element_type(line, emph):
    keywords = element_keywords["other"]
    for element, kw in element_keywords.items():
        for word in kw:
            if word in line and word in emph:
                keywords = kw
                break
        if keywords != element_keywords["other"]:
            break
    # Find the closest keyword to the emph tag
    closest = None
    min_dist = len(line)
    for keyword in keywords:
        idx = line.find(keyword)
        if idx != -1 and idx < emph.find(","):
            dist = len(emph) - len(keyword) - emph.find(keyword)
            if dist < min_dist:
                min_dist = dist
                closest = element
    return closest

