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

#NOTE :git merge and git rebase are two important commands in Git for integrating changes from different branches. 
#git merge:
intergrates changes from one branch to another by combining history of branches, creating new commit called merge commit
If there are conflicts, Git will pause the merge and allow you to resolve them manually. Once resolved, you can complete the merge.
Suitable for when you want to maintain a complete history of all commits and see how branches have merged over time.
#git rebase:
is a Git command used to reapply commits on top of another base tip.
It’s a powerful tool for streamlining and cleaning up a feature branch's commit history before merging it into a main branch
Creates a linear history. Rewrites commit history by creating new commits for each commit in the branch being rebased.
#git stash 
is a useful Git command that allows you to temporarily save your working directory's changes (that are not yet committed) and clean the working directory.
This is especially handy when you need to switch branches or pull updates from a remote repository, but you have uncommitted changes that you don’t want to commit just yet.
#git cherry pick 
is a powerful command in Git that allows you to apply the changes introduced by one or more existing commits from one branch to another.
 It is particularly useful when you want to apply specific changes without merging an entire branch