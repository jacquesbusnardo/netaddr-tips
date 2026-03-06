<!-- -->
<div align="center">

# 🌐 Dicas Práticas e Exemplos com netaddr

**Uma guia prático para dominar a manipulação de endereços IP, IPv6 e MAC em Python**

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![netaddr](https://img.shields.io/badge/netaddr-beyond%200.7.18-brightgreen.svg)](https://pypi.org/project/netaddr/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

</div>

---

## 📋 Índice

- [Sobre este Repositório](#-sobre-este-repositório)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Tutoriais](#-tutoriais)
- [Exemplos Rápidos](#-exemplos-rápidos)
- [Referências](#-referências)

---

## 📦 Sobre este Repositório

A biblioteca **netaddr** é uma ferramenta essencial para quem trabalha com **automação de redes** e **infraestrutura em nuvem**. Este repositório contém:

✅ **Exemplos práticos** de manipulação de endereços IP (IPv4 e IPv6)  
✅ **Dicas de validação** e tratamento de endereços  
✅ **Operações com redes** (sumarização, subdivisão, verificações)  
✅ **Trabalho com endereços MAC** em vários formatos  
✅ **Zona reversa DNS** para configurações de rede  

**Ideal para:**
- 🚀 Automação de redes e infraestrutura
- 🔧 Desenvolvimento de ferramentas de rede  
- 📊 Análise e processamento de dados de IP
- 🛡️ Validação e segurança de endereços

---

## ⚙️ Instalação e Configuração

### Instalar a biblioteca

```bash
pip install netaddr
```

### Manter atualizado

```bash
pip install --upgrade netaddr
```

### Verificar instalação

```bash
python -c "from netaddr import IPAddress; print('✓ netaddr instalado com sucesso!')"
```

---

## 📚 Tutoriais

### 1️⃣ **Tutorial 1 - IPAddress**  
Validação, inspecção e manipulação de endereços IP individuais

**Arquivo:** `Tutorial_1_-_IP_Address.py`

```python
from netaddr import IPAddress

# Criar um endereço IP
addr_obj = IPAddress('203.0.113.75')

# Inspecionar propriedades
print(f"Versão: {addr_obj.version}")                    # 4
print(f"Reverse DNS: {addr_obj.reverse_dns}")          # 75.113.0.203.in-addr.arpa
print(f"Tipo: {'IPv4' if addr_obj.version == 4 else 'IPv6'}")
```

**O que aprenderás:**
- Criar objetos `IPAddress`
- Validar endereços IPv4 e IPv6
- Acessar propriedades (versão, DNS reverso, representação binária)
- Tratar erros de formato inválido

---

### 2️⃣ **Tutorial 2 - IPNetwork e IPSet**  
Trabalhar com redes e conjuntos de endereços

**Arquivo:** `Tutorial_2_-_IPNetwork_e_IPSet.py`

```python
from netaddr import IPNetwork, IPSet

# Criar uma rede
rede = IPNetwork('192.168.1.0/24')
print(f"Rede: {rede}")
print(f"Tamanho: {rede.size} endereços")
print(f"Broadcast: {rede.broadcast}")

# Criar um conjunto de IPs autorizados
ips_autorizados = IPSet()
ips_autorizados.add(IPNetwork('10.0.0.0/8'))
ips_autorizados.add(IPNetwork('192.168.0.0/16'))

# Verificar autorização
print(f"10.50.100.1 autorizado? {'10.50.100.1' in ips_autorizados}")
```

**O que aprenderás:**
- Criar e manipular redes com `IPNetwork`
- Iterar sobre hosts de uma rede
- Dividir redes em sub-redes (subnetting)
- Usar `IPSet` para verificações rápidas de pertença

---

### 3️⃣ **Tutorial 3 - IPRange e IPGlob**  
Trabalhar com intervalos e padrões de endereços

**Arquivo:** `Tutorial_3_-_IPRange_e_IPGlob.py`

```python
from netaddr import IPRange, IPGlob

# Intervalo de IPs
intervalo = IPRange('192.168.1.1', '192.168.1.10')
print(f"Intervalo: {intervalo}")
print(f"Tamanho: {len(intervalo)} IPs")

# Padrão glob (wildcard)
glob = IPGlob('192.168.1.*')
print(f"IPs no padrão: {len(glob)}")
```

**O que aprenderás:**
- Criar intervalos de IPs com `IPRange`
- Usar padrões glob com wildcards
- Trabalhar com IPv4 e IPv6 em intervalos

---

### 4️⃣ **Tutorial 4 - MAC (EUI)**  
Trabalhar com endereços MAC em diferentes formatos

**Arquivo:** `Tutorial_4_-_MAC.py`

```python
from netaddr import EUI, mac_bare, mac_unix, mac_cisco

# Criar endereço MAC
mac = EUI('00:11:22:33:44:55')

# Diferentes formatos de saída
print(f"Padrão (IEEE):      {mac}")
print(f"Formato BARE:       {mac.format(mac_bare)}")
print(f"Formato UNIX:       {mac.format(mac_unix)}")
print(f"Formato CISCO:      {mac.format(mac_cisco)}")

# Representações numéricas
print(f"Hexadecimal:        {hex(int(mac))}")
print(f"Inteira:            {int(mac)}")
```

**O que aprenderás:**
- Validar endereços MAC
- Converter entre múltiplos formatos (IEEE, UNIX, CISCO, BARE)
- Trabalhar com representações binárias e hexadecimais

---

### 5️⃣ **Tutorial 5 - Zona Reversa DNS**  
Criar e gerir zonas de DNS reverso para redes

**Arquivo:** `Tutorial_5_-_Zona_Reversa.py`

```python
from netaddr import IPNetwork, IPAddress

# Definir uma rede
rede = IPNetwork('192.0.2.0/24')

# Obter zona reversa
zona_reversa = rede[0].reverse_dns
print(f"Zona Reversa: {zona_reversa}")
# Output: 2.0.192.in-addr.arpa

# Reverse DNS de IPs individuais
ip = IPAddress('192.0.2.45')
print(f"Reverso de {ip}: {ip.reverse_dns}")
```

**O que aprenderás:**
- Gerar zonas de DNS reverso
- Trabalhar com in-addr.arpa (IPv4) e ip6.arpa (IPv6)
- Criar registos DNS reversos

---

## 💡 Exemplos Rápidos

### ✨ Validar um IP

```python
from netaddr import IPAddress, AddrFormatError

try:
    ip = IPAddress('192.168.1.1')
    print(f"✓ {ip} é válido")
except AddrFormatError:
    print("✗ Endereço inválido")
```

### ✨ Verificar se um IP está numa rede

```python
from netaddr import IPNetwork

rede = IPNetwork('10.0.0.0/8')
print('10.50.100.1' in rede)  # True
print('172.16.0.1' in rede)   # False
```

### ✨ Listar todos os hosts de uma rede

```python
from netaddr import IPNetwork

rede = IPNetwork('192.168.1.0/28')
for ip in rede:
    print(ip)
```

### ✨ Dividir uma rede em sub-redes

```python
from netaddr import IPNetwork

rede = IPNetwork('192.168.0.0/24')
for subrede in rede.subnet(26):
    print(f"{subrede} - {subrede.size} hosts")
```

### ✨ Converter formatos de MAC

```python
from netaddr import EUI, mac_cisco

mac = EUI('00:11:22:33:44:55')
print(mac.format(mac_cisco))  # 0011.2233.4455
```

---

## 📚 Referências

- **[Documentação Oficial do netaddr](https://netaddr.readthedocs.io/)**
- **[Código-fonte no GitHub](https://github.com/netaddr/netaddr)**
- **[PyPI - netaddr](https://pypi.org/project/netaddr/)**

---

## 📝 Licença

Este repositório está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

<div align="center">

**Made with ❤️ para a comunidade de automação de redes**

</div>