<p align = center>
  <a href ="#"><img src="https://i.imgur.com/3Vg0Jfw.png" width="130" /></a>
</p>

# <p align=center>[<img src="https://i.imgur.com/G7LQsqu.png"  height="25" />](https://be-tester.ru/) HomeWork - Lesson 4 (Automation) :fire:<p>

### Description
This Homework includes different Tasks which requires some knowlege and skills of Python.<br>
There are three task sections: __Home__ - one task, __Registration & Login__ - two tasks, __Shop__ - seven tasks.<br>

  
 
  ### Task Sections:
- <details>
  <summary><b>Home</b></summary>
  
  :one: [Adding comment](/01_home_add_comment.py "Open File in New Tab (ctrl + click)")&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[:scroll: description...](#1-home-добавление-комментария "Go to Description of the task")<br>
  </details> 

- <details>
  <summary><b>Registration & Login</b></summary>
  
   :one: [Account registration](/02_registration_login_account_registration.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[:scroll: description...](#2-registration_login-регистрация-аккаунта "Go to Description of the task")<br>
   :two: [Login into account](/03_registration_login_login_into_account.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[:scroll: description...](#3-registration_login-логин-в-систему "Go to Description of the task")
  </details> 

- <details>
  <summary><b>Shop</b></summary>
  
   :one: [Display the product page](/04_shop_display_product_page.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[:scroll: description...](#4-shop-отображение-страницы-товара "Go to Description of the task")<br>
   :two: [Product quantity in category](/05_shop_products_quantity_in_category.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[:scroll: description...](#5-shop-количество-товаров-в-категории "Go to Description of the task")<br>
   :three: [Product sorting](/06_shop_product_sorting.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[:scroll: description...](#6-shop-сортировка-товаров "Go to Description of the task")<br>
   :four: [Display product discount](/07_shop_display_product_discount.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[:scroll: description...](#7-shop-отображение-скидка-товара "Go to Description of the task")<br>
   :five: [Checking price in the cart](/08_shop_check_price_in_the_cart.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[:scroll: description...](#8-shop-проверка-цены-в-корзине "Go to Description of the task")<br>
   :six: [Work with the cart](/09_shop_work_with_cart.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[:scroll: description...](#9-shop-работа-в-корзине "Go to Description of the task")<br>
   :seven: [Buying the book](/10_shop_buy_the_book.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[:scroll: description...](#10-shop-покупка-товара "Go to Description of the task")<br>
  </details> 
<br>

 ### Tasks description:

####  1. <b>Home: добавление комментария</b> 
  
    1. Откройте http://practice.automationtesting.in/
    2. Проскролльте страницу вниз на 600 пикселей
    3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
    4. Нажмите на вкладку "REVIEWS"
    5. Поставьте 5 звёзд
    6. Заполните поле "Review" сообщением: "Nice book!"
    7. Заполните поле "Name"
    8. Заполните "Email"
    9. Нажмите на кнопку "SUBMIT"
 [back](#task-sections "Task Sections")

####  2. <b>Registration_login: регистрация аккаунта</b>

    1. Откройте http://practice.automationtesting.in/
    2. Нажмите на вкладку "My Account Menu"
    3. В разделе "Register", введите email для регистрации
    4. В разделе "Register", введите пароль для регистрации
        • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
        • почту и пароль сохраните, потребуюутся в дальнейшем
    5. Нажмите на кнопку "Register"
 [back](#task-sections "Task Sections") 
 
 ####  3. <b>Registration_login: логин в систему</b> 
  
    1. Откройте http://practice.automationtesting.in/
    2. Нажмите на вкладку "My Account Menu"
    3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
    4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
    5. Нажмите на кнопку "Login"
    6. Добавьте проверку, что на странице есть элемент "Logout"
 [back](#task-sections "Task Sections")

####  4. <b>Shop: отображение страницы товара</b>

    1. Откройте http://practice.automationtesting.in/
    2. Залогиньтесь
    3. Нажмите на вкладку "Shop"
    4. Откройте книгу "HTML 5 Forms"
    5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
 [back](#task-sections "Task Sections") 
  
####  5. <b>Shop: количество товаров в категории</b> 
  
    1. Откройте http://practice.automationtesting.in/
    2. Залогиньтесь
    3. Нажмите на вкладку "Shop"
    4. Откройте категорию "HTML"
    5. Добавьте тест, что отображается три товара
 [back](#task-sections "Task Sections")

####  6. <b>Shop: сортировка товаров</b>

    1. Откройте http://practice.automationtesting.in/
    2. Залогиньтесь
    3. Нажмите на вкладку "Shop"
    4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
        • Используйте проверку по value
    5. Отсортируйте товары по цене от большей к меньшей
        • в селекторах используйте класс Select
    6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
    7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
        • Используйте проверку по value
 [back](#task-sections "Task Sections") 
  
####  7. <b>Shop: отображение, скидка товара</b> 
  
    1. Откройте http://practice.automationtesting.in/
    2. Залогиньтесь
    3. Нажмите на вкладку "Shop"
    4. Откройте книгу "Android Quick Start Guide"
    5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
    6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
    7. Добавьте явное ожидание и нажмите на обложку книги
        • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
    8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
 [back](#task-sections "Task Sections")

####  8. <b>Shop: проверка цены в корзине</b>

    1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
    2. Нажмите на вкладку "Shop"
    3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
    4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
        • Используйте для проверки assert
    5. Перейдите в корзину
    6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
    7. Используя явное ожидание, проверьте что в Total отобразилась стоимость

    # если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии
    # если все книги будут out of stock - тогда пропустите это и следующие два задания
 [back](#task-sections "Task Sections") 
  
####  9. <b>Shop: работа в корзине</b> 
  
    Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()

    1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
    2. Нажмите на вкладку "Shop"
    3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
        • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
        • После добавления 1-й книги добавьте sleep
    4. Перейдите в корзину
    5. Удалите первую книгу
        • Перед удалением добавьте sleep
    6. Нажмите на Undo (отмена удаления)
    7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
        • Предварительно очистите поле с помощью локатор_поля.clear()
    8. Нажмите на кнопку "UPDATE BASKET"
    9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
    10. Нажмите на кнопку "APPLY COUPON"
        • Перед нажатимем добавьте sleep
    11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."

    # если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии
 [back](#task-sections "Task Sections")

####  10. <b>Shop: покупка товара</b>

    1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
    2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
    3. Добавьте в корзину книгу "HTML5 WebApp Development"
    4. Перейдите в корзину
    5. Нажмите "PROCEED TO CHECKOUT"
        • Перед нажатием, добавьте явное ожидание
    6. Заполните все обязательные поля
        • Перед заполнением first name, добавьте явное ожидание
        • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
        • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
    7. Выберите способ оплаты "Check Payments"
        • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
    8. Нажмите PLACE ORDER
    9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
    10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
 [back](#task-sections "Task Sections") 
  
    
 <details><summary>:zap: GitHub Stats</summary>
    <img align="left" alt="MirMX's GitHub Stats" src="https://github-readme-stats.vercel.app/api?username=MirMX&exclude_repo=MirMX.github.io&show_icons=true&hide_border=false&title_color=ff652f&icon_color=FFE400&bg_color=09131B&text_color=ffffff&border_color=0c1a25" />
    </details>
  
<div class="footer">
 <b> © 2022 MirMX · All rights reserved</b>
</div>