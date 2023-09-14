from .models import Person
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer

@api_view(['GET'])
def getPerson(request, name):
    person = Person.objects.get(name=name)
    serializer = PersonSerializer(person)
    return Response(serializer.data)

@api_view(['POST'])  
def addPerson(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
    
@api_view(['PUT'])
def editPerson(request, name):
   person = Person.objects.get(name=name)
   serializer = PersonSerializer(person, data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
   return Response(serializer.errors)
   
@api_view(['DELETE'])
def deletePerson(request, name):
    person = Person.objects.get(name=name)
    person.delete()
    return Response('Person deleted')