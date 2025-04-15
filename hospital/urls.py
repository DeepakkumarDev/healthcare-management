# from django.urls import path,include 
# from rest_framework_nested import routers
# from .import views 


# router = routers.DefaultRouter()
# router.register('doctors',views.DoctorViewSet,basename='doctors')
# router.register(r'patients', views.PatientViewSet, basename='patients')

# patients_router = routers.NestedDefaultRouter(router, r'patients', lookup='patient')
# patients_router.register(r'records', views.MedicalRecordViewSet, basename='patient-records')


# # urlpatterns = router.urls + patients_router.urls  


# # Final urlpatterns
# urlpatterns = [
#     path('', include(router.urls)),
#     path('', include(patients_router.urls)),
#     path('patients/records/add/', views.AddMedicalRecordView.as_view(), name='add-medical-record'),
# ]


from django.urls import path, include
from rest_framework_nested import routers
from . import views



# class NoRootRouter(routers.DefaultRouter):
#     include_root_view = False

# router = NoRootRouter()


router = routers.DefaultRouter()
router.register('doctors', views.DoctorViewSet, basename='doctors')
router.register('patients', views.PatientViewSet, basename='patients')

patients_router = routers.NestedDefaultRouter(router, r'patients', lookup='patient')
patients_router.register('records', views.MedicalRecordViewSet, basename='patient-records')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(patients_router.urls)),
    path('patients/records/add/', views.AddMedicalRecordView.as_view(), name='add-medical-record'),
]
