#!/bin/sh

# Variables can either be defined and directly used...
SOME_VAR="Hello World!"
echo "${SOME_VAR}"

# ...or provided during script invocation like in this task.
# When this script is executed, the REPO_URL variable will
# already be set, so you should use it in your code *without*
# re-defining it!

# To refer to the REPO_URL variable in this script, use the
# following syntax: "${REPO_URL}"
# including the quotation marks

# Add your terminal commands below. Make sure to first run them
# locally on your machine to have more detailed error output.
# When running your script locally, make sure you provide
# REPO_URL on the command line when invoking script.sh as explained
# in the instructions:
#REPO_URL="some-url" ./script.sh

# Clone the repository at `"${REPO_URL}"` into the folder `repo`.
git clone "${REPO_URL}" repo

# Change the working directory to the new folder (using the command `cd`).
cd repo

# Create a new file `c.txt` with the content `ccc`.
echo "ccc" > c.txt

# Add and commit your changes using the message `Add new file c.txt with some content`.
git add c.txt
git commit -m "Add new file c.txt with some content"

# Push the new commit to the repository.
git push
