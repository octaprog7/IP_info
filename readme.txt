https://stackoverflow.com/questions/33035709/can-i-get-a-phone-number-by-user-id-via-telegram-bot-api

No, unfortunately Telegram Bot API doesn't return phone number.
You should either use Telegram API methods instead or ask it explicitly from the user.
You cannot get "friends" of a user as well.

You will definitely retrieve the following information:
    userid
    first_name
    content (whatever it is: text, photo, etc.)
    date(unixtime)
    chat_id

If user configured it, you will also get last_name and username.

Locations and Numbers:  https://core.telegram.org/bots/2-0-intro#locations-and-numbers

Некоторым ботам для правильной работы требуются дополнительные данные от пользователя. Например, знание местоположения
пользователя помогает получить более релевантные результаты с географической привязкой. Номер телефона пользователя
может быть очень полезен для интеграции с другими сервисами, такими как банки и т. Д.

Мы добавили для ботов простой способ спрашивать пользователя об их местонахождении и номере телефона с помощью
специальных кнопок. Обратите внимание, что кнопки и номера телефона, и кнопки запроса местоположения будут работать
только в приватных чатах.

При нажатии этих кнопок клиенты Telegram будут отображать подтверждающее уведомление, которое сообщает пользователю,
что должно произойти.

Руководство: кнопки с цифрами и расположением »

Встроенные боты также могут запрашивать данные о местоположении у своих пользователей. Используйте
команду /setinlinegeo с @BotFather, чтобы включить это. Ваш бот будет запрашивать у пользователя разрешение на
доступ к их местоположению всякий раз, когда он отправляет встроенный запрос.

Sample bot: @foursquare - этот бот запросит разрешение на доступ к местоположению пользователя,
            а затем предоставит результаты с геотаргетингом.

Смотри: https://core.telegram.org/bots/api#keyboardbutton

            request_contact	Boolean	Optional.
            request_location	Boolean

