Значення потрібно редагувати в [configs.ini](/hsc_gov_subscriber/config.ini).

`email` - пошта на яку прийде білет та нагадування.

`office_id` - ID офісу ГСЦ. (71 - м. Миколаїв, пров. Транспортний, 1а/1)

`question_id` - ID послуги. (56 - практичний іспит (транспортний засіб навчального закладу). 49 - Перереєстрація транспортного засобу)

`vin` - Номерний знак або VIN(останні 6 цифр). (обозявковий якщо `question_id` = 49)

`api_id` - `App api_id` з [п.1](/content/configs/configuring.md).

`api_hash` - `App api_hash` з [п.1](/content/configs/configuring.md).

`start_date` - дата з якої потрібно брати талон. (наприклад 2024-05-9 - якщо буде талон на 08.5.2024 - код не візьме
такий талон, якщо прийде 09.5.2024 - код намагатиметься взяти талон)

`end_date` - дата з якої вже не потрібно брати талон. (наприклад 2024-05-14 - якщо буде талон на 15.5.2024 - код не
візьме такий талон, якщо прийде 14.5.2024 або 13.5.2024 - код намагатиметься взяти талон)

Гайд [де брати `OFFICE_ID` та `QUESTION_ID`](/content/configs/browser_requests/pract_ispt_id.md).

### Приклад конфіг файлу для `практичний іспит (транспортний засіб навчального закладу) на категорії B; BE;`

![alt text](/content/configs/photo_2024-05-18_18-08-43.jpg)

### Приклад конфіг файлу для `Перереєстрація транспортного засобу`

![alt text](/content/configs/photo_2024-05-18_18-10-41.jpg)
