import pyotp
import time
import qrcode

chave_mestra = "HTTNVYP5TKLG6IZV7CBHC7BDGDEJMT5Z"

# print(pyotp.random_base32())


codigo = pyotp.TOTP(chave_mestra)
print(codigo.now())

link = pyotp.TOTP(chave_mestra). provisioning_uri(name="Isaac", issuer_name="main")
print(link)
meu_qrcode = qrcode.make(link)
meu_qrcode.save("feito.png")