# Ordina Knowlegde Session - "Setting up a Python development environment"
## by Eva Albers & Giuseppe Lecca

note: it's a good habit to type stuff <- you learn faster (of course this is up to you, you can also copy the commands)

CONTENT

- Git
- Github
- SSH
- Python
- Virtual Environments
- Package management (pip and pypi)
- PyCharm

SOFTWARE TO BE INSTALLED

- git
  - gitbash, included
  - ssh, included
- python
- pycharm, Community Edition


### Git

1. Install git (if not already installed)
- mac: `$ git --version`   # see if it exists, if not it prompts to install 
- windows: [download git](https://git-scm.com/download/win)  
    - during installation choose: 
    - [x] Use bundled OpenSSH 
    - after installation: \
      type "Git Bash" in Windows search and bookmark it on your taskbar. \
      This is your terminal for today.

2. Configure (one time only) your [git configuration](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
```
$ git config --global user.name "Purno de Purno"
$ git config --global user.email purno@purno.com
$ git config --list    # checks which config is there
```
This sets your username and email for all of your git commits.

#### Let's make apple pie!
3. Create a workspace-folder (<-makes the rest of your life easier), a project-folder
 navigate there  and  initialize a .git-repository:
```
 $ mkdir ~/workspace/applepie
 $ cd ~/workspace/applepie 
 $ git init                 
```
You can recognise a git-repository by the `.git` -file that is present in the root of your project. \
`ls -a` shows all files, including hidden (.filename) files. \
`> .. . .git` you should see the .git file in the folder now. 

4. Create the apple pie string and hash it 
- Encode: `$ echo "Apple Pie" | git hash-object --stdin -w` 
  - with this you `echo` (=print) the string apple pie into the input ( `<args for input> | function` ) of 
  the `git hash-object`-function and tell the function to use the `--stdin` (input arguments given). 
  The `-w` writes the output of the function `hash-object` to a `.git`-file.

- Decode: `$ git cat-file -p 23991897e13e47ed0adb91a0082c31c82fe0cbe5` 
  - with this you can decode the hash (`239918...`) back into the byte-value that it was, in this case the string Applie Pie.

Note: that on windows the string encoding is different from mac. Therefore the exact hash on a windows machine is different from that on mac. However, for the functionality of git this doesn't matter.

5. Let's create some folder-structure around it 
- `ls -a` # check what is present in the folder 
- `mkdir recipes` # make a folder 
- `vim menu.txt` # create file 
- `i`, `Apple Pie`, `[ESC]`,`:wq`, `[ENTER]` # fill file with pie 
- `vim recipes/apple_pie.txt`  # create a new file named apple_pie.txt 
- insert here `Apple Pie` as well, save the file 


Check that you have the following structure:
```
 applepie/
   recipes/
     apple_pie.txt
   menu.txt
```

If you accidentally made a type or created a folder in another location:
- `rm -rf <dir>` # force remove directory, if you made a mistake
- `rm <file>` # to remove file
- `cd <dir>` # enter a directory
- `cd ..` # go back one directory 

6. Add the files git 
- `git status`  # check which files are tracked, if is it the files that you expect, continue
- `git add *` # add all untracked files to the commit

note: normally I advice against using `*` for `all`, since you can accidentally check in unwanted material.
Normally it's better to type the files/ folders and only add the ones you actually need:
```commandline
git add recipes/*
git add menu.txt
```
- `git status` # double check that is green what needs to be checked in, and red is what is not part of the commit.
- `git commit -m "First commit!"`  # actually store the code in the repository 

7. Now the fun starts: use the following commands to find the apple pie in the recipes-folder. 
- `git log` 
- `git cat-file -p <sha1>` \
Remember: git has `blob`, `tree`, and `commit` 

Optionally: 
8. Modify menu.txt so that it contains Apple Pie and Cheese Cake 
- use vim to open menu add Cheese Cake, save and close the file
- check the status `git status`
- see what has changed `git diff`
- add the menu.txt file `git add menu.txt`
- commit the file `git commit -m "add cheese cake"`
- check the log and see which objects are present in this second commit. \
Hint: it's no blob, tree or commit.

PS: love yourself, [learn vim](https://vim-adventures.com/![image](https://user-images.githubusercontent.com/59306380/174646861-69a49203-6a81-4ff0-bef6-6cc8723f3e50.png)
)

 
### Github

1. Go to [github.com](https://github.com/) and create github-account (also useful for portfolio puposes)\
note: it is sensible to do this with your private email :)
 
2. Fork, not clone, the current repo to your own account:
   - on https://github.com/ehhalbers/python-dev-env, click [fork]
   - name your fork something senible and confirm
3. Go to your github and check that the fork of the project is present there.

 
### SSH

Goal: Connect your remote repository with git on your laptop via ssh.
1. Make sure you have ssh installed on your laptop:
- type `ssh` in the (gitbash-)terminal and if you see something like this it is recognized
    ```
    $ ssh
    usage: ssh [options][options]
    ```

2. Create a ssh-key pair locally on the laptop
- `ssh-keygen -t ed25519 -C "your_email@example.com"` 
   - where `-t` stands for the algorithm and `-C` to add the github-emailaddress (config?)
- Store the file in the default folder by providing this path to the function:
  - mac: `~/.ssh/id_ed25519` or
  - mac: `/Users/<userfolder>/.ssh/id_ed25519` ! replace userfolder with actual userfolder
  - windows: `/c/Users/<username>/.ssh/id_ed25519`
- Passphrase can be used, but is often left blank (just press [ENTER])
- Now the fingerprint of the key is visible and the id_key and id_key.pub are stored in the .ssh folder.
- Check if the fingerprint is created and the random-art-image appears

3. Starting the ssh-agent (-> client / server)
- `$ eval "$(ssh-agent -s)"` \
  `> Agent pid 59566` # expected output (number can differ)

4. Check if you have a config-file in the .ssh folder, if not create it
- mac: `$ vim ~/.ssh/config`
- windows: `vim /c/Users/<username>/.ssh/config` !! replace  <username> with the folder name on your laptop!

This opens the file regardless of whether it exists, if it exists you see text, if the file is empty enter:
! Make sure the path to the IdentityFile is the same as where your private key is located!  
- mac:
```
Host github.com
   AddKeysToAgent yes
   UseKeychain yes
   IdentityFile ~/.ssh/id_ed25519
```
- windows: !! replace  <username> with the folder name on your laptop!
```
Host github.com
   AddKeysToAgent yes
   IdentityFile /c/Users/<username>/.ssh/id_ed25519
```
- When finished press `[ESC]` (basic mode),`:wq` (write, quit) and `[ENTER]`.


6. Adding the ssh key to your github account
- Copy the content of the .pub-file in your .ssh-folder to github (SSH key input)
- See the instructions on the github manual: [Add a SSH key to Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
  
7. Test if your ssh connection was established correctly
- `ssh -T git@github.com` # if it returns your username as configured in your github account, the connection is succesfull and you can continue with cloning or pushing the repo. 
``` 
Hi ehhalbers! You've successfully authenticated, but GitHub does not provide shell access.
```

All these steps come from the instructions in the github SSH-manual: [generating a new key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

### Clone the repository from your github 

Create a new folder, clone the python_dev_env repository from *your* remote.
1. leave applepie, you also left your git-repo now
- `cd ..` or `cd ~/workspace`
2. Clone the repository present on your github account
- `git clone https://github.com/<your_nane>/<sensible_name_that_you_gave>.git`
3. Go into the folder
- `cd <sensible_name>`
4. Fetch the branches
- `git fetch -vv` # now all the remote branches appear local (currently only main and dev)
    ```commandline
    *main
     dev
    ```
Confirm that you have both branches and that you are on main.



### Python

1. Check current versions
- `python --version` or `python3 -V`
2. Install python
  * mac: `brew install python@3.10`
  * windows: download and install [python3.10](https://www.python.org/downloads/release/python-3104/) 
3. Verify that it worked by writing your first python script
  * open a terminal and open python: `$ python3`
    ```
    >>> print('me') 
    me
    >>> quit()
    ```
  * create new python-file: `$ vim print_me.py`
    ```
    print('My first Python script works!')
    ```
  * press `ESC`, type `:wq` and press `[ENTER]`
  * run the script in the terminal: `python3 print_me.py` 

 
### Virtual environments & packages

1. Create a virtual environment
- `$ python3 -m venv venv_<project_name>` the `-m` stands for _import module_ `venv` \
   ! make sure you have the proper python version. \
For more info, check [venv](https://docs.python.org/3/library/venv.html)
3. Activate the environment
- mac: `$ . venv_<project_name>/bin/activate` or `$ source venv_<project_name>/bin/activate`
- Windows: `$ source venv_project_name\Scripts\activate.bat` 

If the virtual environment is active, you recognise it by th (prefix) in the command line: \
`(venv_<project_name>) $ `
4. Check which packages are present in the current virtual environment
- `$ pip freeze`
5. Install some packages
- `pip install pandas` \
   ! only install packages _inside_ of your virtual environment.
6. Export the packages to a file 
- `pip freeze >> requirements.txt`
   - this will make the life of your colleagues and future you easier, why? see 11.
7. Check the requirements-file, what is in there? Have you installed all that? Those are 'dependencies', 
some packages need other packages to run. Those are installed as well.

8. `$ deactivate` will exit the virtual environment

Optional:
9. Create a new environment called venv_requirements_test
10. activate it
11. Try: `pip install -r requirements.txt`


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
  - Name: 'main' # or <project_name>
  - Script path: /workspace/<project_folder>/main.py
  - Parameters: input arguments can be proved here if the script requires that, e.g. true \
    ! This is the 'PyCharm'-version of `python main.py flag=true`.
  - Make sure the Python Interpreter is referring to the location of the virtual environment
  - Make sure the Working directory refers for <project_folder>
  - Run the code
