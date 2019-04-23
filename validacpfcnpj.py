import re
from typing import Union


class ValidaCpfCnpj:
    """
    Valida CPF ou CNPJ realizando cálculos dos dígitos
    """

    def __init__(self, cpf_cnpj: str = '') -> None:
        """Recebe o CPF/CNPJ

        :param cpf_cnpj: o CPF/CNPJ
        :type cpf_cnpj: str
        """
        self._validado = False
        # O CPF pode ser enviado direto ao instanciar a classe
        # ou como property
        if cpf_cnpj:
            self.cpf_cnpj: str = cpf_cnpj

    def valida(self) -> bool:
        """Realiza toda a validação

        :return: True se for válido, False caso contrário
        :rtype: bool
        """
        if not self.cpf_cnpj:
            return False

        qtd_caractere = len(self.cpf_cnpj)

        # CPF
        if qtd_caractere == 11:
            # Primeiros 9 digitos
            novo_cpf_cnpj: str = self._calcula_digitos(self.cpf_cnpj[:9],
                                                       multiplicador_inicial=10)
            # 9 digitos + primeiro digito verificador
            novo_cpf_cnpj: str = self._calcula_digitos(novo_cpf_cnpj,
                                                       multiplicador_inicial=11)

            if novo_cpf_cnpj == self.cpf_cnpj:
                self._validado = True
                return True

        # CNPJ
        elif qtd_caractere == 14:
            # Primeiros 12 digitos
            novo_cpf_cnpj: str = self._calcula_digitos(self.cpf_cnpj[:12],
                                                       multiplicador_inicial=5)
            # 12 digitos + primeiro digito verificador
            novo_cpf_cnpj: str = self._calcula_digitos(novo_cpf_cnpj,
                                                       multiplicador_inicial=6)

            if novo_cpf_cnpj == self.cpf_cnpj:
                self._validado = True
                return True
        return False

    @property
    def formatado(self):
        """Formata o CPF/CNPJ

        :raises ValueError: Se o CPF/CNPJ não for enviado ou não for válido
        :return: o cpf ou cnpj formatado
        :rtype: str
        """
        if not self._validado:
            if not self.cpf_cnpj or not self.valida():
                raise ValueError("Enviar o CPF e validar para "
                                 "obter CPF formatado.")

        qtd_caracteres = len(self.cpf_cnpj)

        if qtd_caracteres == 11:
            cpf = self.cpf_cnpj

            return '%s.%s.%s-%s' % (cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:],)

        elif qtd_caracteres == 14:
            cnpj = self.cpf_cnpj
            # 63.080.648/0001-35

            return '%s.%s.%s/%s-%s' % \
                   (cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])

    @staticmethod
    def _calcula_digitos(
            fatia_cpf_cnpj: str,
            multiplicador_inicial: int
    ) -> Union[str, bool]:
        """Realiza os cálculos das posições

        :param fatia_cpf_cnpj: fatias de 9 ou 10 digitos do CPF
        :type fatia_cpf_cnpj: str
        :param multiplicador_inicial: o número que inicia os cálculos
        :type multiplicador_inicial: int
        :return: a fatia do CPF mais um dos digitos gerados
        :rtype: Union[str, bool]
        """
        if not fatia_cpf_cnpj:
            return False

        # Evita sequências
        sequencia: str = fatia_cpf_cnpj[0] * len(fatia_cpf_cnpj)
        if sequencia == fatia_cpf_cnpj:
            return False

        soma: int = 0
        for chave, _ in enumerate(range(len(fatia_cpf_cnpj) + 1, 1, -1)):
            soma += int(fatia_cpf_cnpj[chave]) * multiplicador_inicial

            if (multiplicador_inicial == 2):
                multiplicador_inicial = 9
            else:
                multiplicador_inicial -= 1

        resto: int = 11 - (soma % 11)
        resto: int = resto if resto <= 9 else 0

        return fatia_cpf_cnpj + str(resto)

    @property
    def cpf_cnpj(self) -> str:
        """Getter do CPF

        :return: o CPF
        :rtype: str
        """
        self._validado = False
        return self._cpf_cnpj

    @cpf_cnpj.setter
    def cpf_cnpj(self, cpf_cnpj: str):
        """Setter do CPF

        :param cpf: o CPF
        :type cpf: str
        """
        self._cpf_cnpj = self._so_numeros(cpf_cnpj)

    @staticmethod
    def _so_numeros(cpf_cnpj: str) -> str:
        """Remove todos os digitos não numéricos

        :param cpf_cnpj: o cpf ou cnpj
        :type cpf_cnpj: str
        :return: o cpf/cnpj formatado (só com números)
        :rtype: str
        """
        return re.sub('[^0-9]', '', cpf_cnpj)
