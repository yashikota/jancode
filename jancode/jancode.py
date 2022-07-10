import sys

import cv2
import jancode.directory as directory
import numpy as np


class JANCode:
    def __init__(self) -> None:
        """初期化"""
        self._bin_number: str = ""

    def _set_jancode_property(self) -> None:
        """JANコードの長さ、高さ、幅を設定"""
        jancode_guard: int = 11  # ガードバーの太さ(3+5+3)
        self._jancode_length: int = len(self._input_number)
        self._jancode_height: int = int(self._jancode_length * 2 * self._ratio)
        self._jancode_width: int = int(self._jancode_length * 7 * self._ratio) + (
            jancode_guard * self._ratio
        )

    def _is_standard(self) -> None:
        """標準サイズのJANコードかどうかを判定"""
        if self._jancode_length == 13:
            # 標準バーコードの桁数が12桁なので先頭1桁分引く
            self._jancode_number: str = self._input_number[1:]
            self._center_potision: int = 5
            self._decide_combination()  # パリティの組み合わせを決定
        else:
            self._center_potision = 3
            self._jancode_number = self._input_number
            self._combination: str = "OOOO"  # 短縮タイプは左側の文字列は全て奇数パリティ

    def _decide_combination(self) -> None:
        """奇数パリティ、偶数パリティの組み合わせを決定"""
        combi = [
            "OOOOOO",
            "OOEOEE",
            "OOEEOE",
            "OOEEEO",
            "OEOOEE",
            "OEEOOE",
            "OEEEOO",
            "OEOEOE",
            "OEOEEO",
            "OEEOEO",
        ]

        self._combination = combi[int(self._input_number[0])]

    def _left_odd_charcter(self, number: int) -> str:
        charcters = [
            "0001101",
            "0011001",
            "0010011",
            "0111101",
            "0100011",
            "0110001",
            "0101111",
            "0111011",
            "0110111",
            "0001011",
        ]

        return charcters[number]

    def _left_even_charcter(self, number: int) -> str:
        charcters = [
            "0100111",
            "0110011",
            "0011011",
            "0100001",
            "0011101",
            "0111001",
            "0000101",
            "0010001",
            "0001001",
            "0010111",
        ]

        return charcters[number]

    def _right_even_charcter(self, number: int) -> str:
        charcters = [
            "1110010",
            "1100110",
            "1101100",
            "1000010",
            "1011100",
            "1001110",
            "1010000",
            "1000100",
            "1001000",
            "1110100",
        ]

        return charcters[number]

    def _convert_bin(self) -> None:
        """入力された数字をJANコード用の2進数に変換し、ガードバーを追加する"""
        left_right_guard: str = "101"
        center_guard: str = "01010"

        self._bin_number += left_right_guard    # 左ガードバーを追加

        for i in range(len(self._jancode_number)):
            if i < self._center_potision:
                self._convert_left(i)
            elif i == self._center_potision:
                self._convert_left(i)
                self._bin_number += center_guard
            elif i > self._center_potision:
                self._bin_number += self._right_even_charcter(
                    int(self._jancode_number[i])
                )

        self._bin_number += left_right_guard    # 右ガードバーを追加

    def _convert_left(self, i:int) -> None:
        if self._combination[i] == "O":
            self._bin_number += self._left_odd_charcter(int(self._jancode_number[i]))
        else:
            self._bin_number += self._left_even_charcter(int(self._jancode_number[i]))

    def _create_array(self) -> None:
        """画像用の配列を作成"""
        self._image: np.ndarray = np.full(
            (self._jancode_width, self._jancode_height), 255
        )

    def _draw_jancode(self) -> None:
        """JANコードを描画"""
        position = 0

        # bin_numberで1のところを黒にする
        for i in range(len(self._bin_number)):
            if self._bin_number[i] == "1":
                self._image[
                    position : position + self._ratio, 0 : self._jancode_height
                ] = 0
            position += self._ratio

    def _add_margin(self) -> None:
        """余白を追加"""
        margin: int = 10 * self._ratio
        height_margin: int = (margin * 2) + self._jancode_width

        width_array: np.ndarray = np.full((margin, self._jancode_height), 255)
        top_array: np.ndarray = np.full((height_margin, margin), 255)
        bottom_array: np.ndarray = np.full((height_margin, margin * 2), 255)

        # 横の余白を追加
        self._image = np.block(
            [
                [width_array],
                [self._image],
                [width_array],
            ]
        )

        # 縦の余白を追加
        self._image = np.block(
            [
                bottom_array,
                self._image,
                top_array,
            ]
        )

    def _calc_checkdigit(self) -> None:
        """チェックデジットを計算

        1. 偶数桁の数字を足して３を掛ける
        2. 奇数桁の数字を足す(チェックデジットの桁である最後尾の桁は除く)
        3. 偶数桁の数値と奇数桁の数値を足して、その値の1の位を見る
        4. 10から1の位の数値を引く (3で求めた数値が0の場合、チェックデジットは0となる)
        """
        # 1
        even_number: int = 0
        for i in range(1, self._jancode_length, 2):
            even_number += int(self._input_number[i])
        even_number *= 3

        # 2
        odd_number: int = 0
        for i in range(0, self._jancode_length - 1, 2):
            odd_number += int(self._input_number[i])

        # 3
        ones_place: int = (even_number + odd_number) % 10

        # 4
        if ones_place == 0:
            self.calced_checkdigit: int = 0
        else:
            self.calced_checkdigit = 10 - ones_place

    def _check_checkdigit(self) -> None:
        """入力されたチェックデジットと計算されたチェックデジットが一致するか確認"""
        self._input_checkdigit: int = int(self._input_number[self._jancode_length - 1])
        if self._input_checkdigit == self.calced_checkdigit:
            print("チェックデジットが正しいです")
        else:
            print("チェックデジットが不正です")
            print("再入力しますか？")
            result: str = input("yes/no: ")
            if result in ["y", "Y", "yes", "Yes", "YES"]:
                self._main()
            else:
                print("終了します")
                sys.exit()

    def _image_rotation(self) -> None:
        """反時計回りに90度回転"""
        self._image = np.rot90(self._image)

    def _write_jancode(self) -> None:
        """画像を出力"""
        cv2.imwrite("./img/{}.png".format(self._input_number), self._image)

    def _main(self, number: str, ratio: str) -> None:
        """メイン処理"""
        directory.check_dir("./img")
        self._input_number: str = str(number)
        self._ratio: int = int(ratio)
        self._set_jancode_property()
        self._calc_checkdigit()
        self._check_checkdigit()
        self._is_standard()
        self._create_array()
        self._convert_bin()
        self._draw_jancode()
        self._add_margin()
        self._image_rotation()
        self._write_jancode()


def input_jancode() -> str:
    """JANコードを入力"""
    number: str = input("JANコードを入力してください: ")
    # もし入力が数字でなければ再入力
    if not number.isdigit():
        print("数字を入力してください")
        input_jancode()
    # もし8桁か13桁でなければ再入力
    if len(number) not in [8, 13]:
        print("8桁か13桁で入力してください")
        input_jancode()

    return number


def input_ratio() -> str:
    """倍率を入力"""
    ratio: str = input("倍率を入力してください: ")
    # もし入力が数字でなければ再入力
    if not ratio.isdigit():
        print("数字を入力してください")
        input_ratio()

    return ratio


def generate(number: str, ratio: str = "10") -> None:
    """JANコードを生成する"""
    jancode = JANCode()
    jancode._main(number, ratio)


if __name__ == "__main__":
    jan = JANCode()
    number : str = input_jancode()
    ratio : str = input_ratio()
    generate(number, ratio)
