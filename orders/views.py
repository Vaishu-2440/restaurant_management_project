from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get("code")

        if not code :
            return Response(
            {
                "success" : False,
                "message": "Coupon code is required."
            }, status = status.HTTP_400_BAD_REQUEST
            )
        
        coupon = Coupon.objects.filter(code = code).first()
        if not coupon :
            return Response(
            {
                "success" : False,
                "message": "Invalid coupon code."
            }, status = status.HTTP_400_NOT_FOUND
            )

        today = timezone.now().date()
        if not coupon.is_active :
            return Response(
            {
                "success" : False,
                "message" : "Coupon is not active."
            }, status = status.HTTP_403_FORBIDDEN
            )

        if (today < coupon.valid_from) :
            return Response(
            {
                "success" : False,
                "message": "Coupon not yet valid."
            }, status = status.HTTP_400_BAD_REQUEST
            )

        if (today > coupon.valid_until) :
            return Response(
            {
                "success" : False,
                "message" : "Coupon is expired."
            }, status = status.HTTP_410_GONE
            )
            
        return Response(
            {
            "success" : True,
            "code" : coupon.code,
            "discount_percentage" : coupon.discount_percentage
            }, status = status.HTTP_200_OK
            )