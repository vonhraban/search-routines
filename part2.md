# Common query caching in Riak

### Prerequisites

The Riak need to be up and running. 

`docker-compose up -d` will pull it from the docker hub and set up port forwarding 
so that container port 8098 is forwarded to local port 8098

### Creating cache for the top 5 queries

First of all, add the cache. The bucket will be created automatically on demand
if not yet present.

```
curl http://localhost:8098/buckets/hscicNews_search/keys/OR_Care%20Quality%20Commission \
        -XPUT -d '0,1,2,3,4,5,6' \
        -H 'content-type: text/plain'

curl http://localhost:8098/buckets/hscicNews_search/keys/OR_September%202004 \
        -XPUT -d '9' \
        -H 'content-type: text/plain'


curl http://localhost:8098/buckets/hscicNews_search/keys/OR_general%20population%20generally \
        -XPUT -d '6,8' \
        -H 'content-type: text/plain'


curl http://localhost:8098/buckets/hscicNews_search/keys/AND_Care%20Quality%20Commission%20admission \
        -XPUT -d '1' \
        -H 'content-type: text/plain'


curl http://localhost:8098/buckets/hscicNews_search/keys/AND_general%20population%20Alzheimer \
        -XPUT -d '6' \
        -H 'content-type: text/plain'

```

Reading the cached value

```
curl http://localhost:8098/buckets/hscicNews_search/keys/OR_Care%20Quality%20Commission
```


### Monthly indexes

Poupulate the database specifying the index header additionally

```
curl http://localhost:8098/buckets/hscicNews/keys/RESULT:0 \
        -XPUT -d 'June 5 , 2013 : The majority of carers say they are extremely , very or quite ...' \
        -H 'content-type: text/plain' \
        -H 'x-riak-index-month_bin: June 2013'

curl http://localhost:8098/buckets/hscicNews/keys/RESULT:1 \
        -XPUT -d 'July 9 , 2013 : The HSCIC has extended the consultation period on a draft list of ...' \
        -H 'content-type: text/plain' \
        -H 'x-riak-index-month_bin: July 2013'

curl http://localhost:8098/buckets/hscicNews/keys/RESULT:2 \
        -XPUT -d 'June 19 , 2013 : New figures from the Health and Social Care Information Centre ( HSCIC ) show in 2012 ...' \
        -H 'content-type: text/plain' \
        -H 'x-riak-index-month_bin: June 2013'

curl http://localhost:8098/buckets/hscicNews/keys/RESULT:3 \
        -XPUT -d 'June 13 , 2013 : Almost one in five women who gave birth in the North East ...' \
        -H 'content-type: text/plain' \
        -H 'x-riak-index-month_bin: June 2013'

curl http://localhost:8098/buckets/hscicNews/keys/RESULT:4 \
        -XPUT -d 'June 5 , 2013 : The majority of carers say they are extremely ...' \
        -H 'content-type: text/plain' \
        -H 'x-riak-index-month_bin: June 2013'

curl http://localhost:8098/buckets/hscicNews/keys/RESULT:5 \
        -XPUT -d 'April 15 , 2013 Thousands of GP practices around the country that ...' \
        -H 'content-type: text/plain' \
        -H 'x-riak-index-month_bin: April 2013'

curl http://localhost:8098/buckets/hscicNews/keys/RESULT:6 \
        -XPUT -d 'February 19 , 2013 : Mortality among mental health service users aged 19 and over ...' \
        -H 'content-type: text/plain' \
        -H 'x-riak-index-month_bin: February 2013'

curl http://localhost:8098/buckets/hscicNews/keys/RESULT:7 \
        -XPUT -d 'January 23 , 2013 : English A and E departments see the most attendances on a Monday morning ...' \
        -H 'content-type: text/plain' \
        -H 'x-riak-index-month_bin: January 2013'

curl http://localhost:8098/buckets/hscicNews/keys/RESULT:8 \
        -XPUT -d 'December 12 , 2012 : The proportion of final year primary school children who were overweight or obese ...' \
        -H 'content-type: text/plain' \
        -H 'x-riak-index-month_bin: December 2012'

curl http://localhost:8098/buckets/hscicNews/keys/RESULT:9 \
        -XPUT -d 'September 26 , 2012 : Income before tax for UK contract holding GPs fell slightly in 2010 / 11 to  GBP  104' \
        -H 'content-type: text/plain' \
        -H 'x-riak-index-month_bin: September 2012'
```

Retrieving the data by month:

```
> curl localhost:8098/buckets/hscicNews/index/month_bin/June%202013
{"keys":["RESULT:0","RESULT:2","RESULT:4","RESULT:3"]
```

Retrieving particular value:

```
> curl localhost:8098/buckets/hscicNews/keys/RESULT:4
June 5 , 2013 : The majority of carers say they are extremely ...
```

#### Considerations

* The only backend that supports secondary indexes is leveldb, so the backend Riak is run on needs to be leveldb
* Default n_val is 3 which means that the data will be automatically replicated to 3 nodes. This should suffice for
the purposes of caching
* Conflicting values are not really an issue for historical articles, therefore the default conflict resolution strategy
`Causal Context (Siblings Off, fallback to Wall Clock)` is enough
* Given that default values seem to work for us just fine, no custom bucket type needs to be created on this stage.
Perhaps in the future analytics yields more ways this caching settings can be improved and the bucket type can be 
revisited