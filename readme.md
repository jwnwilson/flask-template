# Flask template with docker and circleci setup

To setup your environment you will need python 3.6+ and invoke library installed or if you'd like to set it up run:

`./scripts/init_env.sh`

To list available commands run:

`inv -l`

## Commands

### inv lint

### inv run

### inv test

### inv deploy

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
