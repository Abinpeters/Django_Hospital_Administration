from django.shortcuts import render,redirect
from hospitalapp.models import Docdetails
from hospitalapp.models import Patdetails
from django.shortcuts import get_object_or_404

# Create your views here.
def homePageView(request):
    
    return render(request, 'home.html', {})
def adminPageView(request):
    
    return render(request, 'admin.html', {})

def docdetailsPageView(request):
    
    return render(request, 'docdetails.html', {})




def deletedocview(request,docdetails_id):
    docdetails = Docdetails.objects.filter(pk=docdetails_id)
    docdetails.delete()
    return redirect('doclist')


def deletepatview(request,patdetails_id):
    patdetails = Patdetails.objects.filter(pk=patdetails_id)
    patdetails.delete()
    return redirect('patlist')

def select_doctor(request):
    doctor=Docdetails.objects.all()
    context ={
        'alldoctors':doctor

    }
    return render(request=request,template_name='patdetails.html',context=context)






def doclistPageView(request):
    doctor=Docdetails.objects.all()
    context ={
        'alldoctors':doctor

    }
    return render(request=request,template_name='doclist.html',context=context)



def patlistPageView(request):
    patient=Patdetails.objects.all()
    context ={
        'allpatients':patient

    }
    return render(request=request,template_name='patlist.html',context=context)


def checkadminPageView(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        


        print("Userame: ",username)
        print("Password: ",password)
       
        if username =='abin' and password =='1234':

            return render(request,'admin.html',{})
        else:
            doctor = Docdetails.objects.filter(username=username, password=password).first()  # Get the first matching doctor
            if doctor:
                patients = Patdetails.objects.filter(doctor=doctor)
                context = {'allpatients': patients}
                return render(request=request, template_name='doctor.html', context=context)
            else:
                return render(request, 'home.html', {})






def opatientsPageView(request, patient_id):
    print("pK:",patient_id)
    # Retrieve the specific patient by its primary key or return a 404 error if not found
    patient = get_object_or_404(Patdetails, pk=patient_id)
    print("Patient:",patient)
    
    # Assuming you want to find doctors associated with the same patient
    doctors = get_object_or_404(Docdetails, name=patient.doctor)
    print("doctor:",doctors)
    

    if doctors:
        # Assuming you want to find patients associated with the same doctors
        patients = Patdetails.objects.filter(doctor=doctors)
        
        print("patients:",patients)
        context = {'allpatients': patients}
      # No doctors found, empty list
    
    return render(request=request, template_name='doctor.html', context=context)

       

    
def savedocView(request):
    if request.method == "POST":
        name= request.POST['name']
        specialized= request.POST['specialized']
        address= request.POST['address']
        number= request.POST['number']
        email= request.POST['email']
        username= request.POST['username']
        password= request.POST['password']


        print("Name: ",name)
        print("Specialized:",specialized)
        print("Address: ",address)
        print("Number: ",number)
        print("Email: ",email)
        print("Username: ",username)
        print("Password: ",password)
        docdetails=Docdetails(name=name,specialized=specialized,address=address,number=number,email=email,username=username,password=password)
        docdetails.save()
        return redirect("docdetails")
    


def savepatView(request):
    if request.method == "POST":
        name= request.POST['name']
        age= request.POST['age']
        doctor= request.POST['doctor']
        disease= request.POST['disease']
        address= request.POST['address']
        number= request.POST['number']
        email= request.POST['email']
        


        print("Name: ",name)
        print("Age: ",age)
        print("Doctor: ",doctor)
        print("disease:",disease)
        print("Address: ",address)
        print("Number: ",number)
        print("Email: ",email)
        
        patdetails=Patdetails(name=name,age=age,doctor=doctor,disease=disease,address=address,number=number,email=email)
        patdetails.save()
        return redirect("patdetails")
    

def singlePatientView(request,patient_id):
    patient=Patdetails.objects.get(pk=patient_id)
    context={
        'patient':patient
    }
    return render(request=request,template_name='singlepatient.html',context=context)


def updateSinglePatientView(request,patient_id):
    if request.method=="POST":

        name=request.POST['name']
        age=request.POST['age']
        disease=request.POST['disease']
        address=request.POST['address']
        number=request.POST['number']
        
        email=request.POST['email']
        feedback=request.POST['feedback']

        print("Name- ",name)
        print("Address- ",address)
        print("Email- ",email)

        patient=Patdetails.objects.get(pk=patient_id)
        patient.name=name
        patient.age=age
        patient.disease=disease
        patient.address=address
        patient.number=number
        patient.email=email
        patient.feedback=feedback

        patient.save()

        patient=Patdetails.objects.get(pk=patient_id)
        context={
            'patient':patient
                }
        return render(request=request,template_name='singlepatient.html',context=context)
def deleteSinglePatientView(request,patient_id):
    print(patient_id)
    patient=Patdetails.objects.filter(pk=patient_id)
    patient.delete()
    return redirect('doctor')
def doctorPageView(request):
    patients=Patdetails.objects.all()
    context={
            'allpatients':patients
            }
    return render(request=request,template_name='doctor.html',context=context)



    
    


    




