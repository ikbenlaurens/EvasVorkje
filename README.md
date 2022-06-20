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




### Git

1. install git (if not already installed)
2. configure git (username, .gitconfig etc)
3. ...


### Github
 
1. Create github-account (also useful for portfolio puposes)
2. Fork the current repo to your own account!
  * on https://github.com/ehhalbers/python-dev-env, click [fork]
  * name your fork something senible and confirm

### SSH
 
Connect your repo with git on your laptop via ssh:
1. Creating a ssh-key pair locally on the laptop
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



Clone the repo
1. Clone the repo locally
  * `git clone <url>`
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
  * type `:wq` and press enter
  * run the script in the terminal: `python3 print_me.py` 

 
### Virtual environments & packages

1. Create workspace-folder (<-makes your life easier)/<project folder> and navigate there
  * `$ mkdir ~/workspace/<project_name>` 
  * `$ cd ~/workspace/<project_name>`
2. Create a virtual environment
  * `$ python -m venv venv_<project_name>` the `-m` stands for _import module_ `venv`
  *    ! make sure you have the proper python version.
3. Activate the environment
  * `$ . venv_<project_name>` or `$ source venv_<project_name>`
If the virtual environment is active, you recognise it by th (prefix) in the command line:
  * `$ (venv_<project_name>) blabla`
4. Check which packages are present in the current virtual environment
  * `$ pip freeze`
5. Install some packages
  * `pip install pandas`
  * `pip install django`
  *    ! only install packages _inside_ of your virtual environment.
6. Export the packages to a file <- this will make the life of your colleagues and future you easier, why?
  * `pip freeze >> requirements.txt`
7. Check the requirements-file, what is in there? Have you installed all that?



### PyCharm

1. Install PyCharm (community edition)
  * https://www.jetbrains.com/pycharm/download
   
2. Open project: <project_folder> and check all the settings:
- Check in the terminal that the venv is still activated
- Check The interpreter Python3.10(project) <- should be from the venv, edit interpreter shows the packages
- Check the git branch: dev

3. Set the configuration:
- [Configurations] > Edit configuration
- `+ ` to add, choose 'Python'
  * Name: 'webapp' # or <project_name>
  * Script path: /workspace/<project_folder>/manage.py
  * Parameters: runserver # is a flag that can be added in the terminal
*   ! This is the 'PyCharm'-version of `python manage.py runserver` which is the command with which you can start the webserver in the commandline.
- Make sure the Python Interpreter is referring to the location of the virtual environment
- Make sure the Working directory refers for <project_folder>
-	Run the code
-	Go to http://localhost:8000/my-first-webapp to see if all works 
   
4. Optional: (if the code doesn't run) 
- create debug configuration (bug), similarly to the run-configuration.
- read the error, google it, and solve it ;)

Bonus exercise: 
- change something in the content of the webpage :)

For those who want to know more about Django, the webframework: [RealPython: getting started with Django](https://realpython.com/get-started-with-django-1/)



