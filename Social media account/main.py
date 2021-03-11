class Account:
    def __init__(self, media, username, n_followers):
        self.media = media
        self.username = username
        self.n_followers = n_followers
        print("Account")


# create the class here
class InstagramAccount(Account):
    def __init__(self, username, n_followers, n_following, media="Instagram"):
        self.n_following = n_following
        super().__init__(media, username, n_followers)
