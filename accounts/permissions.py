from rest_framework.permissions import BasePermission, IsAuthenticated


class IsAuth(IsAuthenticated,BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated :
            return True
        return obj.user == request.user


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name='Author').exists() or request.user.type == 'Author'

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user.groups.filter(name='Author').exists() or request.user.type == 'Author' :
            return True
        return obj.user == request.user

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name='Administrator').exists() or request.user.type == 'Administrator'

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user.groups.filter(name='Administrator').exists() or request.user.type == 'Administrator':
            return True
        return obj.user == request.user


class IsReader(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name='Reader').exists() or request.user.type == 'Reader'

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user.groups.filter(name='Admin').exists() or request.user.type == 'Reader':
            return True
        return obj.user == request.user
