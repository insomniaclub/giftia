from typing import Literal


def detect_language(text: str) -> Literal["zh", "en"]:
    zh_cnt, en_cnt = 0, 0
    for char in list(text):
        # 判断字符的Unicode值是否在中文字符的Unicode范围内
        if "\u4e00" <= char <= "\u9fa5":
            zh_cnt += 4
        # 判断字符是否为英文字符（包括大小写字母和常见标点符号）
        elif ("\u0041" <= char <= "\u005a") or ("\u0061" <= char <= "\u007a"):
            en_cnt += 1
    return "zh" if zh_cnt >= en_cnt else "en"
