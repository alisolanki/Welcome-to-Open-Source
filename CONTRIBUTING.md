# Welcome-to-open-source Contributor Guide

## Steps to add yourself to the contributers list.

1) You will first need git which you can download from [here](https://git-scm.com/downloads).

2) Now head [here](https://github.com/alisolanki/Welcome-to-Open-Source) and click on the `fork` button.

3) On the next page you will see a `create fork` button, press it.

4) You will land on your forked repo page, here you will see a `<> Code` button marked in green, click on it and copy the url.

5) Open your terminal and type git clone <url you copied> and press enter.

6) Now you will see a folder named `Welcome-to-Open-Source`, open it and edit the `README.md` file using any text editor, VScode for example.

7) Below is a code snippet for reference as to what has to ADDED in the file. Inside the `<b> </b>` tag you have to put your name, in the `<href >` tag, you have to place your github profile URL. And lastly you have to place your github profile photo url inside the `src` tag.

    ```
    <td align="center">
        <a href="https://alisolanki.com/">
            <img src="https://avatars.githubusercontent.com/u/55312000?v=4" width="100px;" alt="Ali Solanki"/>
            <br />
            <sub><b>Ali Solanki</b></sub>
        </a>
    </td>
     <td align="center">
        <a href="https://github.com/neeraj500">
            <img src="https://avatars.githubusercontent.com/u/81459147?v=4" width="100px;" alt="Neeraj Madake"/>
            <br />
            <sub><b>Neeraj Madake
        </a>
    </td>
    ```

8) Now save your changes and exit the editor, type `git add .`, afterwards `git commit -m "<your name> 🍉"` and lastly `git push origin master`.

9) Go to your forked repo page, `sync` your fork and then there you will see a button in green which says `Open pull request`, press it and in the comments section type "Adding my name to contributer list" and press on `create pull request`.

10) You have created a pull request, wait for a member to review and merge it : )

Lastly, GitHub/Git are vital in open-source contributions, to learn more about them check this blog [here](https://dragon2002.hashnode.dev/git-and-github-must-know-guide#heading-setting-up-github).
