from models.SampleTaxon import SampleTaxon

# @author: Wim van der Putten
class SampleTaxonService:
    def getSample(self, id):
        # retrieves the list
        results = SampleTaxon.findTaxonListBySampleId(id)

        # create some lists
        sample_taxonList = []
        wew_valueList = []
        taxonList = []
        newTaxonList = []

        for result in results:
            # seperate the values to their own lists
            wew_valueList.append(result.WewValue.jsonCalc())
            taxonList.append(result.Taxon)
        taxonList = list(set(taxonList))
        newTaxonList = list((map(lambda x: x.jsonSample(), taxonList)))
        result = SampleTaxon(id, newTaxonList, wew_valueList)
        return result.json()