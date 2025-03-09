import praw
import time

reddit = praw.Reddit(
    client_id="XEN99ZTZrtutFbpY6zMH_Q",
    client_secret="CdVNecsSlt0GW5l5ufGbSxVXbmrVBA",
    password="thealliance123",
    user_agent="bot3478615",
    username="AutomodSucks-4327982",
)

subreddit = reddit.subreddit("downvoteautomod")
checked_comments = set()  
print("Bot started...")

while True:
    try:
        for comment in subreddit.comments(limit=25):  
            if comment.author == "AutoModerator" and comment.id not in checked_comments:
                age = time.time() - comment.created_utc  
                if age <= 120: 
                    comment.reply("bad bot")
                    print(f"Replied to: {comment.id}")
                    checked_comments.add(comment.id)
        
        time.sleep(10)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(60)

print("Program finish")
