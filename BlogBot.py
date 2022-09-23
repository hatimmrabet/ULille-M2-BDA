import api_microblog as api
import random

class User:
    def __init__(self, data):
        self.name = data.split("\t")[0]
        self.password = data.split("\t")[1]

    def __str__(self):
        return self.name + " => " + self.password



global users

def get_random_user():
    global users
    return random.choice(users)

def get_users_from_file():
    with open("users") as f:
        return [User(line.strip()) for line in f.readlines()]

def get_messages_from_file():
    with open("messages") as f:
        return [line.strip() for line in f.readlines()]

def main():
    mb = api.microblog("172.28.100.16")
    global users 
    users = get_users_from_file()
    messages = get_messages_from_file()
    # do it 500 times
    for i in range(0, 100):
        user = get_random_user()
        # publier un message avec un user aleatoire
        msg_id = mb.publish_post(user.name, user.password, random.choice(messages))
        print("User", user.name, "is publishing a message:", msg_id)
        msg = mb.get_message_by_id(msg_id)
        # repondre au message avec un autre user aleatoire
        for _ in range(random.randint(0, 10)):
            user2 = get_random_user()
            msg2_id = mb.publish_post(user2.name, user2.password, random.choice(messages), msg_id)
            print("->User", user2.name, "is replying to", user.name, "message:", msg2_id)
            # 50% de chance de follow le user qui a posté le message
            if(random.randint(0, 1) == 1 and user.name != user2.name):
                print("-->User", user2.name, "is following", user.name)
                mb.follow(user2.name, user2.password, msg.user_id)

        # get all messages
        feed_messages = mb.get_messages()

        for msg in feed_messages:
            # follow the user who replied to my message
            if(msg.replies_to == msg_id and user.name != msg.user_name):
                print("==>User", user.name, "is following", msg.user_name)
                mb.follow(user.name, user.password, msg.user_id)

    print("Done")
    print("Total time:", mb.acc_time)
    print("Total queries:", mb.nb_query)

main()