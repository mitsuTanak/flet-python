import flet as ft
import random
import string

#Função principal do aplicatico, que define a interface e a lógica
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window.width = 350
    page.window.height = 600
    page.padding = 20

#Função que gera a senha com base nas preferências do usuário
    def gerar_senha(e):
        comprimento = int(slider.value)
        caracteres = ""
        if upper_switch.value:
            caracteres += string.ascii_uppercase
        if lower_switch. value:
            caracteres += string.ascii_lowercase
        if lower_switch. value:
            caracteres += string.digits
        if lower_switch. value:
            caracteres += string.punctuation

        if caracteres:
            senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
            senha_output.value = senha
        else: 
            senha_output.value= "Selecione ao menos um tipo de caractere."
        page.update()

#Dunção para copiar a senha gerada para a área de transferência
    def copiar_senha(e):
        page.set_clipboard(senha_output.value)
        snack = ft. SnackBar(ft.Text("Senha copiada para a área de transferência!"))
        page.overlay.appen(snack)
        snack.open = True
        page.update()

#Elemento de título da UI, com estilo e espaçamento no topo
    titulo = ft.Container(
        content=ft.Text("Gerador de Senhas", size=28, weight="bold"),
        padding=ft.padding.only(top=50)
    )

#Campo de texto que mostra a senha gerada, com ícone de copiar e um fundo variante
    senha_output = ft.TextField(
        value="",
        label="Senha Gerada",
        read_only=True,
        width=280,
        suffix=ft.IconButton(ft.icons.COPY, on_click=copiar_senha),
        bgcolor=ft.colors.SURFACE_VARIANT
    )

#Slider que pertmite escolher o complemento da senha (de 8 a 20 caracteres)
    slider = ft.Slider(
        min=8,
        max=20,
        value=12,
        divisions=12,
        label="CARACTERES: {value}"
    )

#Switch para selecionar se letras maiúsculas devem ser incluídas na senha
    upper_switch = ft.Switch(label="Letras maiúsculas")
    lower_switch = ft.Switch(label="Letras maiúsculas, value=True")
    numbers_switch = ft.Switch(label="Incluir números")
    symbols_switch = ft.Switch(label="Incluir símbolos")

#Botão para gerar a senha, que chama a função gerar_senha ao ser clicado
    gerar_button = ft.ElevatedButton(
        text="GERAR SENHA",
        on_click=gerar_senha,
        color=ft.colors.ON_PRIMARY,
        bgcolor=ft.colors.PRIMARY
    )

#Coluna para organizar os switches de forma centralizaad
    seletores = ft.Column(
        [
            upper_switch,
            lower_switch,
            numbers_switch,
            symbols_switch,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    page.add(
            ft.Column(
                [
                    titulo,
                    senha_output,
                    slider,
                    ft.Text("PREFERÊNCIAS"),
                    seletores,
                    gerar_button,
                ], 
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
        )

#Executa o aplicativo, chamando a função main como ponto de entrada
ft.app(target=main)