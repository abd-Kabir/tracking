# class GroupPermission(BasePermission):
#     def has_permission(self, request, view):
#         # view.queryset.model._meta.app_label
#         group_obj = request.user.groups.first()
#         if group_obj:
#             groups_permissions = Group.objects.get(name=group_obj.name).permissions.all()
#             for permission in groups_permissions:
#                 if request.method in view.allowed_methods and permission.content_type.app_label == view.queryset.model._meta.app_label:
#                     return True
#         return False