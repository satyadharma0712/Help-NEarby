from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password

# Create your views here.
def home(request):
    campaigns = Campaign.objects.all()
    doctors = SignupDOCTORS.objects.all()
    consultation = ConsultationBooking.objects.all()
    consultation_count = ConsultationBooking.objects.all().count()
    if "user_id" in request.session:
        return render(request, "home.html", {
            "email": "set",
            "campaigns": campaigns,
            "doctors": doctors,
            "consultation": consultation,
            "consultation_count": consultation_count,
        })
    else:
        return render(request, "home.html",{
            "campaigns": campaigns,
            "doctors": doctors,
            "consultation": consultation,
        })

def register(request):
    return render(request, "select.html")

def signupCDA(request):
    if "user_id" in request.session:
        return redirect("../citizen_dashboard", {
            "email": request.session.get("email")
        })
    else:
        if request.method == "POST":
            name = request.POST["name"]
            phone = request.POST["mobile"]
            email = request.POST["email"]
            password = request.POST["password"]

            if SignupCDA.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect("")

            # ✅ Save data with hashed password
            signup = SignupCDA(
                full_name=name,
                mobile_number=phone,
                email=email,
                password=make_password(password)
            )
            signup.save()

            messages.success(request, "Account created successfully!")
            return redirect("../../loginCDA/")
    return render(request, "signupCDA.html")

def signinADMIN(request):
    return render(request, "signinADMIN.html")

def loginCDA(request):
    if "user_id" in request.session:
        return redirect("../citizen_dashboard", {
            "email": request.session.get("email")
        })
    else:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            try:
                user = SignupCDA.objects.get(email=email)   # get user by email
            except SignupCDA.DoesNotExist:
                messages.error(request, "Invalid email or password")
                return redirect("/")

            # ✅ check hashed password
            if check_password(password, user.password):
                # store user session
                request.session["user_id"] = user.id
                request.session["user_name"] = user.full_name
                messages.success(request, "Login successful!")
                return redirect("../citizen_dashboard")   # redirect to dashboard/home
            else:
                messages.error(request, "Invalid email or password")
                return redirect("/")

    return render(request, "loginCDA.html")

def citizen_dashboard(request):
    if "user_id" in request.session:
        return render(request, "citizendashboard.html", {
            "email": request.session.get("email")
        })
    else:
        return redirect("../")
    
def logout(request):
    request.session.flush()
    return redirect("../")

def signupDOCTORS(request):
    if "user_id" in request.session:
        return redirect("../../doctors", {
            "email": request.session.get("email")
        })
    else:
        if request.method == "POST":
            name = request.POST["name"]
            email = request.POST["email"]
            password = request.POST["password"]
            specialisation = request.POST["specialisation"]
            experience = request.POST["experience"]
            ngo = request.POST["ngo"]

            if SignupDOCTORS.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect("")

            # ✅ Save data with hashed password
            signup = SignupDOCTORS(
                full_name=name,
                email=email,
                password=make_password(password),
                specialisation = specialisation,
                experience = experience,
                ngo = ngo,
            )
            signup.save()

            messages.success(request, "Account created successfully!")
            return redirect("../../loginDOCTORS/")
    return render(request, "signupDOCTORS.html")

def loginDOCTORS(request):
    if "user_id" in request.session:
        return redirect("../doctors", {
            "email": request.session.get("email")
        })
    else:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            try:
                user = SignupDOCTORS.objects.get(email=email)   # get user by email
            except SignupDOCTORS.DoesNotExist:
                messages.error(request, "Invalid email or password")
                return redirect("loginDOCTORS")

            # ✅ check hashed password
            if check_password(password, user.password):
                # store user session
                request.session["user_id"] = user.id
                request.session["user_name"] = user.full_name
                messages.success(request, "Login successful!")
                return redirect("../doctors")   # redirect to dashboard/home
            else:
                messages.error(request, "Invalid email or password")
                return redirect("/")

    return render(request, "loginDOCTORS.html")

def doctors(request):
    if "user_id" in request.session:
        return render(request, "doctors.html", {
            "email": request.session.get("email")
        })
    else:
        return redirect("../")
    
def signupNGO(request):
    if "user_id" in request.session:
        return redirect("../../ngo", {
            "email": request.session.get("email")
        })
    else:
        if request.method == "POST":
            name = request.POST["name"]
            address = request.POST["address"]
            website = request.POST["website"]
            mobile = request.POST["mobile"]
            email = request.POST["email"]
            password = request.POST["password"]

            if SignupNGO.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect("")

            # ✅ Save data with hashed password
            signup = SignupNGO(
                full_name=name,
                address = address,
                website = website,
                mobile = mobile,
                email=email,
                password=make_password(password),
            )
            signup.save()

            messages.success(request, "Account created successfully!")
            return redirect("../../loginNGO/")
    return render(request, "signupNGO.html")

def loginNGO(request):
    if "user_id" in request.session:
        return redirect("../ngo", {
            "email": request.session.get("email")
        })
    else:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            try:
                user = SignupNGO.objects.get(email=email)   # get user by email
            except SignupNGO.DoesNotExist:
                messages.error(request, "Invalid email or password")
                return redirect("loginDOCTORS")

            # ✅ check hashed password
            if check_password(password, user.password):
                # store user session
                request.session["user_id"] = user.id
                request.session["user_name"] = user.full_name
                messages.success(request, "Login successful!")
                return redirect("../ngo")   # redirect to dashboard/home
            else:
                messages.error(request, "Invalid email or password")
                return redirect("/")

    return render(request, "loginNGO.html")

def ngo(request):
    if "user_id" in request.session:
        return render(request, "ngo.html", {
            "email": request.session.get("email")
        })
    else:
        return redirect("../")

#------------------------------ BELOW CITIZEN SECTION ----------------------------
def telemedicine(request):
    if "user_id" in request.session:
        doctors = SignupDOCTORS.objects.all()
        if request.method == "POST":
            name = request.POST["name"]
            phone = request.POST["phone"]
            doctor = request.POST["doctor"]
            reason = request.POST["reason"]
            diagnosis_report = request.FILES.get("diagnosis_report")  # handle file upload

            # Save data into the model
            booking = ConsultationBooking(
                name=name,
                phone=phone,
                doctor=doctor,
                reason=reason,
                diagnosis_report=diagnosis_report
            )
            booking.save()

            messages.success(request, "Your consultation has been booked successfully!")
            return redirect("../telemedicine/")  # redirect to homepage or a success page

        return render(request, "telemedicine.html", {"doctors": doctors})  # your template name
    else:
        return redirect("../")

def campaign(request):
    if "user_id" in request.session:
        campaign = Campaign.objects.all()
        return render(request, "campaign.html", {
            "campaign": campaign
        })
    else:
        return redirect("../")
    
def reportcrisis(request):
    if "user_id" in request.session:
        success = False
        if request.method == "POST":
            report_type = request.POST.get("report_type")
            location = request.POST.get("location")
            details = request.POST.get("details")

            # Save into DB
            HealthReport.objects.create(
                report_type=report_type,
                location=location,
                details=details
            )
            success = True
            return redirect("../")
        return render(request, "crisis.html", {"success": success})
    else:
        return redirect("../")

def track(request):
    if "user_id" in request.session:
        user = SignupCDA.objects.filter(id=request.session["user_id"]).first()
        request.session["phone"] = user.mobile_number
        # citizen_id = request.session.get("phone")
        appointments = ConsultationBooking.objects.filter(phone=user.mobile_number)
       
    #     doc_id = appointments.doctor
    #     doctor = SignupDOCTORS.objects.filter(id=doc_id)
    #     return render(request, "track.html", {
    #         "appointments": appointments,
    #         "doctor": doctor,
    #         })
    # else:
    #     return redirect("../")
        appointments_with_doctors = []
        for appt in appointments:
            doctor = SignupDOCTORS.objects.get(id=appt.doctor)
            appointments_with_doctors.append({
                "appointment": appt,
                "doctor": doctor,
            })

        return render(request, "track.html", {
            "appointments_with_doctors": appointments_with_doctors,
        })
    else:
        return redirect("../")
    
#----------------- BELOW DOCTORS SECTION ---------------------------#  
def appointments(request):
    if "user_id" in request.session:
        doctor_id = request.session.get("user_id")
        appointments = ConsultationBooking.objects.filter(doctor=doctor_id).order_by('-created_at')
        if request.method == "POST":
            booking_id = request.POST.get("booking_id")
            gmeet_link = request.POST.get("gmeet_link")
            schedule_date = request.POST.get("schedule_date")
            booking = get_object_or_404(ConsultationBooking, id=booking_id, doctor=doctor_id)
            booking.gmeet_link = gmeet_link
            booking.schedule_date = schedule_date
            booking.save()
            return redirect("../appointments")  # reload page after saving

        return render(request, "appointment.html", {
            "appointments": appointments
        })
    else:
        return redirect("../")
    
#-----------------------------BELOW NGO SECTIONS-----------------------------------
def createcampaign(request):
    if "user_id" in request.session:
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            date = request.POST.get('date')
            location = request.POST.get('location')
            campaign_type = request.POST.get('type')

            # Basic validation (optional but recommended)
            if not all([title, description, date, location, campaign_type]):
                messages.error(request, "All fields are required.")
                return render(request, 'create_campaign.html')

            # Save to the database
            Campaign.objects.create(
                title=title,
                description=description,
                date=date,
                location=location,
                type=campaign_type
            )

            messages.success(request, "Campaign created successfully!")
            return redirect('../')
        return render(request, "createcampaign.html", {
            "email": request.session.get("email")
        })
    else:
        return redirect("../")
    
def overview(request):
    if "user_id" in request.session:
        campaign = Campaign.objects.all()
        return render(request, "overview.html", {
            "campaign": campaign
        })
    else:
        return redirect("../")
    
def ngoMonitor(request):
    if "user_id" in request.session:
        user = SignupCDA.objects.filter(id=request.session["user_id"]).first()
        request.session["phone"] = user.mobile_number
        # citizen_id = request.session.get("phone")
        appointments = ConsultationBooking.objects.filter(phone=user.mobile_number)
       
    #     doc_id = appointments.doctor
    #     doctor = SignupDOCTORS.objects.filter(id=doc_id)
    #     return render(request, "track.html", {
    #         "appointments": appointments,
    #         "doctor": doctor,
    #         })
    # else:
    #     return redirect("../")
        appointments_with_doctors = []
        for appt in appointments:
            doctor = SignupDOCTORS.objects.get(id=appt.doctor)
            total_appointments = ConsultationBooking.objects.filter(doctor=appt.doctor).count()
            appointments_with_doctors.append({
                "appointment": appt,
                "doctor": doctor,
                "total_appointments": total_appointments,
            })

        return render(request, "ngoMonitor.html", {
            "appointments_with_doctors": appointments_with_doctors,
        })
    else:
        return redirect("../")
    

#----------------------------ADMIN SECTION BELOW--------------------------------

def loginADMIN(request):
    if "user_id" in request.session:
        return redirect("../vaidya_admin", {
            "email": request.session.get("email")
        })
    else:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            try:
                user = Admin.objects.get(email=email)   # get user by email
            except Admin.DoesNotExist:
                messages.error(request, "Invalid email or password")
                return redirect("loginADMIN")

            # ✅ check hashed password
            if check_password(password, user.password):
                # store user session
                request.session["user_id"] = user.id
                request.session["user_name"] = user.full_name
                messages.success(request, "Login successful!")
                return redirect("../vaidya_admin")   # redirect to dashboard/home
            else:
                messages.error(request, "Invalid email or password")
                return redirect("/")

    return render(request, "loginADMIN.html")


def VaidyaAdmin(request):
    if "user_id" in request.session:
        return render(request, "admin.html", {
            "email": request.session.get("email")
        })
    else:
        return redirect("../")
    
def usermanagement(request):
    if "user_id" in request.session:
        return render(request, "usermanagement.html", {
            "email": request.session.get("email")
        })
    else:
        return redirect("../")
    
def adminappoint(request):
    if "user_id" in request.session:
        return render(request, "adminappoint.html", {
            "email": request.session.get("email")
        })
    else:
        return redirect("../")
    
def admincampaign(request):
    if "user_id" in request.session:
        return render(request, "admincampaign.html", {
            "email": request.session.get("email")
        })
    else:
        return redirect("../")
    
def admincomplain(request):
    if "user_id" in request.session:
        return render(request, "complain.html", {
            "email": request.session.get("email")
        })
    else:
        return redirect("../")
    
def adminUser(request):
    if "user_id" in request.session:
        return render(request, "adminUser.html", {
            "email": request.session.get("email")
        })
    else:
        return redirect("../")