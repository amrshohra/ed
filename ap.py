import flet as ft
import webbrowser

WHATSAPP_NUMBER = "01001954254"
MSG = "لعرض وتوصيل إعلانك أبعت إعلانك على رقم الواتس"

def main(page: ft.Page):
    page.title = "الشهرة"
    page.bgcolor = ft.colors.BLACK
    page.window_width = 400
    page.window_height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    text = ft.Text(f"{MSG}\n{WHATSAPP_NUMBER}",
                   size=20,
                   color=ft.colors.WHITE,
                   text_align=ft.TextAlign.CENTER)

    def copy_and_open(e):
        page.set_clipboard(WHATSAPP_NUMBER)
        # افتح دردشة واتساب (يعمل على الويب/الهاتف إذا مسموح)
        webbrowser.open(f"https://wa.me/20{WHATSAPP_NUMBER}" if not WHATSAPP_NUMBER.startswith("+") else f"https://wa.me/{WHATSAPP_NUMBER}")

    btn = ft.ElevatedButton("أرسل عبر واتساب", on_click=copy_and_open)

    page.add(ft.Column(controls=[text, ft.Container(height=20)], alignment=ft.MainAxisAlignment.CENTER))
    page.add(btn)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
