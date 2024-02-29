import os
import dotenv
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



dotenv.load_dotenv()


# DADOS DO REMETENTE E DO DESTINATÁRIO.
remetente = os.getenv('email_email', '')
destinatario = remetente

# CONFIGURAÇÕES DO SERVIDOR SMTP.
smtp_server = os.getenv('smtp_server')
smtp_port = os.getenv('smtp_port')
smtp_user = os.getenv('smtp_user')
smtp_password = os.getenv('email_password_2')

# CAMINHO ARQUIVO TEXT
CAMINHO_ARQUIVO_TEXTO = r'C:\Users\leona\Documents\Projetos VSCode\string_Tamplate.txt'

# MENSAGEM DE TEXTO
with open(CAMINHO_ARQUIVO_TEXTO, 'r') as file:
    text_file = file.read()
    template = Template(text_file)
    text_email = template.substitute(name='Daniela', age= '29',\
date_birth= '06/01/1994', city= 'Ubajara - Ce', work= 'enfermeira',\
wage= 'R$ 1.500,00')

print(text_email)

# TRANSFORMANDO A MENSAGEM EM MIMEMULTIPART
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail.'
corpo_email = MIMEText(text_email, 'txt', 'utf-8')
mime_multipart.attach(corpo_email)

# ENVIA E-MAIL.
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso.')