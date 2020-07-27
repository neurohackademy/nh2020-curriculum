---
title: "Collaborating with a remote repository"
teaching: 25
exercises: 0
questions:
- "How do I update my local repository with changes from the remote?"
- "How can I collaborate using Git?"
objectives:
- "Understand how to pull changes from remote repository"
- "Understand how to resolve merge conflicts"
keypoints:
- "`git pull` to integrate remote changes into local copy of repository"
---


### Pulling changes from a remote repository

Now when we have a remote repository, we can share it and collaborate with
others (and we can also work from multiple locations: for example from a laptop
and a desktop in the lab). But how do we get the latest changes? One way is
simply to clone the repository every time-- but this is inefficient, especially
if our repository is very large! So, Git allows us to get the latest changes
down from a repository.

We'll first do a "dry run" of pulling changes from a remote repository and
then we'll work in pairs for some real-life practice.

First, let us leave our current local repository,

```
$ cd ..
$ ls
```
{: .language-bash}

```
$ git-papers
```
{: .output}

And let us clone our repository again, but this time specify the local
directory name,

```
$ git clone https://github.com/<USERNAME>/git-papers.git nha-papers
Cloning into 'nha-papers'...
```
{: .language-bash}

So we now have two clones of our repository,

```
$ ls
```
{: .language-bash}

```
$ git-papers nha-papers
```
{: .output}

Let's pretend these clones are on two separate machines!
So then we have 3 versions of our repository:
our two local versions on  separate machines (we're still pretending!)
and one on GitHub.
We can edit one of our clones, add a figures section,
commit the file and push these changes to GitHub:

```
$ cd git-papers 			# Switch to the 'git-papers' directory
$ vim journal.md		# Add figures section
$ git add journal.md
$ git commit -m "Add figures"
$ git push
```
{: .language-bash}

Now let's change directory to our other clone and `fetch` the commits from our remote repository:

```
$ cd ../nha-papers		# Switch to the other directory
$ git fetch
```
{: .language-bash}

We can now see what the differences are by doing,

```
$ git diff origin/master
```
{: .language-bash}

which compares our `master` branch with the `origin/master` branch.
`origin/master` is the name of the `master` branch in `origin`
(which is the alias for our cloned repository); that is, the one on GitHub.

We can then `merge` these changes into our current repository,
but given the history hasn't diverged, we don't need a merge commit.
Instead we get a *fast-forward* merge.

```
$ git merge origin/master
```
{: .language-bash}

```
Updating 0cc2a2d..7c239c3
Fast-forward
 journal.md | 4 ++++
 1 file changed, 4 insertions(+)
```
{: .output}

We can inspect the file to confirm that we have our changes.

```
$ cat journal.md
```
{: .language-bash}

Note that, as a short-hand,
we can do a `git pull` which does a `git fetch` followed by a `git merge`.
Next we will update our repo using `git pull`,
but this time starting with changes in the *nha-papers* folder
(you should already be in the *nha-papers* folder!).
Let's write the conclusions:

```
$ vim journal.md		# Write Conclusions
$ git add journal.md
$ git commit -m "Write Conclusions" journal.md
$ git push origin master
$ cd ../git-papers			# Switch back to the git-papers directory
$ git pull origin master	# Get changes from remote repository
```
{: .language-bash}

This is the same scenario as before, so we get another fast-forward merge!

We can check that we have our changes:

```
$ cat journal.md
$ git log
```
{: .language-bash}

> ## `Fetch` vs `pull`
> If `git pull` is a shortcut for `git fetch` followed by `git merge` then, why would
> you ever want to do these steps separately?
>
> Well, depending on what the commits on the remote branch contain,
> you might want to e.g., abandon your local commits before merging.
>
> Fetching first lets you inspect the changes
> before deciding what you want to do with them.
{: .callout}

### Conflicts and how to resolve them

Let's continue to pretend that our two local, cloned, repositories are hosted
on two different machines.
You should currently be in the original *git-papers* folder.
Let's add an affiliation for each author,
and then push these changes to our remote repository:

```
$ nano journal.md		# Add author affiliations
$ git add journal.md
$ git commit -m "Add author affiliations"
$ git push origin master
```
{: .language-bash}

Now let us suppose, at a later date,
we use our other repository (the `nha-papers` clone) on another machine,
and we want to change the order of the authors.

The remote branch `origin/master` is now ahead of our local `master` branch on the other machine,
because we haven't yet updated our local branch using `git pull`.

```
$ cd ../nha-papers		# Switch directory to other copy of our repository
$ vim journal.md		# Change order of the authors
$ git add journal.md
$ git commit -m "Change the first author" journal.md
$ git push origin master
```
{: .language-bash}
```
To https://github.com/<USERNAME>/git-papers.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/<USERNAME>/git-papers.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
{: .output}

Our push fails, as we've not yet pulled down our changes from our remote
repository!
But don't panic.
Before pushing we should always pull, so let's do that...

```
$ git pull origin master
```
{: .language-bash}

and we get:

```
Auto-merging journal.md
CONFLICT (content): Merge conflict in journal.md
Automatic merge failed; fix conflicts and then commit the result.
```
{: .output}

As we saw earlier, with the fetch and merge,
`git pull` pulls down changes from the
repository and tries to merge them.
It does this on a file-by-file basis,
merging files line by line.
We get a **conflict** if a file has changes that
affect the same lines and those changes can't be seamlessly merged.
We had this situation before in the *branching* episode,
 when we merged a *feature* branch into *master*.
If we look at the status:

```
$ git status
```
{: .language-bash}

we can see that our file is listed as *Unmerged* and if we look at
*journal.md*, we see something like:

```
<<<<<<< HEAD
Author
E DuPre, J Smith
=======
author
J Smith, E DuPre
>>>>>>> 1b55fe7f23a6411f99bf573bfb287937ecb647fc
```

The mark-up shows us the parts of the file causing the conflict and the
versions they come from. We now need to manually edit the file to *resolve* the
conflict. Just like we did when we had to deal with the conflict when we were
merging the branches.

We edit the file. Then commit our changes. Now, if we *push* ...

```
$ vim journal.md		# Edit file to resolve merge conflict
$ git add journal.md		# Stage the file
$ git commit			# Commit to mark the conflict as resolved
$ git push origin master
```
{: .language-bash}

... all goes well!
If we now go to GitHub and click on the "Overview" tab,
we can see where our repository diverged and came together again.

This is where version control proves itself better than DropBox or GoogleDrive!
This allows us to merge text files line-by-line and highlight the conflicts
between them,
so no work is ever lost.

We'll finish by pulling these changes into other copy of the repo,
so both copies are up to date:

```
$ cd ../git-papers			# Switch to 'git-papers' directory
$ git pull origin master	# Merge remote branch into local
```
{: .language-bash}