from django.urls import path
from .views import LeadListView,LeadDetailView,SourceView,CampaignView,TagView,TagDetailView,LeadFollowUpViewSet,RequirementView,RequirementDetailView,ProjectView,ProjectDetailView,BookingView,BookingDetailView,ClosureView,ClosureDetailView,ProjectMatchView,ProjectMatchDetailView

urlpatterns = [
    path('lead/',LeadListView.as_view()),
    path('lead/<int:pk>',LeadDetailView.as_view()),
    path('source/',SourceView.as_view()),
    path('campaign/',CampaignView.as_view()),
    path('tag/',TagView.as_view()),
    path('tag/<int:pk>/',TagDetailView.as_view()),
    path('lead_followup/',LeadFollowUpViewSet.as_view()),
    path('requirement/',RequirementView.as_view()),
    path('requirement/<int:pk>/',RequirementDetailView.as_view()),
    path('project/',ProjectView.as_view()),
    path('project/<int:pk>/',ProjectDetailView.as_view()),
    path('booking/',BookingView.as_view()),
    path('booking/<int:pk>/',BookingDetailView.as_view()),
    path('closure/',ClosureView.as_view()),
    path('closure/<int:pk>/',ClosureDetailView.as_view()),
    path('project_match/',ProjectMatchView.as_view()),
    path('project_match/<int:pk>/',ProjectMatchDetailView.as_view())
]

urlpatterns += [
    path('lead/search/', LeadListView.as_view(), name='lead-search'),      #http://127.0.0.1:8000/api/lead/search/?name=arun
    path('project/search/', ProjectView.as_view(), name='project-search'),   #http://127.0.0.1:8000/api/project/search/?title=brigade
]