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


consumer_key='S2xctvw2btwbmP61f9yfuyeXY'
consumer_secret='cIbAr8Ov0jazGY8Elwilxs5D7jXh8R6WihJKShqLz5Fl3cB3LQ'
access_token_key='4300575193-NoZFlFeDchNp09AvEQToKQ9BsrsvLlynKQzN46P'
access_token_secret='fXcIHPC9wnXg3bsfuZ5H5mU6nAAyGgFjCBYLhwOeiLgan'
auth_type='oAuth1'

db_username='admin1'
db_login="password"


##### Pay attention to the delimiter : ‘the twitter’ is the AND twitter, and ‘the,twitter’ is the OR twitter
search_words='trump'
