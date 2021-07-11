#! /bin/bash

echo "Installing invoke & poetry cli tool globally"
pip3 install invoke
pip3 install poetry

echo "Installing dependencies locally for local running / IDE"
virtualenv ./venv
source ./venv/scripts/activate
pip3 install poetry
poetry install

echo "Available commands"
inv -l