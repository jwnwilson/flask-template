# Flask template with docker and circleci setup

A flask swagger template, setup with circle ci and a simple pipeline to get microservices setup.

To see a working / deployed example checkout the `simple` branch. 
https://flask-example-simple-pmeswzvssq-nw.a.run.app/#/

# Getting started

To setup your environment you will need python 3.6+ and invoke and poetry  libraries installed or if you'd like a script to install these globally run:

`./scripts/init_env.sh`

To list available commands run:

`inv -l`

# Commands

## inv lint

run black and isort on the code to make it consistent

## inv run

run the project locally on docker

## inv test

run the rest suite

## Example endpoints
#### Add user 
`curl -d "username=user1&password=abcd" -X POST http://localhost:5000/register`

#### Login
###### _`(Returns Auth Token)`_
`curl -d "username=user1&password=abcd" -X POST http://localhost:5000/user`

#### Add Item
###### _`(Replace with Auth Token)`_
`curl -XGET -H "Authorization: Bearer paste_token_here http://localhost:5000/items/`

# Libraries used in this template

## Flask restful

Flask restful is a framework to make it easier to make a RESTful API, checkout the resources here:

https://flask-restful.readthedocs.io/en/latest/

## Swagger

Swagger is an autodocumentation tool that we can plug into our serializers and it will add that end point to our root path.

I chose flask-apispec as it was the best supported library at time of creating this project and it works with Marshmallow.
https://github.com/jmcarp/flask-apispec

## Marshmallow

A popular serializing library compatible with flask and our swagger implementation

https://marshmallow.readthedocs.io/en/stable/

## Invoke

I've setup project commands using python [invoke](http://www.pyinvoke.org/) which is a nice python wrapper around build commands

# Pipeline

The pipeline here uses [circleci](https://circleci.com/), I tried to create a simple build -> test -> deploy pipeline

I also used circleci orbs to automate the deployment of docker containers to google container registry and creation of
a google cloud run instance. A comprehensive guide is available here:

https://circleci.com/blog/gcp-cloudrun-orb/

# Infrastructure

The infrastructure which is only a database is a terraform script, to use [terraform](https://www.terraform.io/) cli will need to be installed (version 1.0.2).

To use the terraform commands run the invoke wrappers to run from the right folder and handle any auth. To deploy to google download a service account .json file and copy it to the root of this project with the name `service_account.json`

## Terraform commands

### inv tf-init

Will download any terraform plugins we need in this case the google api plugin.

### inv tf-plna

Will connect to google and return the difference between our terraform scripts and reality. Will infor of any changes that need to be made

### inv tf-apply

Will make the changes from plan, will create a DB to be connected to our service

### inv tf-destroy

Will tear down the infrastructure
