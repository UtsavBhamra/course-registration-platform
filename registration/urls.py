from django.urls import path
from .views import home,admin_create_student,admin_create_faculty,course_details,view_cart,add_to_cart,remove_from_cart,request_approval,manage_approvals,approve_students,admin_view_students,admin_view_faculty,admin_view_courses,admin_create_course,admin_delete_courses

urlpatterns = [
    path('home/',home,name='home'),
    path('view_cart/',view_cart,name="view_cart"),
    path('add_to_cart/<int:code>',add_to_cart,name="add_to_cart"),
    path('remove_from_cart/<int:code>',remove_from_cart,name="remove_from_cart"),
    path('request_approval/',request_approval,name="request_approval"),
    path('manage_approvals/<int:code>',manage_approvals,name="manage_approvals"),
    path('approve_students/<int:code>/<int:id>',approve_students,name="approve_students"),
    path('admin_create_students/',admin_create_student,name="admin_create_student"),
    path('admin_create_faculty/',admin_create_faculty,name="admin_create_faculty"),
    path('admin_create_course/',admin_create_course,name="admin_create_course"),
    path('admin_view_students/',admin_view_students,name="admin_view_students"),
    path('admin_view_faculty/',admin_view_faculty,name="admin_view_faculty"),
    path('admin_view_courses/',admin_view_courses,name="admin_view_courses"),
    path('admin_delete_courses/<int:code>',admin_delete_courses,name="admin_delete_courses"),
    path("course_details/<int:code>",course_details,name="course_details"),
]