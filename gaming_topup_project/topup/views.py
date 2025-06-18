from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TopUpOrderSerializer

class TopUpOrderAPIView(APIView):
    def post(self, request):
        serializer = TopUpOrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response({"message": "Order created", "order_id": order.id}, status=201)
        return Response(serializer.errors, status=400)


from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from .models import TopUpOrder, TopUpProduct
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate

@staff_member_required
def dashboard_view(request):
    top_products = TopUpProduct.objects.annotate(
        total_orders=Count('topuporder')
    ).order_by('-total_orders')[:5]

    last_7_days = now() - timedelta(days=6)
    daily_revenue = TopUpOrder.objects.filter(
        status='success',
        created_at__date__gte=last_7_days.date()
    ).annotate(date=TruncDate('created_at')).values('date').annotate(
        total=Sum('product__price')
    ).order_by('date')

    failed_count = TopUpOrder.objects.filter(
        status='failed',
        created_at__month=now().month
    ).count()

    return render(request, 'topup/dashboard.html', {
        'top_products': top_products,
        'daily_revenue': daily_revenue,
        'failed_count': failed_count,
    })

from django.shortcuts import render

def topup_form_view(request):
    return render(request, 'topup/topup_form.html')