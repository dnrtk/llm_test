# main.py

# モジュールインポート
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

# 最小Kivyバージョン
kivy.require('2.0.0')

class PuzzleSolverApp(App):
    def build(self):
        # メインレイアウト
        self.main_layout = BoxLayout(orientation='vertical')

        # ラベル
        self.label = Label(text='3マッチパズルゲームソルバー')
        self.main_layout.add_widget(self.label)

        # 解析開始ボタン
        self.analyze_button = Button(text='解析開始', on_press=self.start_analysis)
        self.main_layout.add_widget(self.analyze_button)

        # 解析結果表示ラベル
        self.result_label = Label(text='')
        self.main_layout.add_widget(self.result_label)

        return self.main_layout

    def start_analysis(self, instance):
        self.label.text = '解析中...'
        # ここで解析処理を呼び出す (未実装)
        Clock.schedule_once(self.show_result, 1) # 1秒後にshow_resultを呼び出す (仮実装)

    def show_result(self, dt):
        # 解析結果をresult_labelに表示する (仮実装)
        self.label.text = '解析完了！'
        self.result_label.text = '最適手：未実装' # TODO: 解析結果を表示するように修正

if __name__ == '__main__':
    PuzzleSolverApp().run()
