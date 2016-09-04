"""Utilities for ElementTree.
"""

import xml.etree.ElementTree as ET

# exported functions
__all__ = ["gettext"]

def gettext(element):
    """Get text immediately inside an element and inside subelements."""

    text = element.text or ""
    for child in element:
        text += gettext(child)
        if child.tail:
            text += child.tail
    return text

# test
if __name__ == "__main__":
    plant = ET.XML("""
    <PLANT>Plant description:
        <COMMON>Bloodroot</COMMON>
        <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$2.44</PRICE>
        <AVAILABILITY>031599</AVAILABILITY>
    </PLANT>""")
    #
    text = gettext(plant)
    assert len(text) > 100
    assert "canadensis" in text
    assert "2.44" in text
    #print(text)

# vim:sw=4:ts=4:ai:et
