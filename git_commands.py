#Git Configuration 
git config --global user.name "ABS"
git config --global user.email "def@gmail.com"
git config --list 

#Basic commands 
git init - initialize local git repo 
git clone URL                 - clone any project 
git status                    -status 
git add [filename]/--all      -add new or changed file in stagging area 
git commit -m "commit msg"    -commit changes 
git rm --cached  [filename]   -pull file back to unstagged /untracked 

#Branching and merging
git branch                    - list all branches 
git branch -a                 - list all branches 
git branch [branchname ]      - create new branch 
git branch -d [branch name ]  - delete branch
git push origin --delete [branch name ] 
git chekckout -b [branchname] - cretate new branch and jump into it 
git chekcout [branchname]     - jump to existing branch 
git switch [branchname]       - switch to branch 
git switch -c [branch name ]  - create and switch to new branch 
git merge branch              - merge chnages in main and other branch 
git stash                     - stash temprorily tracked or untracked changes 
git stash pop                 - bring back all the stashed changes 
git stash list                - list all stash 
git stash clear               - clear all stash 
git rebase [branchname]       - rebase source branch to target branch 
git rebase --continue         - continue ongoing rebasing
git rebase --abort            - abort ongoing rebasing 
git cherry-pick [commit id ]  - infuse speacific commit to branch 

#Remote Repositories 
git remote add <name> <url>   - Adds a remote repository.
git fetch <remote>            - Fetches changes from the remote.
git push <remote> branch      - Pushes local changes to the remote branch.
git pull <remote> branch      - Fetches and merges changes from the remote branch.

#Undo commands 
git reset <file>              - Unstages a specific file
git revert <commit-hash>      - new commit that will undone changes from speacific commit 
git reset --hard <commit-hash>- Resets the repository to the specified commit, discarding all changes.
git reset --soft <commit-hash>- Resets to the specified commit but keeps changes staged.

#version changes 
git diff                      - show changes in working dir 
git diff <commit1> <commit2>  - show changes between two commits 
git show <commit-hash>        - diplay detailed info about a speacific commit 

