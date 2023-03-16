from insta_scraper import InstagramScraper
import argparse
import logging

logging.basicConfig(level=logging.INFO)

def main():

	parser = argparse.ArgumentParser(description='Instagram followers scrapper')
	parser.add_argument('--username','-u', help='<Required> set login username', dest='username', action='store', required=True)
	parser.add_argument('--password','-p', help='<Required> set login password', dest='password', action='store', required=True)
	parser.add_argument('--target', '-t', help='set target of scrap, by default is target and username are the same', dest='target', action='store') # scrap other profiles (only work with public profiles)
	parser.add_argument('--list', '-l', help='printing lists, by default unfollowing list option <u>, <fi> following list , <fe> followers list' , dest='list', action='append') # more options of lists

	args = parser.parse_args()

	scrapper = InstagramScraper(args.username, args.password, args.target, args.list)
	logging.info("Creating session")
	scrapper.create_session()

	logging.info("Extracting followers")
	scrapper.scrape_followers()

	logging.info("Extracting following")
	scrapper.scrape_following()

	logging.info("Generating ists. Please check text files")
	scrapper.generate_list()
    

if __name__ == '__main__':
	main()
	



# Backlog    
# add output name
