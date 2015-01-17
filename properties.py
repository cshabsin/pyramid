import re
import jtwang
import cshabsin

PROPERTIES = {
    'ABUSIR':     lambda w: w[0:2] == 'EX',
    'AMENEMHAT':  lambda w: w[0:2] == 'UN' or w[0:2] == 'EN',
    'AMENYQEMAU': lambda w: w[0] == w[-1],
    'BIKHERIS':   lambda w: w.find('SH') != -1,
    'DJOSER':     None,
    'HAWARA':     None,
    'KHUI':       lambda w: w[-1] == 'S',
    'LISHT':      lambda w: len(jtwang.DistinctHandler.distinct_vowels(w)) == 0,
    'MAZGHUNA':   lambda w: cshabsin.DoubledLetterHandler.has_double(w),
    'MEIDUM':     None,
    'MENKAURE':   None,
    'MERENRE':    None,
    'NEFEREFRE':  None,
    'NURI':       None,
    'PEPI':       lambda w: cshabsin.CharacterTypeHandler.most_common_count(w, 'AEIOU') == 3,
    'QAKAREIBI':  lambda w: w[0] == 'B',
    'SETHKA':     lambda w: w[-2:] == 'NG' or w[-2:] == 'ED',
    'SOBEKNEFERU':None,
    'UNAS':       None,
    }

PROPERTY_RE = re.compile(r"Has property (\w+): (\w+)")
class PropertyHandler(object):
    @staticmethod
    def matches(rule):
        m = PROPERTY_RE.match(rule)
        prop = m.group(1)
        if not PROPERTIES.get(prop, False):
            return False
        return True

    @staticmethod
    def prune(rule, words):
        m = PROPERTY_RE.match(rule)
        prop = m.group(1)
        truth = m.group(2) == "YES"

        handler = PROPERTIES[prop]
        return [w for w in words if handler(w.upper()) == truth]

