from django.shortcuts import render, redirect
from .forms import AlumniRegistrationForm
from .models import AlumniRegistration


def alumni_registration_view(request):
    if request.method == "POST":
        form = AlumniRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("alumni_success")
        else:
            print(form.errors)
    else:
        form = AlumniRegistrationForm()

    return render(
        request,
        "mainapp/dashboard.html",
        {"form": form}
    )



def alumni_success_view(request):
    return render(request, "mainapp/success.html")

from django.views.generic import ListView



class SaudhiApproveList(ListView):
    model = AlumniRegistration
    template_name = "mainapp/saudhi_approve.html"
    context_object_name = "saudhi"
    paginate_by = 10

    def get_queryset(self):
        return (
            AlumniRegistration.objects
            .filter(country="Saudi Arabia", hr_approved=True)
            .order_by("-created_at")
        )
    
class KuwaitApprovedList(ListView):
    model = AlumniRegistration
    template_name = "mainapp/kuwait.html"
    context_object_name = "kuwait"
    paginate_by = 10
    
    def get_queryset(self):
        return (
            AlumniRegistration.objects.filter(country="Kuwait",
                                              hr_approved=True).order_by("-created_at")
            )
        
class OmanApprovedList(ListView):
    model = AlumniRegistration
    template_name = "mainapp/oman.html"
    context_object_name = "oman"
    paginate_by = 10
    
    def get_queryset(self):
        return (
            AlumniRegistration.objects.filter(country="Oman",hr_approved=True).order_by("-created_at")
            )


class QatarApprovedList(ListView):
    model = AlumniRegistration
    template_name = "mainapp/qatar.html"
    context_object_name = "qatar"
    paginate_by = 10
    
    def get_queryset(self):
        return (
            AlumniRegistration.objects.filter(country="Qatar",hr_approved=True).order_by("-created_at")
            )
        


class UaeApprovedList(ListView):
    model = AlumniRegistration
    template_name = "mainapp/uae.html"
    context_object_name = "uae"
    paginate_by = 10
    
    def get_queryset(self):
        return AlumniRegistration.objects.filter(country="United Arab Emirates",hr_approved=True)  # First value
            


class BahrainApprovedList(ListView):
    model = AlumniRegistration
    template_name = "mainapp/bahrain.html"
    context_object_name = "bahrain"
    paginate_by = 10
    
    def get_queryset(self):
        return (
            AlumniRegistration.objects.filter(country="Bahrain",hr_approved=True).order_by("-created_at")
            )
        





class All_Registered_Employee_list(ListView):
    model = AlumniRegistration
    template_name = "mainapp/total_employee.html"
    context_object_name = 'total_employee'
    # paginate_by = 10

    def get_queryset(self):
        return AlumniRegistration.objects.all().order_by("-created_at")
    






from django.views.generic.edit import UpdateView

class Conformation_tick(UpdateView):
    model = AlumniRegistration
    fields = []

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.conform_register = True
        self.object.save()


        return redirect(request.META.get('HTTP_REFERER'))


    




from django.views.generic import DetailView
from .models import AlumniRegistration

class AlumniDetailView(DetailView):
    model = AlumniRegistration
    template_name = "mainapp/employee_detail.html"
    context_object_name = "employee"



class HR_Verification(ListView):
    model = AlumniRegistration
    template_name = "mainapp/hr_verfication.html"
    context_object_name = "hr_approve"
    # paginate_by = 10

    def get_queryset(self):
        return AlumniRegistration.objects.filter(
            hr_approved=False,
        ).order_by("-id")



class Hr_Verification_button(UpdateView):
    model = AlumniRegistration
    fields = []

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.hr_approved = True
        self.object.save()


        return redirect('hr_verfication')
    



