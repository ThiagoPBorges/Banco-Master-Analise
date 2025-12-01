import pandas as pd
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==============================================================================
# BLOCO 1: Configuração do Robô
# ==============================================================================
# O 'Service' baixa automaticamente a versão correta do motorista do Chrome
servico = Service(ChromeDriverManager().install())

# As 'Options' são as configurações do navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") # Começar tela cheia ajuda a evitar erros de layout

# --- O DISFARCE (Essencial para sites com Cloudflare/Anti-Robô) ---
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Inicia o navegador
navegador = webdriver.Chrome(service=servico, options=options)

# ==============================================================================
# BLOCO 2: SITE RECLAME AQUI E SUA MISSÃO
# ==============================================================================
lista_total = []
base_url = "https://www.reclameaqui.com.br/empresa/banco-master/lista-reclamacoes/"

# 1. Navegar para o alvo
navegador.get(base_url)