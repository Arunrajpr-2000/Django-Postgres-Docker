from rest_framework import generics, filters
from .serializers import LeadSerializer,SourceSerializer,CampaignSerializer,TagSerializer,LeadFollowUpSerializer,RequirementSerializer,ProjectSerializer,BookingSerializer,ClosureSerializer,ProjectMatchSerializer
from .models import Lead,Source,Campaign,Tag,LeadFollowUp,Requirement,Project,Booking,Closure,ProjectMatch
from django_filters import rest_framework as filter 
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework.response import Response
# from rest_framework.pagination import PageNumberPagination 


# Create your views here.

class LeadListView(generics.ListCreateAPIView):
    serializer_class=LeadSerializer
    queryset = Lead.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset



class LeadDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=LeadSerializer
    queryset = Lead.objects.all()

class SourceView(generics.ListCreateAPIView):
    serializer_class=SourceSerializer
    queryset = Source.objects.all()

class CampaignView(generics.ListCreateAPIView):
    serializer_class=CampaignSerializer
    queryset = Campaign.objects.all()

class TagView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= TagSerializer
    queryset = Tag.objects.all()   

# class ListPagination(PageNumberPagination):
#     page_size=25
#     page_size_query_param='page_size'
#     max_page_size=200    



class LeadFollowUpViewSet(generics.ListCreateAPIView):
    serializer_class = LeadFollowUpSerializer
    queryset = LeadFollowUp.objects.all()
    # pagination_class = ListPagination
    filter_backends = [filter.DjangoFilterBackend]
    filterset_fields = ['lead_id']

    # lead_param = openapi.Parameter('lead_id', openapi.IN_QUERY, description="filter by Lead Id", type=openapi.TYPE_NUMBER)

    # @swagger_auto_schema(manual_parameters=[lead_param],)
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
        
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)     


class RequirementView(generics.ListCreateAPIView):
    serializer_class = RequirementSerializer
    queryset = Requirement.objects.all()


class RequirementDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RequirementSerializer
    queryset = Requirement.objects.all()

class ProjectView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'type']
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     title = self.request.query_params.get('title', None)
    #     if title:
    #         queryset = queryset.filter(title__icontains=title)
    #     return queryset 
    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title', None)
        type = self.request.query_params.get('type', None)
        
        if title:
            queryset = queryset.filter(title__icontains=title)
        
        if type:
            queryset = queryset.filter(type__icontains=type)
        
        return queryset


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()  
        


class BookingView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    filter_backends = [filter.DjangoFilterBackend]
    filterset_fields = ['lead_id']


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()   


class ClosureView(generics.ListCreateAPIView):
    serializer_class = ClosureSerializer
    queryset = Closure.objects.all()
    filter_backends = [filter.DjangoFilterBackend]
    filterset_fields = ['lead_id']


class ClosureDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClosureSerializer
    queryset = Closure.objects.all()   


class ProjectMatchView(generics.ListCreateAPIView):
    serializer_class = ProjectMatchSerializer
    queryset = ProjectMatch.objects.all()


class ProjectMatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectMatchSerializer
    queryset = ProjectMatch.objects.all()     
        