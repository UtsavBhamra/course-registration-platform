from django.shortcuts import render,redirect
from .models import Course,Cart
from accounts.models import CustomUser,Student,Faculty,Admin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserCreationForm,StudentCreateForm,FacultyCreateForm
from .forms import CourseCreationForm

@login_required
def home(request):
    if request.user.user_type=="ST":
        user_ref = request.user
        course_list_requested = Course.objects.filter(requested_students=user_ref.student)
        course_list_accepted = Course.objects.filter(accepted_students=user_ref.student)
        all_courses = Course.objects.all()
        return render(request,"students/home.html",{"user_ref":user_ref,"course_list_requested":course_list_requested,"course_list_accepted":course_list_accepted,"all_courses":all_courses})
    elif request.user.user_type=="FA":
        faculty_user = request.user
        course_list = Course.objects.filter(instructors = faculty_user.faculty)
        return render(request,"faculty/home.html",{"faculty_user":faculty_user,"course_list":course_list})
    elif request.user.user_type=="AD":
        admin_user = request.user
        course_list = Course.objects.all()
        return render(request,"admin/home.html",{"admin_user":admin_user,"course_list":course_list})
    
@login_required
def view_cart(request):
    if request.user.user_type=="ST":
        student_user = request.user.student
        cart_obj = Cart.objects.get(student = student_user)
        courses = cart_obj.courses.all()
        return render(request,"students/course_cart.html",{"cart_obj":cart_obj,"courses":courses})

@login_required
def add_to_cart(request,code):
    if request.user.user_type=="ST":
        course = Course.objects.get(code=code)
        student_user = request.user.student
        
        cart,created = Cart.objects.get_or_create(student = student_user)
        cart.courses.add(course)
        cart.save()

        return redirect("view_cart")
    
@login_required
def remove_from_cart(request,code):
    if request.user.user_type=="ST":
        course = Course.objects.get(code=code)
        student_user = request.user.student
        cart_item = Cart.objects.get(student = student_user)
        cart_item.courses.remove(course)
        return redirect("view_cart")
    
@login_required
def request_approval(request):
    if request.user.user_type=="ST":
        student_user = request.user.student
        cart_obj = Cart.objects.get(student = student_user)
        courses = cart_obj.courses.all()
        for course in courses:
            course.requested_students.add(student_user)
            cart_obj.courses.remove(course)
        return redirect("home")
    
@login_required
def manage_approvals(request,code):
    if request.user.user_type=="FA":
        course = Course.objects.get(code=code)
        req_students = course.requested_students.all()
        acc_students = course.accepted_students.all()
        return render(request,"faculty/manage_approvals.html",{"course":course,"req_students":req_students,"acc_students":acc_students})
    
@login_required
def approve_students(request,code,id):
    if request.user.user_type=="FA":
        course = Course.objects.get(code=code)
        student = Student.objects.get(student_id=id)
        course.requested_students.remove(student)
        course.accepted_students.add(student)
        course.save()
        return redirect("manage_approvals",code=course.code)

@login_required
def admin_create_student(request):
    if request.user.user_type == "AD":
        if request.method=="POST":
            user_form = CustomUserCreationForm(request.POST)
            student_form = StudentCreateForm(request.POST)
            if user_form.is_valid():
                user = user_form.save()
                if student_form.is_valid():
                    student = student_form.save(commit=False)
                    student.student_user = user
                    student.save()
                    return redirect("home")
        else:
            user_form = CustomUserCreationForm()
            student_form = StudentCreateForm()
        return render(request,'admin/admin_create_student.html',{"user_form":user_form,"student_form":student_form})
    else:
        return HttpResponse("Access denied - not an admin")
    
@login_required
def admin_create_faculty(request):
    if request.user.user_type == "AD":
        if request.method=="POST":
            user_form = CustomUserCreationForm(request.POST)
            faculty_form = FacultyCreateForm(request.POST)
            if user_form.is_valid():
                user = user_form.save()
                if faculty_form.is_valid():
                    faculty = faculty_form.save(commit=False)
                    faculty.faculty_user = user
                    faculty.save()
                    return redirect("home")
        else:
            user_form = CustomUserCreationForm()
            faculty_form = FacultyCreateForm()
        return render(request,'admin/admin_create_faculty.html',{"user_form":user_form,"faculty_form":faculty_form})
    else:
        return HttpResponse("Access denied - not an admin")
    
@login_required
def admin_create_course(request):
    if request.user.user_type == "AD":
        if request.method=="POST":
            course_form = CourseCreationForm(request.POST)
            if course_form.is_valid():
                course_form.save()
                return redirect("admin_view_courses")
        else:
            course_form = CourseCreationForm()
        return render(request,'admin/admin_create_course.html',{"course_form":course_form})
    
@login_required
def admin_view_students(request):
    if request.user.user_type == "AD":
        students = Student.objects.all()
        return render(request,'admin/view_all_students.html',{"students":students})
    
@login_required
def admin_view_faculty(request):
    if request.user.user_type == "AD":
        faculty = Faculty.objects.all()
        return render(request,'admin/view_all_faculty.html',{"faculty":faculty})
    
@login_required
def admin_view_courses(request):
    if request.user.user_type == "AD":
        course_list = Course.objects.all()
        return render(request,'admin/view_all_courses.html',{"course_list":course_list})
    
@login_required
def admin_delete_courses(request,code):
    if request.user.user_type == "AD":
        course = Course.objects.get(code=code)
        course.delete()
        return redirect("admin_view_courses")

@login_required
def course_details(request,code):
    course = Course.objects.get(code=code)
    return render(request,"courses/course_details.html",{"course":course})


