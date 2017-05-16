# Cloud Computing Project

This project is for the COMP90024 Cluster and Cloud Computing, including a **tweet harvester, couchDB connector and couchDB processor**.
## Deploy system with Ansilbe
Ansible is used to make the deployment of system automaticly.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.<br/>

### Prerequisites

* Apache CouchDB [Click to install](http://couchdb.apache.org/) [a toturial](https://www.youtube.com/watch?v=nlqv9Np3iAU&t=586s)
* Python 3.XX version

* TwitterAPI

```
pip3 install TwitterAPI
```
* CouchDB lib

```
pip3 install CouchDB
```
* A Twitter Application Account for developer:[apply one](https://apps.twitter.com/)
```
Login with a twitter account and then apply for a application, collect your consumer key and tokens etc.
```
# HOW TO USE IT
## In the file support.py
* change 'search_tweets' to whichever tokens are you going to search.
* change the 'consumer_key','consumer_secret','access_token_key' and 'access_token_secret' to your own token
## Start harvest
```
python3 Tweet.py -c [city] -t [token]
python3 Tweet_by_city.py -c [city] -t [token]
```
The above [city] refers to any major city described by boudning box in support.py, [token] refers to your secret tokens. The city has to be lowcase characters. (see support.py)

## Exception log
* Any exception occured will be record into log file. Usually the only exception is the duplication issue when inserting an existing tweet into database.

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Twitter API](https://github.com/geduldig/TwitterAPI) - API wrapper for harvest


## Versioning
Currently version one
## Authors

* **Zelong Cong** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Professor Richard Sinnott, gave us great pressure to do the project....ORZ....
