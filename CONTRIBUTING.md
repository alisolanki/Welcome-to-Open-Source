# Welcome-to-open-source Contributor Guide

## Steps to add yourself to the contributers list.

1) You will first need git which you can download from [here](https://git-scm.com/downloads).

2) Now head [here](https://github.com/alisolanki/Welcome-to-Open-Source) and click on the `fork` button.

3) On the next page you will see a `create fork` button, press it.

4) You will land on your forked repo page, here you will see a `<> Code` button marked in green, click on it and copy the url.

5) Open your TERMINAL and type git clone <url you copied> and press enter.

6) Now, using `cd` navigate to `Welcome-to-Open-Source`, open VS code using command `code .` and edit the `README.md` file. You can also open the directory manually and can edit the `README.md` file by using any text editor of your choice.

7) Below is a code snippet for reference, this is what you have to add inside `README.md` file as to what has to be ADDED in the file.

    ```
    <td align="center">
        <a href="https://alisolanki.com/">
            <img src="https://avatars.githubusercontent.com/u/55312000?v=4" width="100px;" alt="Ali Solanki"/>
            <br />
            <sub><b>Ali Solanki</b></sub>
        </a>
    </td>
    ```
INSTRUCTIONS TO ADD A NEW `<td> </td>` TAG:
    Inside the `<td> </td>` tag:
        I) Goto In the `href` attribute of `<a>` tag, you have to place your github profile URL or your portfolio website URL there (tip: replace `https://alisolanki.com/` with your URL).
        II) You have to place your profile photo url inside the `src` attribute of the `<img>` tag (tip: replace `https://avatars.githubusercontent.com/u/81459147?v=4` with your profile photo URL and also updtae alt text `Ali Solanki`).
        III) Lastly, inside `<b> </b>` tag of the `<sub> </sub>` tag place your name in there (tip: replace `Ali Solanki` with your Name).


8) Add one such `<td> </td>` tag inside the `README.md` file, Now save your changes and exit the editor.

9) Go back to the terminal where you left inilially after step 6 and there type `git add .`, afterwards `git commit -m "<your name> 🍉"` and lastly `git push origin master`. OR do it directly if using VScode using Ctrl+Shift+G then type your Name followed by 🍉 and then click on commit.

10) Go to your forked repo page, click `Sync fork` to synchronise your fork and then there you will see a button in green which says `Open pull request`, press it and in the comments section type "Adding my name to contributer list" and press on `Create pull request`. Set-up pull request as per on screen instructions and mention your name in Title followed by 🍉.

11) You have created a pull request, wait for a member to review and merge it and do not forget to Add a post on LinkedIn along with the Repo's link and tagging the owner (Ali Solanki) and also add a Tweet with the Repo's link and tagging the owner (alisolankii) :)

Predominantly, GitHub/Git is vital in open-source contributions, to learn more about it check this blog [here](https://dragon2002.hashnode.dev/git-and-github-must-know-guide#heading-setting-up-github).
