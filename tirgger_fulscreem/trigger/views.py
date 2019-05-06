# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os


@api_view(['GET', 'POST'])
def FullScreemView(request):
    if request.method == "GET":
        return comand_scala()

    elif request.method == "POST":
        try:

            return comand_scala(request.data['status_button'])
        except KeyError:
            return Response({"error": "Problem in the command"},
                            status=status.HTTP_400_BAD_REQUEST)


def comand_scala(status_button):

    try:
        if status_button:
            os.system('python -m scalalink -v -t tcp -p 7700 -H localhost set interVar=True')
        else:
            os.system('python -m scalalink -v -t tcp -p 7700 -H localhost set interVar=True')
        return Response({"detail": "ok"},
                        status=status.HTTP_200_OK)
    except:
        return Response({"error": "Problem in the command"},
                        status=status.HTTP_424_FAILED_DEPENDENCY)
