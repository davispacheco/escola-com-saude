# Este arquivo contém as regras de negócio.

import pandas as pd


class StudentService:
    def __init__(self, excel_file='cadastro_alunos.xlsx'):
        self.excel_file = excel_file

    def add_student(self, student):
        df = pd.DataFrame({
            'Nome': [student.nome],
            'Idade': [student.idade],
            'Peso': [student.peso],
            'Altura': [student.altura],
            'Estado de Saúde': [student.estado_saude],
            'IMC': [student.imc]
        })
        with pd.ExcelWriter(self.excel_file, mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)

    def process_data(self):
        df = pd.read_excel(self.excel_file)
        limite_sobrepeso = 25
        media_acima_peso = df[df['IMC'] >= limite_sobrepeso]['IMC'].mean()
        media_peso_ideal = df[df['IMC'] < limite_sobrepeso]['IMC'].mean()
        porcentagem_com_doenca = (df[df['Estado de Saúde'] != 'Saudável'].shape[0] / df.shape[0]) * 100
        return media_acima_peso, media_peso_ideal, porcentagem_com_doenca
