from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from rest_framework.permissions import IsAuthenticated
from .models import Notice, Course
from .serializers import NoticeSerializer, CourseSerializer
from student.authentication import CustomTokenAuthentication

class NoticeFilterSet(FilterSet):
    notice_type = CharFilter(field_name='notice_type', lookup_expr='in', method='filter_by_notice_types')

    def filter_by_notice_types(self, queryset, name, value):
        notice_types = self.request.query_params.getlist('notice_type')
        if notice_types:
            return queryset.filter(notice_type__in=notice_types)
        return queryset

    class Meta:
        model = Notice
        fields = ['notice_type']

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by('-created_at')
    serializer_class = NoticeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = NoticeFilterSet
    search_fields = ['notice_type']

    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Supports filtering by multiple `notice_type` query params.
        Example: GET /notices/?notice_type=assignment&notice_type=exam
        """
        queryset = super().get_queryset()
        notice_types = self.request.query_params.getlist('notice_type')
        if notice_types:
            queryset = queryset.filter(notice_type__in=notice_types)
        return queryset


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer

    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]
