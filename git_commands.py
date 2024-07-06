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