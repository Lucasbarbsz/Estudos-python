import hashlib
import getpass

banco = [
    {'login': 'joão123', 'senha': '87438b744c34311386b2544ac7b4fe9d46f1833319eda9043a0d7ba4a1e535b4'},
    {'login': 'lucas098', 'senha': 'b037ab542764530ab03fd033fd956d5ecdfab0702baa1179690c22b81cb8a562'},
    {'login': 'mateus45', 'senha': 'e573f0e6513a2d480e4b5d640c2f97909bdbcd799b3bcfe4051ca1b2501b386d'},
]

login_digitado = input('Login: ')
senha_digitada = getpass.getpass('Senha: ')
senha_hash = hashlib.sha256(senha_digitada.encode('utf-8')).hexdigest()
    
for usuario in banco:
    if usuario['login'] == login_digitado and usuario['senha'] == senha_hash:  
        print('Acesso permitido')
        break
else:
    print('Acesso negado')

    
    