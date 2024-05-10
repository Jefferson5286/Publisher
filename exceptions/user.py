class UserAlreadyRegisterError(Exception):
    """
        Exceção Levantada sempre que houver uma tentativa de registro de username já existente.
    """

    def __init__(self):
        super().__init__('User already registered with this username!')


class EmailAlreadyRegisterError(Exception):
    """
        Exceção Levantada sempre que houver uma tentativa de registro de e-mail já existente.
    """

    def __init__(self):
        super().__init__('User already registered with this e-mail!')


class UserNotFound(Exception):
    """
        Exceção levantada sempre que um usuário não for encontrado no banco de dados, sendo por e-mail, username ou
        quaisquer outros dados.
    """

    def __init__(self):
        super().__init__('User not found!')
