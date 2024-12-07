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
# REPO_URL="some-url" ./script.sh

# Clone the repository at `$REPO_URL` into the folder `repo`.
git clone "${REPO_URL}" repo

# Change the working directory to the new folder (using the command `cd`).
cd repo

# Create a new branch with the name `feature_x`
git branch feature_x

# Switch to the newly created branch
git checkout feature_x

# Create a new file `hello.py` with the content `print("Hello World!")`
echo 'print("Hello World!")' > hello.py

# Add and commit the changes using the message `Add "Hello World" example`.
git add hello.py
git commit -m 'Add "Hello World" example'

# Push the new branch to the repository (branches that do not yet exist on the remote must be explicitly named, for example, by invoking `git push origin «your branch»`)
git push origin feature_x

# Switch back to the `main` branch
git checkout main

# To emulate another developer that has worked on the repository in parallel, create a file `bye.py` with the content `# Good Bye`, add it to the index, and commit it to the `main` branch with the commit message `Add "Good Bye" comment`.
echo '# Good Bye' > bye.py
git add bye.py
git commit -m 'Add "Good Bye" comment'

# Now, merge your own feature branch into the `main` branch and use the commit message `Merge "feature_x"`. Like `commit`, `merge` would normally open an editor, but ACCESS is non-interactive, so use the `-m` parameter.
git merge feature_x -m 'Merge "feature_x"'

# Push `main` to the remote.
git push origin main

