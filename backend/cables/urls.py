from django.urls import path

from .views import (
    ActionViewSet,
    InfrastructureViewSet,
    OperationViewSet,
    PoleViewSet,
    SegmentViewSet,
    VisitViewSet,
)

urlpatterns = [
    # No create, update or delete on Infrastructure parent class: to be done on inherited classes
    path(
        "infrastructures/",
        InfrastructureViewSet.as_view({"get": "list"}),
        name="infrastructure_list",
    ),
    path(
        "infrastructures/<int:pk>/",
        InfrastructureViewSet.as_view({"get": "retrieve"}),
        name="infrastructure_detail",
    ),
    path(
        "poles/",
        PoleViewSet.as_view({"get": "list", "post": "create"}),
        name="pole_list",
    ),
    path(
        "poles/<int:pk>/",
        PoleViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
            }
        ),
        name="pole_detail",
    ),
    path(
        "segments/",
        SegmentViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="segment_list",
    ),
    path(
        "segments/<int:pk>/",
        SegmentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
            }
        ),
        name="segment_detail",
    ),
    # No create, update or delete on Infrastructure parent class: to be done on inherited classes
    path(
        "actions/",
        ActionViewSet.as_view(
            {
                "get": "list",
            }
        ),
        name="action_list",
    ),
    path(
        "actions/<int:pk>",
        ActionViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="action_detail",
    ),
    path(
        "visits/",
        VisitViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="visit_list",
    ),
    path(
        "visits/<int:pk>",
        VisitViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
            }
        ),
        name="visit_detail",
    ),
    path(
        "operations/",
        OperationViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="operation_list",
    ),
    path(
        "operations/<int:pk>/",
        OperationViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
            }
        ),
        name="operation_detail",
    ),
]

# urlpatterns = [
#     path(
#         "poto/<int:pk>",
#         PotoViewSet.as_view(
#             {
#                 "get": "list",
#                 "post": "create",
#                 "put": "update",
#                 "patch": "partial_update",
#             }
#         ),
#     ),
#     path(
#         "poles/info/",
#         PoleViewSetInfo.as_view({"get": "list"}),
#         name="pole_list_info",
#     ),
#     path(
#         "poles/edit/",
#         PoleViewSetEdit.as_view(
#             {
#                 "get": "list",
#                 "post": "create",
#                 "put": "update",
#                 "patch": "partial_update",
#             }
#         ),
#         name="pole_list_edit",
#     ),
#     path(
#         "poles/info/<int:pk>/",
#         PoleViewSetInfo.as_view({"get": "retrieve"}),
#         name="pole_info",
#     ),
#     path(
#         "poles/edit/<int:pk>/",
#         PoleViewSetEdit.as_view(
#             {
#                 "get": "retrieve",
#                 "put": "update",
#                 "patch": "partial_update",
#                 "delete": "destroy",
#             }
#         ),
#         name="pole_edit",
#     ),
#     path(
#         "segments/info/",
#         SegmentViewSetInfo.as_view({"get": "list"}),
#         name="segments_list_info",
#     ),
#     path(
#         "segments/edit/",
#         SegmentViewSetEdit.as_view(
#             {
#                 "get": "list",
#                 "post": "create",
#                 "put": "update",
#                 "patch": "partial_update",
#             }
#         ),
#         name="segment_list_edit",
#     ),
#     path(
#         "segments/info/<int:pk>/",
#         SegmentViewSetInfo.as_view({"get": "retrieve"}),
#         name="segment_info",
#     ),
#     path(
#         "segments/edit/<int:pk>/",
#         SegmentViewSetEdit.as_view(
#             {
#                 "get": "retrieve",
#                 "put": "update",
#                 "patch": "partial_update",
#                 "delete": "destroy",
#             }
#         ),
#         name="segment_edit",
#     ),
#     path(
#         "visits/info/",
#         VisitViewSetInfo.as_view({"get": "list"}),
#         name="visit_list_info",
#     ),
#     path(
#         "visits/edit/",
#         VisitViewSetEdit.as_view(
#             {
#                 "get": "list",
#                 "post": "create",
#                 "put": "update",
#                 "patch": "partial_update",
#             }
#         ),
#         name="visit_list_edit",
#     ),
#     path(
#         "visits/info/<int:pk>/",
#         VisitViewSetInfo.as_view({"get": "retrieve"}),
#         name="visits_info",
#     ),
#     path(
#         "visits/edit/<int:pk>/",
#         VisitViewSetEdit.as_view(
#             {
#                 "get": "retrieve",
#                 "put": "update",
#                 "patch": "partial_update",
#                 "delete": "destroy",
#             }
#         ),
#         name="visits_edit",
#     ),
#     path(
#         "operations/info/",
#         OperationViewSetInfo.as_view({"get": "list"}),
#         name="operation_list_info",
#     ),
#     path(
#         "operations/edit/",
#         OperationViewSetEdit.as_view(
#             {
#                 "get": "list",
#                 "post": "create",
#                 "put": "update",
#                 "patch": "partial_update",
#             }
#         ),
#         name="operation_list_edit",
#     ),
#     path(
#         "operations/info/<int:pk>/",
#         OperationViewSetInfo.as_view({"get": "retrieve"}),
#         name="operations_info",
#     ),
#     path(
#         "operations/edit/<int:pk>/",
#         OperationViewSetEdit.as_view(
#             {
#                 "get": "retrieve",
#                 "put": "update",
#                 "patch": "partial_update",
#                 "delete": "destroy",
#             }
#         ),
#         name="operations_edit",
#     ),
# ]
