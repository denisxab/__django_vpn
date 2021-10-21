from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
from main_app.models import OpenVpn


def send_index(request: WSGIRequest):
    if request.method == "POST":
        print(request)
        OpenVpn.objects.create(
            user_name_send=request.POST["SendUserNameInputText"],
            user_name_get=request.POST["GetUserNameInputText"],
            message=request.POST["MessageInputText"],
        )
    context = {
        "": 0,
    }

    return render(request,
                  template_name="main_app/send_index.html",
                  context=context, )


def get_index(request: WSGIRequest):
    context = {
        "SendData": None,
    }

    if request.method == "POST":
        print(request)
        response_db = OpenVpn.objects.filter(user_name_get=request.POST["GetUserNameInputText"])
        context["SendData"] = []
        for _x in response_db:
            context["SendData"].append([_x.user_name_send, _x.message])

        print(context)

    return render(request,
                  template_name="main_app/get_index.html",
                  context=context, )


def index_main(request: WSGIRequest):
    context = {
        "": 0,
    }
    return render(request,
                  template_name="main_app/index_main.html",
                  context=context, )
