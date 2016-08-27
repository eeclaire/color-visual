#!/usr/local/bin/python

from clarifai.client import ClarifaiApi
import seaborn as sns
import sys


def main():

	# Does the access token stuff
	clarifai_api = ClarifaiApi() # assumes environment variables are set.

	for img_id in range(1, len(sys.argv)):
		img = sys.argv[img_id]
		result = clarifai_api.color_urls(img)
		print result


if __name__ == '__main__':
    main()
