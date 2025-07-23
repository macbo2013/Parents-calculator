#原创：@MACBO2013
#github已开源
#made in china
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
################################################################勿动####################################################################
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
    ("爷爷", "哥哥"): ("伯祖父", "爷爷的哥哥是什么？爷爷的哥哥是伯祖父。"),
    ("爷爷", "弟弟"): ("叔祖父", "爷爷的弟弟是什么？爷爷的弟弟是叔祖父。"),
    ("爷爷", "姐姐"): ("姑祖母", "爷爷的姐姐是什么？爷爷的姐姐是姑祖母。"),
    ("爷爷", "妹妹"): ("姑祖母", "爷爷的妹妹是什么？爷爷的妹妹是姑祖母。"),
    ("奶奶", "哥哥"): ("舅祖父", "奶奶的哥哥是什么？奶奶的哥哥是舅祖父。"),
    ("奶奶", "弟弟"): ("舅祖父", "奶奶的弟弟是什么？奶奶的弟弟是舅祖父。"),
    ("奶奶", "姐姐"): ("姨祖母", "奶奶的姐姐是什么？奶奶的姐姐是姨祖母。"),
    ("奶奶", "妹妹"): ("姨祖母", "奶奶的妹妹是什么？奶奶的妹妹是姨祖母。"),
    ("外公", "哥哥"): ("外伯祖父", "外公的哥哥是什么？外公的哥哥是外伯祖父。"),
    ("外公", "弟弟"): ("外叔祖父", "外公的弟弟是什么？外公的弟弟是外叔祖父。"),
    ("外公", "姐姐"): ("外姑祖母", "外公的姐姐是什么？外公的姐姐是外姑祖母。"),
    ("外公", "妹妹"): ("外姑祖母", "外公的妹妹是什么？外公的妹妹是外姑祖母。"),
    ("外婆", "哥哥"): ("外舅祖父", "外婆的哥哥是什么？外婆的哥哥是外舅祖父。"),
    ("外婆", "弟弟"): ("外舅祖父", "外婆的弟弟是什么？外婆的弟弟是外舅祖父。"),
    ("外婆", "姐姐"): ("外姨祖母", "外婆的姐姐是什么？外婆的姐姐是外姨祖母。"),
    ("外婆", "妹妹"): ("外姨祖母", "外婆的妹妹是什么？外婆的妹妹是外姨祖母。"),
    ("伯伯", "哥哥"): ("伯父", "伯伯的哥哥是什么？伯伯的哥哥是伯父。"),
    ("伯伯", "弟弟"): ("叔叔", "伯伯的弟弟是什么？伯伯的弟弟是叔叔。"),
    ("叔叔", "哥哥"): ("伯伯", "叔叔的哥哥是什么？叔叔的哥哥是伯伯。"),
    ("叔叔", "弟弟"): ("叔父", "叔叔的弟弟是什么？叔叔的弟弟是叔父。"),
    ("姑姑", "姐姐"): ("姑妈", "姑姑的姐姐是什么？姑姑的姐姐是姑妈。"),
    ("姑姑", "妹妹"): ("姑姨", "姑姑的妹妹是什么？姑姑的妹妹是姑姨。"),
    ("舅舅", "哥哥"): ("大舅", "舅舅的哥哥是什么？舅舅的哥哥是大舅。"),
    ("舅舅", "弟弟"): ("小舅", "舅舅的弟弟是什么？舅舅的弟弟是小舅。"),
    ("姨妈", "姐姐"): ("大姨", "姨妈的姐姐是什么？姨妈的姐姐是大姨。"),
    ("姨妈", "妹妹"): ("小姨", "姨妈的妹妹是什么？姨妈的妹妹是小姨。"),
    ("曾祖父", "爸爸"): ("高祖父", "曾祖父的爸爸是什么？曾祖父的爸爸是高祖父。"),
    ("曾祖母", "妈妈"): ("高祖母", "曾祖母的妈妈是什么？曾祖母的妈妈是高祖母。"),
    ("伯伯", "儿子"): ("堂哥/堂弟", "伯伯的儿子是什么？伯伯的儿子是堂哥或堂弟。"),
    ("叔叔", "儿子"): ("堂哥/堂弟", "叔叔的儿子是什么？叔叔的儿子是堂哥或堂弟。"),
    ("姑姑", "儿子"): ("表哥/表弟", "姑姑的儿子是什么？姑姑的儿子是表哥或表弟。"),
    ("舅舅", "儿子"): ("表哥/表弟", "舅舅的儿子是什么？舅舅的儿子是表哥或表弟。"),
    ("姨妈", "儿子"): ("表哥/表弟", "姨妈的儿子是什么？姨妈的儿子是表哥或表弟。"),
    ("伯伯", "女儿"): ("堂姐/堂妹", "伯伯的女儿是什么？伯伯的女儿是堂姐或堂妹。"),
    ("叔叔", "女儿"): ("堂姐/堂妹", "叔叔的女儿是什么？叔叔的女儿是堂姐或堂妹。"),
    ("姑姑", "女儿"): ("表姐/表妹", "姑姑的女儿是什么？姑姑的女儿是表姐或表妹。"),
    ("舅舅", "女儿"): ("表姐/表妹", "舅舅的女儿是什么？舅舅的女儿是表姐或表妹。"),
    ("姨妈", "女儿"): ("表姐/表妹", "姨妈的女儿是什么？姨妈的女儿是表姐或表妹。"),
    ("爷爷", "妻子"): ("奶奶", "爷爷的妻子是什么？爷爷的妻子是奶奶。"),
    ("奶奶", "丈夫"): ("爷爷", "奶奶的丈夫是什么？奶奶的丈夫是爷爷。"),
    ("外公", "妻子"): ("外婆", "外公的妻子是什么？外公的妻子是外婆。"),
    ("外婆", "丈夫"): ("外公", "外婆的丈夫是什么？外婆的丈夫是外公。"),
    ("爸爸", "妻子"): ("妈妈", "爸爸的妻子是什么？爸爸的妻子是妈妈。"),
    ("妈妈", "丈夫"): ("爸爸", "妈妈的丈夫是什么？妈妈的丈夫是爸爸。"),
    ("伯伯", "妻子"): ("伯母", "伯伯的妻子是什么？伯伯的妻子是伯母。"),
    ("叔叔", "妻子"): ("婶婶", "叔叔的妻子是什么？叔叔的妻子是婶婶。"),
    ("姑姑", "丈夫"): ("姑父", "姑姑的丈夫是什么？姑姑的丈夫是姑父。"),
    ("舅舅", "妻子"): ("舅妈", "舅舅的妻子是什么？舅舅的妻子是舅妈。"),
    ("姨妈", "丈夫"): ("姨父", "姨妈的丈夫是什么？姨妈的丈夫是姨父。"),
    ("曾祖父", "妻子"): ("曾祖母", "曾祖父的妻子是什么？曾祖父的妻子是曾祖母。"),
    ("曾祖母", "丈夫"): ("曾祖父", "曾祖母的丈夫是什么？曾祖母的丈夫是曾祖父。"),
    ("外曾祖父", "妻子"): ("外曾祖母", "外曾祖父的妻子是什么？外曾祖父的妻子是外曾祖母。"),
    ("外曾祖母", "丈夫"): ("外曾祖父", "外曾祖母的丈夫是什么？外曾祖母的丈夫是外曾祖父。"),
    ("哥哥", "儿子"): ("侄子", "哥哥的儿子是什么？哥哥的儿子是侄子。"),
    ("姐姐", "儿子"): ("外甥", "姐姐的儿子是什么？姐姐的儿子是外甥。"),
    ("哥哥", "女儿"): ("侄女", "哥哥的女儿是什么？哥哥的女儿是侄女。"),
    ("姐姐", "女儿"): ("外甥女", "姐姐的女儿是什么？姐姐的女儿是外甥女。")
   }
#################################################################勿动######################################################################
RELATION_MAP_EN = {("father", "father"): ("grandfather", "Who is father's father? Father's father is grandfather."),
    ("father", "mother"): ("grandmother", "Who is father's mother? Father's mother is grandmother."),
    ("mother", "father"): ("maternal grandfather", "Who is mother's father? Mother's father is maternal grandfather."),
    ("mother", "mother"): ("maternal grandmother", "Who is mother's mother? Mother's mother is maternal grandmother."),
    ("older brother", "mother"): ("mother", "Who is older brother's mother? Older brother's mother is mother."),
    ("older sister", "father"): ("father", "Who is older sister's father? Older sister's father is father."),
    ("father", "older brother"): ("uncle (father's older brother)", "Who is father's older brother? Father's older brother is uncle."),
    ("father", "younger brother"): ("uncle (father's younger brother)", "Who is father's younger brother? Father's younger brother is uncle."),
    ("father", "older sister"): ("aunt (father's sister)", "Who is father's older sister? Father's older sister is aunt."),
    ("father", "younger sister"): ("aunt (father's sister)", "Who is father's younger sister? Father's younger sister is aunt."),
    ("mother", "older sister"): ("aunt (mother's sister)", "Who is mother's older sister? Mother's older sister is aunt."),
    ("mother", "younger sister"): ("aunt (mother's sister)", "Who is mother's younger sister? Mother's younger sister is aunt."),
    ("mother", "older brother"): ("uncle (mother's brother)", "Who is mother's older brother? Mother's older brother is uncle."),
    ("mother", "younger brother"): ("uncle (mother's brother)", "Who is mother's younger brother? Mother's younger brother is uncle."),
    ("grandfather", "father"): ("great-grandfather", "Who is grandfather's father? Grandfather's father is great-grandfather."),
    ("grandmother", "father"): ("great-grandfather", "Who is grandmother's father? Grandmother's father is great-grandfather."),
    ("grandfather", "mother"): ("great-grandmother", "Who is grandfather's mother? Grandfather's mother is great-grandmother."),
    ("grandmother", "mother"): ("great-grandmother", "Who is grandmother's mother? Grandmother's mother is great-grandmother."),
    ("maternal grandfather", "father"): ("maternal great-grandfather", "Who is maternal grandfather's father? Maternal grandfather's father is maternal great-grandfather."),
    ("maternal grandmother", "mother"): ("maternal great-grandmother", "Who is maternal grandmother's mother? Maternal grandmother's mother is maternal great-grandmother."),
    ("older brother", "older brother"): ("older brother", "Who is older brother's older brother? Older brother's older brother is still older brother."),
    ("older sister", "older sister"): ("older sister", "Who is older sister's older sister? Older sister's older sister is still older sister."),
    ("younger brother", "younger brother"): ("younger brother", "Who is younger brother's younger brother? Younger brother's younger brother is still younger brother."),
    ("younger sister", "younger sister"): ("younger sister", "Who is younger sister's younger sister? Younger sister's younger sister is still younger sister."),
    ("older brother", "younger brother"): ("younger brother", "Who is older brother's younger brother? Older brother's younger brother is younger brother."),
    ("older sister", "younger sister"): ("younger sister", "Who is older sister's younger sister? Older sister's younger sister is younger sister."),
    ("younger brother", "older brother"): ("older brother", "Who is younger brother's older brother? Younger brother's older brother is older brother."),
    ("younger sister", "older sister"): ("older sister", "Who is younger sister's older sister? Younger sister's older sister is older sister."),
    ("aunt (father's sister)", "father"): ("grandfather", "Who is aunt's father? Aunt's father is grandfather."),
    ("uncle (father's older brother)", "father"): ("grandfather", "Who is uncle's father? Uncle's father is grandfather."),
    ("uncle (father's younger brother)", "father"): ("grandfather", "Who is uncle's father? Uncle's father is grandfather."),
    ("uncle (mother's brother)", "mother"): ("maternal grandfather", "Who is uncle's mother? Uncle's mother is maternal grandfather."),
    ("aunt (mother's sister)", "mother"): ("maternal grandmother", "Who is aunt's mother? Aunt's mother is maternal grandmother."),
    ("grandfather", "older brother"): ("great-uncle (grandfather's brother)", "Who is grandfather's older brother? Grandfather's older brother is great-uncle."),
    ("grandfather", "younger brother"): ("great-uncle (grandfather's brother)", "Who is grandfather's younger brother? Grandfather's younger brother is great-uncle."),
    ("grandfather", "older sister"): ("great-aunt (grandfather's sister)", "Who is grandfather's older sister? Grandfather's older sister is great-aunt."),
    ("grandfather", "younger sister"): ("great-aunt (grandfather's sister)", "Who is grandfather's younger sister? Grandfather's younger sister is great-aunt."),
    ("grandmother", "older brother"): ("great-uncle (grandmother's brother)", "Who is grandmother's older brother? Grandmother's older brother is great-uncle."),
    ("grandmother", "younger brother"): ("great-uncle (grandmother's brother)", "Who is grandmother's younger brother? Grandmother's younger brother is great-uncle."),
    ("grandmother", "older sister"): ("great-aunt (grandmother's sister)", "Who is grandmother's older sister? Grandmother's older sister is great-aunt."),
    ("grandmother", "younger sister"): ("great-aunt (grandmother's sister)", "Who is grandmother's younger sister? Grandmother's younger sister is great-aunt."),
    ("maternal grandfather", "older brother"): ("maternal great-uncle", "Who is maternal grandfather's older brother? Maternal grandfather's older brother is maternal great-uncle."),
    ("maternal grandfather", "younger brother"): ("maternal great-uncle", "Who is maternal grandfather's younger brother? Maternal grandfather's younger brother is maternal great-uncle."),
    ("maternal grandfather", "older sister"): ("maternal great-aunt", "Who is maternal grandfather's older sister? Maternal grandfather's older sister is maternal great-aunt."),
    ("maternal grandfather", "younger sister"): ("maternal great-aunt", "Who is maternal grandfather's younger sister? Maternal grandfather's younger sister is maternal great-aunt."),
    ("maternal grandmother", "older brother"): ("maternal great-uncle", "Who is maternal grandmother's older brother? Maternal grandmother's older brother is maternal great-uncle."),
    ("maternal grandmother", "younger brother"): ("maternal great-uncle", "Who is maternal grandmother's younger brother? Maternal grandmother's younger brother is maternal great-uncle."),
    ("maternal grandmother", "older sister"): ("maternal great-aunt", "Who is maternal grandmother's older sister? Maternal grandmother's older sister is maternal great-aunt."),
    ("maternal grandmother", "younger sister"): ("maternal great-aunt", "Who is maternal grandmother's younger sister? Maternal grandmother's younger sister is maternal great-aunt."),
    ("uncle (father's older brother)", "older brother"): ("elder uncle", "Who is uncle's older brother? Uncle's older brother is elder uncle."),
    ("uncle (father's older brother)", "younger brother"): ("uncle (father's younger brother)", "Who is uncle's younger brother? Uncle's younger brother is uncle."),
    ("uncle (father's younger brother)", "older brother"): ("uncle (father's older brother)", "Who is uncle's older brother? Uncle's older brother is uncle."),
    ("uncle (father's younger brother)", "younger brother"): ("younger uncle", "Who is uncle's younger brother? Uncle's younger brother is younger uncle."),
    ("aunt (father's sister)", "older sister"): ("elder aunt", "Who is aunt's older sister? Aunt's older sister is elder aunt."),
    ("aunt (father's sister)", "younger sister"): ("younger aunt", "Who is aunt's younger sister? Aunt's younger sister is younger aunt."),
    ("uncle (mother's brother)", "older brother"): ("elder uncle", "Who is uncle's older brother? Uncle's older brother is elder uncle."),
    ("uncle (mother's brother)", "younger brother"): ("younger uncle", "Who is uncle's younger brother? Uncle's younger brother is younger uncle."),
    ("aunt (mother's sister)", "older sister"): ("elder aunt", "Who is aunt's older sister? Aunt's older sister is elder aunt."),
    ("aunt (mother's sister)", "younger sister"): ("younger aunt", "Who is aunt's younger sister? Aunt's younger sister is younger aunt."),
    ("great-grandfather", "father"): ("great-great-grandfather", "Who is great-grandfather's father? Great-grandfather's father is great-great-grandfather."),
    ("great-grandmother", "mother"): ("great-great-grandmother", "Who is great-grandmother's mother? Great-grandmother's mother is great-great-grandmother."),
    ("uncle (father's older brother)", "son"): ("cousin (male)", "Who is uncle's son? Uncle's son is male cousin."),
    ("uncle (father's younger brother)", "son"): ("cousin (male)", "Who is uncle's son? Uncle's son is male cousin."),
    ("aunt (father's sister)", "son"): ("cousin (male)", "Who is aunt's son? Aunt's son is male cousin."),
    ("uncle (mother's brother)", "son"): ("cousin (male)", "Who is uncle's son? Uncle's son is male cousin."),
    ("aunt (mother's sister)", "son"): ("cousin (male)", "Who is aunt's son? Aunt's son is male cousin."),
    ("uncle (father's older brother)", "daughter"): ("cousin (female)", "Who is uncle's daughter? Uncle's daughter is female cousin."),
    ("uncle (father's younger brother)", "daughter"): ("cousin (female)", "Who is uncle's daughter? Uncle's daughter is female cousin."),
    ("aunt (father's sister)", "daughter"): ("cousin (female)", "Who is aunt's daughter? Aunt's daughter is female cousin."),
    ("uncle (mother's brother)", "daughter"): ("cousin (female)", "Who is uncle's daughter? Uncle's daughter is female cousin."),
    ("aunt (mother's sister)", "daughter"): ("cousin (female)", "Who is aunt's daughter? Aunt's daughter is female cousin."),
    ("grandfather", "wife"): ("grandmother", "Who is grandfather's wife? Grandfather's wife is grandmother."),
    ("grandmother", "husband"): ("grandfather", "Who is grandmother's husband? Grandmother's husband is grandfather."),
    ("maternal grandfather", "wife"): ("maternal grandmother", "Who is maternal grandfather's wife? Maternal grandfather's wife is maternal grandmother."),
    ("maternal grandmother", "husband"): ("maternal grandfather", "Who is maternal grandmother's husband? Maternal grandmother's husband is maternal grandfather."),
    ("father", "wife"): ("mother", "Who is father's wife? Father's wife is mother."),
    ("mother", "husband"): ("father", "Who is mother's husband? Mother's husband is father."),
    ("uncle (father's older brother)", "wife"): ("aunt (uncle's wife)", "Who is uncle's wife? Uncle's wife is aunt."),
    ("uncle (father's younger brother)", "wife"): ("aunt (uncle's wife)", "Who is uncle's wife? Uncle's wife is aunt."),
    ("aunt (father's sister)", "husband"): ("uncle (aunt's husband)", "Who is aunt's husband? Aunt's husband is uncle."),
    ("uncle (mother's brother)", "wife"): ("aunt (uncle's wife)", "Who is uncle's wife? Uncle's wife is aunt."),
    ("aunt (mother's sister)", "husband"): ("uncle (aunt's husband)", "Who is aunt's husband? Aunt's husband is uncle."),
    ("great-grandfather", "wife"): ("great-grandmother", "Who is great-grandfather's wife? Great-grandfather's wife is great-grandmother."),
    ("great-grandmother", "husband"): ("great-grandfather", "Who is great-grandmother's husband? Great-grandmother's husband is great-grandfather."),
    ("maternal great-grandfather", "wife"): ("maternal great-grandmother", "Who is maternal great-grandfather's wife? Maternal great-grandfather's wife is maternal great-grandmother."),
    ("maternal great-grandmother", "husband"): ("maternal great-grandfather", "Who is maternal great-grandmother's husband? Maternal great-grandmother's husband is maternal great-grandfather."),
    ("older brother", "son"): ("nephew", "Who is older brother's son? Older brother's son is nephew."),
    ("older sister", "son"): ("nephew", "Who is older sister's son? Older sister's son is nephew."),
    ("older brother", "daughter"): ("niece", "Who is older brother's daughter? Older brother's daughter is niece."),
    ("older sister", "daughter"): ("niece", "Who is older sister's daughter? Older sister's daughter is niece.")}

RELATIONS = [
    "爸爸", "妈妈", "爷爷", "奶奶", "外公", "外婆", "哥哥", "姐姐", "弟弟", "妹妹", "姑姑", "伯伯", "叔叔", "舅舅", "姨妈", "曾祖父", "曾祖母", "外曾祖父", "外曾祖母","丈夫","妻子"
]

RELATION_GROUPS = {
    "父母": ["爸爸", "妈妈"],
    "祖辈": ["爷爷", "奶奶", "外公", "外婆", "曾祖父", "曾祖母", "外曾祖父", "外曾祖母"],
    "兄弟姐妹": ["哥哥", "姐姐", "弟弟", "妹妹"],
    "旁系": ["姑姑", "伯伯", "叔叔", "舅舅", "姨妈","丈夫","妻子"],
}
#################################################################勿动######################################################################
class RelativeCalculator(QWidget):
    def confirm_option2(self):
        if not hasattr(self, 'second_selected') or not self.second_selected:
            t = self.texts[self.language]
            QMessageBox.warning(self, t['title'], t['warning2'])
            return
        self.label_step2.hide()
        for btn in self.group2_btns:
            btn.hide()
        for btn in self.option2_btns:
            btn.hide()
        self.confirm_btn2.hide()
        self.calculate()
    def __init__(self):
        super().__init__()
        self.language = 'cn'  # 默认中文
        self.setWindowTitle("亲属计算器")
        self.resize(900, 700)
        self.setMinimumSize(600, 480)
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.init_ui()

    def init_ui(self):
        # 语言文本映射
        self.texts = {
            'cn': {
                'title': '亲属计算器',
                'step1': '请选择第一个亲属分组:',
                'step2': '请选择第二个亲属分组:',
                'clear': '清除',
                'confirm': '确定',
                'result_placeholder': '结果将在这里显示',
                'think_placeholder': '思考过程将在这里显示',
                'restart': '重新开始计算',
                'fullscreen_on': '开启全屏',
                'fullscreen_off': '关闭全屏',
                'warning1': '请选择第一个亲属！',
                'warning2': '请选择第二个亲属！',
                'warning_both': '请选择两个亲属！',
            },
            'en': {
                'title': 'Relative Calculator',
                'step1': 'Please select the first relative group:',
                'step2': 'Please select the second relative group:',
                'clear': 'Clear',
                'confirm': 'Confirm',
                'result_placeholder': 'Result will be shown here',
                'think_placeholder': 'Thinking process will be shown here',
                'restart': 'Restart Calculation',
                'fullscreen_on': 'Fullscreen',
                'fullscreen_off': 'Exit Fullscreen',
                'warning1': 'Please select the first relative!',
                'warning2': 'Please select the second relative!',
                'warning_both': 'Please select two relatives!',
            }
        }
        import ctypes
        # 检测Windows深色模式
        def is_dark_mode():
            try:
                import winreg
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
                value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
                return value == 0
            except Exception:
                return False
#################################################################勿动######################################################################
        self.is_dark = is_dark_mode()
        # 配色方案
        if self.is_dark:
            # 深色模式
            bg_color = "#181c24"
            card_bg = "#232a36"
            title_color = "#43cea2"
            label_color = "#43cea2"
            btn_bg = "#232a36"
            btn_grad = "#232a36"
            btn_text = "#fff"
            btn_highlight = "#43cea2"
            border_color = "#43cea2"
            think_bg = "#222831"
            think_text = "#e0e7ef"
            copyright_color = "#888"
        else:
            # 浅色模式
            bg_color = "#f7fafc"
            card_bg = "#f7fafc"
            title_color = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #43cea2, stop:1 #185a9d)"
            label_color = "#185a9d"
            btn_bg = "#43cea2"
            btn_grad = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #43cea2, stop:1 #185a9d)"
            btn_text = "#fff"
            btn_highlight = "#185a9d"
            border_color = "#43cea2"
            think_bg = "#e0e7ef"
            think_text = "#3a3a3a"
            copyright_color = "#999"
#################################################################勿动######################################################################
        self.setStyleSheet(f"background: {bg_color};")
        font_title = QFont("微软雅黑", 22, QFont.Bold)
        font_result = QFont("微软雅黑", 20, QFont.Bold)
        font_think = QFont("微软雅黑", 14)
        self.btn_font = QFont("微软雅黑", 16)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(30, 30, 30, 20)
        self.layout.setSpacing(18)
        self.setLayout(self.layout)

        # 语言选择下拉框（右上角）
        self.lang_combo = QComboBox(self)
        self.lang_combo.addItem('中文 Chinese', 'cn')
        self.lang_combo.addItem('English 英文', 'en')
        self.lang_combo.setFixedWidth(220)
        self.lang_combo.setMinimumHeight(48)
        self.lang_combo.setFont(QFont("微软雅黑", 18, QFont.Bold))
        self.lang_combo.setStyleSheet("QComboBox {margin-right: 20px; margin-top: 20px; font-size: 20px; border-radius: 16px; background: #43cea2; color: #fff; font-weight: bold;} QComboBox QAbstractItemView {font-size: 18px;}")
        self.lang_combo.currentIndexChanged.connect(self.change_language)
        # 右上角布局
        top_layout = QHBoxLayout()
        top_layout.addStretch()
        top_layout.addWidget(self.lang_combo)
        self.layout.addLayout(top_layout)
        # 分组和亲属英文映射
        self.group_names_map = {
            '父母': {'cn': '父母', 'en': 'Parents'},
            '祖辈': {'cn': '祖辈', 'en': 'Grandparents'},
            '兄弟姐妹': {'cn': '兄弟姐妹', 'en': 'Siblings'},
            '旁系': {'cn': '旁系', 'en': 'Extended Family'},
        }
        self.relation_names_map = {
            '爸爸': {'cn': '爸爸', 'en': 'Father'}, '妈妈': {'cn': '妈妈', 'en': 'Mother'},
            '爷爷': {'cn': '爷爷', 'en': 'Grandfather'}, '奶奶': {'cn': '奶奶', 'en': 'Grandmother'},
            '外公': {'cn': '外公', 'en': 'Maternal Grandfather'}, '外婆': {'cn': '外婆', 'en': 'Maternal Grandmother'},
            '哥哥': {'cn': '哥哥', 'en': 'Older Brother'}, '姐姐': {'cn': '姐姐', 'en': 'Older Sister'},
            '弟弟': {'cn': '弟弟', 'en': 'Younger Brother'}, '妹妹': {'cn': '妹妹', 'en': 'Younger Sister'},
            '姑姑': {'cn': '姑姑', 'en': "Aunt (Father's Sister)"}, '伯伯': {'cn': '伯伯', 'en': "Uncle (Father's Older Brother)"},
            '叔叔': {'cn': '叔叔', 'en': "Uncle (Father's Younger Brother)"}, '舅舅': {'cn': '舅舅', 'en': "Uncle (Mother's Brother)"},
            '姨妈': {'cn': '姨妈', 'en': "Aunt (Mother's Sister)"}, '曾祖父': {'cn': '曾祖父', 'en': 'Great Grandfather'},
            '曾祖母': {'cn': '曾祖母', 'en': 'Great Grandmother'}, '外曾祖父': {'cn': '外曾祖父', 'en': 'Maternal Great Grandfather'},
            '外曾祖母': {'cn': '外曾祖母', 'en': 'Maternal Great Grandmother'}, '丈夫': {'cn': '丈夫', 'en': 'Husband'},
            '妻子': {'cn': '妻子', 'en': 'Wife'},
        }

        self.title_label = QLabel(self.texts[self.language]['title'])
        self.title_label.setFont(QFont("微软雅黑", 28, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet(f"color: {title_color}; margin-bottom: 10px;")
        self.layout.addWidget(self.title_label)

        self.label_step = QLabel(self.texts[self.language]['step1'])
        self.label_step.setFont(font_title)
        self.label_step.setAlignment(Qt.AlignCenter)
        self.label_step.setStyleSheet(f"color: {label_color}; margin-bottom: 8px;")
        self.layout.addWidget(self.label_step)

        self.group_grid = QWidget()
        self.group_grid_layout = QVBoxLayout()
        self.group_grid_layout.setSpacing(12)
        self.group_grid.setLayout(self.group_grid_layout)
        self.group_btns = []
        group_names = list(RELATION_GROUPS.keys())
        for i in range(0, len(group_names), 2):
            row = QHBoxLayout()
            row.setSpacing(16)
            for j in range(2):
                if i + j < len(group_names):
                    group = group_names[i + j]
                    btn = QPushButton(self.group_names_map[group][self.language])
                    btn.group_key = group
                    btn.setMinimumWidth(180)
                    btn.setMinimumHeight(60)
                    btn.setFont(QFont("微软雅黑", 18, QFont.Bold))
                    btn.setSizePolicy(QPushButton().sizePolicy())
                    btn.setStyleSheet(f"QPushButton {{border-radius: 18px; background: {btn_grad}; color: {btn_text}; font-weight: bold; border:2px solid #43cea2;}} QPushButton:hover {{background: {btn_highlight};}}")
                    btn.clicked.connect(lambda checked, g=group: self.show_options(g))
                    row.addWidget(btn)
                    self.group_btns.append(btn)
            self.group_grid_layout.addLayout(row)
        # 安全的点击动画：点击时临时改变样式，延时恢复
        def safe_click_effect(btn):
            orig_style = btn.styleSheet()
            btn.setStyleSheet(orig_style + "QPushButton {transform: scale(0.96); box-shadow: 0px 8px 24px #43cea2cc;}")
            from PyQt5.QtCore import QTimer
            QTimer.singleShot(120, lambda: btn.setStyleSheet(orig_style))
        for btn in self.group_btns:
            btn.pressed.connect(lambda b=btn: safe_click_effect(b))
        self.layout.addWidget(self.group_grid)

        # 第一个分组选择区下方添加清除按钮
        self.clear_btn1 = QPushButton(self.texts[self.language]['clear'])
        self.clear_btn1.setMinimumWidth(100)
        self.clear_btn1.setMinimumHeight(36)
        self.clear_btn1.setFont(QFont("微软雅黑", 13, QFont.Bold))
        self.clear_btn1.setStyleSheet("QPushButton {border-radius: 12px; background: #e57373; color: #fff; font-weight: bold;} QPushButton:hover {background: #ff8a65;}")
        self.clear_btn1.clicked.connect(self.reset_ui)
        self.layout.addWidget(self.clear_btn1)

        self.line1 = QFrame()
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.line1.setStyleSheet(f"color: {border_color}; margin: 10px 0;")
        self.layout.addWidget(self.line1)

        self.option_grid = QWidget()
        self.option_grid_layout = QVBoxLayout()
        self.option_grid_layout.setSpacing(10)
        self.option_grid.setLayout(self.option_grid_layout)
        self.option_btns = []
        self.layout.addWidget(self.option_grid)

        self.confirm_btn = QPushButton(self.texts[self.language]['confirm'])
        self.confirm_btn.setMinimumWidth(140)
        self.confirm_btn.setMinimumHeight(48)
        self.confirm_btn.setFont(self.btn_font)
        self.confirm_btn.setStyleSheet(f"QPushButton {{border-radius: 16px; background: {btn_grad}; color: {btn_text}; font-weight: bold; border:2px solid #43cea2;}} QPushButton:hover {{background: {btn_highlight};}}")
        self.confirm_btn.clicked.connect(self.confirm_option)
        self.confirm_btn.hide()
        self.layout.addWidget(self.confirm_btn)

        self.label_step2 = QLabel(self.texts[self.language]['step2'])
        self.label_step2.setFont(font_title)
        self.label_step2.setAlignment(Qt.AlignCenter)
        self.label_step2.setStyleSheet(f"color: {label_color}; margin-bottom: 8px;")
        self.label_step2.hide()
        self.layout.addWidget(self.label_step2)

        self.group2_grid = QWidget()
        self.group2_grid_layout = QVBoxLayout()
        self.group2_grid_layout.setSpacing(12)
        self.group2_grid.setLayout(self.group2_grid_layout)
        self.group2_btns = []
        for i in range(0, len(group_names), 2):
            row = QHBoxLayout()
            row.setSpacing(16)
            for j in range(2):
                if i + j < len(group_names):
                    group = group_names[i + j]
                    btn = QPushButton(self.group_names_map[group][self.language])
                    btn.group_key = group
                    btn.setMinimumWidth(180)
                    btn.setMinimumHeight(60)
                    btn.setFont(QFont("微软雅黑", 18, QFont.Bold))
                    btn.setSizePolicy(QPushButton().sizePolicy())
                    btn.setStyleSheet(f"QPushButton {{border-radius: 18px; background: {btn_grad}; color: {btn_text}; font-weight: bold; border:2px solid #43cea2;}} QPushButton:hover {{background: {btn_highlight};}}")
                    btn.clicked.connect(lambda checked, g=group: self.show_options2(g))
                    row.addWidget(btn)
                    self.group2_btns.append(btn)
                    btn.hide()
            self.group2_grid_layout.addLayout(row)
        self.layout.addWidget(self.group2_grid)

        # 第二个分组选择区下方添加清除按钮
        self.clear_btn2 = QPushButton(self.texts[self.language]['clear'])
        self.clear_btn2.setMinimumWidth(100)
        self.clear_btn2.setMinimumHeight(36)
        self.clear_btn2.setFont(QFont("微软雅黑", 13, QFont.Bold))
        self.clear_btn2.setStyleSheet("QPushButton {border-radius: 12px; background: #e57373; color: #fff; font-weight: bold;} QPushButton:hover {background: #ff8a65;}")
        self.clear_btn2.clicked.connect(self.reset_ui)
        self.clear_btn2.hide()
        self.layout.addWidget(self.clear_btn2)

        self.line2 = QFrame()
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.line2.setStyleSheet(f"color: {border_color}; margin: 10px 0;")
        self.line2.hide()
        self.layout.addWidget(self.line2)

        self.option2_grid = QWidget()
        self.option2_grid_layout = QVBoxLayout()
        self.option2_grid_layout.setSpacing(10)
        self.option2_grid.setLayout(self.option2_grid_layout)
        self.option2_btns = []
        self.layout.addWidget(self.option2_grid)

        self.confirm_btn2 = QPushButton(self.texts[self.language]['confirm'])
        self.confirm_btn2.setMinimumWidth(140)
        self.confirm_btn2.setMinimumHeight(48)
        self.confirm_btn2.setFont(self.btn_font)
        self.confirm_btn2.setStyleSheet(f"QPushButton {{border-radius: 16px; background: {btn_grad}; color: {btn_text}; font-weight: bold; border:2px solid #43cea2;}} QPushButton:hover {{background: {btn_highlight};}}")
        self.confirm_btn2.clicked.connect(self.confirm_option2)
        self.confirm_btn2.hide()
        self.layout.addWidget(self.confirm_btn2)

        self.result_card = QWidget()
        self.result_card_layout = QVBoxLayout()
        self.result_card_layout.setContentsMargins(20, 20, 20, 20)
        self.result_card_layout.setSpacing(10)
        self.result_card.setLayout(self.result_card_layout)
        self.result_card.setStyleSheet(f"background: {card_bg}; border-radius: 18px; box-shadow: 0px 2px 12px {border_color}22; margin-top: 18px;")

        self.result_label = QLabel(self.texts[self.language]['result_placeholder'])
        self.result_label.setFont(font_result)
        self.result_label.setStyleSheet(f"color: {label_color};")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_card_layout.addWidget(self.result_label)

        self.think_label = QLabel(self.texts[self.language]['think_placeholder'])
        self.think_label.setFont(font_think)
        self.think_label.setStyleSheet(f"background: {think_bg}; color: {think_text}; border-radius: 12px; padding: 10px; font-size: 14px;")
        self.think_label.setWordWrap(True)
        self.result_card_layout.addWidget(self.think_label)
        # 新增：重新计算按钮
        self.restart_btn = QPushButton(self.texts[self.language]['restart'])
        self.restart_btn.setMinimumWidth(140)
        self.restart_btn.setMinimumHeight(44)
        self.restart_btn.setFont(QFont("微软雅黑", 15, QFont.Bold))
        self.restart_btn.setStyleSheet("QPushButton {border-radius: 14px; background: #ffb300; color: #333; font-weight: bold; margin-top: 8px;} QPushButton:hover {background: #ffd54f;}")
        self.restart_btn.clicked.connect(self.reset_ui)
        self.restart_btn.hide()
        self.result_card_layout.addWidget(self.restart_btn)

        self.layout.addWidget(self.result_card)

        # 全屏/窗口切换按钮
        self.fullscreen_btn = QPushButton(self.texts[self.language]['fullscreen_off'])
        self.fullscreen_btn.setMinimumWidth(120)
        self.fullscreen_btn.setMinimumHeight(36)
        self.fullscreen_btn.setFont(QFont("微软雅黑", 13, QFont.Bold))
        self.fullscreen_btn.setStyleSheet("QPushButton {border-radius: 12px; background: #43cea2; color: #fff; font-weight: bold;} QPushButton:hover {background: #185a9d;}")
        self.fullscreen_btn.clicked.connect(self.toggle_fullscreen)
        self.layout.addWidget(self.fullscreen_btn)
    def select_second(self, relation):
        self.second_selected = relation
        # 高亮已选项
        for btn in self.option2_btns:
            if btn.relation_key == relation:
                btn.setStyleSheet("QPushButton {border-radius: 8px; background: #ffb300; color: #333; font-weight: bold; border:2px solid #ffb300;}")
            else:
                btn.setStyleSheet("QPushButton {border-radius: 8px; background: #81d4fa; color: #333; font-weight: bold; border:2px solid #1976d2;}")

    def show_options(self, group):
        # 清空选项按钮
        for btn in self.option_btns:
            btn.setParent(None)
        self.option_btns.clear()
        self.selected_group = group
        # 高亮分组按钮
        for btn in self.group_btns:
            if btn.group_key == group:
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
                    btn = QPushButton(self.relation_names_map[relation][self.language])
                    btn.relation_key = relation
                    btn.setMinimumWidth(150)
                    btn.setMinimumHeight(48)
                    btn.setFont(QFont("微软雅黑", 16, QFont.Bold))
                    btn.setSizePolicy(QPushButton().sizePolicy())
                    btn.setStyleSheet("QPushButton {border-radius: 12px; background: #81d4fa; color: #333; font-weight: bold; border:2px solid #1976d2; font-size: 16px;}")
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
            t = self.texts[self.language]
            QMessageBox.warning(self, t['title'], t['warning1'])
            return
        self.label_step.hide()
        self.clear_btn1.hide()
        for btn in self.group_btns:
            btn.hide()
        for btn in self.option_btns:
            btn.hide()
        self.confirm_btn.hide()
        self.label_step2.show()
        self.clear_btn2.show()
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
            if btn.group_key == group:
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
                    btn = QPushButton(self.relation_names_map[relation][self.language])
                    btn.relation_key = relation
                    btn.setMinimumWidth(150)
                    btn.setMinimumHeight(48)
                    btn.setFont(QFont("微软雅黑", 16, QFont.Bold))
                    btn.setSizePolicy(QPushButton().sizePolicy())
                    btn.setStyleSheet("QPushButton {border-radius: 12px; background: #81d4fa; color: #333; font-weight: bold; border:2px solid #1976d2; font-size: 16px;}")
                    btn.clicked.connect(lambda checked, r=relation: self.select_second(r))
                    row.addWidget(btn)
                    self.option2_btns.append(btn)
            self.option2_grid_layout.addLayout(row)
        self.confirm_btn2.show()

    def change_language(self):
        # 切换语言
        self.language = self.lang_combo.currentData()
        t = self.texts[self.language]
        self.title_label.setText(t['title'])
        self.label_step.setText(t['step1'])
        self.label_step2.setText(t['step2'])
        self.clear_btn1.setText(t['clear'])
        self.clear_btn2.setText(t['clear'])
        self.confirm_btn.setText(t['confirm'])
        self.confirm_btn2.setText(t['confirm'])
        self.result_label.setText(t['result_placeholder'])
        self.think_label.setText(t['think_placeholder'])
        self.restart_btn.setText(t['restart'])
        # 分组按钮
        for btn in self.group_btns:
            btn.setText(self.group_names_map[btn.group_key][self.language])
        for btn in self.group2_btns:
            btn.setText(self.group_names_map[btn.group_key][self.language])
        # 选项按钮
        for btn in self.option_btns:
            if hasattr(btn, 'relation_key'):
                btn.setText(self.relation_names_map[btn.relation_key][self.language])
        for btn in self.option2_btns:
            if hasattr(btn, 'relation_key'):
                btn.setText(self.relation_names_map[btn.relation_key][self.language])
        # 全屏按钮根据状态
        if self.isFullScreen():
            self.fullscreen_btn.setText(t['fullscreen_off'])
        else:
            self.fullscreen_btn.setText(t['fullscreen_on'])
    def toggle_fullscreen(self):
        t = self.texts[self.language]
        if self.isFullScreen():
            self.showNormal()
            self.resize(900, 700)
            qr = self.frameGeometry()
            cp = self.screen().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
            self.fullscreen_btn.setText(t['fullscreen_on'])
        else:
            self.showFullScreen()
            self.fullscreen_btn.setText(t['fullscreen_off'])

    def calculate(self):
        first = self.first_selected
        second = self.second_selected
        t = self.texts[self.language]
        if not first or not second:
            QMessageBox.warning(self, t['title'], t['warning_both'])
            return
        if self.language == 'en':
            # 1111111111111111111111111111111111111111111111111111111111111111111
            # 英文映射请粘贴到文件顶部 RELATION_MAP_EN
            first_en = self.relation_names_map.get(first, {}).get('en', first).lower()
            second_en = self.relation_names_map.get(second, {}).get('en', second).lower()
            result, thinking = RELATION_MAP_EN.get((first_en, second_en), ("Unknown (If you can ask this, you are the answer!)", self.generate_thinking_en(first_en, second_en)))
            self.result = result
            self.thinking = thinking
        else:
            self.result, self.thinking = RELATION_MAP.get((first, second), ("未知(能问出这种问题的人是这个)", self.generate_thinking(first, second)))
        self.show_fullscreen_thinking(self.thinking)

    def generate_thinking_en(self, first, second):
        return f"Who is {first}'s {second}? {first}'s {second} is... (not yet included)"

    def show_fullscreen_thinking(self, text):
        self.result_label.hide()
        self.think_label.hide()
        # 创建全屏遮罩（自适应窗口大小）
        self.fullscreen_label = QLabel("", self)
        self.fullscreen_label.setAlignment(Qt.AlignCenter)
        # 根据深浅色模式设置背景色
        bg = "#181c24" if getattr(self, 'is_dark', False) else "white"
        text_color = "#43cea2" if getattr(self, 'is_dark', False) else "#185a9d"
        self.fullscreen_label.setStyleSheet(f"background: {bg}; color: {text_color};")
        self.fullscreen_label.setFont(QFont("微软雅黑", 40, QFont.Bold))
        self.fullscreen_label.setWordWrap(True)
        self.fullscreen_label.setGeometry(self.rect())
        self.fullscreen_label.show()
        # 支持英文切换
        if self.language == 'en':
            self.full_text = self.translate_thinking(text)
        else:
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
        t = self.texts[self.language]
        self.fullscreen_label.hide()
        self.result_label.show()
        self.think_label.show()
        if self.language == 'cn':
            self.result_label.setText(f"结果：{self.result}")
            self.think_label.setText(f"思考过程：{self.thinking}")
        else:
            self.result_label.setText(f"Result: {self.translate_result(self.result)}")
            self.think_label.setText(f"Thinking: {self.translate_thinking(self.thinking)}")
        self.restart_btn.show()
        QTimer.singleShot(30000, QApplication.instance().quit)
    def reset_ui(self):
        # 重置所有界面和状态，回到初始选择
        self.first_selected = None
        self.second_selected = None
        self.result = None
        self.thinking = None
        t = self.texts[self.language]
        self.result_label.setText(t['result_placeholder'])
        self.think_label.setText(t['think_placeholder'])
        self.result_label.hide()
        self.think_label.hide()
        self.restart_btn.hide()
        self.label_step.show()
        self.clear_btn1.show()
        self.clear_btn2.hide()
        for btn in self.group_btns:
            btn.show()
            btn.setStyleSheet(f"QPushButton {{border-radius: 16px; background: #43cea2; color: #fff; font-weight: bold; border:2px solid #43cea2;}} QPushButton:hover {{background: #185a9d;}}")
        for btn in self.option_btns:
            btn.hide()
        self.confirm_btn.hide()
        self.label_step2.hide()
        for btn in self.group2_btns:
            btn.hide()
        self.line2.hide()
        for btn in self.option2_btns:
            btn.hide()
        self.confirm_btn2.hide()
        self.option_btns.clear()
        self.option2_btns.clear()
        if hasattr(self, 'fullscreen_label'):
            self.fullscreen_label.hide()
    def translate_result(self, result):
        # 结果翻译（简易映射）
        result_map = {
            '爷爷': 'Grandfather', '奶奶': 'Grandmother', '外公': 'Maternal Grandfather', '外婆': 'Maternal Grandmother',
            '爸爸': 'Father', '妈妈': 'Mother', '哥哥': 'Older Brother', '姐姐': 'Older Sister', '弟弟': 'Younger Brother', '妹妹': 'Younger Sister',
            '姑姑': 'Aunt (Father’s Sister)', '伯伯': 'Uncle (Father’s Older Brother)', '叔叔': 'Uncle (Father’s Younger Brother)',
            '舅舅': 'Uncle (Mother’s Brother)', '姨妈': 'Aunt (Mother’s Sister)', '曾祖父': 'Great Grandfather', '曾祖母': 'Great Grandmother',
            '外曾祖父': 'Maternal Great Grandfather', '外曾祖母': 'Maternal Great Grandmother', '丈夫': 'Husband', '妻子': 'Wife',
            '伯祖父': 'Great Uncle (Father’s Uncle)', '叔祖父': 'Great Uncle (Father’s Younger Uncle)', '姑祖母': 'Great Aunt (Father’s Aunt)',
            '舅祖父': 'Great Uncle (Mother’s Uncle)', '姨祖母': 'Great Aunt (Mother’s Aunt)', '外伯祖父': 'Maternal Great Uncle',
            '外叔祖父': 'Maternal Great Uncle', '外姑祖母': 'Maternal Great Aunt', '外舅祖父': 'Maternal Great Uncle', '外姨祖母': 'Maternal Great Aunt',
            '伯母': 'Aunt (Uncle’s Wife)', '婶婶': 'Aunt (Uncle’s Wife)', '姑父': 'Uncle (Aunt’s Husband)', '舅妈': 'Aunt (Uncle’s Wife)',
            '姨父': 'Uncle (Aunt’s Husband)', '堂哥/堂弟': 'Cousin (Father’s Brother’s Son)', '表哥/表弟': 'Cousin (Aunt/Uncle’s Son)',
            '堂姐/堂妹': 'Cousin (Father’s Brother’s Daughter)', '表姐/表妹': 'Cousin (Aunt/Uncle’s Daughter)',
            '侄子': 'Nephew', '侄女': 'Niece', '外甥': 'Nephew (Sister’s Son)', '外甥女': 'Niece (Sister’s Daughter)',
            '未知(能问出这种问题的人是这个)': 'Unknown (If you can ask this, you are the answer!)',
        }
        return result_map.get(result, result)

    def translate_thinking(self, thinking):
        # 思考过程翻译（简易规则）
        # 只翻译常见句式
        thinking = thinking.replace('思考过程：', 'Thinking: ')
        thinking = thinking.replace('结果：', 'Result: ')
        thinking = thinking.replace('是什么？', ' is what?')
        thinking = thinking.replace('是', ' is ')
        thinking = thinking.replace('暂未收录', 'not yet included')
        thinking = thinking.replace('的', "'s ")
        return thinking

    def generate_thinking(self, first, second):
        return f"{first}的{second}是什么？{first}的{second}是……（暂未收录）"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RelativeCalculator()
    window.showFullScreen()
    window.fullscreen_btn.setText(window.texts[window.language]['fullscreen_off'])
    sys.exit(app.exec_())
#原创：@MACBO2013
#github已开源