# Welcome-to-open-source Contributor Guide

## Steps to add yourself to the contributors list.

1) You will first need git which you can download from [here](https://git-scm.com/downloads).

2) Now head [here](https://github.com/alisolanki/Welcome-to-Open-Source) and click on the `fork` button.

3) On the next page you will see a `create fork` button, press it.

4) You will land on your forked repo page, here you will see a `<> Code` button marked in green, click on it and copy the url.

5) Open your terminal, navigate to your desired directory, and clone your fork:
   ```bash
   git clone <url you copied>
   ```

6) Navigate into the repository directory:
   ```bash
   cd Welcome-to-Open-Source
   ```
   Open and edit `README.md` using any text editor (e.g., VS Code).

7) Below is a code snippet for reference as to what has to be added to `README.md`:
   - Inside the `<b> </b>` tags, place your full name.
   - In the `href` attribute of the `<a>` tag, place your GitHub profile URL.
   - In the `src` attribute of the `<img>` tag, place your GitHub profile picture URL.
   - Set the `alt` attribute of the `<img>` tag to your name.

   > ⚠️ **IMPORTANT:** Add your `<td>...</td>` entry at the **very end** of the table (immediately before `</tbody> </table>`). Do not overwrite, replace, or delete existing contributors.

    ```html
    <td align="center">
        <a href="https://alisolanki.com/">
            <img src="https://avatars.githubusercontent.com/u/55312000?v=4" width="100px;" alt="Ali Solanki"/>
            <br />
            <sub><b>Ali Solanki</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/aryanmangrule402/">
            <img src="https://avatars.githubusercontent.com/u/132284891?v=4" width="100px;" alt="Aryan Mangrule"/>
            <br />
            <sub><b>Aryan Mangrule</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/codewithgaani">
            <img src="https://avatars.githubusercontent.com/u/174890660?v=4" width="100px;" alt="Krishna Bhatt"/>
            <br />
            <sub><b>Krishna Bhatt</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://bytemaster2000.github.io/">
            <img src="https://avatars.githubusercontent.com/u/181435418?v=4" width="100px;" alt="Lakshmi Priya"/>
            <br />
            <sub><b>Lakshmi Priya</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/itsTIMUS">
            <img src="https://avatars.githubusercontent.com/u/55312000?v=4" width="100px;" alt="Sumit Saha"/>
            <br />
            <sub><b>Sumit Saha</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Sahitha03">
            <img src="https://avatars.githubusercontent.com/u/110535773?v=4" width="100px;" alt="Aluri Sai Sahitha"/>
            <br />
            <sub><b>Aluri Sai Sahitha</b></sub>
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
        <a href="https://github.com/misha141">
            <img src="https://avatars.githubusercontent.com/u/39346270?v=4" width="100px;" alt="Misha Kumari"/>
            <br />
            <sub><b>Misha Kumari</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/PriyatoshKumarShahi">
            <img src="https://avatars.githubusercontent.com/u/174815858?v=4" width="100px;" alt="Priyatosh Kumar"/>
            <br />
            <sub><b>Priyatosh Kumar</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Sathvik-Shetty-1569">
            <img src="https://avatars.githubusercontent.com/u/192092160?v=4" width="100px;" alt="Sathvik Shetty"/>
            <br />
            <sub><b>Sathvik Shetty</b></sub>
        </a>
    </td>
    ```

8) Save your changes and return to your terminal. Stage and commit your changes, then push to your fork:
   ```bash
   git add README.md
   git commit -m "<your name> 🍉"
   git push origin <branch-name>
   ```

9) Go to your forked repo page, `sync` your fork and then there you will see a button in green which says `Open pull request`, press it and in the comments section type "Adding my name to contributor list" and press on `create pull request`.

10) You have created a pull request, wait for a member to review and merge it : )

Lastly, GitHub/Git are vital in open-source contributions, to learn more about them check this blog [here](https://dragon2002.hashnode.dev/git-and-github-must-know-guide#heading-setting-up-github).
