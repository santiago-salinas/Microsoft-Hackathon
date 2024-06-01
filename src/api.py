safe = "SAFE"
dangerous = "DANGEROUS"
colorGreen = (161, 221, 112)
colorRed = (238, 78, 78)

database = [
    {"code": "ZME2015", "level": dangerous, "color": colorRed},
    {"code": "DAA76", "level": dangerous, "color": colorRed},
    {"code": "SCW2648", "level": safe, "color": colorGreen},
]


def findPlateState(code: str):
    for index, item in enumerate(database):
        if code == item["code"]:
            return item
    return None


def createAlert(code: str):
    result = findPlateState(code)
    if result is None:
        database.extend([{"code": code, "color": colorRed, "level": dangerous}])
    else:
        result["color"] = colorRed
        result["level"] = dangerous
