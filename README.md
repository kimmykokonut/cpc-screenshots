# Automated Screenshot Script
_by [Kim Robinson](https://kimmykokonut.github.io/)_

This project uses headless Playwright in Python to take screenshots of desired urls for documenting before/after website refresh by [PDX Digital Corps](https://digitalcorpspdx.org/) for [Cape Perpetua Collaborative](https://www.capeperpetuacollaborative.org/).
See our report/slideshow [here](https://digitalcorpspdx.org/report).

### Landing Page
| Before | After |
| --- | --- |
| <img src="./src/assets/home-before.png" alt="Landing page before" width="300"> | <img src="./src/assets/home-after.png" alt="Landing page after" width="300">

### Visit Page
| Before | After |
| --- | --- |
| <img src="./src/assets/visit-before.png" alt="Visit page before" width="250"> | <img src="./src/assets/visit-after.png" alt="Visit page after" width="250"><img src="./src/assets/visit-do.png" alt="Visit to do page after" width="250"> |

### 🔧 Built With
![Playwright](https://img.shields.io/badge/-playwright-%232EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## ⌛ Setup

### Clone repository

1. Navigate to the [repository](https://github.com/kimmykokonut/cpc-screenshots).
2. Click the `Fork` button and you will be taken to a new page where you can give your repository a new name and description. Choose "create fork".
3. Click the `Code` button and copy the url for HTTPS.
4. On your local computer, create a working directory of your choice.
5. In this new directory, via the terminal, type
```sh
   $ git clone https://github.com/cpc-screenshots
```
6. View or Edit: On your terminal, type `$ code .` to open the project in VS Code.

### Run Script via Docker Container

1. Download [docker desktop](https://www.docker.com/products/docker-desktop)
2. (Optional) Install [Docker VS Code extension](https://code.visualstudio.com/docs/containers/overview)
3. Build docker image:

```sh
# Build docker image
$ docker build -t cpc-screenshots .
```

4. Run automated script in docker container

```sh
$ docker run -v $(pwd)/screenshots:/screenshots -v $(pwd)/src:/src cpc-screenshots
```

---

## 📝 Notes

Created for a specific url, you will need to alter code depending on differing content of other websites.

The biggest challenges I faced were slower page loads due to animation and waiting for embedded iframes holding youtube videos and 3rd party widgets like EventBrite.  Having to wait for specific iframes to load, or scrolling to the bottom of the page/top of the page made this too challenging for a generic website screenshot tool.  Regardless, this can be used again for Cape Perpetua for documentation or other needs.

### Issues
* pages to manual screenshot:
   - /team: mobile- img blurry regardless of scrolling.
   - /land-sea-symposium: mobile - youtube iframe not visible by playwright, leaving as-is for now. Spent a lot of troubleshooting time, not worth more.

## ⏫ Level Up
   [] refactor code to be more generic/multi-purpose
   ISSUE: Async content like iframes and widgets are page specific and beyond scope of this project.

## 📫 Contact
- GitHub: [@kimmykokonut](https://github.com/kimmykokonut)
- LinkedIn: https://www.linkedin.com/in/robinson-kim/
- Portfolio: https://kimmykokonut.github.io/
