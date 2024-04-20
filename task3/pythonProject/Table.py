import tabulate
from Rules import get_win_index
from colorama import Fore, Style


class Table:
    def __init__(self, headers):
        self.headers = headers

    def generate_table(self):
        headers_row = self.generate_headers_row()
        table_data = [headers_row] + self.generate_rows()
        results = self.format_table(table_data)
        print(results)

    def generate_headers_row(self):
        return ['v PC\\User >'] + [f'{move}' for move in self.headers]

    def generate_rows(self):
        rows = []
        for move_col in self.headers:
            row = self.generate_row(move_col)
            rows.append(row)
        return rows

    def generate_row(self, move_col):
        row = [f'{move_col}']
        for move_row in self.headers:
            result = get_win_index(self.headers, move_col, move_row)
            cell_value = self.format_values(result)
            row.append(cell_value)
        return row

    def format_values(self, result):
        if result == 0:
            return Fore.LIGHTCYAN_EX + Style.BRIGHT + 'Draw' + Style.RESET_ALL
        elif result == 1:
            return Fore.LIGHTRED_EX + Style.BRIGHT + 'Lose' + Style.RESET_ALL
        elif result == -1:
            return Fore.LIGHTGREEN_EX + Style.BRIGHT + 'Win' + Style.RESET_ALL

    def format_table(self, table_data):
        return tabulate.tabulate(table_data, headers='firstrow', tablefmt='grid')
