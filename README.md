### このリポジトリの説明

- 学校の自主プロジェクトという授業内の成果物の制御部分です
- 機械部分は[gnbo/mechanic]([https://github.com/nalinally/gnbo-control.git](https://github.com/nalinally/gnbo-mechanic.git))リポジトリにまとまっています

<img width="937" height="727" alt="GNBO_最終成果物" src="https://github.com/user-attachments/assets/a0c9431e-daac-465c-accd-a4b734990577" />

### ファイル構造

- `src`
  - GNBOに載せた[NodeMCU](https://amzn.asia/d/0hBeHOqJ)というマイコンで動かすプログラムです
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


