from django.contrib import admin
from .models import User, Organization, OrganizationUser, Customer, Project, ProjectManager, ProjectTeamMember, Task, Stage, TaskStage, TaskAssignment, Payment

admin.site.register(User)
admin.site.register(Organization)
admin.site.register(OrganizationUser)
admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(ProjectManager)
admin.site.register(ProjectTeamMember)
admin.site.register(Task)
admin.site.register(Stage)
admin.site.register(TaskStage)
admin.site.register(TaskAssignment)
admin.site.register(Payment)
