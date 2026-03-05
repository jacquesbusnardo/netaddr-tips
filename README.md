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

