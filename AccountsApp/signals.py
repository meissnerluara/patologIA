# from django.db.models.signals import post_migrate
# from django.contrib.auth.management import create_permissions
# from django.contrib.auth.models import Group, Permission
# from django.dispatch import receiver

# @receiver(post_migrate)
# def create_groups_and_permissions(sender, **kwargs):
#     # Create the necessary groups
#     teacher_group, created = Group.objects.get_or_create(name='teacher')
#     student_group, created = Group.objects.get_or_create(name='student')
#     guest_group, created = Group.objects.get_or_create(name='guest')

#     # Create the necessary permissions
#     permission = Permission.objects.get(codename='can_view_teacher_pages')
#     teacher_group.permissions.add(permission)

#     permission = Permission.objects.get(codename='can_view_student_pages')
#     student_group.permissions.add(permission)

#     permission = Permission.objects.get(codename='can_view_guest_pages')
#     guest_group.permissions.add(permission)

#     # Ensure all the permissions are created
#     create_permissions(Group._meta.app_config, verbosity=0)

#     teacher_group.save()
#     student_group.save()
#     guest_group.save()