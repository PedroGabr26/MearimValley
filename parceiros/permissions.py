from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminEditOrReadOnly(BasePermission):
    """
    Permite apenas leitura para qualquer usuário.
    Somente admins podem criar, editar ou deletar.
    """
    def has_permission(self, request, view):
        # SAFE_METHOD = ['GET','OPTIONS','HEAD']
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
    

class IsAdminGetorPost(BasePermission):
    """
    Permite apenas leitura e criação para qualquer usuário.
    Somente admins podem editar ou deletar.
    """
    def has_permission(self, request, view):
        # SAFE_METHOD = ['GET','OPTIONS','HEAD']
        if request.method in SAFE_METHODS or request.method == "POST":
            return True
        return request.user and request.user.is_staff