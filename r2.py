# 對話記錄整理_02 (line對話記錄格式)
# 統計、計數


# 讀取檔案.txt
def read_file(filename): # 把檔名變成參數來投入
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: # utf-8-sig可以去除文字前的編碼
        for line in f:
            lines.append(line.strip()) # .strip()去除\n
    return lines


# 貼圖、圖片、字數加總
def convert(lines):
    new = []
    person = None # 宣告person，None為無的意思
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ') # .split(' ') 遇到空白鍵切割
        time = s[0]
        name = s[1]
        if name == 'Allen': # 如果name是Allen就向下執行
            if s[2] == '貼圖': # 如果s[2]是貼圖的話
                allen_sticker_count += 1 # 貼圖就+1
            elif s[2] == '圖片': # 如果是圖片
                allen_image_count += 1 # 圖片+1
            else: # 不是的話
                for msg in s[2:]: # 就進行文字數的加總
                    allen_word_count += len(msg)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for msg in s[2:]:
                    viki_word_count += len(msg)
    print('Allen說了：', allen_word_count, '個字。')
    print('Allen傳了：', allen_sticker_count, '個貼圖。')
    print('Allen傳了：', allen_image_count, '張圖片。')

    print('Viki說了：', viki_word_count, '個字。')
    print('Viki傳了：', viki_sticker_count, '個貼圖。')
    print('Viki傳了：', viki_image_count, '張圖片。')

    new.append('Allen說了：' + str(allen_word_count) + '個字。')
    new.append('Allen傳了：' + str(allen_sticker_count) + '個貼圖。')
    new.append('Allen傳了：' + str(allen_image_count) + '張圖片。')
    new.append('Viki說了：' + str(viki_word_count) + '個字。')
    new.append('Viki傳了：' + str(viki_sticker_count) + '個貼圖。')
    new.append('Viki傳了：' + str(viki_image_count) + '張圖片。')
    return new


# 寫入檔案
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines: # for loop迴圈，用line來讀取lines清單的每一行
            f.write(line + '\n') # 寫入每一個檔案並加上換行符號


# 主程式(進入點)
def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    write_file('Line-output.txt', lines)


main()