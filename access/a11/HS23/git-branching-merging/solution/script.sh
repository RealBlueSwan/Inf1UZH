git clone $REPO_URL repo
cd repo

git checkout -b feature_x
printf "print(\"Hello World!\")" > hello.py
git add hello.py
git commit -m "Add \"Hello World\" example"
git push origin feature_x

git checkout main
printf "# Good Bye" > bye.py
git add bye.py
git commit -m "Add \"Good Bye\" comment"

git merge feature_x -m "Merge \"feature_x\""

git push
