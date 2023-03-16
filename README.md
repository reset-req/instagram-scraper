# instagram-scraper

Based on apoorva-dave's instagram-scraper

"Note: This script does not work with accounts where two factor authentication is enabled."

"This python script is to retrieve list of usernames whom you should unfollow :p (People whom you follow but they don't follow you)" - Apoorva-dave

## New Features 

### I - You may target other profiles.

   ` python main.py -u <USERNAME> -p <PASSWORD> -t <TARGET>`
   
   Only works on **open profiles** or private profiles that you `<USERNAME>` are **following**.
### II - Output following and followers list.

`python main.py -u <USERNAME> -p <PASSWORD> -t <TARGET> -l 'fi' -l 'fe'`



## Dependencies

1. Python3 
2. instaloader
3. numpy

## Steps to run

` pip install -r requirements.txt `

not sure if it's working.

Select a account or create a new account.

`
python main.py -u <USERNAME> -p <PASSWORD>
`

If there are special characters in the password use ` " " `.

After running you will receive a output on terminal and a .txt file.

## Additional Instructions

By default generates a file named `unfollowers_.txt` in your directory containing the list of people to unfollow, other flags may be used to create a list of `follower_.txt` and `followings_.txt`.

By default scraped profile is `<USERNAME>`, you may change using 
 `
  python main.py --username <USERNAME> --password <PASSWORD> --target <TARGET> 
 `
 
 
 If you are having trouble logging in try this site https://instaloader.github.io/troubleshooting.html .

## --help

options:

  `--username USERNAME`, `-u USERNAME`
                        <Required> set login username
  
  `--password PASSWORD`, `-p PASSWORD`
                        <Required> set login password
                          
  `--target TARGET`, `-t TARGET`
                        set target of scrap, by default is target and username are the same
                          
  `--list LIST`, `-l LIST`  printing lists, by default unfollowing list option `<u>`, `<fi>` following list , `<fe>` followers list

