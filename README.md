# Introduction
Easily recognized by their symmetric grids and numbered squares, crosswords have provided entertainment and fun for over a century. While crossword puzzles have existed in print media, such as newspapers, for most of their existence, the emergence of the internet and the digital world opened brand new doors of possibility for the future of crosswords.
 
The New York Times (NYT) is widely known and recognized for publishing high-quality and thought-provoking puzzles. They have three types of puzzles: Daily puzzles, which are the standard-size (15x15 grid Monday-Saturday and 21x21 grid on Sunday) puzzles that get released every day; Mini puzzles, which are a 5x5 grid and are released daily; Bonus puzzles, which are released on the first day of every month and typically are strongly tied to a theme.
With such large amounts of data from their app, the NYT has an opportunity to provide users with statistics and visualizations about their solve times. However, nearly no data or insights are provided openly to users.

<img title="NYT Games statistics page" alt="" src="images/readme_images/current_stats_page.png">
A screenshot of the current NYT Daily crossword statics page on their website. There is no statistics page for the mini or bonus puzzles.

With this project, I aim to provide users with insights into their crossword data. Visualizations will show patterns, statistics, and expand upon the statistics that the NYT currently provides.

# Running the App

## 1. Prerequisites
You must be using Python 3.8.8 or higher.

## 2. Clone the Repository
If you have git, this can be done by running the following in a new terminal:

```bash
git clone https://github.com/jorbler/crossword-stats-app.git
```

```bash
cd crossword-stats-app
```

If not, you can download this repository by clicking the green "<> Code" button on the top right of the GitHub repository page and click "Download ZIP" from the dropdown. Unzip this ZIP file and make sure you know where the unzipped folder is located.

Open the terminal and navigate to the location of the folder by typing 

```bash
cd FOLDER_LOCATION
```

if your folder was in your downloads folder, for example, you would type something like 
```bash
cd Downloads/crossword-stats-app
```

If you are having trouble or are getting errors, type `ls` and hit enter. All of the folders/files in the current directory will be listed and you can change the directory one folder at a time.

## 3. Install required packages


```bash
pip install -r requirements.txt
```
**Before running the app, please look at the data section (section 4)**
### To run the app:
```bash 
python3 crossword_app.py
```

## 4. Data
To run the app with your own data, you will first need to get your cookie associated with your NYT Games account, which you can do by following the instructions below.

If you do not have a NYT Games account or do not want to load your own data, there is sample data in the sample_data folder. Delete the data/ folder and rename the sample_data/ folder to data/.

### Getting your cookie

1. Open https://www.nytimes.com/crosswords in Google Chrome.

2. Log in to your account if not already logged in.

3. Click on the three dots in the top right corner of the window
<img title="a title" alt="" src="images/cookie_instructions/menu1.png">

4. Click on "More Tools" and then "Developer Tools"
<img title="a title" alt="" src="images/cookie_instructions/menu2.png">

5. Click on "Application"
<img title="a title" alt="" src="images/cookie_instructions/menu3.png">


6. On the left panel, click "Cookies"; this will show a drop-down menu below. Click on "https://nytimes.com"
<img title="a title" alt="" src="images/cookie_instructions/menu4.png">

7. Under the "Name" column, scroll down to find "NYT-S". The value for your cookie will be in the "Value" column, however it will be truncated. Click on "NYT-S" in the "Name" column. Your full cookie will be in the bottom panel (showed below). Highlight the full cookie and copy it.
<img title="a title" alt="" src="images/cookie_instructions/menu5.png">

8. When you open the app, you will be prompted for your cookie. Paste it in the box and wait for your data to load!





