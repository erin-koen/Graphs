import random


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

        # create an array of users, starting at zero and going up until numUsers (exlcusive) to match userId
        newUsers = []
        for i in range(0, numUsers):
            newUsers.append(i)

        for user in newUsers:  # loop through that array, create a user out of each, and add it to the graph
            self.addUser(User(user))

        # Create friendships
        # using the same array (b/c you indexed to zero), for each user, create a randomized array of potential friends, and slice off a random number between 0 and 2*num inclusive of those friends from the front. Loop through that second array (here is the scaling issue) and call the add friendships
        # for user in newUsers:  # O(n)
        #     random_friends = FYS(newUsers)  # O(n)
        #     random_number = random.randint(0, 2*avgFriendships)
        #     if random_number == 0:
        #         pass
        #     else:
        #         for friend in range(0, random_number):  # O(n)
        #             if user == random_friends[friend]:
        #                 pass
        #             elif random_friends[friend] in self.friendships[user] or user in self.friendships[random_friends[friend]]:
        #                 pass
        #             else:
        #                 self.friendships[user].add(random_friends[friend])
        #                 self.friendships[random_friends[friend]].add(user)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

sg = SocialGraph()
sg.populateGraph(10,2)

print(sg.users)