仮想通貨取引ボット
このプロジェクトは、Bybit取引所のAPIを使用してRSI（相対力指数）に基づいた自動売買を行う仮想通貨取引ボットです。

機能
指定された仮想通貨の履歴価格データを取得
RSIを計算し、買いおよび売りシグナルを生成
市場注文を使用してBybit取引所で取引を実行
リスク管理のためのストップロス注文を実装
インストール
リポジトリをクローン:

bash
コードをコピーする
git clone https://github.com/yourusername/crypto-trading-bot.git
cd crypto-trading-bot
必要な依存関係をインストール:

bash
コードをコピーする
pip install -r requirements.txt
config.pyファイルを作成し、BybitのAPIキーを設定:

python
コードをコピーする
api_key = 'your_api_key'
api_secret = 'your_api_secret'
使い方
ボットを実行:

bash
コードをコピーする
python bot.py
パラメータ設定:

symbol: 取引する仮想通貨のシンボル（例: "BTCUSD"）
interval: データの取得間隔（例: "1" 分足）
注意事項
リスク管理: 自動取引にはリスクが伴います。ボットの使用による損失については自己責任で行ってください。
セキュリティ: APIキーとシークレットキーは第三者に公開しないでください。これらの情報は安全に管理し、.gitignoreを使用してリポジトリに含めないようにしてください。
API制限とエラー処理: Bybit APIの制限に注意し、適切なエラーハンドリングを実装していますが、実運用前に十分にテストしてください。
ライセンス
このプロジェクトはMITライセンスの下で提供されています。詳細はLICENSEファイルを参照してください。

貢献
このプロジェクトへの貢献は歓迎されます。プルリクエストを提出する前に、CONTRIBUTINGガイドラインをお読みください。
