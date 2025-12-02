from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import send_custom_email

class FeedbackView(APIView) :
    def post(self, request) :
        user_email = request.data.get("email")
        subject = "Thank you for contacting us!"
        message = "We have received your message and we will get back to you soon."

        result = send_custom_email(user_email, subject, message)

        if result is True :
            return Response({"Message" : "Email sent successfully."})
        return Response({"error" : "result"}, status = 400)


