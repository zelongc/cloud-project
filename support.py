#!/usr/bin/python

from TwitterAPI import TwitterAPI


city_box={
    #data come from www.flickr.com/place
    "sydney":"150.6396,-34.1399,151.3439,-33.5780",
    "brisbane":"152.6859,-27.6633,153.4685,-27.0220",
    "melbourne":"144.5532,-38.2250,145.5498,-37.5401",
    "hobart":"147.1762,-42.9619,147.4628,-42.6999",
    "perth":"115.5607,-32.4824,116.4151,-31.4552",
    "adeliade":"138.4421,-35.3490,138.7832,-34.6481",
    "camberra":"148.9960,-35.4799,149.3993,-35.1244",
    "darwin":"130.8151, -12.4882, 130.9691, -12.3293"
}

city_box_central={"sydney":"-33.8563,151.0210",
                  "brisbane":"152.9435,-27.4720",
                  "melbourne":"145.1028, -37.8658",
                  "hobart":"147.3121,-42.8299",
                  "perth":"116.0075,-31.9827",
                  "adeliade":"138.5982,-34.9181",
                  "camberra":"149.1521, -35.2847",
                  "darwin":"130.9042, -12.4082"
                  }

Auth=[
    {
"consumer_key":'',   # Zelong1
"consumer_secret":'LQ',
"access_token_key":'4300575109AvlynKQzN46P',
"access_token_secret":'fXcIHPC95H5mU6LhwOeiLgan'
       },
    {
"consumer_key":'uIN4i4BzvW',      # Aosen 1
"consumer_secret":'9UdK5bF2xyJbP362Jonljbh2qB06',
"access_token_key":'85600724-Qy11kT48LUdLHFt4IUodbL',
"access_token_secret":'0TNXR9j0MERX4X7nfs'
    },

]

auth_type='oAuth1'

db_username=""
db_login=""


##### Pay attention to the delimiter : ‘the twitter’ is the AND twitter, and ‘the,twitter’ is the OR twitter
search_words='the,i,to,a,and,is,in,it,you,of,!,?,.,for,on,my,\'s,that,at'
