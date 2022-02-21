# first-selenium-project


<span>
    <div>
 	<h2 style=color:blue align=center >Подготовка окружения</h2> 
 	<img src="https://avatars.mds.yandex.net/i?id=6fe87387809f66c5068829163ca17a29-4406655-images-thumbs&n=13" alt="selenium" align="left" width="130" margin="0">
    </div>

<p>В этом модуле мы создадим с нуля полноценный тестовый проект, который будет являться вашим финальным заданием. Для этого будем использовать популярные в индустрии инструменты&nbsp;Git и GitHub,&nbsp;с которыми в общих чертах мы познакомились в предыдущем модуле.&nbsp;</p>

<p>Добавлять изменения мы будем постепенно, чтобы в вашем репозитории была красивая история коммитов. Потому что именно так происходит написание промышленного кода, а наша задача в этом курсе — максимально приблизиться к этому процессу.&nbsp;</p>

<p>Итак:</p>

<ol>
	<li>Создайте отдельный <strong>публичный</strong> репозиторий с осмысленным названием на GitHub.</li>
	<li>Склонируйте его к себе на локальную машину.</li>
	<li>Добавьте туда файл <em>conftest.py&nbsp;</em>из предыдущего модуля. Убедитесь дополнительно, что там есть параметр для задания языка интерфейса, по умолчанию равный&nbsp;"<strong>en</strong>".</li>
	<li>Убедитесь что ни во вложенных папках, ни во внешних папках нет других файлов <em>conftest.py</em>, почему это важно смотри здесь:&nbsp;<a href="https://stepik.org/lesson/237240/step/4" rel="noopener noreferrer nofollow">Conftest.py — конфигурация тестов</a>.</li>
	<li>Добавьте в репозиторий&nbsp;файл <em>requirements.txt&nbsp;</em>из предыдущего модуля.&nbsp;</li>
	<li>Создайте пустой файл <em>__init__.py</em>,&nbsp;чтобы работали относительные импорты.</li>
	<li>Создайте файл<em> </em><em>test_main_page.py&nbsp;</em>и добавьте в него тест из предыдущего модуля:&nbsp;
	<pre><code class="hljs ruby"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">test_guest_can_go_to_login_page</span><span class="hljs-params">(browser)</span></span>:
    link = <span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span>
    browser.get(link)
    login_link = browser.find_element_by_css_selector(<span class="hljs-string">"#login_link"</span>)
    login_link.click()</code></pre>
	</li>
	<li>Не забудьте активировать окружение, которое мы создали ранее. Опционально, можно создать для этого проекта новое виртуальное окружение&nbsp;для удобства.&nbsp;В&nbsp;таком случае убедитесь что вы установили туда все необходимые пакеты из <em>requirements.txt.&nbsp;</em>А еще не стоит добавлять файлы окружения в репозиторий и вообще в отслеживаемые&nbsp;—&nbsp;лишние&nbsp;файлы на GitHub&nbsp;это моветон.&nbsp;</li>
	<li>Убедитесь, что тест работает, с помощью следующей команды:&nbsp;<code>pytest -v --tb=line --language=en test_main_page.py</code>. Здесь и далее мы будем использовать эту команду для запуска.&nbsp;В этой команде мы использовали опцию PyTest <strong>--tb=line</strong>, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста. Так вам будет проще разобраться в том, как выглядят сообщения об ошибках.&nbsp;</li>
	<li>Добавьте все новые файлы в Git командой <code><strong>git add *</strong></code></li>
	<li>Проверьте, что нужные файлы попали в планируемый коммит:&nbsp;<code><strong>git status</strong></code></li>
	<li>Зафиксируйте изменения коммитом с осмысленным сообщением: <code><strong>git commit -m "write your message".</strong></code></li>
	<li>По желанию&nbsp;добавьте описание репозитория с описанием вашего тестового проекта.</li>
</ol></span>
