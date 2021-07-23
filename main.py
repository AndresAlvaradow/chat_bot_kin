from os import name
from telegram.ext import *
import logging
import connection_dbpedia as dbpedia
import OWLconexion as owl




# Set up the logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

# Message error


def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')

# MENUS



def second_submenu_1(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="Listo te avisare cuando esté listo")

# COMMANDS


def help_command(update, context):
    update.message.reply_text(

        "\n\nYo soy Kin, tu asistente te apoyare en todo tu pedido"
        "\n\nPara interartuar utliza el comando /start")



def ingredients_command(update, context):
    user_says = " ".join(context.args)
    # update.message.reply_text("You said: " + user_says)
    update.message.reply_text(
        "Los ingredientes de  " + user_says + " son:\n\n"+dbpedia.get_response_dbpedia_ingredients(user_says.capitalize()))





def start_command(update, context):
    update.message.reply_text(
        'Hola, yo soy Kin :\n\n te ayudara con tu Pedido')
    update.message.reply_text(
        "Puedes usar los siguientes comandos :\n"
        #"\n/formenu -> realiza tu pedido mediante un menu (recomendado)"
        #"\n/help -> muestra mas información de mí Kin"
        "\n/listPizzaDb -> muestra el listado de pizzas de DBpedia"
        "\n/PizzaOWL -> muestra el listado de pizzas de OWL Pizza")
        #"\n/pizza -> muestra las pizzas que puedes buscar"
       # "\n/ingredients \"nombre de la pizza\" -> permite buscar los ingredientes de la pizza (utiliza el commando /pizza para ver que pizzas puedes buscar)")


def types_command_dbpedia(update, context):
    qres = dbpedia.get_response_dbpedia_pizzas()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name, ing,  image_url = result['name']['value'], result['res']['value'], result['image']['value']
        update.message.reply_text('Nombre de la pizza : ' + name + "\n Ingredientes: " + ing +
                                 "\n" + image_url)


def types_command_owl(update, context):
    qres = owl.get_response_pizzas()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        qres2 = owl.get_response_ingredients(name)
        update.message.reply_text('Nombre de la pizza : ' + name)
        update.message.reply_text('ingredientes : ')
        for j in range(len(qres2['results']['bindings'])):
            result2 = qres2['results']['bindings'][j]
            name2 = result2['name']['value']
            update.message.reply_text(name2)


if __name__ == '__main__':
    updater = Updater(token="", use_context=True)

    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    #dp.add_handler(CommandHandler('formenu', menu_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('listPizzaDb', types_command_dbpedia))
    dp.add_handler(CommandHandler('PizzaOWL', types_command_owl))
    #dp.add_handler(CommandHandler('pizza', pizza_command))
    dp.add_handler(CommandHandler(
        'ingredients', ingredients_command, pass_args=True))


    # Messages
    #dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
