import PySimpleGUI as sg

# Define o layout da janela
layout = [[sg.Text("Digite os números:")],
          [sg.InputText(size=(10, 1), key="-NUM1-"), sg.InputText(size=(10, 1), key="-NUM2-")],
          [sg.Text("Selecione a operação:"), sg.Combo(["+", "-", "*", "/"], key="-OP-")],
          [sg.Button("Calcular"), sg.Button("Sair")],
          [sg.Text("Resultado: "), sg.Text(size=(10,1), key="-OUTPUT-")]]

# Cria a janela a partir do layout
window = sg.Window("Calculadora", layout)

# Loop principal da janela
while True:
    event, values = window.read()

    # Encerra o programa se a janela for fechada
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break

    # Calcula o resultado da operação
    num1 = float(values["-NUM1-"])
    num2 = float(values["-NUM2-"])
    op = values["-OP-"]

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2

    # Atualiza a saída de texto na janela com o resultado
    window["-OUTPUT-"].update(result)

# Fecha a janela
window.close()