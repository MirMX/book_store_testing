<p align = "center">
  <a href ="#"><img src="https://i.imgur.com/3Vg0Jfw.png" width="130" /></a>
</p>

# <p align="center">[<img src="https://i.imgur.com/G7LQsqu.png"  height="25" />](https://be-tester.ru/ "https://be-tester.ru") HomeWork - Lesson 4 (Automation) :fire:</p>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python%20&%20Magic-blue.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/Total%20code--coverage-100%25-green)](#)

### Description
The Homework includes different Exercises which requires some knowlege and skills of Python.<br>
There are three task sections: __Home__ - one task, __Registration & Login__ - two tasks, __Shop__ - seven tasks.<br><br>
These assignments were designed to improve a Test Automation mastery.<br>
 
  ### Task Sections and Specifications:
- <details>
  <summary><b>Home</b></summary>

    - <details>
      <summary>1. <b>Home:</b> добавление комментария</summary> 

        1️⃣ [Adding comment][1]&nbsp;&nbsp;&nbsp;&nbsp; [![Generic badge](https://img.shields.io/badge/code--coverage-100%25-green)](#)<br>

            1. Откройте http://practice.automationtesting.in/
            2. Проскролльте страницу вниз на 600 пикселей
            3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
            4. Нажмите на вкладку "REVIEWS"
            5. Поставьте 5 звёзд
            6. Заполните поле "Review" сообщением: "Nice book!"
            7. Заполните поле "Name"
            8. Заполните "Email"
            9. Нажмите на кнопку "SUBMIT"
      </details>
  </details> 

- <details>
  <summary><b>Registration & Login</b></summary>
  
    - <details>
      <summary>1. <b>Registration_login:</b> регистрация аккаунта</summary>

        2️⃣ [Account registration][2]&nbsp;&nbsp;&nbsp;&nbsp; [![Generic badge](https://img.shields.io/badge/code--coverage-100%25-green)](#)<br>

            1. Откройте http://practice.automationtesting.in/
            2. Нажмите на вкладку "My Account Menu"
            3. В разделе "Register", введите email для регистрации
            4. В разделе "Register", введите пароль для регистрации
                - составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
                - почту и пароль сохраните, потребуюутся в дальнейшем
            5. Нажмите на кнопку "Register"
      </details>

    - <details>
      <summary>2. <b>Registration_login:</b> логин в систему</summary> 

        3️⃣ [Login into account][3]&nbsp;&nbsp;&nbsp;&nbsp; [![Generic badge](https://img.shields.io/badge/code--coverage-100%25-green)](#)

            1. Откройте http://practice.automationtesting.in/
            2. Нажмите на вкладку "My Account Menu"
            3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
            4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
            5. Нажмите на кнопку "Login"
            6. Добавьте проверку, что на странице есть элемент "Logout"
      </details>
  </details> 

- <details>
  <summary><b>Shop</b></summary>
  
    - <details>
      <summary>1. <b>Shop:</b> отображение страницы товара</summary>
        
        4️⃣ [Display the product page][4]&nbsp;&nbsp;&nbsp;&nbsp; [![Generic badge](https://img.shields.io/badge/code--coverage-100%25-green)](#)<br>

            1. Откройте http://practice.automationtesting.in/
            2. Залогиньтесь
            3. Нажмите на вкладку "Shop"
            4. Откройте книгу "HTML 5 Forms"
            5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
      </details>
    - <details>  
      <summary>2. <b>Shop:</b> количество товаров в категории</summary> 

        5️⃣ [Product quantity in category][5]&nbsp;&nbsp;&nbsp;&nbsp; [![Generic badge](https://img.shields.io/badge/code--coverage-100%25-green)](#)<br>
        
            1. Откройте http://practice.automationtesting.in/
            2. Залогиньтесь
            3. Нажмите на вкладку "Shop"
            4. Откройте категорию "HTML"
            5. Добавьте тест, что отображается три товара
      </details>
    - <details>
      <summary>3. <b>Shop:</b> сортировка товаров</summary>

        6️⃣ [Product sorting][6]&nbsp;&nbsp;&nbsp;&nbsp; [![Generic badge](https://img.shields.io/badge/code--coverage-100%25-green)](#)<br>

            1. Откройте http://practice.automationtesting.in/
            2. Залогиньтесь
            3. Нажмите на вкладку "Shop"
            4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
                - Используйте проверку по value
            5. Отсортируйте товары по цене от большей к меньшей
                - в селекторах используйте класс Select
            6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
            7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
                - Используйте проверку по value
      </details>
    - <details>  
      <summary>4. <b>Shop:</b> отображение, скидка товара</summary> 

        7️⃣ [Display product discount][7]&nbsp;&nbsp;&nbsp;&nbsp; [![Generic badge](https://img.shields.io/badge/code--coverage-100%25-green)](#)<br>

            1. Откройте http://practice.automationtesting.in/
            2. Залогиньтесь
            3. Нажмите на вкладку "Shop"
            4. Откройте книгу "Android Quick Start Guide"
            5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
            6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
            7. Добавьте явное ожидание и нажмите на обложку книги
                - Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
            8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
      </details>

    - <details>
      <summary>5. <b>Shop:</b> проверка цены в корзине</summary>

        8️⃣ [Checking price in the cart][8]&nbsp;&nbsp;&nbsp;&nbsp; [![Generic badge](https://img.shields.io/badge/code--coverage-100%25-green)](#)<br>

            1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
            2. Нажмите на вкладку "Shop"
            3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
            4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
                - Используйте для проверки assert
            5. Перейдите в корзину
            6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
            7. Используя явное ожидание, проверьте что в Total отобразилась стоимость

            # если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии 
            # если все книги будут out of stock - тогда пропустите это и следующие два задания
      </details>
    - <details>  
      <summary>6. <b>Shop:</b> работа в корзине</summary> 

        9️⃣ [Work with the cart][9]&nbsp;&nbsp;&nbsp;&nbsp; [![Generic badge](https://img.shields.io/badge/code--coverage-100%25-green)](#)<br>

        Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()

            1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
            2. Нажмите на вкладку "Shop"
            3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
                - Перед добавлением первой книги, проскролльте вниз на 300 пикселей
                - После добавления 1-й книги добавьте sleep
            4. Перейдите в корзину
            5. Удалите первую книгу
                - Перед удалением добавьте sleep
            6. Нажмите на Undo (отмена удаления)
            7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
                - Предварительно очистите поле с помощью локатор_поля.clear()
            8. Нажмите на кнопку "UPDATE BASKET"
            9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
            10. Нажмите на кнопку "APPLY COUPON"
                - Перед нажатимем добавьте sleep
            11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."

            # если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии
      </details>
    - <details>
      <summary>7. <b>Shop:</b> покупка товара</summary>

        🔟 [Buying the book][10]&nbsp;&nbsp;&nbsp;&nbsp; [![Generic badge](https://img.shields.io/badge/code--coverage-100%25-green)](#)<br>

            1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
            2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
            3. Добавьте в корзину книгу "HTML5 WebApp Development"
            4. Перейдите в корзину
            5. Нажмите "PROCEED TO CHECKOUT"
                - Перед нажатием, добавьте явное ожидание
            6. Заполните все обязательные поля
                - Перед заполнением first name, добавьте явное ожидание
                - Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
                - Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
            7. Выберите способ оплаты "Check Payments"
                - Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
            8. Нажмите PLACE ORDER
            9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
            10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
      </details>
  </details> 
<!-- ----------------------------------------------------------------------- -->
[1]: /01_home_add_comment.py "Open File in New Tab (ctrl + click)"
[2]: /02_registration_login_account_registration.py "Open File in New Tab (ctrl + click)"
[3]: /03_registration_login_login_into_account.py "Open File in New Tab (ctrl + click)"
[4]: /04_shop_display_product_page.py "Open File in New Tab (ctrl + click)"
[5]: /05_shop_products_quantity_in_category.py "Open File in New Tab (ctrl + click)"
[6]: /06_shop_product_sorting.py "Open File in New Tab (ctrl + click)"
[7]: /07_shop_display_product_discount.py "Open File in New Tab (ctrl + click)"
[8]: /08_shop_check_price_in_the_cart.py "Open File in New Tab (ctrl + click)"
[9]: /09_shop_work_with_cart.py "Open File in New Tab (ctrl + click)"
[10]: /10_shop_buy_the_book.py "Open File in New Tab (ctrl + click)"
<!-- ----------------------------------------------------------------------- -->
---
### **Framework**
- <details>
  <summary><b>Page Object Model</b></summary>

    [<img src="https://i.imgur.com/nbaqwhv.png" />][11]
  </details>
- <details>
  <summary><b>How to Use</b></summary>

    - <details>
      <summary><b>Soft Requirements:</b></summary>

        - Python 3.8.5 
        - Pytest 7.0.1 (to install use `pip install pytest` in terminal)
        - Allure 2.17.3 (to install use `pip install allure-pytest` in terminal)

      </details>
    - <details>
      <summary><b>to Run Tests:</b></summary>

        
        Framework ([framework][12]) <br>
        execute code with command below in PowerShell
        ```PowerShell
        pytest -vs --alluredir=%allure_result_folder% ./Tests/<test_name.py>
        ```
        the key `-v` is to show more detailed report<br>
        the key `-s` is to see print in terminal<br>

        to generate allure report
        ```
        allure serve %allure_result_folder%
        ```
      </details>

        - <details>
          <summary><b>to chose which test to run:</b></summary>

            Uncomment `@pytest.mark.skip` to skip test(s)<br>
            [<img src="https://i.imgur.com/CeICYVo.gif" />][13]
          </details>
    - <details>
      <summary><b>Results:</b></summary>

        There are 16 tests and each of them has his own result bases on Task Requirements:<br>
        [<img src="https://i.imgur.com/yVorhBC.png" />][14]
        [<img src="https://i.imgur.com/0jxpx3N.png" />][15]
        [<img src="https://i.imgur.com/MQkLh3p.png" />][16]
        Allure Report:<br>
        [<img src="https://i.imgur.com/SbK3oJd.png" />][17]
      </details>
  </details> 

<!-- ----------------------------------------------------------------------- -->
[11]: https://i.imgur.com/nbaqwhv.png "Open File in New Tab (ctrl + click)"
[12]: /framework "Open File in New Tab (ctrl + click)"
[13]: https://i.imgur.com/CeICYVo.gif "Open File in New Tab (ctrl + click)"
[14]: https://i.imgur.com/yVorhBC.png "Open File in New Tab (ctrl + click)"
[15]: https://i.imgur.com/0jxpx3N.png "Open File in New Tab (ctrl + click)"
[16]: https://i.imgur.com/MQkLh3p.png "Open File in New Tab (ctrl + click)"
[17]: https://i.imgur.com/SbK3oJd.png "Open File in New Tab (ctrl + click)"
<!-- ----------------------------------------------------------------------- -->
---
### Contributors

 - **Maxim Mir**

 ---
<details>

<summary><b>:zap: GitHub Stats</b></summary>

  [![MirMX's GitHub stats](https://github-readme-stats.vercel.app/api?username=MirMX&hide=contribs,prs&show_icons=true&&theme=dark&hide_border=false&title_color=007acc&icon_color=79ff97&bg_color=151515&border_color=0c1a25")](#)
  
  [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=MirMX&repo=book_store_testing&theme=dark&&title_color=007acc&show_icons=true&layout=compact)](#)
</details>

---  

###### <p align ="center">[<img align ="center" src="https://i.imgur.com/3Vg0Jfw.png" width="30" />](#)&nbsp;&nbsp; © 2022 MirMX</p>
