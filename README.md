<p align = center>
  <a href ="#"><img src="https://i.imgur.com/3Vg0Jfw.png" width="130" /></a>
</p>

# <p align=center>[<img src="https://i.imgur.com/G7LQsqu.png"  height="25" />](https://be-tester.ru/) HomeWork - Lesson 4 (Automation) :fire:<p>

### Description
This Homework includes different Tasks which requires some knowlege and skills of Python.<br>
There are three task sections: __Home__ - one task, __Registration & Login__ - two tasks, __Shop__ - seven tasks.<br>

  
 
  ### Task Sections and Description:
- <details>
  <summary><b>Home</b></summary>

    - <details>
      <summary><b>1. Home: добавление комментария</b></summary> 

        1️⃣ [Adding comment](/01_home_add_comment.py "Open File in New Tab (ctrl + click)")<br>

        >1. Откройте http://practice.automationtesting.in/
        >2. Проскролльте страницу вниз на 600 пикселей
        >3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
        >4. Нажмите на вкладку "REVIEWS"
        >5. Поставьте 5 звёзд
        >6. Заполните поле "Review" сообщением: "Nice book!"
        >7. Заполните поле "Name"
        >8. Заполните "Email"
        >9. Нажмите на кнопку "SUBMIT"
      </details>
  </details> 

- <details>
  <summary><b>Registration & Login</b></summary>
  
    - <details>
      <summary>2. <b>Registration_login: регистрация аккаунта</b></summary>

        2️⃣ [Account registration](/02_registration_login_account_registration.py)<br>

        >1. Откройте http://practice.automationtesting.in/
        >2. Нажмите на вкладку "My Account Menu"
        >3. В разделе "Register", введите email для регистрации
        >4. В разделе "Register", введите пароль для регистрации
        >    - составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
        >    - почту и пароль сохраните, потребуюутся в дальнейшем
        >5. Нажмите на кнопку "Register"
      </details>

    - <details>
      <summary>3. <b>Registration_login: логин в систему</b></summary> 

        3️⃣ [Login into account](/03_registration_login_login_into_account.py)

        >1. Откройте http://practice.automationtesting.in/
        >2. Нажмите на вкладку "My Account Menu"
        >3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
        >4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
        >5. Нажмите на кнопку "Login"
        >6. Добавьте проверку, что на странице есть элемент "Logout"
      </details>
  </details> 

- <details>
  <summary><b>Shop</b></summary>
  
    - <details>
      <summary>4. <b>Shop: отображение страницы товара</b></summary>
        
        4️⃣ [Display the product page](/04_shop_display_product_page.py)<br>

        >1. Откройте http://practice.automationtesting.in/
        >2. Залогиньтесь
        >3. Нажмите на вкладку "Shop"
        >4. Откройте книгу "HTML 5 Forms"
        >5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
      </details>
    - <details>  
      <summary>5. <b>Shop: количество товаров в категории</b></summary> 

        5️⃣ [Product quantity in category](/05_shop_products_quantity_in_category.py)<br>
        
        >1. Откройте http://practice.automationtesting.in/
        >2. Залогиньтесь
        >3. Нажмите на вкладку "Shop"
        >4. Откройте категорию "HTML"
        >5. Добавьте тест, что отображается три товара
      </details>
    - <details>
      <summary>6. <b>Shop: сортировка товаров</b></summary>

        6️⃣ [Product sorting](/06_shop_product_sorting.py)<br>

        >1. Откройте http://practice.automationtesting.in/
        >2. Залогиньтесь
        >3. Нажмите на вкладку "Shop"
        >4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
        >    - Используйте проверку по value
        >5. Отсортируйте товары по цене от большей к меньшей
        >    - в селекторах используйте класс Select
        >6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
        >7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
        >    - Используйте проверку по value
      </details>
    - <details>  
      <summary>7. <b>Shop: отображение, скидка товара</b></summary> 

        7️⃣ [Display product discount](/07_shop_display_product_discount.py)<br>

        >1. Откройте http://practice.automationtesting.in/
        >2. Залогиньтесь
        >3. Нажмите на вкладку "Shop"
        >4. Откройте книгу "Android Quick Start Guide"
        >5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
        >6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
        >7. Добавьте явное ожидание и нажмите на обложку книги
        >    - Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
        >8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
      </details>

    - <details>
      <summary>8. <b>Shop: проверка цены в корзине</b>></summary>

        8️⃣ [Checking price in the cart](/08_shop_check_price_in_the_cart.py)<br>

        >1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
        >2. Нажмите на вкладку "Shop"
        >3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
        >4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
        >    - Используйте для проверки assert
        >5. Перейдите в корзину
        >6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
        >7. Используя явное ожидание, проверьте что в Total отобразилась стоимость<br><br>

        >* если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии 
        >* если все книги будут out of stock - тогда пропустите это и следующие два задания
      </details>
    - <details>  
      <summary>9. <b>Shop: работа в корзине</b></summary> 

        9️⃣ [Work with the cart](/09_shop_work_with_cart.py)<br>

        Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()

        >1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
        >2. Нажмите на вкладку "Shop"
        >3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
        >    - Перед добавлением первой книги, проскролльте вниз на 300 пикселей
        >    - После добавления 1-й книги добавьте sleep
        >4. Перейдите в корзину
        >5. Удалите первую книгу
        >    - Перед удалением добавьте sleep
        >6. Нажмите на Undo (отмена удаления)
        >7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
        >    - Предварительно очистите поле с помощью локатор_поля.clear()
        >8. Нажмите на кнопку "UPDATE BASKET"
        >9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
        >10. Нажмите на кнопку "APPLY COUPON"
        >    - Перед нажатимем добавьте sleep
        >11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."

        >* если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии
      </details>
    - <details>
      <summary>10. <b>Shop: покупка товара</b></summary>

        :keycap_ten: [Buying the book](/10_shop_buy_the_book.py)<br>

        >1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
        >2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
        >3. Добавьте в корзину книгу "HTML5 WebApp Development"
        >4. Перейдите в корзину
        >5. Нажмите "PROCEED TO CHECKOUT"
        >    - Перед нажатием, добавьте явное ожидание
        >6. Заполните все обязательные поля
        >    - Перед заполнением first name, добавьте явное ожидание
        >    - Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
        >    - Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
        >7. Выберите способ оплаты "Check Payments"
        >    - Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
        >8. Нажмите PLACE ORDER
        >9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
        >10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
      </details>
  </details> 
<br>

 

 
    
<details><summary>:zap: GitHub Stats</summary>
    <img align="left" alt="MirMX's GitHub Stats" src="https://github-readme-stats.vercel.app/api?username=MirMX&exclude_repo=MirMX.github.io&show_icons=true&hide_border=false&title_color=ff652f&icon_color=FFE400&bg_color=09131B&text_color=ffffff&border_color=0c1a25" />
</details><br>
  
<div align ="center" class="footer">
 <b> © 2022 MirMX</b>
</div>