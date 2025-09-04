
class IsAuthOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view,obj):
        if request.user.is_authenticated:
            return request.user.is_authenticated