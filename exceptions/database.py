from config import env


class PermissionLevelNotAccept(Exception):
    """
        Exceção levantada quando uma houver uma tentativa de execução de operação não aceitável ao nível de permissão.
    """
    def __int__(self):
        super().__init__(f'O nível pe permissão para a execução da função não foi aceito. LEVEL={env.LEVEL}')
