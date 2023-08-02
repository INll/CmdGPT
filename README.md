<h2 align="center">🤖CmdGPT🔧</h2>
<p align="center">This Python project packs ChatGPT into a CLI application.
</p>
<div align="center"><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjBuaTBna3hraXA3YmZsb21ydWUybXVxYmp3ODIyZmVld2tsZDk2ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Xl11AkqgCrseiR8y2b/giphy.gif" width="70%" height="20%" /></div>
<p align="center">Real-time Demonstration (response speed may vary)</p>

## 📝 Description
Runs a Selenium-based headless Chrome browser under the hood, this CLI application connects to Poe.com and access its free ChatGPT service.

*Note: This application **may break** if Poe.com implements anti-bot measures in the future.*

## 🌟 Features
#### Few-shot prompting
Prime ChatGPT with detailed prompts to shape its functionality. Scroll down to preview sample prompts provided in `./prompts`.
#### Multi-line pasting
Accepts pasting long text with Line Breaks through mouse right-click.
<div align="center"><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2V0ZWFtMmk5ZW04YTNqcXJvM3BweHgyYWgxdTF5aDM3OHhoYzMyMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/o4aVPic0NmQq46FokR/giphy.gif" width="70%" height="20%" /></div>
<p align="center">Summarize a long new article then ask a follow-up question</p>

##  🛠️ Project Setup
### 1. Get this repository
```
git clone https://github.com/INll/CmdGPT.git
```
### 1.5 (Optional) Create and activate virtual environment
```
py -m venv $pwd
Scripts\activate
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3. Register an account on Poe.com and duplicate Chrome's `User Data`
This program depends on the ChatGPT service provided by [Poe.com](https://poe.com/ChatGPT). To access it via the command line, you will need to register a free account and login at least once first.

Then, copy your ***entire*** `User Data`  folder to the root directory. This allows the command line to bypass logging into [Poe.com](https://poe.com/ChatGPT) when launched.
### 4. Run script
```
py run.py
```
To enable prompts, add `--prompts`:
```
py run.py --prompts
```
## 📦 Dependencies
```
Selenium
```
