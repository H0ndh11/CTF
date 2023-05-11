# Angrとは
主にRev問で使うツール<br>
これを使うことで特定のアドレス到達するための標準入力を自動で見つけることができる<br>
私はUbuntuで使用しています．うまくいかなかったら公式ドキュメントを読んでね

インストール方法(Unix環境)
~~~
pip install angr
~~~

# 使用例<br>
①"Correct!"といった特定の文字列が出力されるアドレスに到達するため標準入力を探す
~~~
# angrのインポート
import angr

# ./challを解析するangrプロジェクトの作成
proj = angr.Project('./chall')
# プロジェクトの初期状態を作成
state = proj.factory.entry_state()
# シミュレーションマネージャーの作成。こいつが複数の状態を管理し、探索をする
simgr = proj.factory.simgr(state)

# シミュレーションマネージャーを使って特定のアドレスに到達するための標準入力を探す。
# findパラメータは目標となる条件を指定する
# 今回は"Correct!"が含まれる文字列を見つけることが目標となる
simgr.explore(find=lambda s: b'Correct!' in s.posix.dumps(1))

# 解決作画見つかった場合
if simgr.found:
    # 最初の解決状態オブジェクトを取得する
    solution_state = simgr.found[0]
    # 標準入力から解決策を取得し、表示する
    print(solution_state.posix.dumps(0))
else:
    print('No solution found')
~~~


②
アドレスを直接指定して，そのアドレスに到達するための標準入力を探す
~~~
# angrのインポート
import angr

project = angr.Project('./chall')

# 0xAAAAAAにフックを設定．ここに到達すると以下の関数が呼び出される
@project.hook(0xAAAAAA)
def print_flag(state):
    print("FLAG SHOULD BE:", state.posix.dumps(0))
    # プロジェクトの実行を修了
    project.terminate_execution()

# プロジェクトを実行
project.execute()
~~~

その他備考<br>
angrプロジェクト作成時に，`auto_load_libs=False`を設定するとライブラリの自動ロードが無効化され，解析速度が早くなる．ただしシミュレーションの正確性が下がるのでケースバイケース