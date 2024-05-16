from rest_framework.response import Response
from rest_framework.decorators import api_view
from mailweb.tasks import send_feedback_email_task


@api_view(['POST', 'GET'])
def HomeView(request):
    context = dict()
    context['message'] =  'Sending'
    try:
        result = send_feedback_email_task.delay('crn96m@gmail.com')
        context['message'] =  'Email sent'
        # context['result'] =  f'{ result.get() }'
    except Exception as e:
        context['message'] =  f'Email not sent: because {e}'
    return Response(context)