import itertools
from collections import defaultdict, deque
import heapq


# My solution
from typing import List


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = defaultdict(list)
        self.following = defaultdict(set)
        self.followedBy = defaultdict(set)
        self.currentMessages = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.messages[userId].append((self.time, userId, tweetId))
        for i in self.followedBy[userId] | {userId}:
            heapq.heappush(self.currentMessages[i], (self.time, userId, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        cnt = 0
        res = []
        visited = set()
        while self.currentMessages[userId] and cnt != 10:
            time, user, tweet = heapq.heappop(self.currentMessages[userId])
            if user in self.following[userId] | {userId} and tweet not in visited:
                cnt += 1
                res.append((time, user, tweet))
                visited.add(tweet)
        for i in res:
            heapq.heappush(self.currentMessages[userId], i)
        return [i[2] for i in res]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.following[followerId]:
            self.following[followerId].add(followeeId)
            self.followedBy[followeeId].add(followerId)
            for i in self.messages[followeeId]:
                heapq.heappush(self.currentMessages[followerId], i)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.following[followerId].discard(followeeId)
        self.followedBy[followeeId].discard(followerId)

class Twitter2(object):

    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = defaultdict(deque)
        self.followees = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)


if __name__ == '__main__':
    # Your Twitter object will be instantiated and called as such:
    # obj = Twitter()
    # obj.postTweet(userId,tweetId)
    # param_2 = obj.getNewsFeed(userId)
    # obj.follow(followerId,followeeId)
    # obj.unfollow(followerId,followeeId)

    obj = Twitter()
    obj.postTweet(1, 5)
    print(obj.getNewsFeed(1))
    obj.follow(1, 2)
    obj.follow(1, 2)
    obj.postTweet(2, 6)
    print(obj.getNewsFeed(2))
    print(obj.getNewsFeed(1))
    obj.unfollow(1, 2)
    # obj.follow(1, 2)
    print(obj.getNewsFeed(1))
