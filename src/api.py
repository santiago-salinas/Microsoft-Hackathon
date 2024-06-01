safe = "SAFE"
dangerous = "DANGEROUS"
colorGreen = (161, 221, 112)
colorRed = (0, 0, 255)

class PlateDatabase:
    def __init__(self):
        self.database = [
            {"code": "ZME2015", "level": safe, "color": colorGreen},
            {"code": "OAA7644", "level": dangerous, "color": colorRed},
            {"code": "SCW2648", "level": safe, "color": colorGreen},
        ]

    def findPlateState(self, code: str):
        for item in self.database:
            if code == item["code"]:
                return item
        return None

    def removePlateState(self, code: str):
        for index, item in enumerate(self.database):
            if code == item["code"]:
                self.database.pop(index)
                return True
        return False

    def createAlert(self, code: str):
        print(self.database)
        print(f"Creating alert for plate: {code}")
        result = self.findPlateState(code)
        print(result)
        if result is None:
            print("Plate not found in database")
            self.database.append({"code": code, "color": colorRed, "level": dangerous})
        else:
            print("Plate found in database")
            self.removePlateState(code)
            self.database.append({"code": code, "color": colorRed, "level": dangerous})
        print(self.database)

