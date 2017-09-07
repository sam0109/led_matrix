import Image
import twitter
import text_led
import time

from rgbmatrix import Adafruit_RGBmatrix

api = twitter.Api(consumer_key="srJbKZIU4J2Cy6xbDFVWO5oF9",
                  consumer_secret="5RSXdVyrnOoJZIfZwySi77RtDFRQNWw6Uwlb7Pff2huYRVUqiM",
                  access_token_key="57201894-S8UkCYPEuOlffiVASVIe5FKEhO3RsnS08wgXcuuzZ",
                  access_token_secret="An6seL5SNVYTigN96XCiU67xy3YZeqv4w3GaKdpmJH55i")
results = api.GetSearch(raw_query="q=from%3ArealDonaldTrump%20since%3A2017-08-08&src=typd")

matrix = Adafruit_RGBmatrix(32, 4)
saved_status = ""
while(1):
	statuses = api.GetUserTimeline(screen_name="realDonaldTrump")
	if(saved_status != statuses[0].text):
		saved_status = statuses[0].text
		text_led.scroll_text(matrix, saved_status)
	time.sleep(60)