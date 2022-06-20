# Ordina Knowlegde Session - "Setting up a Python development environment"
## by Eva Albers & Giuseppe Lecca

**notes beforehand:
- it's a good habit to type stuff <- you learn faster (of course this is up to you, you can also copy the command)
- ...

CONTENT

- Git
- Github
- SSH
- Python
- Virtual Environments
- Package management (pip and pypi)
- PyCharm

REQUIREMENTS

- git
  - gitbash
  - ssh 
- python
- pycharm, CE


### Git

1. Install git (if not already installed)\
mac: `$ git --version`   # see if it exists, if not it prompts to install \
windows: [download git](https://git-scm.com/download/win) 
- on windows, [x] Use bundled OpenSSH
- type "Git Bash" in Windows search and bookmark it on your taskbar. This is your terminal for today.

2. Configure (one time only) your [git configuration](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
```
$ git config --global user.name "Purno de Purno"
$ git config --global user.email purno@purno.com
$ git config --list    # checks which config is there
```

#### Let's make apple pie!
3. Create workspace-folder (<-makes the rest of your life easier) and a project-folder
 navigate there  and  initialize a .git-repository:
```
 $ mkdir ~/workspace/applepie
 $ cd ~/workspace/applepie 
 $ git init                 
```

4. Create the apple pie string and hash it\
Encode: `$ echo "Apple Pie" | git hash-object --stdin -w` \
Decode: `$ git cat-file -p 23991897e13e47ed0adb91a0082c31c82fe0cbe5` \
\
5. Let's create some folder-structure around it 
 * `ls -a` # check what is present in the folder 
 * `mkdir recipes` # make a folder 
 * `vim menu.txt` # create file 
 * `i`, `Apple Pie`, `[ESC]`,`:wq`, `[ENTER]` # fill file with pie 
 * `vim recipes/apple_pie.txt`  # create a new file named apple_pie.txt 
 * insert here `Apple Pie` as well, save the file 
 
 * `rm -rf <dir>` # force remove directory, if you made a mistake 
 * `rm <file>` # to remove file 
 * `cd <dir>` # enter a directory 
 * `cd ..` # go back one directory 

Check that you have the following structure:
```
 applepie/
   recipes/
     apple_pie.txt
   menu.txt
```

6. Add the files git \  
- `git status`  # check which files are tracked, if is it the files that you expect, continue
- `git add *` # add all untracked files to the commit, (note: normally I advice against using `*` for all, since you can accidentally check in unwanted material)
- `git commit -m "First commit!"   # actually store the code in the repository 

7. Now the fun starts: use the following commands to find the apple pie in the recipes-folder. \
- `git log` 
- `git cat-file -p <sha1>` 
Remember: git has `blob`, `tree`, and `commit` 

Optionally: \
8. Modify menu.txt so that it contains Apple Pie and Cheese Cake \
- use vim to open menu add Cheese Cake, save and close the file
- check the status `git status`
- see what has changed `git diff`
- add the menu.txt file `git add menu.txt`
- commit the file `git commit -m "add cheese cake"`
- check the log and see which objects are present in this second commit
Hint: it's no blob, tree or commit.

PS: love yourself, [learn vim](https://vim-adventures.com/![image](https://user-images.githubusercontent.com/59306380/174646861-69a49203-6a81-4ff0-bef6-6cc8723f3e50.png)
)

 
### Github

1. Go to [github.com](https://github.com/) and create github-account (also useful for portfolio puposes)\
note: it is sensible to do this with your private email :)
 
2. Fork the current repo to your own account!
  * on https://github.com/ehhalbers/python-dev-env, click [fork]
  * name your fork something senible and confirm

 
### SSH

Connect your repo with git on your laptop via ssh:
0. Make sure you have ssh installed on your laptop:
  * type `ssh` in the terminal and if you see something like this it is recognized
  * ```
    $ ssh
    usage: ssh [options][options]
 ```
1. Create a ssh-key pair locally on the laptop
  * `ssh-keygen -t ed25519 -C "your_email@example.com"` where `-t` stands for the algorithm and `-C` for #todo...
  * Store the file in the default folder
  * `~/.ssh/id_ed25519`
  * Passphrase can be used, but is often left blank (just press [ENTER])
  * Now the fingerprint of the key is visible and the id_key and id_key.pub are stored on the .ssh folder.

2. Starting the ssh-agent (-> client / server)
  * `$ eval "$(ssh-agent -s)"`
  * expected output: `> Agent pid 59566`

3. Check if you have a config-file in the .ssh folder
  * `$ open ~/.ssh/config`
  * output: `> The file /Users/you/.ssh/config does not exist.`


3b. Create config file (if not present yet, else add the key):
    * `vim ~/.ssh/config`  # note we use again vim here!
    * `i` to go into insert mode and type:
    * ```
      Host github.com
           AddKeysToAgent yes
           UseKeychain yes
           IdentityFile ~/.ssh/id_ed25519
           ```
    * When finished press `[ESC]` (basic mode),`:wq` (write, quit) and `[ENTER]`.
    

4. Adding the ssh key to the configuration-file
  * `ssh-add -K ~/.ssh/id_ed25519`

5. Adding the ssh key to your github account
  * Follow the instructions on the github manual: [Add a SSH key to Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

6.  Test if your ssh connection was established correctly
  * `ssh -T git@github.com` # if it returns your username as configured in your github account, the connection is succesfull and you can continue with cloning or pushing the repo.

All these steps come from: the instructions on github
  * SSH: [generating a new key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

 
### Back to Git

1. Make sure you are still in apple pie
2. add a remote repository to your personal github and push applepie there
 ```
     $ git remote add origin git@github.com:ehhalbers/<your_name>.git
     $ git push -u origin main
 ```
 3. Check on github.com if you see your code. If so, done!
 
>>>>>>>> This can be removed
 
2. Clone the repository present on your github account
  * `git clone https://github.com/<your_nane>/<sensible_name>`
2. Fetch the branches
  * `git fetch` # now all the remote branches appear local (currently only main)
3. Create a new development-branch
  * `git checkout -b dev`
4. Check on which branch you are
  * `git branch` # the checkout branch has a star 
  *   ! You can move between branches with `git switch <branch_name>`
  <do some work>
5. Check the status of your work
  * `git status` # red is not tracked, green is tracked
6. Add the files you need
  * `git add <files you need>`
7. Commit the files you need
  * `git commit -m '<project_name>: <what you did>'` # the `-m` stand for message to add, e.g. `git commit -m "webapp: initial commit"`
8. Push the files to the remote
  * `git push --set-upstream origin dev` # the `--set-upstream` is only necessary once, after that the local branch keeps tracking the remote.


And now you think you're there, but you're not. If you go to github.com and login to your repo, you'll see that there are two branches. The last step is to compare both branches and 'merge' them if it is code you want to keep. This is irl often one with a four eye principle, but for now you can do it yourself.


 If you have done that, you go back to your local terminal, switch to the main branch and pull the new code in `git pull`. What happens with the files?

>>>>>>>> until here

### Python

1. Check current versions
- `python --version` or `python3 -V`
2. Install python
  * mac: `brew install python@3.10`
  * windows: download and install [python3.10](https://www.python.org/downloads/release/python-3104/)
3. Verify that it worked by writing your first python script
  * open a terminal and open python: `$ python3`
    ```
    >>> print(‘me’) 
    me
    >>> quit()
    ```
  * create new python-file: `$ vim print_me.py`
    ```
    print(‘My first Python script works!’)
    ```
  * press `ESC`, type `:wq` and press `[ENTER]`
  * run the script in the terminal: `python3 print_me.py` 

 
### Virtual environments & packages

2. Create a virtual environment
  * `$ python3 -m venv venv_<project_name>` the `-m` stands for _import module_ `venv`
  *    ! make sure you have the proper python version.
  * For more info, check [venv](https://docs.python.org/3/library/venv.html)
3. Activate the environment
  * mac: `$ . venv_<project_name>/bin/activate` or `$ source venv_<project_name>/bin/activate`
  * Windows: `$ source venv_project_name\Scripts\activate.bat`
If the virtual environment is active, you recognise it by th (prefix) in the command line:
  * `(venv_<project_name>) $ `
4. Check which packages are present in the current virtual environment
  * `$ pip freeze`
5. Install some packages
  * `pip install pandas`
  *    ! only install packages _inside_ of your virtual environment.
6. Export the packages to a file <- this will make the life of your colleagues and future you easier, why?
  * `pip freeze >> requirements.txt`
7. Check the requirements-file, what is in there? Have you installed all that?
8. `$ deactivate` will exit the virtual environment




### PyCharm

1. Install PyCharm (community edition)
  * https://www.jetbrains.com/pycharm/download
   
2. Open project: <project_folder> and check all the settings:
- Check in the terminal that the venv is still activated
- Check The interpreter Python3.10(project) <- should be from the venv, edit interpreter shows the packages
- Check the git branch: dev

2b. [Python project structure](https://realpython.com/python-application-layouts/)
                                               
                                               
3. Set the configuration:
- [Configurations] > Edit configuration
- `+ ` to add, choose 'Python'
  * Name: 'main' # or <project_name>
  * Script path: /workspace/<project_folder>/main.py
  * Parameters: input arguments can be proved here if the script requires that
*   ! This is the 'PyCharm'-version of `python main.py flag=true`.
- Make sure the Python Interpreter is referring to the location of the virtual environment
- Make sure the Working directory refers for <project_folder>
-	Run the code

>>>>>> too much
Optionally:
4. Clone webapp from your repository to local

Go to http://localhost:8000/my-first-webapp to see if all works 
   
5. Optional: (if the code doesn't run) 
- create debug configuration (bug), similarly to the run-configuration.
- read the error, google it, and solve it ;)

Bonus exercise: 
- change something in the content of the webpage :)

For those who want to know more about Django, the webframework: [RealPython: getting started with Django](https://realpython.com/get-started-with-django-1/)
   
>>>>>>> end 


