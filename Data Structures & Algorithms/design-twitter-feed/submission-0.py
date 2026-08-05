class Twitter:

    def __init__(self):
        self.tweet = []
        self.user_following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        following = self.user_following.get(userId, set())

        i = len(self.tweet) - 1

        while i > -1:
            if len(res) == 10:
                return res

            post_userId, tweetId = self.tweet[i]
            
            if post_userId in following or post_userId == userId:
                res.append(tweetId)

            i -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        following = self.user_following.get(followerId, set())
        following.add(followeeId)
        self.user_following[followerId] = following

    def unfollow(self, followerId: int, followeeId: int) -> None:
        following = self.user_following.get(followerId, set())
        following.discard(followeeId)
        self.user_following[followerId] = following
        
