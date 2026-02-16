## How to Add Yourself to the Contributors List

Follow these simple steps:

---

### **1️⃣ Install Git**

You need Git to contribute. Download it here: [Git Downloads](https://git-scm.com/downloads)
After installing, you can use it from your terminal or command prompt.

---

### **2️⃣ Fork the Repository**

1. Go to the repository: [Welcome-to-Open-Source](https://github.com/alisolanki/Welcome-to-Open-Source)
2. Click the **Fork** button at the top-right.
3. Press **Create Fork** on the next page.

> This makes a copy of the project under your GitHub account.

---

### **3️⃣ Clone Your Fork**

1. On your forked repo, click the green **Code** button.
2. Copy the URL (it looks like `https://github.com/your-username/Welcome-to-Open-Source.git`).
3. Open your terminal and type:

   ```bash
   git clone <paste-your-url-here>
   ```
4. Press **Enter**. This downloads the project to your computer.

---

### **4️⃣ Edit the README**

1. Open the folder `Welcome-to-Open-Source`.
2. Open `README.md` in a text editor (VS Code is recommended).
3. Add your information in the **contributors table**.

Here’s an example to copy and edit:

```html
<td align="center">
    <a href="https://github.com/YOUR-GITHUB-USERNAME">
        <img src="YOUR-PROFILE-PIC-URL" width="100px;" alt="YOUR-NAME"/>
        <br />
        <sub><b>YOUR NAME</b></sub>
    </a>
</td>
```

* Replace `YOUR-GITHUB-USERNAME` with your GitHub profile URL.
* Replace `YOUR-PROFILE-PIC-URL` with your profile image link.
* Replace `YOUR NAME` with your full name.

---

### **5️⃣ Save & Push Changes**

1. Save the file and close your editor.
2. In terminal, type:

   ```bash
   git add .
   git commit -m "Added my name 🍉"
   git push origin master
   ```

---

### **6️⃣ Open a Pull Request**

1. Go to your forked repo on GitHub.
2. Click **Sync** if needed.
3. Press the green **Open Pull Request** button.
4. Add a comment: `"Adding my name to contributors list"`
5. Click **Create Pull Request**

> That’s it! 🎉 Now wait for a member to review and merge your PR.

---

Lastly, GitHub/Git are vital in open-source contributions, to learn more about them check this blog [here](https://dragon2002.hashnode.dev/git-and-github-must-know-guide#heading-setting-up-github).
