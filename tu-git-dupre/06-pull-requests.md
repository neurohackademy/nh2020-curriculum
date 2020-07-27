---
title: "Pull Requests"
teaching: 5
exercises: 10
questions:
- "How can I contribute to a repository to which I don't have write access?"
objectives:
- "Understand what it means to fork a repository"
- "Be able to fork a repository on GitHub"
- "Understand how to submit a pull request"
keypoints:
- "A `fork` is a `git clone` into your (GitHub) account"
- "A `pull request` asks the owner of a repository to incorporate your changes"
---

Pull Requests are a great solution for contributing to repositories to which
you don't have write access.
Adding other people as *collaborators* to a remote repository is a good idea,
but sometimes you may not have a specific group of potential collaborators in mind.

This is especially true of open source projects,
in which the community of potential contributors can be very big.
Keeping the source code safe--but at the same allowing new people to make contributions--is one of the keys to success in open source.

Leveraging the power of Git,
GitHub provides a functionality called *Pull Requests*.
Essentially, it's "requesting the owner of the repository to pull in
your contributions".
As the owner of a repository, you may or may not accept a pull request.
But as a contributor, pull requests provide a path to engage with the community.

## The process

- Find a repository on GitHub that belongs to someone else (e.g., https://github.com/emdupre/more-papers)
- **Fork** it on GitHub's servers into your GitHub account
- Then `git clone` it to your PC/laptop
- Make changes, and push them to your repository on GitHub
- Request that the owner of the repository you *forked* pulls in your changes

![Conceptual illustration of a pull request - image adapted from [here](http://acrl.ala.org/techconnect/post/coding-collaboration-on-github)](../fig/github-diagram.png)

## Advice for submitting Pull Requests

- Keep your Pull Request small and focused (makes it easier to process!)
	- Submit one PR per issue
	- Create a separate branch for each issue you work on
	  (you can submit a PR from any branch)
- Take advantage of available resources!
	- If the repository has contributing guidelines, read them!
	- Some repositories pre-populate the body of the PR or issue message
	  with a template.
		- Follow the instructions (e.g. provide the information requested)
- Consider creating a new issue first to discuss your ideas before submitting a PR.
  Some repositories ask for this in their contributing guidelines,
  but this can be a good approach even if it isn't required,
  so that you know whether the owner agrees with your suggestion.
  They might also bring up ideas and/or challenges you haven't considered.

## After submitting your pull request

Your PR may get merged just as it is.
It's very normal, too, for there to be some discussion (on GitHub)
and a request for further edits to be made.
Given that your pull request haven't been merged get,
you can make changes by adding further commits to your branch and pushing them.
In either case, your PR will update automatically once you have pushed your commits.

> ## Exercise
> Let's look at the workflow and try to repeat it:
>
> 1. **Fork** [this
> repository](https://github.com/emdupre/more-papers.git)
> by  clicking on the `Fork` button at the top of the page.
>
> 2. Clone the repository from **YOUR** GitHub account. When you run `git remote -v`
> you should get something like this:
>
> 	```{.output}
>	origin	https://github.com/YOUR_USERNAME/more-papers.git(fetch)
> 	origin	https://github.com/YOUR_USERNAME/more-papers.git(push)
> 	```
>
> 3. `cd` into the directory you just cloned. Make changes you want to contribute.
> Commit and push them back to your repository.
> You won't be able to push back to the repository you forked from
> because you are not added as a contributor!
> 4. Go to your GitHub account and in the forked repository find a green button
> for creating Pull Requests. Click it and follow the instructions.
> 5. The owner of the original repository gets a notification that someone
> created a pull request - the request can be reviewed, commented and merged in
> (or not) via GitHub.
{: .challenge}
