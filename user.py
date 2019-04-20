class User:
    """
    Represents user.
    Base class for Seller and Buyer.
    """
    def __init__(self, nickname):
        """
        Initialize user.
        """
        self.nickname = nickname
        self.comand_list = []

    def get_comands(self):
        print(self.comand_list)


if __name__ == '__main__':
    user = User("Wall-e")
    user.get_comands()
