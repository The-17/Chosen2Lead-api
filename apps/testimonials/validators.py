from django.core.exceptions import ValidationError

ALLOWED_TYPES = [
            "video/mp4", "video/quicktime", "video/x-msvideo", "video/x-ms-wmv",
            "video/x-flv", "video/x-matroska", "video/webm", "video/mpeg",
            "video/3gpp", "video/ogg"
        ]

def video_file_validator(file):
    if file.content_type not in ALLOWED_TYPES:
        raise ValidationError("Invalid file type. Only mp4 videos are allowed.")
    