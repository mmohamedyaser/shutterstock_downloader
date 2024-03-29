<p align="center">
  <a href="https://github.com/mmohamedyaser/shutterstock_downloader" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/hh0SP1Hl.png" alt="Shutterstock premium downloader"></a>
</p>

<h3 align="center">Shutterstock premium downloader</h3>

<div align="center">

[![Status](https://img.shields.io/badge/Status-Active-green)]()
[![GitHub forks](https://img.shields.io/github/forks/mmohamedyaser/shutterstock_downloader)](https://github.com/mmohamedyaser/shutterstock_downloader/network)
[![GitHub issues](https://img.shields.io/github/issues/mmohamedyaser/shutterstock_downloader)](https://github.com/mmohamedyaser/shutterstock_downloader/issues)
[![GitHub stars](https://img.shields.io/github/stars/mmohamedyaser/shutterstock_downloader)](https://github.com/mmohamedyaser/shutterstock_downloader/stargazers)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/mmohamedyaser/shutterstock_downloader/pulls)

</div>

---

<p align="center"> The project's purpose is to help Shutterstock premium users download multiple images or vectors all in one go.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Installing](#installing)
- [Built Using](#built_using)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

The project's purpose is to help Shutterstock premium users download multiple images or vectors in one go. 
The code also downloads the max resolution of 100 cm width or height depending on the image.

### Prerequisites

Thing you will need to make the program function properly:
 - Python 3

### Installing <a name = "installing"></a>

Let's go one by one:
  - First git clone the repo, using the below command.
  ```
  git clone https://github.com/mmohamedyaser/shutterstock_downloader.git 
  ```
  - To install all python requirements, run the below(Windows OS): 
  ```
  python -m pip install -r requirements.txt
  ```
  - [NEW] Open Chrome browser, click on the person icon left of the three dots.
  - [NEW] Click add. Click continue without account. Give the new profile a name.
  - [NEW] A new browser window will open up. Go to Shutterstock.com and login to your profile. After the login close the browser.
  - [NEW] Open profile.csv, input your Chrome data file location followed by ||| and then the user profile name. (i.e, "C:\Users\username\AppData\Local\Google\Chrome\User Data"|||"Profile 1")
  - The above part is a onetime step. Does not required to be repeated.
  - Now open the urls.csv and insert all your shutterstock image links.
  - Lastly run the below (Windows OS) 
  ```
  python shutterstock_downloader.py
  ```

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Python

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Just a hobby 😉
