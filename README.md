# Automated Screenshot Script

This project uses Playwright to take screenshots of various urls for before/after site refresh for PDX DC for CPC

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)

## Setup

1. Clone the repository:

   ```sh
   $ git clone https://github.com/cpc-screenshots
   ```

## Run via Docker Container

1. [Download docker desktop](https://www.docker.com/)
2. (Optional) [Install Docker VS Code extension](https://code.visualstudio.com/docs/containers/overview)
3. Build docker image and run container:

```sh
# Build docker image
$ docker build -t cpc-screenshots .
```

```sh
# Run docker container which runs automated script
$ docker run -v $(pwd)/screenshots:/screenshots -v $(pwd)/src:/src cpc-screenshots
```

---

### Notes

Created for a specific url, you may need to alter code depending on what content.

### Issues
* iframe loading and navbar position when scrolling/waiting for home page load
* pages wip
   - /about: partners not all shwoing up
   - /team- img blurr
   - /learn - youtube not visible
   - /visit: img not visible
      - todepool area
      - hikes
      - trails
