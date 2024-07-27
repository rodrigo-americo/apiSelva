from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Usuario
from .serializer import UsuarioSerializers


class UsuarioView(APIView):

    def get(self, request):
        usuarios = Usuario.objects.all()
        output = [{"id": user.id,
                   "userName": user.userName,
                   "password": user.password,
                   "active": user.active,
                   "datecreatedAt": user.datecreatedAt} for user in usuarios]
        return Response(output)

    def post(self, request):
        serializer = UsuarioSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetailView(APIView):

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializers(usuario)
        return Response(serializer.data)

    def put(self, request, pk):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializers(usuario, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
