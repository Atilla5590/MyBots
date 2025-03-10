import praw
import time

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)

subreddit = reddit.subreddit("downvoteautomod")
checked_comments = set()  
print("Bot started...")

while True:
    try:
        for comment in subreddit.comments(limit=55):  
            if comment.author == "AutoModerator" and comment.id not in checked_comments:
                comment.reply("bad bot")
                print(f"Replied to: {comment.id}")
                checked_comments.add(comment.id)
        
        time.sleep(10)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(60)

print("Program finish")
