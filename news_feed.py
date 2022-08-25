import feedparser
import notify2
import os
import time


def parseFeed():
	# feedparser will parse news data from the feed URl
	f = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")

	# Set icon in notification bar
	ICON_PATH = os.getcwd() + "/icon.ico"
	
	# Initialize D-bus connection
	notify2.init('News Notify')

	# Recieves relevant information like title , summary, and notification icon
	for newsitem in f['items']:
		n = notify2.Notification(newsitem['title'],
								newsitem['summary'],
								icon=ICON_PATH
								)
	# Sets urgency level
	n.set_urgency(notify2.URGENCY_NORMAL)

	# Shows notification on the Desktop
	n.show()

	# How long the notifcation shows on the Desktop
	n.set_timeout(15000)

	# Displays news notification every 1200 seconds
	time.sleep(1200)
	
if __name__ == '__main__':
	parseFeed()
