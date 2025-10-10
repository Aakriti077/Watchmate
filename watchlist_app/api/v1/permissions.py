from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
        return False

class IsReviewUserOrReadOnly(BasePermission):
    def has_object_permission(self,request,view,obj):
        # if request.method.lower() == 'get':
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.user

