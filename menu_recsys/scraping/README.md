# このフォルダについて
## menu.py
### 概要
学食のメニューページからメニュー情報を取得するためのメソッドが入ってます。

### 使い方
- cd コマンドでこのフォルダ（menu_recsys/scraping/）に移動して以下を実行してください
    - conda install --name django_app --file conda_requirements.txt
- get_menu_urls を使用する場合はさらに、menu.pyと同じ階層にchromedriverをインストールしてください。
    - https://zenn.dev/ryo427/articles/7ff77a86a2d86a
    - このページでダウンロードしたzipの中に入っている「chromedriver」というファイル名のものだけコピーしておいてくれたらいいです。

### メソッド概要
- get_menu_info
    - メニュー詳細ページから、１つのメニューの詳細情報を取得する関数
    - 入力：メニューURL(str型)
    - 出力：料理名や栄養素など(dict型)。（詳しくはソースコード要確認）

- get_menu_urls
    - 食堂ごとのメニュー一覧ページから、メニュー詳細ページへのURL一覧を取得する
    - 入力：食堂id (どの食堂のメニュー一覧を取得するか判定. 食堂idは以下のようにします)
    - 出力：各メニューの詳細ページに飛ぶためのURL一覧（list形式）
        - ただし、売り切れになっている商品のURLは含まない