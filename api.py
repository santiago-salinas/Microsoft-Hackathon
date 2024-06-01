from model import VehicleEventRecord


class PlateRecognitionService:
    def recognize(self, plateNumber):
        return VehicleEventRecord.select().where(VehicleEventRecord.plateCode == plateNumber)
