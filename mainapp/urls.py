from django.urls import path
from .views import *

urlpatterns = [
    path("", alumni_registration_view, name="alumni_register"),
    path("success/", alumni_success_view, name="alumni_success"),
    path('ksa/',SaudhiApproveList.as_view(),name="ksa"),
    path("saudi/approve/<int:pk>/",Conformation_tick.as_view(),name="confirm"),
    path("all_list/",All_Registered_Employee_list.as_view(),name="total_employee"),
    path("employee/<int:pk>/", AlumniDetailView.as_view(), name="employee_detail"),
    path("kuwait/",KuwaitApprovedList.as_view(),name="kuwait"),
    path("hr_verfication/",HR_Verification.as_view(),name="hr_verfication"),
    path("hr/approve/<int:pk>/",Hr_Verification_button.as_view(),name="hr_approval"),
    path('bahraain/',BahrainApprovedList.as_view(),name="bahrain"),
    path('omann/',OmanApprovedList.as_view(),name="oman"),
    path('unitedAe/',UaeApprovedList.as_view(),name="uae"),
    path('qatarr/',QatarApprovedList.as_view(),name="qatar"),


]
