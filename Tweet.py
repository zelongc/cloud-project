#!/usr/bin/python

#author: Zelong Cong
# COMP 90024 Cluster and Cloud Computing

from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterRestPager
from TwitterAPI.TwitterError import TwitterConnectionError,TwitterRequestError
from support import *
import argparse
import threading
import connect_db
import datetime
import time


lock=threading.Lock()

# aquire the arguments---Target City
ap = argparse.ArgumentParser()
ap.add_argument("-c","--city",required=True,help="The target city which is going to be harvested")
ap.add_argument("-t","--tokens",required=True,help="The access tokens")
args = vars(ap.parse_args())

#two types of geo_location
#  1. bound box
#  2. a round area given a diameter and radius

geo_for_streaming=city_box[args["city"]]
geo_for_searching=city_box_central[args["city"]]
token_number=int(args['tokens'])
#create a database Object

db=connect_db.db_server(username=db_username,login=db_login)

####### Recreate the function when using the couchDB
def FileSave(content):
    lock.acquire(True)
    try:
        content['_id']=content['id_str']
        db.insert(content)
    finally:
        lock.release()
####################################################

#  streaming must use oAuth1 mode
def Streaming():
    api = TwitterAPI(consumer_key=Auth[token_number]['consumer_key'],
                     consumer_secret=Auth[token_number]['consumer_secret'],
                     access_token_key=Auth[token_number]['access_token_key'],
                     access_token_secret=Auth[token_number]['access_token_secret'],
                     auth_type='oAuth1')

    while 1:
        try:
            r = api.request('statuses/filter', {'track':search_words,'locations':geo_for_streaming})

            print('Begin to get tweets')
            print(r.status_code)
            for item in r.get_iterator():
                if 'text' in item:
                    FileSave(item)

                elif 'message' in item and item['code'] == 88:
                    print('SUSPEND, RATE LIMIT EXCEEDED: %s\n' % item['message'])
                    time.sleep(910)
                    break
                elif 'disconnect' in item:
            #TwitterRequestError is thrown whenever the request fails
            # (i.e. when the response status code is not 200). A status
            # code of 500 or higher indicates a server error which is safe
            # to ignore. Any other status code indicates an error with your
            # request which you should fix before re-trying.
        except TwitterRequestError as e:
            if e.status_code < 500:
                print(e.status_code)
                print('TwitterRequestError')
                # something needs to be fixed before re-connecting
                raise
            else:
                print('TwitterRequestError')
                print()
                # temporary interruption, re-try request
                pass

        #TwitterConnectionError is thrown when the connection times out or is interrupted.
        # You can always immediately try making the request again.
        except TwitterConnectionError:
            print('disconnected from Twitter Connection Error')
            # temporary interruption, re-try request
            pass


def Searching():
    api = TwitterAPI(consumer_key=Auth[token_number]['consumer_key'],
                     consumer_secret=Auth[token_number]['consumer_secret'],
                     access_token_key=Auth[token_number]['access_token_key'],
                     access_token_secret=Auth[token_number]['access_token_secret'],
                     auth_type='oAuth2')

    #https://dev.twitter.com/rest/reference/get/search/tweets
    #result_type:   'mixed' 'recent' 'popular'
    # come with the cursor of Max_id
    r=TwitterRestPager(api,'search/tweets',{'q':search_words,
                                   'geocode':geo_for_searching +',50km',
                                   'result_type':'mixed',
                                   'count':100,
                                   })

    for item in r.get_iterator():
        FileSave(item)
if __name__=="__main__":
    threading.Thread(target=Streaming).start()
    threading.Thread(target=Searching).start()
