from rest_framework import serializers  
from .models import Lead,Source,Campaign,Tag,LeadFollowUp,Requirement,Project,Booking,Closure,ProjectMatch

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Source
        fields=('__all__')


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model=Campaign
        fields=('__all__')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=('__all__')



class LeadFollowUpSerializer(serializers.ModelSerializer):
    lead_name=serializers.SerializerMethodField()

    def get_lead_name(self,instance):
        if instance.lead_id is not None:
            return instance.lead_id.name
        return None
    
    class Meta:
        model = LeadFollowUp
        fields=('id','lead_id','lead_name','note','date_time')

        

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model= Requirement
        fields=('id','lead_id','property_type','budget','property_status','booking_in_date','purchase_reason','loan_required','notes','bhk','size','location')       
    
  

class BookingSerializer(serializers.ModelSerializer):

    project_name=serializers.SerializerMethodField()
    
    def get_project_name(self,instance):
        if instance.project_id is not None:
            return instance.project_id.title
        return None
    
    class Meta:
        model= Booking
        fields=('id','lead_id','project_id','project_name','booking_date','booking_amount','note','cancelled')


class ClosureSerializer(serializers.ModelSerializer):
    project_name=serializers.SerializerMethodField()
    
    def get_project_name(self, instance):
        if instance.project_id is not None:
            return instance.project_id.title
        return None
    
    class Meta:
        model=Closure
        fields=('id','lead_id','project_id','project_name','closure_date','sale_amount','note')



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','title','type','price_range_min','price_range_max')


class ProjectMatchSerializer(serializers.ModelSerializer):
    project_detail = ProjectSerializer(source='project_id', read_only=True) 
    booking = BookingSerializer(many=True,read_only = True,source='lead_id.booking_set')

    class Meta:
        model=ProjectMatch
        fields=('id','project_id','lead_id','add_to_cma','project_detail','booking')

class LeadSerializer(serializers.ModelSerializer):
    source_detail= SourceSerializer(source='lead_source',read_only=True)
    campaign_detail =CampaignSerializer(source='campaign',read_only=True)
    tag_details = TagSerializer(many=True,source='tags', read_only=True)
    lead_followup= LeadFollowUpSerializer(read_only=True,many=True)
    lead_requirement= RequirementSerializer(many=True,read_only=True)
    bookings = BookingSerializer(many=True, source='booking_set',read_only=True)
    closure = ClosureSerializer(read_only=True)
    project_match= ProjectMatchSerializer(many=True,source='projectmatch_set',read_only=True)


    class Meta:
        model= Lead
        fields=('id','name','mobile','email','favorite','new','created_ts','modified_ts','notes','lead_source','source_detail','campaign','campaign_detail','tags','tag_details','lead_followup','lead_requirement','bookings','closure','project_match') 






        