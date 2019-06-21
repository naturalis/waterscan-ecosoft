from models.WewFactor import WewFactor
from models.WewFactorClass import WewFactorClass
from models.WewValue import WewValue
from services.AuthService import AuthService
from flask import request, jsonify

class WewService:
    @AuthService.tokenRequired
    def getFactors(self):
        factors = list(WewFactor.query.all())
        classes = list(WewFactorClass.query.all())
        webFactors = []
        for factor in factors:
            wewFactorWeb = factor
            factorClasses = list(map(lambda x: x.json(), filter(lambda x: x.factor_id == factor.id, classes)))
            wewFactorWeb.classes = factorClasses
            webFactors.append(wewFactorWeb)

        return list(map(lambda x: x.json(), webFactors))

    @AuthService.adminRequired
    def saveFactors(self):
        json = request.json
        factorID = 1
        factorClassID = 1
        factorClasses = []
        for f in json:
            factor = WewFactor(factorID, f["name"])
            factor.save()
            for c in f["classes"]:
                wewFactor = WewFactorClass(factorClassID, factorID, c["code"], c["description"], c["order"])
                wewFactor.save()
                factor.classes.append(wewFactor.json())
                factorClassID += 1
            factorID += 1
            factorClasses.append(factor.json())
        return factorClasses

    @AuthService.adminRequired
    def saveValue(self):
        print("saving...")
        json = request.json
        valueList = []
        for v in json:
            valueList.append(WewValue(None, v["c"], v["t"], v["v"]))
        WewValue.bulkInsert(valueList)
        return jsonify({"count": len(valueList)})

    @AuthService.adminRequired
    def isEmpty(self):
        factors = list(WewFactor.query.all())
        classes = list(WewFactorClass.query.all())
        value = list(WewValue.query.all())
        return not (factors and classes and value)

    @AuthService.adminRequired
    def emptyTables(self):
        WewFactorClass.delete()
        WewValue.delete()
        WewFactor.delete()
        WewFactorClass.delete(self)

    def getTaxonWewValue(self, taxonId):
        return list(map(lambda x: x.jsonTaxonWewValue(), WewValue.findWewValuesByTaxonId(taxonId)))
