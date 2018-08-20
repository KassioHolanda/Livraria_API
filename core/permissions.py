from rest_framework import permissions


class isLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            return request.user.tipo_usuario == 'BIBLIOTECÁRIO'



class isLibrarianOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_anonymous:
            return False
        return request.user.tipo_usuario == 'BIBLIOTECÁRIO'


class isUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_anonymous:
            return False
        return request.user.tipo_usuario == 'USUÁRIO'
