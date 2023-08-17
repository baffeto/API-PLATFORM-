from rest_framework import permissions

# Грубо говоря, обычные пользователи смогут смотреть на запись, но удалить ее смогут только администраторы
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # если метод безопасный - то даем доступ всем пользователям, а если нет - только администраторам
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)
    
# Только владелец магазина сможет изменять данные, остальные смогут только смотреть
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user


