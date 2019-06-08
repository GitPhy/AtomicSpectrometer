# 2019年6月9日
# 当你的Endnote无法导入百度学术的文件时。。。除了吐槽，还可以试用一下这个程序。
# 不要怕，用了不会怀孕。

# 第一步，故作镇定，在百度学术上找文献，然后点击批量引用。
# 第二步，在百度学术上选择GBT1774的格式，然后一键复制，把文字复制粘贴到一个ABC.txt的文本文档里面。
# 第三步，用本程序打开ABC.txt，此时在文件夹里面出现了一个ABD.enw的文件。
# 第四步，打开Endnote的一个Library，然后双击ABD.enw。
# 第五步，不出意外的话，这个时候文献就会导入到Endnote里面。

import re
FileName = 'NewC.enw'
FidGB = open(r'C:\Users\yy\Desktop\TempFile\BaiduXueShuGB.txt')
NumPaper = 0
FidEnw = open(r'EnwTest.enw','r+')
while True:
    LinesGB = FidGB.readline()[0:-1]
    if len(LinesGB) == 0 or NumPaper == 30:  # 如果读完了则跳出去
        break
    if LinesGB[0].strip():  # # 如果本行内容不为空
        NumPaper = NumPaper + 1
        LinesGB.lstrip()
        if not re.search(r'\w', LinesGB[0]):
            LinesGB = ''.join([x for x in LinesGB if x != ' '])  # 去除空格
        LinesGB = LinesGB.replace(',V', ",")  # 替换
        LinesGB = LinesGB.replace(',v.', ",")  # 替换
        LinesGB = LinesGB.replace('；No.', "")  # 替换
        # print(LinesGB)
        if '[J]' in LinesGB:
            EnwText = []
            PaAuthor = []
            PaVol = ''
            PaNo = ''
            PaPage = ''

            p1 = r"^.+?\."
            PaAuthor = re.search(re.compile(p1), LinesGB).group(0)[0:-1]
            PaAuthor = PaAuthor.split(',')
            # print(PaAuthor2)
            PaTitle = re.search(re.compile(r"\..+?\[J\]\."), LinesGB).group(0)[1:-4]
            # print(PaTitle)
            PaJournal = re.search(re.compile(r"\[J\].+?,"), LinesGB).group(0)[4:-1]
            print(LinesGB)
            LinesGB = ''.join([x for x in LinesGB if x != ' '])  # 去除空格
            PaYear = re.search(re.compile(r",\d+?\W"), LinesGB).group(0)[1:-1]
            if PaYear + ',' in LinesGB:
                LinesGB = LinesGB.replace(PaYear + ',', "@V@")  # 替换
                p1 = r'@V@.+?\W'
                PaVol = re.search(re.compile(p1), LinesGB).group(0)[3:-1]
            if '(' in LinesGB:
                PaNo = re.search(re.compile(r"\(.+?\)"), LinesGB).group(0)[1:-1]
            if '-' in LinesGB:
                PaPage = re.search(re.compile(r":.+?\."), LinesGB).group(0)[1:-1]

            PaJournal = '%J ' + PaJournal + '\n'
            PaRefType = '%0 Journal Article \n'
            PaVol = '%V ' + PaVol + '\n'
            PaNo = '%N ' + PaNo + '\n'
            PaPage = '%P ' + PaPage + '\n'
            PaYear = '%D ' + PaYear + '\n'
            PaTitle = '%T ' + PaTitle + '\n'
            PaNewLine = '\n'

            EnwText.append(PaRefType)
            for N3N in range(len(PaAuthor)):
                PaAuthor2 = '%A ' + PaAuthor[N3N] + '\n'
                EnwText.append(PaAuthor2)
            EnwText.append(PaTitle)
            EnwText.append(PaYear)
            EnwText.append(PaJournal)
            EnwText.append(PaPage)
            EnwText.append(PaVol)
            EnwText.append(PaNo)
            EnwText.append(PaNewLine)

            for N4N in range(len(EnwText)):
                TextLine = EnwText[N4N]
                print(TextLine)
                FidEnw.write(TextLine)
FidEnw.close()
FidGB.close()


