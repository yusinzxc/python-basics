class InstagramUser:
    def __init__(self,fullname,username,post,followers,following,bio,followingList):
        self.fullname = fullname
        self.username = username
        self.post = post
        self.followers = followers
        self.following = following
        self.bio = bio
        self.followingList = followingList
    def profile(self):
        print(self.fullname.upper(),"@"+self.username)
        print("Post","Followers","Following")
        print("",self.post,"   ",self.followers,"      ",self.following)
    def allFollowing(self):
        print("FOLLOWING:")
        for i in self.followingList:
            print(i)

user32 = InstagramUser("Jeon Heejin","Heeki3",40,"1M",11,"PTT",["Haseul","Chuu","Kimlip","Hyunjin","Yves","Vivi","Olivia Hye","Choerry","Gowon","Jinsoul"])

user32.profile()
print("Go to:")
userTo = input("(P/p) to post, (Fs/fs) to followers, (Fg/fg) to following >>> ")

if userTo == "P" or userTo == "p":
    print("Working")
elif userTo == "Fs" or userTo == "fs":
    print("Working")
elif userTo == "Fg" or userTo == "fg":
    user32.allFollowing()
