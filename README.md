<h2 align="center">🤖CmdGPT🔧</h2>
<p align="center">This Python project packs ChatGPT into a CLI application.
</p>

<div align="center"><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOW03NDYxaDBkZWh5ZWVhajdncGlqcGt4ZnF6YjZ5bmRkdTcza2JyZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L9W6E8DwOjpUziKpOI/giphy.gif" width="60%" height="20%" /></div>
<p align="center">Email Generation + follow-up request</p>
<br /><br />



## 📝 Description
Runs a headless Chrome browser under the hood, this CLI application connects to Poe.com and accesses its free ChatGPT service.


## 🌟 Features
#### Few-shot Prompting 
Prime ChatGPT with detailed prompts to shape its functionality. You will be optionally asked to select a starting prompt when you first launch the program.

#### Multi-line Pasting
Accepts pasting long text with Line Breaks through mouse right-click.

#### Chat Continuation and Reset
After your first response you can either continue the conversation or start over.

<br />
<div align="center"><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWVwMTdxNWdqZ3JlbzliZDRhcGw4M2Zic2JpZDhyc214Y3hrOGFzZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7oLngGMu6M5CN1PSm8/giphy.gif" width="60%" height="20%" /></div>
<p align="center">Teaches you Japanese</p>

##  🛠️ Project Setup
#### 1. Get this repository
```
git clone https://github.com/INll/CmdGPT.git
```
#### 1.5 (Optional) Create and activate virtual environment
```
py -m venv $pwd
Scripts\activate
```
#### 2. Install SeleniumBase
```
pip install seleniumbase
```
#### 3. Set up user profile
This program relies on the free ChatGPT service provided by [Poe.com](https://poe.com/ChatGPT). Like many other websites, you need an account to use its free service.

#### Steps:

1. Create a new Chrome profile, register an account if you haven't, then log in to [Poe.com](https://poe.com/ChatGPT). Close pop-ups, if any.
2. Type `Chrome://version` in the address bar to see path to the new profile folder: `Chrome\User Data\{Your Profile Name}`.
3. **Close Chrome**, then duplicate the **entire** User Data folder *(yes it's large)*. You may ignore missing log files, if prompted.
4. In the duplicated folder, delete all other profiles  (Default, Profile 1, 2, etc) except for the new profile you'd just created.
5. Open `myConstants.py` and update the `USER_DIR` and `PROFILE` keys to the path to the duplicated folder and the new profile name. For example:
```
USER_DIR = 'D:/Chrome profile/User Data/'
PROFILE = 'Profile 3'
```

#### 4. Run it!
```
py run.py
```
## 💪 Motivation
This program frees manual labour from accessing the power of LLMs, hence enabling the following potential applications:

##### **Customer support**
- Analyze support ticket content
- Determine most likely topic out of a list of topics
- Retrieve documentation mapped to that topic
- Respond to support ticket based on materials

##### **Content generation**
- Feed a large collection of sample content
- Generate content
- Populate websites/reviews with high-quality content


Personally though, I see this as a hobby in practising programming and prototyping. The `Wrapper` class has potential to be used in other future projects.

## 📦 Dependencies
```
seleniumbase 4.18.1
```
