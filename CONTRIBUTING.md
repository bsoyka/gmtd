# Contributing Guide

Thank you for choosing to contribute to Give Me the Docs! We welcome
contributions of almost any kind, including ideas, bug reports, and code
contributions. :tada:

## Contributing process

1. Start with an issue. Unless you're making an incredibly trivial fix, create
   an issue first. This allows us to review proposed changes before work is even
   started so no effort is wasted.
    - Wait until you're assigned to an issue before you start working on it.
2. Make your changes on a new branch in a fork of the repository.
    - Don't bump the version of the library. This will be done by a maintainer
      prior to releasing a new version.
3. Commit your changes with a well written [commit message](#commit-messages).
    - Don't commit any changes to files that aren't related to the issue.
4. Push your changes to your fork and create a pull request.
    - Link the original issue in your pull request.
5. Wait for a maintainer to review your changes and give yourself a pat on the
   back! Just make sure to follow up on any comments or reviews you receive.

### Code style and tools

We use an assortment of tools to ensure our code style remains consistent and to
allow easier contributions.

Run the following command to ensure you have the latest versions of all the
necessary development tools installed for this project:

```console
pip install --upgrade autoflake black flit isort poethepoet
```

No additional configuration is needed to use any of these tools once installed.
Most commands you'll need to use can be run using Poe the Poet.

#### Fomatting code

To format Python code in the repository, run the following command:

```console
poe format
```

This will format code and sort imports across the entire project.

#### Installing GMTD locally

To install Give Me the Docs locally for development, run the following command:

```console
poe install
```

This will add a symlink to your site packages directory linking to GMTD in this
repository.

### Commit messages

Commit messages are an important part of contributing to the project. They are
crucial to tracking progress and ensuring that your work is accepted.

Please follow these guidelines when writing a commit message:

- Start your message with an appropriate emoji according to
  [Gitmoji](https://gitmoji.dev/).
- Follow the emoji with one space and a short description of what you changed.
- Start your message with a capital letter.
- Use the imperative mood. (i.e. "Add this" rather than "Added this" or "Adding
  this")
- Don't use puncuation at the end of your message.
- If needed, add additional details in the body of your commit using proper
  English grammar and punctuation.

Here's an example of a good commit message:

> :sparkles: Add flag to open the first result in a browser

## Ideas and bug reports

Sharing suggestions and reporting bugs are incredibly important parts of the
open source workflow.

Before opening an issue, please check over the open
[issues](https://github.com/bsoyka/gmtd/issues) and
[pull requests](https://github.com/bsoyka/gmtd/pulls) to see if your issue has
already been addressed.

Do not open issues or pull requests for security vulnerabilities. Instead,
please see the [relevant section](#security-vulnerabilities) below for
instructions.

Here are some tips to write a great issue:

- Be specific.
- If you're reporting a bug, include detailed instructions to reproduce it.
- Make sure you're using the latest version of the library to see if your issue
  or suggestion has already been resolved.
- Only include one bug or suggestion per issue. Create additional issues for
  additional topics.

### Security vulnerabilities

If you find a security issue in the GMTD library, please report it according to
our [security policy](https://bsoyka.me/security) and do not make an issue or
share the details publicly.

## Code of conduct

By participating in this project and its community, you are expected to uphold
our [code of conduct](https://bsoyka.me/conduct).

If you have any questions or need to report a conduct issue, please email
hello@bsoyka.me.
