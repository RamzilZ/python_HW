class StringUtils:

    def capitalize(self, string: str) -> str:

        return string.capitalize()

    def trim(self, string: str) -> str:

        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def contains(self, string: str, symbol: str) -> bool:

        Пример 1: `contains("SkyPro", "S") -> True`
        Пример 2: `contains("SkyPro", "U") -> False`

        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass

        return res

    def delete_symbol(self, string: str, symbol: str) -> str:
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string