import logging
import re

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(_name_)

# Expresión regular para detectar mensajes que contienen palabras clave relacionadas con la comida
expresion_comida = re.compile(r"menu|comida|plato", re.IGNORECASE)

# Menú de comidas disponibles con sus ingredientes
menu_comidas = {
    "tacos": ["tortillas de maíz", "carne asada", "cebolla", "cilantro", "salsa verde", "limón"],
    "enchiladas": ["tortillas de maíz", "pollo deshebrado", "queso fresco", "salsa roja", "crema", "cebolla"],
    "guacamole": ["aguacate", "tomate", "cebolla", "cilantro", "limón", "sal", "chile serrano"],
    "tamales": ["masa de maíz", "relleno de carne de cerdo o pollo", "hoja de maíz"],
    "chiles en nogada": ["chiles poblanos", "relleno de picadillo", "nuez", "perejil", "granada"],
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    menu_text = "\n".join([f"\u200b\u200b- Nombre: {comida}" for comida, ingredientes in menu_comidas.items()])
    await update.message.reply_html(
        rf"Bienvenid@ {user.mention_html()}! ¿Qué te gustaría comer hoy?. Aquí tienes nuestro menú: {menu_text}",
        reply_markup=ForceReply(selective=True),
    )




async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Puedes pedirme el menú de comidas disponibles.")


async def buscar_comida(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Buscar la comida solicitada por el usuario y enviar los ingredientes si está en el menú."""
    message_text = update.message.text
    comida_encontrada = None

    # Buscar la comida solicitada por el usuario en el mensaje utilizando expresiones regulares
    for comida in menu_comidas:
        if re.search(rf"\b{comida}\b", message_text):
            comida_encontrada = comida
            break

    if comida_encontrada:
        ingredientes = ", ".join(menu_comidas[comida_encontrada])
        await update.message.reply_text(f"Los ingredientes de {comida_encontrada} son: {ingredientes}")
    else:
        await update.message.reply_text("Lo siento, no tengo información sobre esa comida.")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token("7093118754:AAFxr2DjKfeYqFIEnGWSWULavJ8rP4_hzsM").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buscar_comida))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if _name_ == "_main_":
    main()