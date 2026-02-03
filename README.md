### このリポジトリの説明

- 学校の自主プロジェクトという授業内の成果物の制御部分です
- 機械部分は[gnbo/mechanic](https://github.com/nalinally/gnbo-mechanic.git)リポジトリにまとまっています

<img width="937" height="727" alt="GNBO_最終成果物" src="https://github.com/user-attachments/assets/a0c9431e-daac-465c-accd-a4b734990577" />


### プロジェクト概要

- 3機のモジュール型ロボットが合体・協調して一つのロボットのように振る舞います
- それぞれのロボットは磁石の力を使って、動的に結合/結合解除を行います


### システム構成

- それぞれのロボットをメインとなるPCから制御します
- 各ロボットには[NodeMCU](https://amzn.asia/d/0hBeHOqJ)というWiFi通信可能なマイコンを載せます
- httpリクエスト/サービスの枠組みを用いてPCとロボット間の通信を行います

<img width="1075" height="379" alt="system_configuration" src="https://github.com/user-attachments/assets/88aa093c-4624-48f9-8f5c-d28d55f4e307" />


### ファイル構造

- `src`
  - GNBOに載せた[NodeMCU](https://amzn.asia/d/0hBeHOqJ)で動かすプログラムです
- `script`
  - PCで動かすプログラムです
  - `launch.sh`
    - このファイルを実行して起動します
  - `http_robot_driver.py`
    - ロボットのクラスです。各機構を動かす一番単純な機能（Drive）を持っています
  - `http_robot_operator.py`
    - HttpRobotDriverクラスのオブジェクトを持ち、Driveよりも少し複雑な動き（Operate）ができます
  - `main.py`
    - DriveとOperateを使ってロボットにタスクを行わせます


