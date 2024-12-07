#!/bin/sh

# Add your terminal commands here. Make sure to first run them
# locally on your machine to have more detailed error output.
echo "Hello World!"

# Initialize a Git repository in the current folder.
git init

# Create a new file `a.txt` with the content `aaa` (You can achieve this on the command line via `printf "aaa" > a.txt`).
printf "aaa" > a.txt

# Create a new file `b.txt` with the content `bbb`.
printf "bbb" > b.txt

# Add both files to the Git index.
git add a.txt b.txt

# Commit the current index and use the commit message `Add files a.txt and b.txt` (since ACCESS grading is non-interactive, use the `-m` parameter to pass the commit message when committing).
git commit -m "Add files a.txt and b.txt"

# *Append* the text `b2` in a new line to `b.txt` (You can achieve this via `printf "\nb2" >> b.txt`, please note the `\n` and the `>>`)
printf "\nb2" >> b.txt

# Add and commit your changes using the message `Add second line to b.txt`.
git commit -a -m "Add second line to b.txt"
