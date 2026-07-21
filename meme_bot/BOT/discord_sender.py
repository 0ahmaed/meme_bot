import requests
import json

class DiscordSender:
    def __init__(self, webhook_url , meme_data):
        self.webhook_url = webhook_url
        self.meme_data = meme_data

    def default_message(self):
        #sends the response message :"no new memes currently"
        MESSAGE={"content":"No new memes currently"}
        response = requests.post(
            self.webhook_url,
            data=json.dumps(MESSAGE),
            headers={"Content-Type": "application/json"}
        )
    
    def send_meme(self, meme_data):
        """Send a meme to Discord via webhook"""
        
        # Build the embed
        embed = {
            "title": meme_data['title'],
            "url": meme_data['link'],
            "color": 0x5865F2,  # Discord blurple
            "thumbnail": {
                "url": meme_data['image']
            },
            "fields": [
                {
                    "name": "📤 Uploader",
                    "value": meme_data['uploader'],
                    "inline": True
                },
                {
                    "name": "📅 Uploaded",
                    "value": meme_data['upload_time'],
                    "inline": True
                },
                {
                    "name": "📝 About",
                    "value": meme_data['about'][:500] + ("..." if len(meme_data['about']) > 500 else ""),
                    "inline": False
                },
                {
                    "name": "📍 Origin",
                    "value": meme_data['origin'][:500] + ("..." if len(meme_data['origin']) > 500 else ""),
                    "inline": False
                }
            ],
            "image": {
                "url": meme_data['image']
            }
        }
        
        # Add video field if available
        if meme_data.get('video_url'):
            embed["fields"].append({
                "name": "🎬 Watch Video",
                "value": f"[Click here to watch]({meme_data['video_url']})",
                "inline": False
            })
        
        # Build the payload
        payload = {
            "username": "Meme Scraper",
            "avatar_url": "https://www.reddit.com/r/lostmedia/comments/1sc0dic/talk_could_the_original_tung_tung_tung_sahur/",
            "embeds": [embed]
        }
        
        # Send it
        response = requests.post(
            self.webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )
        
        return response.status_code == 204 


if __name__=="__main__":
    pass