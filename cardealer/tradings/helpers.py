import os
import time
from django.utils.timezone import now

def user_directory_path(instance, filename):
    today = time.strftime("%Y/%m/%d")
    base, ext = os.path.splitext(filename)
    new_filename = f"{now().strftime('%Y%m%d%H%M%S')}{str(instance.id)[24:32]}{ext}"
    return f'user_{instance.user.username}/thumbnails/photos/{today}/{new_filename}'

def user_directory_path_image(instance, filename):
    today = time.strftime("%Y/%m/%d")
    base, ext = os.path.splitext(filename)
    new_filename = f"{now().strftime('%Y%m%d%H%M%S')}{str(instance.id)[24:32]}{ext}"
    return f'user_{instance.vehicle.user.username}/car/photos/{today}/{new_filename}'