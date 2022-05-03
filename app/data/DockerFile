# ベースイメージはpython:3.7
FROM python:3.7

# 環境変数設定
ENV PYTHONIOENCODING utf-8
ENV TZ='Asia/Tokyo'

# workdirの設定
WORKDIR /app

# 作業ディレクトリ作成
RUN mkdir /app/source
RUN mkdir /app/data

# apt-getのアップデートなど
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y apt-utils
RUN pip install --upgrade pip

# 必要なpythonライブラリのインストール
RUN pip install selenium

# Chromeドライバーのダウンロード
RUN wget -q -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Chromeのインストール
RUN apt-get install -y libgbm1 libappindicator3-1 libappindicator1 fonts-liberation libasound2 libnspr4 libnss3 libxss1 lsb-release xdg-utils libfontconfig
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb

# 日本語設定
RUN export LANG=C.UTF-8
RUN export LANGUAGE=en_US:
RUN apt-get install -y fonts-ipafont

# コンテナ起動時に実行するコマンドを設定
CMD [ "python", "source/main.py" ]