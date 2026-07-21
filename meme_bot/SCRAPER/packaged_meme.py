from .latest_meme_info import get_meme_details
from .latest_meme_link import get_latest_meme_link


def packaged_meme():
    FAILURE_MESSAGE="Failure ❎"

    MEME_DETAILS={
        "title": str,
        "link": str,
        "uploader": str,
        "upload_time": str,
        "image": str,
        "about": str,
        "origin": str,
        "video_url": str
        }
    latest_meme_link=get_latest_meme_link()
    if not latest_meme_link:
        return FAILURE_MESSAGE 
    
    details=get_meme_details(latest_meme_link)

    MEME_DETAILS["title"] = details["title"]
    MEME_DETAILS["link"] = details["link"]
    MEME_DETAILS["uploader"] = details["uploader"]
    MEME_DETAILS["upload_time"] = details["upload_time"]
    MEME_DETAILS["image"] = details["image"]
    MEME_DETAILS["about"] = details["about"]
    MEME_DETAILS["origin"] = details["origin"]
    MEME_DETAILS["video_url"] = details["video_url"]
    
    return MEME_DETAILS