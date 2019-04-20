from user import User

class Buyer(User):
    """
    Represent a seller.
    Subclass of User.
    """

    def __init__(self, nickname):
        """
        Initialize a seller
        """
        super().__init__(nickname)
        self.comand_list = ["find", "comparate"]




if __name__ == '__main__':
    buyer = Buyer("Yana")
    buyer.get_comands()
