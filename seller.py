from user import User

class Seller(User):
    """
    Represent a seller.
    Subclass of User.
    """

    def __init__(self, nickname):
        """
        Initialize a seller
        """
        super().__init__(nickname)
        self.comand_list = ["search", "analyze"]




if __name__ == '__main__':
    seller = Seller("Solomiia")
    seller.get_comands()
