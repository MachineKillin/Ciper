import random, urllib, os, threading, configparser, datetime, time, requests, re, static_ffmpeg
from bs4 import BeautifulSoup
from ctypes import windll
from colorama import Fore, init
from tkinter import filedialog
from urllib.parse import urlparse, parse_qs, unquote
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from pytesseract import *
e = datetime.datetime.now()
current_date = e.strftime("%Y-%m-%d-%H-%M-%S")
bypass, bypasscook, imgurl = "", "", ""
page, dupe, valid, line, parsed, ppm, ppm1, linkes, error, tries, ink, num, errors, upm, upm1 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
dorks, results = [], []
blacklist = ['bing.com','php.net','wikipedia.org','stackoverflow.com','amazon.com','microsoft.com','youtube.com','reddit.com','quora.com','telegram.org','facebook.com','apple.com','twitter.com','instagram.com','cracked.io','nulled.to','yahoo.com','github.com','books.google','books.google.nl','google.nl']
init()
reset = Fore.RESET
black = Fore.BLACK
blue = Fore.BLUE
cyan = Fore.CYAN
green = Fore.GREEN
gray = Fore.LIGHTBLACK_EX
lightblue = Fore.LIGHTBLUE_EX
lightcyan = Fore.LIGHTCYAN_EX
orange = Fore.LIGHTGREEN_EX
pink = Fore.LIGHTMAGENTA_EX
lightred = Fore.LIGHTRED_EX
lightwhite = Fore.LIGHTWHITE_EX
lightyellow = Fore.LIGHTYELLOW_EX
magenta = Fore.MAGENTA
red = Fore.RED
white = Fore.WHITE
yellow = Fore.YELLOW
logo = f''' 
        {green}▄████▄  ██ ██████  █████ ██▀███▄ 
        ██▀ ▀█  ██ ██   ██ █   ▀ ██   ██
        ██    ▄ ██ ██  ██{orange}▓{green} ███   ██  ▄█{orange}▒{green}
        ██▄ ▄██ ██ ██▄█{orange}▓▒{green}  █   ▄ ██▀▀█▄  
        {orange}▒{green}████▀  ██ ██{orange}▒ ░   {green}█████ ██  {orange}▒{green}██
        {orange}░░▒ ▒   ▓  ▓▒░ ░   ░ ▒░  ▒▓  ▒▓
         ░  ▒   ▒  ▒ ░     ░ ░   ░▒   ▒
                ▒  ░         ░   ░░   ░ 
                ░            ░    ░{green}\n'''
headerz = [{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0'},
{'User-Agent' : 'Mozilla/5.0 (X11; Linux ppc64le; rv:75.0) Gecko/20100101 Firefox/75.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/75.0'},
{'User-Agent' : 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:75.0) Gecko/20100101 Firefox/75.0'},
{'User-Agent' : 'Mozilla/5.0 (X11; Linux; rv:74.0) Gecko/20100101 Firefox/74.0'},
{'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/73.0'},
{'User-Agent' : 'Mozilla/5.0 (X11; OpenBSD i386; rv:72.0) Gecko/20100101 Firefox/72.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:71.0) Gecko/20100101 Firefox/71.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:70.0) Gecko/20191022 Firefox/70.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:70.0) Gecko/20190101 Firefox/70.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 9.1; en-US; rv:12.9.1.11) Gecko/20100821 Firefox/70'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:69.2.1) Gecko/20100101 Firefox/69.2'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:68.7) Gecko/20100101 Firefox/68.7'},
{'User-Agent' : 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577'},
{'User-Agent' : 'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931'},
{'User-Agent' : 'Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}]

def filter(link):
    try:
        o = urlparse(link, 'http')
        if o.netloc and 'google' not in o.netloc: return link
        if o.netloc and o.path.startswith('/url'):
            try:
                link = parse_qs(o.query)['url'][0]
                o = urlparse(link, 'http')
                if o.netloc and 'google' not in o.netloc: return link
            except KeyError: pass
        if link.startswith('/url?'):
            try:
                link = parse_qs(o.query)['q'][0]
                o = urlparse(link, 'http')
                if o.netloc and 'google' not in o.netloc: return link
            except KeyError:
                link = parse_qs(o.query)['url'][0]
                o = urlparse(link, 'http')
                if o.netloc and 'google' not in o.netloc: return link
    except Exception: pass
    return None

def tokenextract(driver):
    try:
        token = driver.get_cookie('GOOGLE_ABUSE_EXEMPTION')['value']
        print(token)
        bypass = token
    except:
        pars = str(urlparse(url))
        print(pars)
        token = str(re.findall("(?<=GOOGLE_ABUSE_EXEMPTION=).+?(?=; path=/;)", str(pars)))
        print(token)
        token = token.replace("['", "").replace("']", "")
        print(token)
        bypass = token
    return bypass

def imagesolve(driver):
    try:
        parent_element = driver.find_element(By.ID, "captcha-form")
        element = parent_element.find_element(By.TAG_NAME, "img")
        element.screenshot('captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        os.remove('captcha.png')
        print(text)
        driver.find_element(By.XPATH, "//input[@id='captcha']").send_keys(text)
        time.sleep(0.5)
        driver.find_element(By.NAME, "btn-submit").click()
    except Exception as e:
        print(e)
    
def solver(url):
    global bypass
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)
    #if "To continue, please type the characters below:" in driver.find_element(By.XPATH, "/html/body").text:
        #imagesolve(driver)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'logo')))
        #time.sleep(1)
        #bypass = tokenextract(driver)
        #this was coded to bypass the other type of captcha google will give when too many requests
    try:
        recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
        solver = RecaptchaSolver(driver=driver)
        solver.click_recaptcha_v2(iframe=recaptcha_iframe)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'logo')))
            time.sleep(1)
            bypass = tokenextract(driver)
        except:
            if "Your computer or network may be sending automated queries. To protect our users, we can't process your request right now. For more details visit" in driver.find_element(By.XPATH, "/html/body").text:
                print("ip banned")
                time.sleep(10)
    except:
        print("no captcha to solve")
    driver.close()
    driver.quit()

def parser(dork):
    global page, ppm, errors, url, bypass, parsed, valid, dupe, ink, upm, linkes
    if bypass == "":
        url = f'https://www.google.com/search?q={urllib.parse.quote(dork)}&start={page*10}'
    else:
        url = f'https://www.google.com/search?q={urllib.parse.quote(dork)}&google_abuse=GOOGLE_ABUSE_EXEMPTION={bypass}&start={page*10}'
    try:
        cookie = {'GOOGLE_ABUSE_EXEMPTION':bypass, 'CONSENT':'YES+'}
        req = requests.get(url=url, headers=random.choice(headerz), cookies=cookie)
        soup = BeautifulSoup(req.text, 'html.parser')
        if "Our systems have detected unusual traffic from your computer network." in req.text:
            if f"Your search - {dork} - did not match any documents." in req.text:
                pass
            elif "sorry/index?continue=" in req.url:
                print(cyan+"Grabbing Token! (Please Wait Around 10-20 Seconds.)")
                solver(req.url)
                parser(dork)
        else:
            for d in soup.find_all("div", class_="yuRUbf"):
                for a in d.find_all('a'):
                    link = a['href']
                    upm+=1
                    linkes+=1
                    filter(link)
                    link = unquote(link)
                    if "translate.google.com" in link: link = link.split("&u=")[1]
                    if link not in results:
                        results.append(link)
                        domain = urlparse(link).netloc
                        try: domain = domain.replace("www.","")
                        except: pass
                        if domain not in blacklist:
                            if '=' in link:
                                valid+=1
                                ink+=1
                                with open(r'results/Parser/'+current_date+r'/Filtered.txt', 'a') as File: File.write(link) + File.write('\n')
                                if mode == "log": print(green+link)
                            else:
                                with open(r'results/Parser/'+current_date+r'/Unfiltered.txt', 'a') as File: File.write(link) + File.write('\n')
                                if mode == "log": print(red+link)
                    else: dupe+=1
        if ink == 0 or page >= pages:
            page=0
            parsed+=1
            dorkstart()
        else:
            ink=0
            page+=1
            parser(dork)            
    except:
        errors+=1
        page=0
        parser(dork)

def dorkstart():
    global ext, line, dork
    dork = ext[line].strip()
    line+=1
    threading.Thread(parser(dork)).start()

def loadconfig():
    global pages, mode, tries, threads
    if not os.path.exists('results/Parser/'+current_date):
        os.makedirs('results/Parser/'+current_date)
    if not os.path.isfile("config.ini"):
        config = configparser.ConfigParser(allow_no_value=True)
        config['ParserSettings'] = {'; cli/log': None, 'Mode': 'log', 'MaxPages': '10'}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    read_file = configparser.ConfigParser()
    read_file.read('config.ini')
    pages = int(read_file['ParserSettings']['MaxPages'])
    mode = str(read_file['ParserSettings']['Mode'])

def cliscreen():
    global parsed, ext, linkes, dupe, upm, upm1, error, valid, sqls, MySQL, MsSQL, PostGRES, Oracle, MariaDB, none, errorr
    upm1 = upm
    upm = 0
    os.system('cls')
    windll.kernel32.SetConsoleTitleW(f"Ciper Parser By KillinMachine | Parsed: {parsed}/{len(ext)} | Links: {linkes} | Duplicates: {dupe} | Valid: {valid} | Errors: {error} | UPM: {upm1*60}")
    print(logo)
    print(f'''   {orange}Parsing{green}
 Parsed: {yellow}{parsed}/{len(ext)}{green}
 Links: {yellow}{linkes}{green}
 Duplicates: {yellow}{dupe}{green}
 Valid: {yellow}{valid}{green}
 Error's: {yellow}{error}{green}
 UPM: {yellow}{upm1*60}{green}''')
    time.sleep(1)
    threading.Thread(target=cliscreen, args=()).start()

def logscreen():
    global parsed, ext, linkes, dupe, upm, upm1, error, valid
    upm1 = upm
    upm = 0
    windll.kernel32.SetConsoleTitleW(f"Ciper Parser By KillinMachine | Parsed: {parsed}/{len(ext)} | Links: {linkes} | Duplicates: {dupe} | Valid: {valid} | Errors: {error} | UPM: {upm1*60}")
    time.sleep(1)
    threading.Thread(target=logscreen, args=()).start()

def main():
    global ext, threads, num
    static_ffmpeg.add_paths()
    os.system('cls')
    loadconfig()
    print(logo)
    windll.kernel32.SetConsoleTitleW("Ciper Parser By KillinMachine")
    print(" Select your Dork's. ")
    file_path = filedialog.askopenfilename()
    file = open(file_path, 'r+', encoding='utf-8', errors='ignore')
    with file as e: ext = e.readlines()
    print(f" Loaded [{len(ext)}] Dorks.")
    if mode == "log":
        logscreen()
    else:
        cliscreen()
    if len(ext) > num:
        num+=1
        dorkstart()
    else:
        print("Finished Parsing!")
main()