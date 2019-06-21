from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from Database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from sqlalchemy import create_engine

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
api.add_resource(AdminResource, "/admin")
api.add_resource(AdminResetResource, "/admin/password")
api.add_resource(LoginUserResource, "/authenticate/login")
api.add_resource(UserChangePasswordResource, "/user/editpassword")
api.add_resource(CalculateResource, "/calculate/sample/<int:id>")
api.add_resource(SampleTaxonResource, "/calculate/sample2/<int:id>") # new sample
api.add_resource(ReferencetaxonResourceValue, "/calculate/reference2/<int:id>")
api.add_resource(CalulateReferenceResource, "/calculate/reference/<int:id>")
api.add_resource(LocationResource, "/location/id/<int:id>")
api.add_resource(LocationByCodeResource, "/location/code/<string:code>")
api.add_resource(LocationsResource, "/location/all")
api.add_resource(LocationByIds, "/location/ids")
api.add_resource(ReferenceResource, "/reference/<int:id>")
api.add_resource(ReferencesResource, "/reference")
api.add_resource(ReferenceByWatertypeResource, "/reference/watertype/<int:watertype_id>")
api.add_resource(ReferenceTaxonResource, "/admin/reference")
api.add_resource(SampleByLocationResource, "/sample/location/<int:locationId>")
api.add_resource(SampleResource, "/sample/<int:id>")
api.add_resource(SamplesResource, "/sample/all")
api.add_resource(RecentSamples, "/sample/recent/<int:count>")
api.add_resource(TaxonGroupResource, "/taxongroup/id/<int:id>")
api.add_resource(TaxonGroupsResource, "/taxongroup/all")
api.add_resource(TaxonByIdsResource, "/taxon/ids")
api.add_resource(TaxonFamilyResource, "/taxon/family/<int:id>")
api.add_resource(TaxonLevelResource, "/taxonlevel/id/<int:id>")
api.add_resource(TaxonLevelsResource, "/taxonlevel/all")
api.add_resource(TaxonResource, "/taxon/id/<int:id>")
api.add_resource(TaxonsResource, "/taxon/all")
api.add_resource(TaxonFindResource, "/taxon/findOrCreate")
api.add_resource(UserResource, "/user/id/<int:id>")
api.add_resource(WaterschapResource, "/waterschap/id/<int:id>")
api.add_resource(WaterschappenResource, "/waterschap/all")
api.add_resource(WatertypeResource, "/watertype/id/<int:id>")
api.add_resource(WatertypesResource, "/watertype/all")
api.add_resource(WewResource, "/wew")
api.add_resource(WewValueResource, "/wew/value")
api.add_resource(TaxonWewValueResource, "/wew/value/taxon/<int:taxonId>")
api.add_resource(WewAdminResource, '/wew/admin/isEmpty')
api.add_resource(WewAdminEmptyResource, '/wew/admin/emptyAll')
api.add_resource(WewFactorResource, "/wew/factor")
api.add_resource(UserGroupResource, "/usergroup/id/<int:id>")
api.add_resource(UserGroupsResource, "/usergroup/all")
api.add_resource(MapResource, "/markers/filter")
api.add_resource(SampleYearsResource, "/sample/getyears")

@app.route("/")
def hello():
    engine = create_engine("mysql://debian-sys-maint:UROX1VQsnwcq68Lo@127.0.0.1/waterscan")
    inspector = inspect(engine)
    for table_name in inspector.get_table_names():
        for column in inspector.get_columns(table_name):
            a = "Column: %s" % column['name'] 
            #print("Column: %s" % column['name'])
    return a
    #db2 = SQLAlchemy(app)
    #try:
    #    db2.session.query("1").from_statement("SELECT 1").all()
    #    return '<h1>It works.</h1>'
    #except Exception as e:
    #    return e
        #return '<h1>Something is broken.</h1>'
    #return "<h1 style='color:blue'>Hello Thereee!</h1>"

# Application runner where you can choose a portnumber
if __name__ == "__main__":
    db.init_app(app)
    app.run(port=8080, debug=True)
