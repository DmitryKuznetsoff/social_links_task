Необходимо написать python скрипт, который на входе будет принимать параметр query (в него будем передавать емейл), а на выходе мы должны выдать json следующего формата:
```
{
"result": {....}
}
```

В result мы можем поместить ответ от gravatar, но с изменениям по именованию полей:
* id -> id
* hash -> email_hash
* profileUrl -> url
* preferredUsername -> alias
* thumbnailUrl -> thumb
* photos -> photos
* name.formatted -> person
* currentLocation -> location
* emails -> emails
* accounts -> accounts
* urls -> urls 
Таким образом, ответ будет содержать:
```
{
  "result": {
    "id": 1,
    "email": "example@mail.ru",
    "email_hash": "af0f2257cdaaaf1236dd3ce027ec7cfe",
    "name": "test example",
    ...
  }
}
```
Примеры емейлов:
* eehzntm5@hotmail.com
* manuruel@yahoo.com
* russellebb912@hotmail.com
* jnkitchener@btinternet.com
* ras-nie@web.de
* ghagen4@gmail.com
* mattdhoey@gmail.com
Можно взять любой емейл, получить от него md5 хеш, и подставить в url:
```https://ru.gravatar.com/d6ac4c55425d6f9d28db9068dbb49e09```
и переместимся сразу на страницу пользователя с таким email адресом.
А вот так можно получить сразу ответ в json формате:
```https://ru.gravatar.com/d6ac4c55425d6f9d28db9068dbb49e09.json```