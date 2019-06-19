import random
from queue import LifoQueue, Queue


def FYS(l):
    for i in range(0, len(l)):
        # random.randint gives you a random interval between i and len(l)-1 inclusive
        random_index = random.randint(0, len(l)-1)
        l[random_index], l[i] = l[i], l[random_index]  # swap
    return l


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # create an array of users, starting at 1 and going up until numUsers + 1 (exlcusive) to match userId
        newUsers = []
        for i in range(1, numUsers+1):
            newUsers.append(i)

        for user in newUsers:  # loop through that array, create a user out of each, and add it to the graph
            self.addUser(User(user))

        # Create friendships
        # create a randomized array of potential friends, and slice off a random number between 0 and 2*num inclusive of those friends from the front. Loop through that second array (here is the scaling issue) and call the add friendships
        for userId in self.users.keys():  # O(n)
            #eliminate friends with yourself
            newUsers.remove(userId)
            #randomize the rest of the array
            random_friends = FYS(newUsers)  # O(n)

            random_number = random.randint(0, 2*avgFriendships)
            # in the case userId has no friends
            if random_number == 0:
                pass 
            # loop through the randomized array the random number of times. Evenly distributed psuedorandom numbers between 0 and n should average out to n/2
            else:
                for i in range(0, random_number):  # O(n)
                    if random_friends[i] in self.friendships[userId] or user in self.friendships[random_friends[i]]:
                        pass
                    else:
                        self.friendships[userId].add(random_friends[i])
                        self.friendships[random_friends[i]].add(userId)
                    # print('test', self.friendships[userId])
            newUsers.append(userId)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        { 1: 2, 3, 4}
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.put([userID])
        while q.empty() is False:
            path = q.get()
            v = path[-1]
            for friend in self.friendships[v]:
                if friend not in visited:
                    visited[friend] = path
                    path_copy = list(path)
                    path_copy.append(friend)
                    q.put(path_copy)
           

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(20, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
