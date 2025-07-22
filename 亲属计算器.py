import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout,
    QMessageBox, QFrame
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

RELATION_MAP = {
    ("爸爸", "爸爸"): ("爷爷", "爸爸的爸爸是什么？爸爸的爸爸是爷爷。"),
    ("爸爸", "妈妈"): ("奶奶", "爸爸的妈妈是什么？爸爸的妈妈是奶奶。"),
    ("妈妈", "爸爸"): ("外公", "妈妈的爸爸是什么？妈妈的爸爸是外公。"),
    ("妈妈", "妈妈"): ("外婆", "妈妈的妈妈是什么？妈妈的妈妈是外婆。"),
    ("哥哥", "妈妈"): ("妈妈", "哥哥的妈妈是什么？哥哥的妈妈是妈妈。"),
    ("姐姐", "爸爸"): ("爸爸", "姐姐的爸爸是什么？姐姐的爸爸是爸爸。"),
    ("爸爸", "哥哥"): ("伯伯", "爸爸的哥哥是什么？爸爸的哥哥是伯伯。"),
    ("爸爸", "弟弟"): ("叔叔", "爸爸的弟弟是什么？爸爸的弟弟是叔叔。"),
    ("爸爸", "姐姐"): ("姑姑", "爸爸的姐姐是什么？爸爸的姐姐是姑姑。"),
    ("爸爸", "妹妹"): ("姑姑", "爸爸的妹妹是什么？爸爸的妹妹是姑姑。"),
    ("妈妈", "姐姐"): ("姨妈", "妈妈的姐姐是什么？妈妈的姐姐是姨妈。"),
    ("妈妈", "妹妹"): ("姨妈", "妈妈的妹妹是什么？妈妈的妹妹是姨妈。"),
    ("妈妈", "哥哥"): ("舅舅", "妈妈的哥哥是什么？妈妈的哥哥是舅舅。"),
    ("妈妈", "弟弟"): ("舅舅", "妈妈的弟弟是什么？妈妈的弟弟是舅舅。"),
    ("爷爷", "爸爸"): ("曾祖父", "爷爷的爸爸是什么？爷爷的爸爸是曾祖父。"),
    ("奶奶", "爸爸"): ("曾祖父", "奶奶的爸爸是什么？奶奶的爸爸是曾祖父。"),
    ("爷爷", "妈妈"): ("曾祖母", "爷爷的妈妈是什么？爷爷的妈妈是曾祖母。"),
    ("奶奶", "妈妈"): ("曾祖母", "奶奶的妈妈是什么？奶奶的妈妈是曾祖母。"),
    ("外公", "爸爸"): ("外曾祖父", "外公的爸爸是什么？外公的爸爸是外曾祖父。"),
    ("外婆", "妈妈"): ("外曾祖母", "外婆的妈妈是什么？外婆的妈妈是外曾祖母。"),
    ("哥哥", "哥哥"): ("哥哥", "哥哥的哥哥是什么？哥哥的哥哥还是哥哥。"),
    ("姐姐", "姐姐"): ("姐姐", "姐姐的姐姐是什么？姐姐的姐姐还是姐姐。"),
    ("弟弟", "弟弟"): ("弟弟", "弟弟的弟弟是什么？弟弟的弟弟还是弟弟。"),
    ("妹妹", "妹妹"): ("妹妹", "妹妹的妹妹是什么？妹妹的妹妹还是妹妹。"),
    ("哥哥", "弟弟"): ("弟弟", "哥哥的弟弟是什么？哥哥的弟弟是弟弟。"),
    ("姐姐", "妹妹"): ("妹妹", "姐姐的妹妹是什么？姐姐的妹妹是妹妹。"),
    ("弟弟", "哥哥"): ("哥哥", "弟弟的哥哥是什么？弟弟的哥哥是哥哥。"),
    ("妹妹", "姐姐"): ("姐姐", "妹妹的姐姐是什么？妹妹的姐姐是姐姐。"),
    ("姑姑", "爸爸"): ("爷爷", "姑姑的爸爸是什么？姑姑的爸爸是爷爷。"),
    ("伯伯", "爸爸"): ("爷爷", "伯伯的爸爸是什么？伯伯的爸爸是爷爷。"),
    ("叔叔", "爸爸"): ("爷爷", "叔叔的爸爸是什么？叔叔的爸爸是爷爷。"),
    ("舅舅", "妈妈"): ("外公", "舅舅的妈妈是什么？舅舅的妈妈是外公。"),
    ("姨妈", "妈妈"): ("外婆", "姨妈的妈妈是什么？姨妈的妈妈是外婆。"),

}

RELATIONS = [
    "爸爸", "妈妈", "爷爷", "奶奶", "外公", "外婆", "哥哥", "姐姐", "弟弟", "妹妹", "姑姑", "伯伯", "叔叔", "舅舅", "姨妈", "曾祖父", "曾祖母", "外曾祖父", "外曾祖母"
]

RELATION_GROUPS = {
    "父母": ["爸爸", "妈妈"],
    "祖辈": ["爷爷", "奶奶", "外公", "外婆", "曾祖父", "曾祖母", "外曾祖父", "外曾祖母"],
    "兄弟姐妹": ["哥哥", "姐姐", "弟弟", "妹妹"],
    "旁系": ["姑姑", "伯伯", "叔叔", "舅舅", "姨妈",],
}

class RelativeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("亲属计算器")
        self.resize(600, 480)
        self.setMinimumSize(400, 320)
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.init_ui()

    def init_ui(self):
        font_title = QFont("微软雅黑", 15, QFont.Bold)
        font_result = QFont("微软雅黑", 16, QFont.Bold)
        font_think = QFont("微软雅黑", 13)
        self.btn_font = QFont("微软雅黑", 14)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label_step = QLabel("请选择第一个亲属分组:")
        self.label_step.setFont(font_title)
        self.label_step.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_step)

        # 分组按钮区，多行自适应
        self.group_grid = QWidget()
        self.group_grid_layout = QVBoxLayout()
        self.group_grid.setLayout(self.group_grid_layout)
        self.group_btns = []
        group_names = list(RELATION_GROUPS.keys())
        for i in range(0, len(group_names), 2):
            row = QHBoxLayout()
            for j in range(2):
                if i + j < len(group_names):
                    group = group_names[i + j]
                    btn = QPushButton(group)
                    btn.setMinimumWidth(120)
                    btn.setMinimumHeight(40)
                    btn.setFont(self.btn_font)
                    btn.setSizePolicy(QPushButton().sizePolicy())
                    btn.setStyleSheet("QPushButton {border-radius: 8px; background: #4fc3f7; color: #fff; font-weight: bold;}")
                    btn.clicked.connect(lambda checked, g=group: self.show_options(g))
                    row.addWidget(btn)
                    self.group_btns.append(btn)
            self.group_grid_layout.addLayout(row)
        self.layout.addWidget(self.group_grid)

        self.line1 = QFrame()
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(self.line1)

        # 选项按钮区，多行自适应
        self.option_grid = QWidget()
        self.option_grid_layout = QVBoxLayout()
        self.option_grid.setLayout(self.option_grid_layout)
        self.option_btns = []
        self.layout.addWidget(self.option_grid)

        self.confirm_btn = QPushButton("确定")
        self.confirm_btn.setMinimumWidth(120)
        self.confirm_btn.setMinimumHeight(40)
        self.confirm_btn.setFont(self.btn_font)
        self.confirm_btn.setStyleSheet("QPushButton {border-radius: 8px; background: #43a047; color: #fff; font-weight: bold;}")
        self.confirm_btn.clicked.connect(self.confirm_option)
        self.confirm_btn.hide()
        self.layout.addWidget(self.confirm_btn)

        self.label_step2 = QLabel("请选择第二个亲属分组:")
        self.label_step2.setFont(font_title)
        self.label_step2.setAlignment(Qt.AlignCenter)
        self.label_step2.hide()
        self.layout.addWidget(self.label_step2)

        self.group2_grid = QWidget()
        self.group2_grid_layout = QVBoxLayout()
        self.group2_grid.setLayout(self.group2_grid_layout)
        self.group2_btns = []
        for i in range(0, len(group_names), 2):
            row = QHBoxLayout()
            for j in range(2):
                if i + j < len(group_names):
                    group = group_names[i + j]
                    btn = QPushButton(group)
                    btn.setMinimumWidth(120)
                    btn.setMinimumHeight(40)
                    btn.setFont(self.btn_font)
                    btn.setSizePolicy(QPushButton().sizePolicy())
                    btn.setStyleSheet("QPushButton {border-radius: 8px; background: #4fc3f7; color: #fff; font-weight: bold;}")
                    btn.clicked.connect(lambda checked, g=group: self.show_options2(g))
                    row.addWidget(btn)
                    self.group2_btns.append(btn)
                    btn.hide()
            self.group2_grid_layout.addLayout(row)
        self.layout.addWidget(self.group2_grid)

        self.line2 = QFrame()
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.line2.hide()
        self.layout.addWidget(self.line2)

        self.option2_grid = QWidget()
        self.option2_grid_layout = QVBoxLayout()
        self.option2_grid.setLayout(self.option2_grid_layout)
        self.option2_btns = []
        self.layout.addWidget(self.option2_grid)

        self.confirm_btn2 = QPushButton("确定")
        self.confirm_btn2.setMinimumWidth(120)
        self.confirm_btn2.setMinimumHeight(40)
        self.confirm_btn2.setFont(self.btn_font)
        self.confirm_btn2.setStyleSheet("QPushButton {border-radius: 8px; background: #43a047; color: #fff; font-weight: bold;}")
        self.confirm_btn2.clicked.connect(self.confirm_option2)
        self.confirm_btn2.hide()
        self.layout.addWidget(self.confirm_btn2)

        self.result_label = QLabel("结果将在这里显示")
        self.result_label.setFont(font_result)
        self.result_label.setStyleSheet("color: #2b7a78;")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.result_label)

        self.think_label = QLabel("思考过程将在这里显示")
        self.think_label.setFont(font_think)
        self.think_label.setStyleSheet("color: #3a3a3a;")
        self.think_label.setWordWrap(True)
        self.layout.addWidget(self.think_label)

        self.first_selected = None
        self.second_selected = None
        self.result = None
        self.thinking = None

    def show_options(self, group):
        # 清空选项按钮
        for btn in self.option_btns:
            btn.setParent(None)
        self.option_btns.clear()
        self.selected_group = group
        # 高亮分组按钮
        for btn in self.group_btns:
            if btn.text() == group:
                btn.setStyleSheet("QPushButton {border-radius: 8px; background: #1976d2; color: #fff; font-weight: bold; border:2px solid #1976d2;}")
            else:
                btn.setStyleSheet("QPushButton {border-radius: 8px; background: #4fc3f7; color: #fff; font-weight: bold; border:2px solid #1976d2;}")
        # 创建新选项，多行自适应
        relations = RELATION_GROUPS[group]
        self.option_grid_layout.setSpacing(8)
        for i in range(0, len(relations), 4):
            row = QHBoxLayout()
            for j in range(4):
                if i + j < len(relations):
                    relation = relations[i + j]
                    btn = QPushButton(relation)
                    btn.setMinimumWidth(120)
                    btn.setMinimumHeight(40)
                    btn.setFont(self.btn_font)
                    btn.setSizePolicy(QPushButton().sizePolicy())
                    btn.setStyleSheet("QPushButton {border-radius: 8px; background: #81d4fa; color: #333; font-weight: bold; border:2px solid #1976d2;}")
                    btn.clicked.connect(lambda checked, r=relation: self.select_first(r))
                    row.addWidget(btn)
                    self.option_btns.append(btn)
            self.option_grid_layout.addLayout(row)
        self.confirm_btn.show()

    def select_first(self, relation):
        self.first_selected = relation
        # 高亮已选项
        for btn in self.option_btns:
            if btn.text() == relation:
                btn.setStyleSheet("QPushButton {border-radius: 8px; background: #ffb300; color: #333; font-weight: bold; border:2px solid #ffb300;}")
            else:
                btn.setStyleSheet("QPushButton {border-radius: 8px; background: #81d4fa; color: #333; font-weight: bold; border:2px solid #1976d2;}")

    def confirm_option(self):
        if not self.first_selected:
            QMessageBox.warning(self, "提示", "请选择第一个亲属！")
            return
        self.label_step.hide()
        for btn in self.group_btns:
            btn.hide()
        for btn in self.option_btns:
            btn.hide()
        self.confirm_btn.hide()
        self.label_step2.show()
        for btn in self.group2_btns:
            btn.show()
        self.line2.show()

    def show_options2(self, group):
        for btn in self.option2_btns:
            btn.setParent(None)
        self.option2_btns.clear()
        self.selected_group2 = group
        # 高亮分组按钮
        for btn in self.group2_btns:
            if btn.text() == group:
                btn.setStyleSheet("QPushButton {border-radius: 8px; background: #1976d2; color: #fff; font-weight: bold; border:2px solid #1976d2;}")
            else:
                btn.setStyleSheet("QPushButton {border-radius: 8px; background: #4fc3f7; color: #fff; font-weight: bold; border:2px solid #1976d2;}")
        relations = RELATION_GROUPS[group]
        self.option2_grid_layout.setSpacing(8)
        for i in range(0, len(relations), 4):
            row = QHBoxLayout()
            for j in range(4):
                if i + j < len(relations):
                    relation = relations[i + j]
                    btn = QPushButton(relation)
                    btn.setMinimumWidth(120)
                    btn.setMinimumHeight(40)
                    btn.setFont(self.btn_font)
                    btn.setSizePolicy(QPushButton().sizePolicy())
                    btn.setStyleSheet("QPushButton {border-radius: 8px; background: #81d4fa; color: #333; font-weight: bold; border:2px solid #1976d2;}")
                    btn.clicked.connect(lambda checked, r=relation: self.select_second(r))
                    row.addWidget(btn)
                    self.option2_btns.append(btn)
            self.option2_grid_layout.addLayout(row)
        self.confirm_btn2.show()

    def select_second(self, relation):
        self.second_selected = relation
        # 高亮已选项
        for btn in self.option2_btns:
            if btn.text() == relation:
                btn.setStyleSheet("QPushButton {border-radius: 8px; background: #ffb300; color: #333; font-weight: bold; border:2px solid #ffb300;}")
            else:
                btn.setStyleSheet("QPushButton {border-radius: 8px; background: #81d4fa; color: #333; font-weight: bold; border:2px solid #1976d2;}")

    def confirm_option2(self):
        if not self.second_selected:
            QMessageBox.warning(self, "提示", "请选择第二个亲属！")
            return
        self.label_step2.hide()
        for btn in self.group2_btns:
            btn.hide()
        for btn in self.option2_btns:
            btn.hide()
        self.confirm_btn2.hide()
        self.calculate()

    def calculate(self):
        first = self.first_selected
        second = self.second_selected
        if not first or not second:
            QMessageBox.warning(self, "提示", "请选择两个亲属！")
            return
        self.result, self.thinking = RELATION_MAP.get((first, second), ("未知", self.generate_thinking(first, second)))
        self.show_fullscreen_thinking(self.thinking)

    def show_fullscreen_thinking(self, text):
        self.result_label.hide()
        self.think_label.hide()
        # 创建全屏遮罩（自适应窗口大小）
        self.fullscreen_label = QLabel("", self)
        self.fullscreen_label.setAlignment(Qt.AlignCenter)
        self.fullscreen_label.setStyleSheet("background: white;")
        self.fullscreen_label.setFont(QFont("微软雅黑", 40, QFont.Bold))
        self.fullscreen_label.setWordWrap(True)
        self.fullscreen_label.setGeometry(self.rect())
        self.fullscreen_label.show()
        self.full_text = text
        self.full_idx = 0
        # 播放音乐，自动适配exe所在目录
        base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(sys.argv[0])))
        music_path = os.path.join(base_dir, "parentsmusic.MP3")
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(music_path)))
        self.player.play()
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate_thinking_fullscreen)
        self.timer.start(1000)
        # 跟随窗口大小变化
        self.resizeEvent = self.fullscreen_resize_event

    def fullscreen_resize_event(self, event):
        if hasattr(self, 'fullscreen_label') and self.fullscreen_label.isVisible():
            self.fullscreen_label.setGeometry(self.rect())
        QWidget.resizeEvent(self, event)

    def animate_thinking_fullscreen(self):
        self.full_idx += 1
        if self.full_idx <= len(self.full_text):
            self.fullscreen_label.setText(self.full_text[:self.full_idx])
        else:
            self.timer.stop()
            QTimer.singleShot(1000, self.show_result_after_thinking)

    def show_result_after_thinking(self):
        self.fullscreen_label.hide()
        self.result_label.show()
        self.think_label.show()
        self.result_label.setText(f"结果：{self.result}")
        self.think_label.setText(f"思考过程：{self.thinking}")
        # 30秒后自动退出
        QTimer.singleShot(30000, QApplication.instance().quit)

    def generate_thinking(self, first, second):
        return f"{first}的{second}是什么？{first}的{second}是……（暂未收录）"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RelativeCalculator()
    window.show()
    sys.exit(app.exec_())
