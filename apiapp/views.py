from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import JsonResponse
import django
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
@api_view(["POST"])
def IdealWeight(heightdata):
    try:
        height=json.loads(heightdata.body)
        weight=str((height*100000)/12)

        return JsonResponse("The monthly Salary would be close to :"+weight+" Rs",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)