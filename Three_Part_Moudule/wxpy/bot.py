from wxpy import Bot, FEMALE


if __name__ == "__main__":
    bot = Bot()
    my_friend = bot.friends().search('胜男酱', sex=FEMALE)[0]
    
    message = input()
    while message != "exit":
        my_friend.send(message)
        message = input()
