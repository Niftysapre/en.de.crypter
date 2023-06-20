import pyAesCrypt

choice = input("Выберите операцию (1.зашифровать/2.расшифровать) и введите цифру: ")

if choice.lower() == "1":
    password = input('Введите пароль для файла: ')
    pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)
    print("Файл успешно зашифрован.")
elif choice.lower() == "2":
    password = input('Введите пароль для расшифровки файла: ')
    pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)
    print("Файл успешно расшифрован.")
else:
    print("Некорректный выбор операции. Пожалуйста, выберите 'зашифровать' или 'расшифровать'.")