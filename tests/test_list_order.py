def register_new_courier_and_return_login_password():
    # (ваш код, который вы уже написали)

    if response.status_code == 201: # если регистрация прошла успешно
        id = response.json()['data']['_id']  # получаем id курьера из ответа
        print("Courier ID:", id)  # выводим id курьера
        login_pass.append(id)  # добавляем id курьера в список
        login_pass.append(login)  # добавляем логин курьера в список
        login_pass.append(password)  # добавляем пароль курьера в список

    return login_pass  # возвращаем список