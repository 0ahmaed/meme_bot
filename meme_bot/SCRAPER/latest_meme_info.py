import requests
from bs4 import BeautifulSoup
from .headers import headers
import pprint
def get_meme_details(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Title
    title = soup.select_one("h1.content-title").text.strip()
    
    # Uploader (Added by)
    uploader_elements = soup.select(".entry-timestamps p:last-child a")
    uploader = uploader_elements[0].text.strip() if uploader_elements else "Unknown"
    
    # Upload time
    time_elements = soup.select(".entry-timestamps abbr.timeago")
    upload_time = time_elements[0].text.strip() if time_elements else "Unknown"
    
    # Image
    image = soup.select_one('meta[property="og:image"]')["content"]
    
    # About - first paragraph after #about heading
    about_heading = soup.select_one("#about")
    about = ""
    if about_heading:
        about_p = about_heading.find_next("p")
        if about_p:
            about = about_p.text.strip()
    
    # Origin - first paragraph after #origin heading
    origin_heading = soup.select_one("#origin")
    origin = ""
    if origin_heading:
        origin_p = origin_heading.find_next("p")
        if origin_p:
            origin = origin_p.text.strip()
    
    # Video
    video_element = soup.select_one("lite-youtube")
    video_id = video_element.get("videoid") if video_element else None
    video_url = f"https://www.youtube.com/watch?v={video_id}" if video_id else None
    
    return {
        "title": title,
        "link": url,
        "uploader": uploader,
        "upload_time": upload_time,
        "image": image,
        "about": about,
        "origin": origin,
        "video_url": video_url
    }

if __name__ == "__main__":
    url = "https://knowyourmeme.com/memes/this-is-fine"
    details = get_meme_details(url)
    pprint.pprint(details)