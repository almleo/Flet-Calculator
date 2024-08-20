
import flet as ft

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text
       

class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text,  button_clicked, expand)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text,  button_clicked, expand)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

class Calculator(ft.Container):
    def __init__(self):
        super().__init__()
        self.visor = ft.Text(value = "0", color=ft.colors.WHITE, size=20)

        self.reset()

        self.linha_0 = ft.Row(controls=[self.visor], alignment="end")
        
        self.linha_1 = ft.Row(
        # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[ExtraActionButton("AC",button_clicked=self.button_clicked), ExtraActionButton("+/-",button_clicked=self.button_clicked),ExtraActionButton("%",button_clicked=self.button_clicked), ActionButton("/",button_clicked=self.button_clicked)]
        )
        self.linha_2 = ft.Row(
            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[DigitButton("7",button_clicked=self.button_clicked), DigitButton("8",button_clicked=self.button_clicked), DigitButton("9",button_clicked=self.button_clicked), ActionButton("*",button_clicked=self.button_clicked)]
        )
        self.linha_3 = ft.Row(
            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[DigitButton("4",button_clicked=self.button_clicked), DigitButton("5",button_clicked=self.button_clicked), DigitButton("6",button_clicked=self.button_clicked), ActionButton("-",button_clicked=self.button_clicked)]
        )   
        self.linha_4 = ft.Row(
            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[DigitButton("1",button_clicked=self.button_clicked), DigitButton("2",button_clicked=self.button_clicked), DigitButton("3",button_clicked=self.button_clicked), ActionButton("+",button_clicked=self.button_clicked)]
        ) 
        self.linha_5 = ft.Row(
            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[DigitButton("0",button_clicked=self.button_clicked,expand=2), DigitButton(".",button_clicked=self.button_clicked), ActionButton("=",button_clicked=self.button_clicked)]
        )
        self.width=350
        self.bgcolor=ft.colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.content = ft.Column( controls = [self.linha_0, self.linha_1, self.linha_2, self.linha_3, self.linha_4, self.linha_5])

    def button_clicked(self, event):
        data = event.control.data
        if data == 'AC':
            self.visor.value = '0'
            self.number1 = 0
            self.number2 = 0
            self.repeat = False
        elif data in ('0','1','2','3','4','5','6','7','8','9','.'):
            if self.visor.value == "0" or self.new_number:
                self.visor.value = data 
                self.new_number = False
            else:
                self.visor.value = self.visor.value + data 
        elif data in ("+", "-", "*", "/"):
            self.operation = data
            if self.number1 != 0 and self.repeat == False:
                self.number1 = self.do_calc(self.number1, float(self.visor.value), self.operation)
                self.visor.value = self.number1
            else:
                self.number1 = float(self.visor.value)
            self.new_number = True
            self.repeat = False
        elif data in ("%"):
            if self.number1 == 0:
                self.visor.value = "0"
            else:
                self.visor.value = self.number_format(self.number1 * (float(self.visor.value)/100))


        elif data in ("="):
            if self.repeat == True:
                self.number1 = float(self.visor.value)
                result = self.do_calc(self.number1, self.number2, self.operation)
                self.visor.value = result

            else:
                self.number2 = float(self.visor.value)
                result = self.do_calc(self.number1, self.number2, self.operation)
                self.visor.value = result
                self.new_number = True
                self.repeat = True
                

        self.update()

    def number_format(self, n):
        if n % 1 == 0:
            return int(n)
        else:
            return float(n)

    def do_calc(self, n1, n2, op):
        if op == "+":
            return self.number_format(n1 + n2)
        elif op == "-":
            return self.number_format(n1 - n2)
        elif op == "*":
            return self.number_format(n1 * n2)
        elif op == "/":
            return self.number_format(n1 / n2)

    def reset(self):
        self.number1 = 0
        self.number2 = 0
        self.new_number = True
        self.repeat = False
        self.operation = ''

def main(page:ft.Page):
    page.Title="Calculator"
    
    calculator = Calculator()
    page.add(calculator)
    

ft.app(main)