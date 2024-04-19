class Errors:
    @staticmethod
    def err1():
        print("""Unexpected count of arguments!
                 Tip: Enter odd number of arguments separated by space""")

    @staticmethod
    def err2():
        print("""Syntax error!
                 Tip: Enter unique arguments""")

    @staticmethod
    def err3():
        print("""Too little of arguments!
                 Tip: Enter odd number of arguments (more than 3) separated by space""")