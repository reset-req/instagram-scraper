import instaloader
import numpy as np

class InstagramScraper:

    def __init__(self, username, password, target=None, list=None):
        
        self.username = username
        self.password = password
        
        if target is None:
            self.target = username
        else:
            self.target = target

        if list is None:
            self.list = 'u'
        else:
            self.list = list
            self.list.append('u')

        self.followers_list = []
        self.following_list = []

    def create_session(self):

        L = instaloader.Instaloader(max_connection_attempts=1) # login errors may occur without it
        L.login(self.username, self.password) # Login or load session
        self.target = instaloader.Profile.from_username(L.context, self.target) 
        

    def scrape_followers(self):
       
        for follower in self.target.get_followers():
            self.followers_list.append(follower.username)

    def scrape_following(self):

        for followee in self.target.get_followees():
            self.following_list.append(followee.username)

    def generate_list(self):

        for opts in self.list:    
            
            
            match opts:
                case 'fi':
                    list = self.following_list
                    name = "following_"
                case 'fe':
                    list = self.followers_list
                    name = "followers_"
                case 'u':
                    list = np.setdiff1d(self.following_list, self.followers_list) 
                    name = "unfollowing_"

            filename = name + ".txt" 
            file = open(filename, "w")
            print("People in list: ", list)
            for person in list:
                file.write(person + "\n")
            file.close()




        # Extra description:
        
        # unfollow people who are only in following list and not in followers list
        # now obtain profile metadata from target (before was username)

        ##########################################################################
        # Backlog:

        # there is probably a better way to do target is none...
        # choose better names for flas
        # improve file names
        # save session
