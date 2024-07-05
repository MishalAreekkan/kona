from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# from django.contrib.auth.models import AbstractUser,Group, Permission
# from django.contrib.auth.models import Group,Permission
# from django.contrib.contenttypes.models import ContentType
from BookDetails.models import BedField

# class User(AbstractUser):
#     Hotel_Manager = 1
#     Receptionist = 2
#     customer = 3
      
#     ROLE_CHOICES = (
#         (Hotel_Manager, 'Hotel Manager'),
#         (Receptionist, 'Receptionist'),
#         (customer, 'customer'),
#     )
      
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,blank=True,null=True)
    
#     class Meta:
#         permissions = [
#             ("manage_hotel", "Can manage hotel"),
#             ("add_guest", "Can add guest"),
#             ("view_guest", "Can view guest"),
#             ("change_guest", "Can change guest"),
#             ("delete_guest", "Can delete guest"),
#         ]
        
        
#     def __str__(self):
#        return self.username


class MyUserManager(BaseUserManager):
    def create_user(self, email=None, username=None, password=None, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, username=None, password=None, **kwargs):
        user = self.create_user(email=email, username=username)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=150,null=True,blank=True)
    last_name = models.CharField(max_length=150,null=True,blank=True)
    password = models.CharField(max_length=150)
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=150, unique=True, null=True, blank=True)
    date_joined = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

   
class StayPics(models.Model):
    customer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    room = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    
    def __str__(self):
        return self.room




class DinePics(models.Model):
    
    LUNCH = 'Lunch'
    EVENING = 'Evening'
    DINNER = 'Dinner'
    
    meal_choices = [
        (LUNCH, 'Lunch'),
        (EVENING,'Evening'),
        (DINNER, 'Dinner')
    ]

    meal_time = models.CharField(max_length=10, choices=meal_choices)
    meal_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    
    def __str__(self):
        return self.name    



  
  
  
  
# hotel_manager_group,created = Group.objects.get_or_create(name='Hotel Manager')
# receptionist_group,created = Group.objects.get_or_create(name='Receptionist')
# staff_group,created = Group.objects.get_or_create(name='staff')


# manage_hotel =Permission.objects.get(name='manage_hotel')
# check_guest = Permission.objects.get(codename='check_guest') ####
# can_clean = Permission.objects.get(name = 'can_clean')


# hotel_manager_group.permissions.add(manage_hotel)
# receptionist_group.permissions.add(check_guest)
# staff_group.permissions.add(can_clean)


# user = User.objects.get(username = 'calix')
# user.groups.add(manage_hotel)


# dinner = DinePics(meal_type=DinePics.DINNER, start_time=time(18, 30), end_time=time(23, 0))








