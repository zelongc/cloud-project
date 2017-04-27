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
"consumer_key":'S2xctvw2btwbmP61f9yfuyeXY',   # Zelong1
"consumer_secret":'cIbAr8Ov0jazGY8Elwilxs5D7jXh8R6WihJKShqLz5Fl3cB3LQ',
"access_token_key":'4300575193-NoZFlFeDchNp09AvEQToKQ9BsrsvLlynKQzN46P',
"access_token_secret":'fXcIHPC9wnXg3bsfuZ5H5mU6nAAyGgFjCBYLhwOeiLgan'
       },
    {
"consumer_key":'uIN4ivMibcf674B3TsL2sizvW',      # Aosen 1
"consumer_secret":'9UdK5bF2xyJEIY68FBHpEKIYRbP362JjwnEE9Bgonljbh2qB06',
"access_token_key":'856007242964844544-Qy11kT48LUdLNATA7kNjWHFt4IUodbL',
"access_token_secret":'0TNXR9j0sFpgzY0trIIobRARG6tOSa19k6xMERX4X7nfs'
    },

    {
"consumer_key":'1ixAh4Yn7ItYrgIdvFHOJCbwu',      # Linlin 1
"consumer_secret":'pqM4dmbtqBbY8dHo8DkuweZ6YgizP0ZTTEwrjM9YVoID009EYy',
"access_token_key":'754531029281497088-4QkRdJN2tp8ReBqKveaMfZXBguon8OF',
"access_token_secret":'50I97xklT9VuBlCvOX3OQnCRnX25igWynzi0KrXapqxXd'
    },

    {
"consumer_key":'WMNfhetpBXOLtRCiU27AmuOOA',      # Linlin 2
"consumer_secret":'jfQnm2QoTWyXiA1kOTGTOQE1GuS1wF7TpMS0GFqkdUll4OIbIL',
"access_token_key":'754531029281497088-B0tEIHKqGrmmQXtii9Yh40Z8RSjJgol',
"access_token_secret":'RxrvdPd4ZeiAygog2DJNOMUxcCyPDSrvzS3FiS1Z5dVKT'
    },
    {
"consumer_key":'YeEH7IEv6HNxav1YfR4g0as6R',      # Zelong 2
"consumer_secret":'aVQFsgcpupJXKyt1AiZsMZQxDGmSPdSGZA4Ay5SnE2Qhh2WyuU',
"access_token_key":'4300575193-cirlUSBMrRo7LIX7NZ3LvWov4b7Lg73voSod8Kd',
"access_token_secret":'zSNoTc99ixUhzFBtnxZvBP8cKg52RGV1SMGTJikpQG88u'
    },
    {
"consumer_key":'GH5DlC8Qpo5VFBxcFNuDeYpa7',      # Linlin 3
"consumer_secret":'36FIuNEnjDbHRT85jJTGJTNPVDTfHM2G0POkvKSixeSPIHLlUR',
"access_token_key":'857490608922820609-HGC6cPzcGyuQkH05wrnZOGHKMvlH32x',
"access_token_secret":'mLxAWoGzLAA9WERUCD1KdHuE4tp4lquKdde6jNJMzx7mn'
    },
    {
"consumer_key":'wI3u0xwn2Qob4VVzpVmS6tkPu',      # Linlin 4
"consumer_secret":'mbR8z9Y7sQ1em1lkSCjk8DxfcTUPzXSh9hmoxV3wIq5OaNLOEF',
"access_token_key":'857490608922820609-TZ95jyfoDx0LMlPQGCtAGEROWZt8iuH',
"access_token_secret":'UyGnjZUemdu37FfKvaJBzZ2pzttg2IVnplpjXbU6N1R1y'
    },
    {
"consumer_key":'q8fS8KggpfccAuoeL25Jf2PGN',      # Jiaying 1
"consumer_secret":'Ca8Cm7Ypf3hWfcn3QTDCjj1pq4gwQJSZxu3eDvUMqSOedOupZq',
"access_token_key":'857490594586804224-jCvKJSsO8YPhvTKerD6Yg1DSpwrgoaE',
"access_token_secret":'mn9k1rDMVO2s99BqUVWwa3yBQFONL5lCKSfc6QTnAy6lB'
    },

    {
"consumer_key":'uEHbY5gapfTwrPXA0uz0EGaCw',      # Jiaying 2
"consumer_secret":'P0YLRyPb2QSYsK1VJpwbR6edSnEFAvMCr8oi0VagH2Y66TW0LK',
"access_token_key":'857490594586804224-qt9hSzvIusUYZGyszfWFlivRoYegVEe',
"access_token_secret":'VTs2d1IidrjvuWuRuIGGIYra2FBOKL5zw7pXVjSvBzDL1'

    }


]

auth_type='oAuth1'

db_username="admin1"
db_login="password"


##### Pay attention to the delimiter : ‘the twitter’ is the AND twitter, and ‘the,twitter’ is the OR twitter
search_words='the,i,to,a,and,is,in,it,you,of,!,?,.,for,on,my,\'s,that,at'
