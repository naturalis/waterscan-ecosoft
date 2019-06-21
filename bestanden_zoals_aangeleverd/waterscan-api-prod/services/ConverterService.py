import math
from services.AuthService import AuthService

# @author: Wim van der Putten
class ConverterService:
    """Returns location for map component"""
    @AuthService.tokenRequired
    def convert(self, location):
        xReference = 155000
        yReference = 463000
        dX = (location.x_coor - xReference) * math.pow(10.0, -5.0)
        dY =(location.y_coor - yReference) * math.pow(10.0, -5.0)
        sumN = 3235.65389 * dY + -32.58297 * math.pow(dX, 2.0) + -0.2475 * math.pow(dY, 2.0) + -0.84978 * math.pow(dX, 2.0) * dY + -0.0655 * math.pow(dY, 3.0) + -0.01709 * math.pow(dX, 2.0) * math.pow(dY, 2.0) + -0.00738 * dX + 0.0053 * math.pow(dX, 4.0) + -3.9E-4 * math.pow(dX, 2.0) * math.pow(dY, 3.0) + 3.3E-4 * math.pow(dX, 4.0) * dY + -1.2E-4 * dX * dY;
        sumE = 5260.52916 * dX + 105.94684 * dX * dY + 2.45656 * dX * math.pow(dY, 2.0) + -0.81885 * math.pow(dX, 3.0) + 0.05594 * dX * math.pow(dY, 3.0) + -0.05607 * math.pow(dX, 3.0) * dY + 0.01199 * dY + -0.00256 * math.pow(dX, 3.0) * math.pow(dY, 2.0) + 0.00128 * dX * math.pow(dY, 4.0) + 2.2E-4 * math.pow(dY, 2.0) + -2.2E-4 * math.pow(dX, 2.0) + 2.6E-4 * math.pow(dX, 5.0);
        referenceWgs84X = 52.15517
        referenceWgs84Y = 5.387206
        latitude = referenceWgs84X + sumN / 3600.0
        longitude = referenceWgs84Y + sumE / 3600.0
        location.longitude = longitude
        location.latitude = latitude
        return location
