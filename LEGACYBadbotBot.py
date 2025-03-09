# Start of the program
print("program has now Started")

print("Importing PRAW")
import praw
print("Importing Time")
import time
print("Imports succesful Imported: PRAW, time")

print("Sharing credientials with PRAW")

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)
print("Credientials now shared with PRAW")
subreddit=reddit.subreddit("downvoteautomod")
alreadychecked=[]
infinity=99999999999999999999
for d in range(infinity):
    posts = subreddit.new(limit=1)
    for idpost in posts:
        print(idpost)
    print(idpost.id)

    last = len(alreadychecked)
    if alreadychecked:
        last = last-1
        checker = alreadychecked[last]
    else:
        checker=00
    if not idpost.id == checker:
        commentid=idpost.comments
        for textid in commentid:
            if "AutoModerator allows anything to be commented by the config file" in textid.body:
                textid.reply("bad bot")
                print("its Automod which is badass")
            else:
                print("its not him good.")
        alreadychecked.append(idpost.id)
    else:
        print("same post going to next in 60 seconds")
        time.sleep(60)
#end of the program
print("Program has been finished")
