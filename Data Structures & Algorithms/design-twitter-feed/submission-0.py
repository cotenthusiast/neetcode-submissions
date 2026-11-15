class Twitter:

    def __init__(self):
        self.feed = []
        self.tweet_map = {}
        self.user_friends = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed = [tweetId] + self.feed
        self.tweet_map[tweetId] = userId

    def getNewsFeed(self, userId: int) -> List[int]:
        ret_list = []
        count = 0

        while count < len(self.feed) and len(ret_list) < 10:
            tweet_id = self.feed[count]
            author = self.tweet_map[tweet_id]

            if author == userId or author in self.user_friends.get(userId, set()):
                ret_list.append(tweet_id)

            count += 1

        return ret_list

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_friends:
            self.user_friends[followerId] = set()

        self.user_friends[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_friends:
            self.user_friends[followerId].discard(followeeId)