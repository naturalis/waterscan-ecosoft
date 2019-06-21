from models.reference_wew_factor_class_temp import reference_wew_factor_class_temp
from models.CalculationData import CalculationData
from services.AuthService import AuthService

class CalculateService:
    @AuthService.tokenRequired
    def getSampleById(self, id):
        """Returns JSON object of wew values for one sample"""
        return list(map(lambda x: x.json(), CalculationData.findCalculationBySampleId(id)))

    @AuthService.tokenRequired
    def getReferenceById(self, id):
        """Returns JSON object of wew values for one reference"""
        return list(map(lambda x: x.jsonComputed(), reference_wew_factor_class_temp.findAllFactors(id)))
