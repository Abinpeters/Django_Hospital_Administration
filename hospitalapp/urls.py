from django.urls import path,include
from . import views
urlpatterns = [
    path(route='home', view= views.homePageView, name='home'),
    path(route='admin', view= views.adminPageView, name='admin'),
    path(route='docdetails', view= views.docdetailsPageView, name='docdetails'),
    path(route='select-doctor', view= views.select_doctor, name='patdetails'),
    path(route='doclist', view= views.doclistPageView, name='doclist'),
    path(route="save",view =views.savedocView,name='save'),
    path(route='check', view= views.checkadminPageView, name='check'),
    path(route='save1', view= views.savepatView, name='save1'),
    path(route="delete/<int:docdetails_id>", view= views.deletedocview, name='deletedocview'),
    path(route="deletedpatview/<int:patdetails_id>", view= views.deletepatview, name='deletepatview'),
    path(route='patlist', view= views.patlistPageView, name='patlist'),
    path(route="<int:patient_id>",view=views.singlePatientView,name='getsinglepatient'),
    path(route="singleupdatepa/<int:patient_id>",view=views.updateSinglePatientView,name='updatesinglepatient'),
    path(route="singledeletepa/<int:patient_id>",view=views.deleteSinglePatientView,name='deletesinglepatient'),
    path(route= 'doctor', view= views.doctorPageView, name='doctor'),
    path(route= 'opatients/<int:patient_id>', view= views.opatientsPageView, name='opatients'),
    
    
]
