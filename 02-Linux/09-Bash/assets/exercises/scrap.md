# Scrap - Give me your data

## Introduction

There is a plethora of useful data on the web, some of which you might want to **use**/**have** on your system. However, there might not always be an **API** to get it. Fortunately there is a practice (_although not always legal_) called [web scraping](https://www.techopedia.com/definition/5212/web-scraping) to do just that and this exercise will have you explore it.

After learning how to use the [curl](https://curl.haxx.se/) command to **get a page's HTML**. You should write a script to get all the _laptops_ from [this](https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops) webshop page and print each one of them on a line in your terminal. 

The example below shows a possible output format, but the important thing is that for each laptop you have: **the name**, **the price** and **the description**.

``` bash
## Example of output for your script (one line)
Aspire E1-510 | 15.6", Pentium N3520 2.16GHz, 4GB, 500GB, Linux | $306.99
```

Follow the instructions below to guide you through the process.

- Research and learn about the `curl` command.
- Research and learn about **web scraping with the shell**.
- Actually write the script (Tips: you could use `sed`, `cut` or/and `awk`).
- Push your script to your fork of the repository (_same location than the challenge_) with the name `scrap.sh`.

> **NOTE**: Web scraping with shell scripting is not the simplest of things and in the future you will most likely use languages like _Python_ or _Nim-Lang_ with already existing libraries to do it, but you should see this challenge as an opportunity to practice the `cut`, `sed`, and/or `awk` commands.

## Resources

* [Web Scraping with Bash](https://medium.com/@LiliSousa/web-scraping-with-bash-690e4ee7f98d)
* [Linux Shell for Web Scraping](https://www.joyofdata.de/blog/using-linux-shell-web-scraping/)
