#!/usr/local/bin/python

from clarifai.client import ClarifaiApi
import matplotlib.pyplot as plt
import seaborn as sns
import sys


def main():

	# Does the access token stuff
	clarifai_api = ClarifaiApi() # assumes environment variables are set.

	color_palette = []

	for img_id in range(1, len(sys.argv)):
		colors = get_image_colors(clarifai_api, img_id)
		color_palette.append(colors)
		#print color_palette

	color_names = []
	color_probabilities = []
	for image in color_palette:
		for color in image:
			color_names.append(color['w3c']['name'])
			color_probabilities.append(color['density'])
	plot = sns.barplot(color_names, color_probabilities)
	plt.show()


def get_image_colors(clarifai_api, img_id):
	color_palette = []
	img = sys.argv[img_id]
	result = clarifai_api.color_urls(img)

	for img_result in result['results']:
		colors = img_result['colors']
		for color in colors:
			color_palette.append(color)
	return color_palette

if __name__ == '__main__':
    main()
