# Welcome to Open-Source Contributor Guide

## Steps to add yourself to the contributors list.

1. You will first need Git, which you can download from [here](https://git-scm.com/downloads).

2. Now head [here](https://github.com/alisolanki/Welcome-to-Open-Source) and click on the `fork` button.

3. On the next page, you will see a `create fork` button, press it.

4. You will land on your forked repo page. Here, you will see a `<> Code` button marked in green. Click on it and copy the URL.

5. Open your terminal, type `git clone <url you copied>`, and press enter.

6. Now you will see a folder named `Welcome-to-Open-Source`. Open it and edit the `README.md` file using any text editor, such as VS Code.

7. Below is a code snippet for reference as to what needs to be **added** to the file. Inside the `<b> </b>` tag, you have to put your name. In the `<a href="">` tag, you have to place your GitHub profile URL. Lastly, you have to place your GitHub profile photo URL inside the `src` tag.

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
           <sub><b>Neeraj Madake</b></sub>
       </a>
   </td>

   <td align="center">
        <a href="https://github.com/SameerShiekh77">
            <img src="https://avatars.githubusercontent.com/u/50289158?v=4"/>
            <br />
            <sub><b>Sameer Shiekh</b></sub>
        </a>
    </td>
   ```

8. Now save your changes and exit the editor. Type `git add .`, followed by `git commit -m "<your name> 🍉"`, and lastly `git push origin master`.

9. Go to your forked repo page, `sync` your fork, and then you will see a green button that says `Open pull request`. Press it and in the comments section, type "Adding my name to the contributor list" and press `create pull request`.

10. You have created a pull request. Wait for a member to review and merge it. 😊

Lastly, GitHub/Git are vital in open-source contributions. To learn more about them, check this blog [here](https://dragon2002.hashnode.dev/git-and-github-must-know-guide#heading-setting-up-github).
