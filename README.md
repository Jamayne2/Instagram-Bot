# Instagram Bot

This is a simple Instagram bot written in Python that can log into an account and automatically like posts. 

## Features

The bot can:

- Log into Instagram using a username and password
- Navigate to the home page feed
- Like posts (up to 10)
- Print the username to confirm login

## Usage

1. Ensure Chrome and chromedriver are installed
2. Input your username and password in the script
3. Run the script using:

```
python instagrambot.py
```

4. Bot will automatically log in and start liking posts

## Modules Used

- Selenium - For browser automation and controlling Chrome
- Time - Adds delays between steps
- OS - For file paths
- Pyautogui - For controlling keyboard/mouse (not used but imported) 

## Customizing

- Change the username and password by modifying the **init** parameters
- Adjust the number of posts to like by changing the loop range
- Add headless option for Chrome instead of visible browser

## Next Steps  

Potential improvements:

- Comment on posts
- Follow/Unfollow users
- Direct message users
- Automate posts
- Run bot headlessly
