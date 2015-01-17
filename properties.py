import re
__PROPERTIES = {
    'ABUSIR':     None,
    'AMENEMHAT':  None,
    'AMENYQEMAU': None,
    'BIKHERIS':   None,
    'DJOSER':     None,
    'HAWARA':     None,
    'KHUI':       None,
    'LISHT':      None,
    'MAZGHUNA':   None,
    'MEIDUM':     None,
    'MENKAURE':   None,
    'MERENRE':    None,
    'NEFEREFRE':  None,
    'NURI':       None,
    'PEPI':       None,
    'QAKAREIBI':  None,
    'SETHKA':     None,
    'SOBEKNEFERU':None,
    'UNAS':       None,
    }

PROPERTY_RE = re.compile(r"Has property (\w+): (\w+)")
class PropertyHandler(object):
    @staticmethod
    def matches(rule):
        m = PROPERTY_RE.match(rule)
        prop = m.group(1)
        if not __PROPERTIES.get(prop, False):
            return False
        return True

    @staticmethod
    def prune(rule, words):
        m = PROPERTY_RE.match(rule)
        prop = m.group(1)
        truth = m.group(2) == "YES"

        handler = __PROPERTIES[prop]
        return [w for w in words if handler(w) == truth]

