from rest_framework import permissions


class RegisteredByGerenteOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.gerente == request.user


class IsGerenteOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            print(request.user.tipo_usuario)
            return True
        else:
            return request.user.tipo_usuario == 'GERENTE'


class IsClienteOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            print(request.user.tipo_usuario)
            return True
        else:
            return request.user.tipo_usuario == 'CLIENTE'