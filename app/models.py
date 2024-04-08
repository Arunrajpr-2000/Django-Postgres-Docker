from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Source(models.Model):
    source_name=models.CharField(max_length=100)
    source_type=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.source_name

class Campaign(models.Model):
    name=models.CharField(max_length=100)
    organization=models.IntegerField(default=2000)
    created_ts = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)
    organization=models.IntegerField(default=2000)
    group_name=models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return self.name


class Lead(models.Model):
    name = models.CharField(max_length=100)
    mobile= models.CharField(max_length=10)
    email = models.EmailField(max_length=70,blank=True,unique=True)
    favorite = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)
    notes=models.CharField(max_length=300)
    lead_source= models.ForeignKey(Source,on_delete=models.DO_NOTHING,null=True)
    campaign= models.ForeignKey(Campaign, on_delete=models.DO_NOTHING,null=True)
    tags= models.ManyToManyField(Tag,blank=True)



    def __str__(self) -> str:
        return self.name
    

class LeadFollowUp(models.Model):
    note=models.CharField(max_length=300)
    lead_id=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='lead_followup')
    date_time= models.DateTimeField()

    def __str__(self) -> str:
        return self.lead_id
    

class Requirement(models.Model):

    BHK_CHOICE = [
    ('1 BHK', '1 BHK'),
    ('1.5 BHK', '1.5 BHK'),
    ('2 BHK', '2 BHK'),
    ('2.5 BHK', '2.5 BHK'),
    ('3 BHK', '3 BHK'),
    ('4 BHK', '4 BHK'),
    ('5 BHK', '5 BHK'),
    ]

    property_type=models.CharField(max_length=100)
    budget = models.BigIntegerField()
    property_status= models.CharField(max_length=200)
    booking_in_date=models.DateTimeField(auto_now_add=True)
    purchase_reason = models.CharField(max_length=100)
    loan_required= models.BooleanField(default=False)
    notes=models.CharField(max_length=300)
    lead_id=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='lead_requirement')
    bhk = ArrayField(models.CharField(max_length=20, choices=BHK_CHOICE), null=True, blank=True,default=list)
    size = ArrayField(models.IntegerField(),null=True,blank=True,default = list)
    location= ArrayField(models.CharField(),null=True,blank=True,default=list)



class Project(models.Model):
    title= models.CharField(max_length=300)
    type=models.CharField(max_length=200)
    price_range_max= models.BigIntegerField()
    price_range_min= models.BigIntegerField()

    def __str__(self) -> str:
        return self.title


class Booking(models.Model):
    booking_date= models.DateTimeField(auto_now_add=True)
    booking_amount= models.BigIntegerField()
    note=models.CharField(max_length=300)
    cancelled= models.BooleanField(default=False)
    lead_id=models.ForeignKey(Lead,on_delete=models.CASCADE, blank=True, null=True)
    project_id=models.ForeignKey(Project,on_delete=models.CASCADE, blank=True, null=True)


class Closure(models.Model):
    closure_date= models.DateTimeField(auto_now_add=True)
    sale_amount= models.BigIntegerField()
    note=models.CharField(max_length=300)
    lead_id=models.OneToOneField(Lead,on_delete=models.CASCADE, blank=True, null=True)
    project_id=models.OneToOneField(Project,on_delete=models.CASCADE, null=True,related_name='project')  

    def __str__(self):
        return self.lead_id


class ProjectMatch(models.Model):
    add_to_cma = models.BooleanField(default =False)
    project_id =models.ForeignKey(Project,on_delete=models.CASCADE,null=True,related_name='project_id')
    lead_id = models.ForeignKey(Lead,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.lead_id




