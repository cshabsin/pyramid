import re
import util

QWERTY_RE = re.compile(r"Letters located in the (top|middle|bottom) row on a QWERTY keyboard: (.*)")
class QwertyHandler(object):
    @staticmethod
    def matches(line):
        return QWERTY_RE.match(line)

    @staticmethod
    def prune(line, words):
        location = QWERTY_RE.match(line).group(1)
        desc = QWERTY_RE.match(line).group(2)
        if location == "top":
            matchLetters = "QWERTYUIOP"
        if location == "middle":
            matchLetters = "ASDFGHJKL"
        if location == "bottom":
            matchLetters = "ZXCVBNM"
        def matchCount(word, matchLetters):
            return sum([1 for letter in word.upper() if letter in matchLetters])
        words = [word for word in words 
                 if util.value_matches(desc, matchCount(word, matchLetters), len(word))]
        return words

NONOVERLAPPING_RE = re.compile(r"If you marked nonoverlapping (.*), you could mark at most: (.*)")
WORD_SETS = {
    "US state postal abbreviations": ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"],
    "chemical element symbols (atomic number 112 or below)":[
        "H",
        "HE",
        "LI",
        "BE",
        "B",
        "C",
        "N",
        "O",
        "F",
        "NE",
        "NA",
        "MG",
        "AL",
        "SI",
        "P",
        "S",
        "CL",
        "AR",
        "K",
        "CA",
        "SC",
        "TI",
        "V",
        "CR",
        "MN",
        "FE",
        "CO",
        "NI",
        "CU",
        "ZN",
        "GA",
        "GE",
        "AS",
        "SE",
        "BR",
        "KR",
        "RB",
        "SR",
        "Y",
        "ZR",
        "NB",
        "MO",
        "TC",
        "RU",
        "RH",
        "PD",
        "AG",
        "CD",
        "IN",
        "SN",
        "SB",
        "TE",
        "I",
        "XE",
        "CS",
        "BA",
        "LA",
        "CE",
        "PR",
        "ND",
        "PM",
        "SM",
        "EU",
        "GD",
        "TB",
        "DY",
        "HO",
        "ER",
        "TM",
        "YB",
        "LU",
        "HF",
        "TA",
        "W",
        "RE",
        "OS",
        "IR",
        "PT",
        "AU",
        "HG",
        "TL",
        "PB",
        "BI",
        "PO",
        "AT",
        "RN",
        "FR",
        "RA",
        "AC",
        "TH",
        "PA",
        "U",
        "NP",
        "PU",
        "AM",
        "CM",
        "BK",
        "CF",
        "ES",
        "FM",
        "MD",
        "NO",
        "LR",
        "RF",
        "DB",
        "SG",
        "BH",
        "HS",
        "MT",
        "DS",
        "RG",
        "CN"],
    "officially-assigned ISO 3166-1 alpha-2 country codes":[
        "AD",
        "AE",
        "AF",
        "AG",
        "AI",
        "AL",
        "AM",
        "AO",
        "AQ",
        "AR",
        "AS",
        "AT",
        "AU",
        "AW",
        "AX",
        "AZ",
        "BA",
        "BB",
        "BD",
        "BE",
        "BF",
        "BG",
        "BH",
        "BI",
        "BJ",
        "BL",
        "BM",
        "BN",
        "BO",
        "BQ",
        "BR",
        "BS",
        "BT",
        "BV",
        "BW",
        "BY",
        "BZ",
        "CA",
        "CC",
        "CD",
        "CF",
        "CG",
        "CH",
        "CI",
        "CK",
        "CL",
        "CM",
        "CN",
        "CO",
        "CR",
        "CU",
        "CV",
        "CW",
        "CX",
        "CY",
        "CZ",
        "DE",
        "DJ",
        "DK",
        "DM",
        "DO",
        "DZ",
        "EC",
        "EE",
        "EG",
        "EH",
        "ER",
        "ES",
        "ET",
        "FI",
        "FJ",
        "FK",
        "FM",
        "FO",
        "FR",
        "GA",
        "GB",
        "GD",
        "GE",
        "GF",
        "GG",
        "GH",
        "GI",
        "GL",
        "GM",
        "GN",
        "GP",
        "GQ",
        "GR",
        "GS",
        "GT",
        "GU",
        "GW",
        "GY",
        "HK",
        "HM",
        "HN",
        "HR",
        "HT",
        "HU",
        "ID",
        "IE",
        "IL",
        "IM",
        "IN",
        "IO",
        "IQ",
        "IR",
        "IS",
        "IT",
        "JE",
        "JM",
        "JO",
        "JP",
        "KE",
        "KG",
        "KH",
        "KI",
        "KM",
        "KN",
        "KP",
        "KR",
        "KW",
        "KY",
        "KZ",
        "LA",
        "LB",
        "LC",
        "LI",
        "LK",
        "LR",
        "LS",
        "LT",
        "LU",
        "LV",
        "LY",
        "MA",
        "MC",
        "MD",
        "ME",
        "MF",
        "MG",
        "MH",
        "MK",
        "ML",
        "MM",
        "MN",
        "MO",
        "MP",
        "MQ",
        "MR",
        "MS",
        "MT",
        "MU",
        "MV",
        "MW",
        "MX",
        "MY",
        "MZ",
        "NA",
        "NC",
        "NE",
        "NF",
        "NG",
        "NI",
        "NL",
        "NO",
        "NP",
        "NR",
        "NU",
        "NZ",
        "OM",
        "PA",
        "PE",
        "PF",
        "PG",
        "PH",
        "PK",
        "PL",
        "PM",
        "PN",
        "PR",
        "PS",
        "PT",
        "PW",
        "PY",
        "QA",
        "RE",
        "RO",
        "RS",
        "RU",
        "RW",
        "SA",
        "SB",
        "SC",
        "SD",
        "SE",
        "SG",
        "SH",
        "SI",
        "SJ",
        "SK",
        "SL",
        "SM",
        "SN",
        "SO",
        "SR",
        "SS",
        "ST",
        "SV",
        "SX",
        "SY",
        "SZ",
        "TC",
        "TD",
        "TF",
        "TG",
        "TH",
        "TJ",
        "TK",
        "TL",
        "TM",
        "TN",
        "TO",
        "TR",
        "TT",
        "TV",
        "TW",
        "TZ",
        "UA",
        "UG",
        "UM",
        "US",
        "UY",
        "UZ",
        "VA",
        "VC",
        "VE",
        "VG",
        "VI",
        "VN",
        "VU",
        "WF",
        "WS",
        "YE",
        "YT",
        "ZA",
        "ZM",
        "ZW"]
}


def best(word, wordset):
    currentIndex = 0
    while (currentIndex < len(word)):
        matches = [target for target in wordset if word[currentIndex:].startswith(target)]
        if len(matches) > 0:
            bestScore = 0
            return max([len(match) + best(word[currentIndex + len(match):], wordset) for match in matches])
        else:
            currentIndex += 1
    return 0


class NonoverlappingHandler(object):
    @staticmethod
    def matches(line):
        m = NONOVERLAPPING_RE.match(line)
        if not m: return False
        wordSetName = NONOVERLAPPING_RE.match(line).group(1)
        return wordSetName in WORD_SETS
        
    @staticmethod
    def prune(line, words):
        wordSetName = NONOVERLAPPING_RE.match(line).group(1)
        desc = NONOVERLAPPING_RE.match(line).group(2)
        wordSet = WORD_SETS[wordSetName]
        words = [word for word in words
                 if util.value_matches(desc, best(word.upper(), wordSet), len(word))]
        return words
            
ALL_HANDLERS = {
    11: [QwertyHandler],
    120: [NonoverlappingHandler]
    }
