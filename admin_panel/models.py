from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    
    def __str__(self):
        return self.org_name

class Organization(models.Model):
    org_name = models.CharField(max_length=255)

    def __str__(self):
        return self.org_name

class OrganizationUser(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
        
    def __str__(self):
        return self.user.username

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
        
    def __str__(self):
        return self.customer_name

class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    pay_rate = models.DecimalField(max_digits=10, decimal_places=2)
        
    def __str__(self):
        return self.project_name

class ProjectManager(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.user.username


class ProjectTeamMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.project.project_name + " - " + self.user.username

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    start_date = models.DateField()
    due_date = models.DateField()
    count = models.DecimalField(max_digits=10, decimal_places=2) #pay_rate * count = received payment
        
    def __str__(self):
        return self.task_name

class Stage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=255)
    pay_scale = models.DecimalField(max_digits=10, decimal_places=2) #received payment * pay_scale = payment to team members at each stage
        
    def __str__(self):
        return self.stage_name

class TaskStage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.task.task_name + " - " + self.stage.stage_name

class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        
    def __str__(self):
        return self.task.task_name + " - " + self.user.username

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
        
    def __str__(self):
        return self.user.username + " - " + self.task.task_name + " - " + self.amount
