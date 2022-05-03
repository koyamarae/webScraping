from selenium import webdriver
import time

# chromeドライバーを起動する時のオプションを設定
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # ヘッドレスで起動
options.add_argument('--no-sandbox') # 仮想環境下では、sandboxで起動すると失敗するので無効にする
options.add_argument('--disable-gpu') # ヘッドレスモードで起動するときに必要
options.add_argument('--window-size=1280,1024')  # 画面サイズの指定

# chromeドライバーを起動
driver = webdriver.Chrome(options=options)

# googleを開く
driver.get("https://www.google.co.jp/")

# 画面が表示されるまで待つ
time.sleep(3)

# スクリーンショットを撮る
driver.save_screenshot("./data/screenshot.png")