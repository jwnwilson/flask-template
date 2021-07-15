# Flask template with docker and circleci setup

A flask swagger template, setup with circle ci and a simple pipeline to get microservices setup.

To see a working / deployed example checkout the `simple` branch. 
https://flask-example-simple-pmeswzvssq-nw.a.run.app/#/

To setup your environment you will need python 3.6+ and invoke library installed or if you'd like to set it up run:

`./scripts/init_env.sh`

To list available commands run:

`inv -l`

## Commands

### inv lint

run black and isort on the code to make it consistent

### inv run

run the project locally on docker

### inv test

run the rest suite

### Example endpoints
#### Add user 
`curl -d "username=user1&password=abcd" -X POST http://localhost:5000/register`

#### Login
###### _`(Returns Auth Token)`_
`curl -d "username=user1&password=abcd" -X POST http://localhost:5000/user`

#### Add Item
###### _`(Replace with Auth Token)`_
`curl -XGET -d "store_id=1&price=2.309" \
 -H "Authorization: Bearer paste_token_here http://localhost:5000/item/xyz`
