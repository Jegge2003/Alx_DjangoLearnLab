from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden  # ✅ Handle unauthorized access

def is_admin(user):
    """Check if user is an Admin"""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin, login_url='/login/')  # ✅ Redirects unauthorized users to login
def admin_dashboard(request):
    if not is_admin(request.user):  # Extra safeguard
        return HttpResponseForbidden("You are not authorized to access this page.")
    return render(request, 'relationship_app/admin_view.html', {'user': request.user})
