from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        print(request.user.role)
        return request.user.role.lower()=='admin'

class IsMentor(BasePermission):
    def has_permission(self, request, view):
        if request.user.role.lower()=='mentor':
            return request.method =='POST' or request.method in SAFE_METHODS
        return request.user.role.lower()=='admin'
        
    
     