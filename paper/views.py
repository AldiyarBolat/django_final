from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import models, serializers


class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_super_admin:
            serializer.save()
        return Response({'into': 'admins only allowed'})

    def update(self, request, *args, **kwargs):
        if self.request.user.is_super_admin:
            instance = self.get_object()
            serializer = self.get_serializer(instance=instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        return Response({'into': 'admins only allowed'})

    def destroy(self, request, *args, **kwargs):
        if self.request.user.is_super_admin:
            instance = self.get_object()
            self.perform_destroy(instance=instance)

            return Response({'info': 'successfully deleted'})
        return Response({'into': 'admins only allowed'})


class JournalViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = models.Journal.objects.all()
    serializer_class = serializers.JournalSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_super_admin:
            serializer.save()
        return Response({'into': 'admins only allowed'})

    def update(self, request, *args, **kwargs):
        if self.request.user.is_super_admin:
            instance = self.get_object()
            serializer = self.get_serializer(instance=instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        return Response({'into': 'admins only allowed'})

    def destroy(self, request, *args, **kwargs):
        if self.request.user.is_super_admin:
            instance = self.get_object()
            self.perform_destroy(instance=instance)

            return Response({'info': 'successfully deleted'})
        return Response({'into': 'admins only allowed'})
