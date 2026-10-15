# git bisect demo

To run this demo:
1. Create `bisect_test.py` at the top level of this repo with the following
   contents:

    ```python

    from git_bisect_demo.string_utils import slugify


    def test_slugify_buried_treasure():
        assert slugify("Secret password!") == "You've found the buried treasure!"
    ```

1. Run `git add bisect_test.py && git stash`
1. Create `bisect-test.sh` somewhere outside this directory. For example, in
`$HOME/scripts/bisect-test.sh`. Ensure the script is executable.

    ```sh
    #!/bin/bash

    cd $1
    git stash pop

    pytest bisect_test.py
    STATUS=$?

    git stash

    exit $STATUS
    ```

1. Run the following sequence of commands in this repo to find the commit that introduced a bug:

    ```sh
    git bisect start
    git bisect bad HEAD
    git bisect good v1.0.0
    git bisect run $HOME/scripts/bisect-test.sh $(pwd)
    ```
