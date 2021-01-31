import argparse
import logging
import os.path
import requests
import sys
import time

def does_this_file_exist(filename=None):
    logger.debug("does_this_file_exist() started!")
    exists = os.path.isfile(filename)
    logger.debug("exists is: " + str(exists))
    return exists

def fire_a_string_one_at_a_time(url_endpoint, words_to_test):
    logger.debug("fire_a_string_one_at_a_time started!")
    juicy_results = []
    for word in words_to_test:
        logger.debug("Now testing: " + str(word))
        try:
            r = requests.get(url_endpoint + word, timeout=10)
            if r.status_code == 200:
                logger.debug("We found a hit with word: " + str(word))
                juicy_results.append(word)
        except Exception as e:
            logger.debug("We hit an error: " + str(e))
        time.sleep(3)
    return juicy_results

def load_a_bunch_of_strings_into_memory(word_list=None):
    logger.debug("load_a_bunch_of_strings_into_memory started!")
    fo = open(word_list, "r")
    words_in_memory = fo.read().splitlines() 
    logger.debug("words_in_memory is: " + str(words_in_memory))
    fo.close()
    return words_in_memory

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('main_thread_logger')

    # Default Wordlist
    wordlist = "lfi_lols.txt"

    parser = argparse.ArgumentParser(description="Fires lotsa_fun_word.py word list at a given --url, debug mode included")
    parser.add_argument("-u", "--url", required=True, type=str, dest="endpoint", help="The URL endpoint you want to fire the list at.")
    parser.add_argument("-w", "--wordlist", required=False, type=str, dest="wordlist", help="File name of your custom wordlist.")
    parser.add_argument("-d", "--debug", required=False, dest="debug_switch", action="store_true", help="This flag will set logging to Debug mode.")

    results = parser.parse_args()

    if results.debug_switch == True:
        logger.setLevel(logging.DEBUG)
        logger.debug("User has requested debugging mode!")

    if results.wordlist is not None:
        logger.debug("User has requested a custom word list.")
        does_file_exist = does_this_file_exist(results.wordlist)
        if does_file_exist == False:
            logger.debug("The user requested to use a word list that does not appear to exist on disk.")
            logger.info("I'm sorry, the word list you requested: " + str(results.wordlist) + " does not appear to exist. Exiting now!")
            sys.exit()
        else:
            wordlist = results.wordlist

    words = load_a_bunch_of_strings_into_memory(wordlist)
    logger.debug("The words we've loaded into memory are...get ready for this:\n")
    logger.debug(words)

    logger.info("Starting Test For Fun Files Now!")
    juicy_results = fire_a_string_one_at_a_time(results.endpoint, words)
    logger.debug("juicy_results is: " + str(juicy_results))