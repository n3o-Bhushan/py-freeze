# py-freeze
A script to generate a requirements.txt file for you automatically. Good for users not familiar with CLI.

# Idea

Recently I worked with some people who are new to python, even though their role might involve usage of Python, it
is limited to analysis purpose. So they struggle with the CLI commands or dependancies. I thought it would be really nice to develop a simple script which will generate requirements.txt and they will be able to share their scripts with other people.

# Requirement

This script is more effective if run in a virtual env. Otherwise it will list all the pip distribution on your machine. 

# Usage

Write your script and once you are done and you feel like sharing your program with your folks, download run py-freeze.py in the same folder of your program with v-env turned on. 

Voila, you will get he requirements.txt generated.
