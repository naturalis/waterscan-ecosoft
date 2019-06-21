from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from Database import db

from resources.MapResource import MapResource
from resources.CalculateResource import CalculateResource, CalulateReferenceResource
from resources.AdminResource import AdminResource, AdminResetResource
from resources.SampleTaxonResource import SampleTaxonResource
from resources.UserResource import UserResource, LoginUserResource, UserChangePasswordResource
from resources.ReferenceResource import ReferenceResource, ReferencesResource, ReferenceByWatertypeResource
from resources.ReferenceTaxonResource import ReferenceTaxonResource, ReferencetaxonResourceValue
from resources.WewResource import WewResource, WewFactorResource, WewAdminResource, WewAdminEmptyResource, WewValueResource, TaxonWewValueResource
from resources.LocationResource import LocationResource, LocationByIds, LocationByCodeResource, LocationsResource
from resources.SampleResource import SampleResource, SamplesResource, SampleByLocationResource, RecentSamples, SampleYearsResource
from resources.WaterschapResource import WaterschapResource, WaterschappenResource
from resources.TaxonResource import TaxonResource, TaxonsResource, TaxonByIdsResource, TaxonFindResource, TaxonFamilyResource
from resources.TaxonGroupResource import TaxonGroupResource, TaxonGroupsResource
from resources.TaxonLevelResource import TaxonLevelResource, TaxonLevelsResource
from resources.WatertypeResource import WatertypeResource, WatertypesResource
from resources.UserGroupResource import UserGroupResource, UserGroupsResource


# Flask framework used as REST API
app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:ubuntu@127.0.0.1/waterscan"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://debian-sys-maint:UROX1VQsnwcq68Lo@127.0.0.1/waterscan"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
db.init_app(app)
CORS(app)

# The different resources linked to a specific path which can be found by the client
api.add_resource(AdminResource, "/api/admin")
api.add_resource(AdminResetResource, "/api/admin/password")
api.add_resource(LoginUserResource, "/api/authenticate/login")
api.add_resource(UserChangePasswordResource, "/api/user/editpassword")
api.add_resource(CalculateResource, "/api/calculate/sample/<int:id>")
api.add_resource(SampleTaxonResource, "/api/calculate/sample2/<int:id>") # new sample
api.add_resource(ReferencetaxonResourceValue, "/api/calculate/reference2/<int:id>")
api.add_resource(CalulateReferenceResource, "/api/calculate/reference/<int:id>")
api.add_resource(LocationResource, "/api/location/id/<int:id>")
api.add_resource(LocationByCodeResource, "/api/location/code/<string:code>")
api.add_resource(LocationsResource, "/api/location/all")
api.add_resource(LocationByIds, "/api/location/ids")
api.add_resource(ReferenceResource, "/api/reference/<int:id>")
api.add_resource(ReferencesResource, "/api/reference")
api.add_resource(ReferenceByWatertypeResource, "/api/reference/watertype/<int:watertype_id>")
api.add_resource(ReferenceTaxonResource, "/api/admin/reference")
api.add_resource(SampleByLocationResource, "/api/sample/location/<int:locationId>")
api.add_resource(SampleResource, "/api/sample/<int:id>")
api.add_resource(SamplesResource, "/api/sample/all")
api.add_resource(RecentSamples, "/api/sample/recent/<int:count>")
api.add_resource(TaxonGroupResource, "/api/taxongroup/id/<int:id>")
api.add_resource(TaxonGroupsResource, "/api/taxongroup/all")
api.add_resource(TaxonByIdsResource, "/api/taxon/ids")
api.add_resource(TaxonFamilyResource, "/api/taxon/family/<int:id>")
api.add_resource(TaxonLevelResource, "/api/taxonlevel/id/<int:id>")
api.add_resource(TaxonLevelsResource, "/api/taxonlevel/all")
api.add_resource(TaxonResource, "/api/taxon/id/<int:id>")
api.add_resource(TaxonsResource, "/api/taxon/all")
api.add_resource(TaxonFindResource, "/api/taxon/findOrCreate")
api.add_resource(UserResource, "/api/user/id/<int:id>")
api.add_resource(WaterschapResource, "/api/waterschap/id/<int:id>")
api.add_resource(WaterschappenResource, "/api/waterschap/all")
api.add_resource(WatertypeResource, "/api/watertype/id/<int:id>")
api.add_resource(WatertypesResource, "/api/watertype/all")
api.add_resource(WewResource, "/api/wew")
api.add_resource(WewValueResource, "/api/wew/value")
api.add_resource(TaxonWewValueResource, "/api/wew/value/taxon/<int:taxonId>")
api.add_resource(WewAdminResource, '/api/wew/admin/isEmpty')
api.add_resource(WewAdminEmptyResource, '/api/wew/admin/emptyAll')
api.add_resource(WewFactorResource, "/api/wew/factor")
api.add_resource(UserGroupResource, "/api/usergroup/id/<int:id>")
api.add_resource(UserGroupsResource, "/api/usergroup/all")
api.add_resource(MapResource, "/api/markers/filter")
api.add_resource(SampleYearsResource, "/api/sample/getyears")

# Application runner where you can choose a portnumber
if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)