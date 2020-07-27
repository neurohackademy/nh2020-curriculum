---
title: "Getting started with GitHub"
teaching: 25
exercises: 0
questions:
- "What is a remote repository?"
- "How can I use GitHub to work from multiple locations?"
objectives:
- "Understand how to set up remote repository"
- "Understand how to push local changes to a remote repository"
- "Understand how to clone a remote repository"
keypoints:
- "Git is the version control system: GitHub is a remote repositories provider."
- "`git clone` to make a local copy of a remote repository"
- "`git push` to send local changes to remote repository"
---

We're going to set up a remote repository that we can use from multiple
locations. The remote repository can also be shared with colleagues, if we want
to.

### GitHub

[GitHub](http://GitHub.com) is a company which provides remote repositories for
Git and a range of functionalities supporting their use. GitHub allows users to
set up  their private and public source code Git repositories. It provides
tools for browsing, collaborating on and documenting code. GitHub, like other
services such as [GitLab](https://about.gitlab.com/) and
[Bitbucket](https://bitbucket.org),  supports a wealth of resources to support
projects including:

* Browsing code from within a web browser, with syntax highlighting
* Software release management
* Issue and bug tracking
* Project management tools

### GitHub for research

GitHub **isn't** the only remote repositories provider.
It is very popular, however, particularly within the open source communities.

Also, GitHub has [functionality which is particularly useful
for researchers](https://github.com/blog/1840-improving-github-for-sciences)
such as making code citable!

---

### Get an account

Let's get back to our tutorial. We'll first need a GitHub account.

[Sign up](https://GitHub.com) or [sign in](https://GitHub.com) if you already have an account.

### Create a new repository

Now, we can create a repository on GitHub,

* Log in to [GitHub](https://GitHub.com/)
* Click on the **Create** icon on the top right
* Enter Repository name: "git-papers"
* For the purpose of this exercise we'll create a public repository
* Since we'll be importing a local repository, make sure that **Initialize this repository with a README** is **unselected**
* Click **Create Repository**

You'll get a page with new information about your repository. We already have
our local repository and we will be *pushing* it to GitHub,
so we can do the following:

```
$ git remote add origin https://github.com/<USERNAME>/git-papers.git
```
{: .language-bash}

This line sets up an alias `origin`,
to correspond to the URL of our new repository on GitHub.

### Push locally tracked files to a remote repository

Now we can execute the following:

```
$ git push -u origin master
```
{: .language-bash}
```
Counting objects: 32, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (28/28), done.
Writing objects: 100% (32/32), 3.29 KiB | 0 bytes/s, done.
Total 32 (delta 7), reused 0 (delta 0)
To https://github.com/emdupre/git-papers.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
```
{: .output}

This **pushes** our `master` branch to the remote repository, (named via the alias `origin`) and creates a new `master` branch in the remote repository.

Now, on GitHub, we should see our code,
and if we click the `Commits` tab we should see our complete history of commits.

Our local repository is now available on GitHub.
This means that anywhere we can access GitHub,
we can access our repository!

### Push other local branches to a remote repository

Let's push each of our local branches into our remote repository:

```
$ git push origin branch_name
```
{: .language-bash}

The branch should now be created in our GitHub repository.

To list all branches (local and remote):

```
$ git branch -a
```
{: .language-bash}

> ## Deleting branches (for information only)
> **Don't do this now.** This is just for information.
> To delete branches, use the following syntax:
>
> ```
> $ git branch -d <branch_name>			# For local branches
> $ git push origin --delete <branch_name>	# For remote branches
> ```
> {: .language-bash}
{: .callout}

### Cloning a remote repository

Now, let's do something drastic!
But before that step,
**make sure that you pushed all your local branches into the remote repository!**

```
$ cd ..
$ rm -rf git-papers
```
{: .language-bash}

Gulp! We've just wiped our local repository!
But, because we've pushed to GitHub, we have still have a copy!
We can just copy the repository down using `git clone`:

```
$ git clone https://github.com/<USERNAME>/git-papers.git
```
{: .language-bash}
```
Cloning into 'git-papers'...
remote: Counting objects: 32, done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 32 (delta 7), reused 32 (delta 7), pack-reused 0
Unpacking objects: 100% (32/32), done.
Checking connectivity... done.
```
{: .output}

Cloning creates an exact copy of the repository. By default it creates
a directory with the same name as the name of the repository.

Now, if we change into *git-papers* we can see that we have our repository,

```
$ cd git-papers
$ git log
```
{: .language-bash}
and we can see our Git configuration files too:

```
$ ls -A
```
{: .language-bash}

In order to see the other branches locally, we can check them out as before:

```
$ git branch -r					# Show remote branches
$ git checkout paperWJohn			# Check out the paperWJohn branch
```
{: .language-bash}

### Push changes to a remote repository

We can use our cloned repository just as if it were the original, local repository !
So, let's make some changes to our files and commit these.

```
$ git checkout master				# We'll continue working on the master branch
$ vim journal.md				# Add results section
$ git add journal.md				# Stage changes
$ git commit
```
{: .language-bash}

Having done that, how do we send our changes back to the remote repository?
We can do this by *pushing* our changes:

```
$ git push origin master
```
{: .language-bash}

If we now check our GitHub page we should be able to see our new changes under
the *Commit* tab.

To see all configured remotes for this repository (we can have multiple!),
type:

```
$ git remote -v
```
{: .language-bash}
{: .language-bash}
