from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Ticket
from .serializers import TicketSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@cache_page(60)
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def ticket_list(request):

    if request.method == "GET":

        tickets = Ticket.objects.all()

        title = request.query_params.get("title")
        description = request.query_params.get("description")
        ordering = request.query_params.get("ordering")

        if title:
            tickets = tickets.filter(title=title)

        if description:
            tickets = tickets.filter(description=description)

        if ordering:
            tickets = tickets.order_by(ordering)

        paginator = PageNumberPagination()
        paginator.page_size = 2

        
        paginated_tickets = paginator.paginate_queryset(tickets, request)

        serializer = TicketSerializer(paginated_tickets, many=True)

       
        return paginator.get_paginated_response(serializer.data)


    if request.method == "POST":

        
        serializer = TicketSerializer(data=request.data)

   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)



@cache_page(60)
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def ticket_details(request, id):

    try:
        ticket = Ticket.objects.get(id=id)
    except Ticket.DoesNotExist:
        return Response({"error": "Not Found"}, status=404)

    if request.method == "GET":

        
        serializer = TicketSerializer(ticket)

        return Response(serializer.data)


    if request.method == "PUT":

        serializer = TicketSerializer(ticket, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

       
        return Response(serializer.errors, status=400)


    if request.method == "PATCH":

        serializer = TicketSerializer(ticket, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


        return Response(serializer.errors, status=400)


    if request.method == "DELETE":

        ticket.delete()

      
        return Response({"message": "Ticket Deleted"}, status=204)