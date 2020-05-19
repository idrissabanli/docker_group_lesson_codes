## Contributing

The [issue tracker](https://github.com/mauroreisvieira/hello-week/issues) is the preferred channel for bug reports, feature requests, and submitting pull requests.

Please do not use the issue tracker for personal support requests.

Stack Overflow **[Hello Week](https://stackoverflow.com/questions/tagged/hello-week)** is a better place to get help.

#### Setting up your development environment

You'll need a recent version of [Node](https://nodejs.org/en/) to work this project.

Once node is installed, simply clone our repository (or your fork of it) and run `yarn install` or `npm install`

```bash
  $ git clone git@github.com:mauroreisvieira/hello-week.git
  $ cd hello-week && yarn install
```

#### Running development server

```bash
  $ yarn run watch # Listen changes and Hello Week.
  $ yarn run start # Run the files in demos folder.
  $ open http://localhost:8082/# # Open the browser to see the demos.
```

This should aid you in initial development of a component. It's served on port 8080.

#### Building

```bash
  $ yarn run build # Cleans out build/ and builds.
```

#### Linting / Testing

```bash
  $ yarn run lint:ts # Lints typescript using tslint
  $ yarn run:lint:scss # Lints (S)CSS using stylelint

  $ yarn run test #  Only runs the mocha tests
```

#### Feature requests

Feature requests are welcome, but please take a moment to find out whether your idea fits with the scope and aims of the project.
It's up to you to make a strong case to convince the project's developers of the merits of this feature.

To get approval for your feature request, please create an issue on the issue tracker with as much detail and context as possible.

#### Reporting Bugs

A bug is a demonstrable, reproducible problem that is caused by the code in the repository. Good bug reports are extremely helpful, so thanks!

**Guidelines for bug reports:**

1. Use the GitHub issue search — check if the issue has already been reported.
2. Check if the issue has been fixed — try to reproduce it using the latest **develop** branch in the repository.
3. Isolate the problem - you NEED to provide a live example — ideally also create a reduced test case.

This [CodePen](https://codepen.io/anon/pen/prvbMp), [JSFiddle](https://jsfiddle.net/h8x8bvn9/2/) are helpful templates you can fork or clone.

#### Submitting Pull requests

Good pull requests are a amazing help.

They should remain focused in scope and avoid containing unrelated commits.

Adhering to the following process is the best way to get your work included in the project:

[Fork](https://help.github.com/fork-a-repo/) the project, clone your fork, and configure the remotes:

```bash
  $ git clone https://github.com/<your-username>/hello-week.git
  $ cd hello-week
  $ git remote add upstream https://github.com/mauroreisvieira/hello-week.git
```

If you cloned a while ago, get the latest changes from upstream:

```bash
  $ git checkout develop
  $ git pull [--rebase] upstream develop
```

Create a new topic branch (off the main project **develop** branch) to contain your feature, change, or fix:

```bash
  git checkout -b <topic-branch-name>
```

Commit your changes in logical chunks. Please adhere to these [guidelines](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

Use Git's [interactive rebase](https://help.github.com/articles/interactive-rebase) feature to tidy up your commits before making them public.

Locally merge (or rebase) the upstream development branch into your topic branch:

```bash
  $ git pull [--rebase] upstream develop
```

Push your topic branch up to your fork:

```bash
  $ git push origin <topic-branch-name>
```

[Open a Pull Request](https://help.github.com/articles/using-pull-requests/) with a clear title and description against the **develop** branch.

By submitting a patch, you agree to allow the project owner to license your work under the terms of the [MIT License](LICENSE).
