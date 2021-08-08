# 對話記錄整理_01

# 讀取檔案.txt
def read_file(filename): # 把檔名變成參數來投入
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: # utf-8-sig可以去除文字前的編碼
        for line in f:
            lines.append(line.strip()) # .strip()去除\n
    return lines


def convert(lines):
    new = []
    person = None # 宣告person，None為無的意思
    for line in lines:
        if line == 'Allen': # 如果line等於Allen時
            person = 'Allen' # 變數person就等於Allen
            continue # 跳到下一個迴圈
        elif line == 'Tom': # 如果line等於Tom時
            person = 'Tom' # 變數person就等於Tom
            continue # 跳到下一個迴圈
        if person: # 如果person有值，就向下
            new.append(person + ': ' + line)
    return new


# 寫入檔案
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines: # for loop迴圈，用line來讀取lines清單的每一行
            f.write(line + '\n') # 寫入每一個檔案並加上換行符號


# 主程式(進入點)
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)


main()