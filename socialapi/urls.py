from django.urls import path
from .views import SendFRView, RespondFRView, YourFrAcceptedView, YourFrRejectedView, ListAcceptsFRView, ListRejectedFRView, ListPendingFRView

urlpatterns = [
    path('friend-request/send/', SendFRView.as_view(), name='send-friend-request'),
    path('fr/respond/<int:id>/', RespondFRView.as_view(), name='respond-friend-request'),
    path('fr/requestAccepted/', YourFrAcceptedView.as_view(), name='list-requestAccepted'),
    path('fr/requestRejected/', YourFrRejectedView.as_view(), name='list-requestRejected'),
    path('fr/You-accepted/', ListAcceptsFRView.as_view(), name='list-accepts-friends'),
    path('fr/You-rejected/', ListRejectedFRView.as_view(), name='list-rejects-friends'),
    path('fr/pendingUser/', ListPendingFRView.as_view(), name='list-pending-requests'),

]
