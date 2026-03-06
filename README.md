# 🌐 Dicas práticas e exemplos de como usar netaddr

A biblioteca **netaddr** é uma ferramenta essencial para quem trabalha com **automação de redes**.  
Ela permite manipular endereços **IPv4**, **IPv6** e **MAC** de forma eficiente, sendo ideal para tarefas como:

✅ Validação de endereços  
✅ Agrupamento e sumarização de redes  
✅ Manipulação e conversão de formatos  
✅ Operações matemáticas com IPs  

---

## 📦 Sobre este repositório

Aqui você encontrará **dicas práticas** e **exemplos de código** que demonstram como utilizar os principais recursos da biblioteca `netaddr` em projetos reais de automação de rede.

Se você trabalha com **infraestrutura de redes** ou está dando os primeiros passos no mundo da **automação**, este conteúdo foi feito para ajudar você a:

🚀 Ganhar produtividade  
🧠 Escrever códigos mais robustos  
🔧 Tratar endereços IP e MAC com segurança e elegância  


---

📘 **Dica:** Mantenha a biblioteca sempre atualizada:

```bash
pip install --upgrade netaddr

```
---

📘 **Tutorial 1  - IPAddress**

```python
from netaddr import IPAddress
addr_obj = IPAddress('203.0.113.75')

print(f"Version: {addr_obj.version}")
print(f"ReverseDNS: {addr_obj.reverse_dns}")

# Version: 4
# Reversw DNS: 75.113.0.203.in-addr.arpa.

# Outros exemplos em Tutorial_1_-_IP_Address.py
```

---

📘 **Tutorial 2  - IPNetwork e IPSet**

```python
from netaddr import IPNetwork, IPSet

ips_autorizados = IPSet()
ips_autorizados.add(IPNetwork('10.0.0.0/8'))      # Rede interna
ips_autorizados.add(IPNetwork('172.16.0.0/12'))   # Rede privada
ips_autorizados.add(IPNetwork('192.168.0.0/16'))  # Rede privada

ips_para_testar = ['10.50.100.1', '8.8.8.8', '172.20.1.1', '192.168.100.1']

print(f"IPs autorizados: {len(ips_autorizados)} endereços totais\n")
for ip in ips_para_testar:
    autorizado = ip in ips_autorizados
    status = "✓ Autorizado" if autorizado else "✗ Não autorizado"
    print(f"  {ip}: {status}")

#IPs autorizados: 17891328 endereços totais

#  10.50.100.1: ✓ Autorizado
#  8.8.8.8: ✗ Não autorizado
#  172.20.1.1: ✓ Autorizado
#  192.168.100.1: ✓ Autorizado
```

---

📘 **Tutorial 3  - IPRange e IPGlob**

```python
from netaddr import IPRange

i# Criar um intervalo de IPs
intervalo = IPRange('192.168.1.1', '192.168.1.10')
print(f"Intervalo: {intervalo}")
print(f"Tamanho: {len(intervalo)} IPs")
print()

# Listar os IPs no intervalo
print("IPs no intervalo:")
for ip in intervalo:
    print(f"  - {ip}")

#Intervalo: 192.168.1.1-192.168.1.10
#Tamanho: 10 IPs

#IPs no intervalo:
#  - 192.168.1.1
#  - 192.168.1.2
#  - 192.168.1.3
#  - 192.168.1.4
#  - 192.168.1.5
#  - 192.168.1.6
#  - 192.168.1.7
#  - 192.168.1.8
#  - 192.168.1.9
#  - 192.168.1.10

from netaddr import IPGlob

# Padrão simples com wildcard
glob1 = IPGlob('192.168.1.*')
print(f"Padrão: 192.168.1.*")
print(f"Tamanho: {len(glob1)} IPs")
print("Primeiros 5 IPs:")
for ip in list(glob1)[:5]:
    print(f"  - {ip}")

#Padrão: 192.168.1.*
#Tamanho: 256 IPs
#Primeiros 5 IPs:
#  - 192.168.1.0
#  - 192.168.1.1
#  - 192.168.1.2
#  - 192.168.1.3
#  - 192.168.1.4
```

---

📘 **Tutorial 4  - MAC**

```python
from netaddr import EUI, mac_bare, mac_unix, mac_cisco

mac = EUI('00:11:22:33:44:55')

# Diferentes formatos de saída
print(f"Padrão (IEEE):      {mac}")
print(f"Formato BARE:       {mac.format(mac_bare)}")
print(f"Formato UNIX:       {mac.format(mac_unix)}")
print(f"Formato CISCO:      {mac.format(mac_cisco)}")
print()

print(f"Binária:            {bin(int(mac))}")
print(f"Hexadecimal:        {hex(int(mac))}")
print(f"Inteira:            {int(mac)}")
print()

#Padrão (IEEE):      00-11-22-33-44-55
#Formato BARE:       001122334455
#Formato UNIX:       0:11:22:33:44:55
#Formato CISCO:      0011.2233.4455

#Binária:            0b1000100100010001100110100010001010101
#Hexadecimal:        0x1122334455
#Inteira:            73588229205
```

---

## 📚 Referências

- **Documentação Oficial do netaddr**: https://netaddr.readthedocs.io/en/latest/index.html