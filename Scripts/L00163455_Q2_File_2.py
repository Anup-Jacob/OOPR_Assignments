# ---------------------------------

# File          : L00163455_Q2_File_2.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 15/11/2021
# Modified Date : 15/11/2021
# Description   :
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

import requests
from bs4 import BeautifulSoup

# my_URL = 'http://192.168.182.128/'
my_URL = input("Enter the URL to be searched for : ")


# Input taken from the user for the url used to search the word

def data_scrape():
    try:
        response = requests.get(my_URL)
        parse_to_html = BeautifulSoup(response.content, "html.parser")
        get_header(parse_to_html)
        find_all = parse_to_html.findAll()

        ''''
        #Commented since used for testing purposes
        #print(find_all)
        #print(find_all[0].text)
        '''

        full_text = find_all[0].text
        # print(full_text)  # Commented to check the full text in the URL

        word = input("Enter the word to be searched for : ")
        # Input taken from the user for the word used to search in the URL
        # lower_word = word.lower()  # test for checking case sensitivity

        word_count = full_text.count(word)

        print("\nThe number of times the word '{}' occurs is : {}".format(word, word_count))

    except Exception as e:
        print(e)


def get_header(web_response):
    page_head = web_response.find("head").text
    print("As per the url generated {}, the heading generated is : {}".format(my_URL, page_head))


if __name__ == '__main__':
    data_scrape()