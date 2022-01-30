""" File: scrape-gofundme-donation-history.py
Author: Kevin Dick
Date: 2022-01-30
---
Description: a simple scraper to extract donation history (public information)
from a GoFundMe page. Currently the script is limited to only the latest donations
(approx. 40 entries) however with autoscrolling implemented, this could be extended to
a longer history of donations.

Students using this for the basis of their projects should implement autoscrolling with something like:
https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python

NOTE: This script is intended for demonstrative purposes only.
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from datetime import datetime
import numpy as np
import pandas as pd
import time
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-i', '--input_fundraiser', required=True,
                    help='input fundraiser name, from the GoFundMe target URL')
parser.add_argument('-c', '--write_to_csv', action='store_true',
                    help='outputs scraped data to a CSV file')
parser.add_argument('-s', '--write_source_html', action='store_true',
                    help='outputs scraped website HTML to file')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='increase verbosity')
args = parser.parse_args()

# EXAMPLE: python scrape-gofundme-donation-history.py -i taking-back-our-freedom-convoy-2022 -c -s -v

def write_tuples_to_CSV(combined_data):
	""" write_tuples_to_CSV
	    Writes the combined tuples to CSV with a date-time naming convention to avoid overwrites.
	    INPUT: combined_data, a list of three-tuples to write to CSV.
	    OUTPUT: None
	"""
	now = datetime.now()
	now_str = now.strftime("%Y-%m-%d-%Y_%H-%M-%S")
	out_str = "\n".join([f'{tup[0].strip()},{tup[1].strip()},{tup[2].strip()}' for tup in combined_data])
	open(f'{args.input_fundraiser}_{now_str}.csv', 'w').write(out_str)

def write_page_source_to_file(page_src):
	""" write_page_source_to_file
            Writes the scraped source page html to file with a date-time naming convention to avoid overwrites.
            INPUT: page_src, the html content to write to file.
            OUTPUT: None
	"""
	now = datetime.now()
	now_str = now.strftime("%Y-%m-%d-%Y_%H-%M-%S")
	open(f'{args.input_fundraiser}_{now_str}.html', 'w').write(page_src)

def main():
	""" main function """
	# Page base url appends /donations/ to bring up the overpage with donation history
	base_url  = f'https://www.gofundme.com/f/{args.input_fundraiser}'
	query_url = f'{base_url}/donations/'
	
	# Make sure your own executable is downloaded and placed in this directory (get it from here https://chromedriver.chromium.org/downloads)
	driver = webdriver.Chrome('./chromedriver')
	
	# Download the webpage into a parseable tree
	driver.get(query_url)
	
	# Use Chrome Developer Tools to identfy the type of element you want to pull from the page
	elems_to_parse = driver.find_elements_by_xpath('//*[@id="portal"]/div/div/div/div[3]/div/div/div/div[2]/ul')[0]
	
	if args.verbose: print(elems_to_parse)
	
	# Extract from the elems parse tree the individual elements of interest; store as equally sized lists
	names = elems_to_parse.find_elements_by_class_name("m-person-info-name")
	amounts = elems_to_parse.find_elements_by_class_name("weight-900")
	time_since = elems_to_parse.find_elements_by_class_name("m-meta-list-item")
	time_since = [i for i in time_since if  not '$' in i.text] # remove duplicate amounts in capture
	print([i.text for i in names])
	print([i.text for i in amounts])
	print([i.text for i in time_since])
	# Combine each of the elements of interest into a three-tuple: (<donor-name>, <donated-amount>, <time-since-donation>)
	combined = [(names[i].text, amounts[i].text, time_since[i].text) for i in range(len(names))]
	
	# Print to terminal if verbosity is set
	if args.verbose: print([f"\n{i}th Donator:\n{combined[i]}" for i in range(len(combined))])
	
	# Write the data to CSV if flag present
	if args.write_to_csv: write_tuples_to_CSV(combined)

	# We can also save all of the page source to a variable and parse later:
	if args.write_source_html: write_page_source_to_file(driver.page_source)
	
	driver.close()

if __name__ == "__main__": main()
