from django.shortcuts import render
from dotenv import load_dotenv
from django.http import HttpResponse
from .forms import ContactForm
from django.utils import timezone
from .models import get_db
import os, requests


load_dotenv()
api = os.getenv("API_KEY")
url = os.getenv("URL")


# views start here.
def home(request):
    return render(request, "home.html")


def weather(request):
    context = {}
    if request.method == "POST":
        city = request.POST.get("city", "").strip()
        if city:
            try:
                params = {
                    "access_key": api,
                    "query": city,
                    "units": "m",
                }
                response = requests.get(url, params=params, timeout=5)
                data = response.json()

                if "error" in data:
                    context["error"] = data["error"].get(
                        "info", "City not found. Please try again."
                    )
                    context["city"] = city
                elif "current" in data:
                    context["weather"] = {
                        "city": data["location"]["name"],
                        "country": data["location"]["country"],
                        "region": data["location"]["region"],
                        "localtime": data["location"]["localtime"],
                        "temp_c": data["current"]["temperature"],
                        "feels_like": data["current"]["feelslike"],
                        "description": (
                            data["current"]["weather_descriptions"][0]
                            if data["current"]["weather_descriptions"]
                            else "N/A"
                        ),
                        "icon": (
                            data["current"]["weather_icons"][0]
                            if data["current"]["weather_icons"]
                            else ""
                        ),
                        "humidity": data["current"]["humidity"],
                        "wind_speed": data["current"]["wind_speed"],
                        "wind_dir": data["current"]["wind_dir"],
                        "pressure": data["current"]["pressure"],
                        "visibility": data["current"]["visibility"],
                        "uv_index": data["current"]["uv_index"],
                        "cloud_cover": data["current"]["cloudcover"],
                        "is_day": data["current"].get("is_day", "yes"),
                    }
                else:
                    context["error"] = "Unexpected response from weather service."
                    context["city"] = city
            except requests.exceptions.ConnectionError:
                context["error"] = (
                    "Network error. Please check your internet connection."
                )
                context["city"] = city
            except Exception as e:
                context["error"] = f"Something went wrong: {str(e)}"
                context["city"] = city
        else:
            context["error"] = "Please enter a city name."
    return render(request, "weather.html", context)


def services(request):
    return render(request, "services.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            db = get_db()
            collection = db["form_submissions"]  # collection name

            document = {
                "full_name": form.cleaned_data["full_name"],
                "email": form.cleaned_data["email"],
                "option": form.cleaned_data["option"],
                "message": form.cleaned_data["message"],
                "submitted_at": timezone.now(),  # current date & time
            }
            collection.insert_one(document)
            success = True
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form, "success": success})


def login(request):
    pass


def register(request):
    pass
