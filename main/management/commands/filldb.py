from django.core.management import BaseCommand
from main.models import Client, Mailing, Message
from blog.models import Blog
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        owner = User.objects.get(name='User')

        c1 = Client.objects.create(
            email='red@redmail.org',
            fio='Краснов А.А.',
            comment='Менеджер',
            user=owner
        )

        c2 = Client.objects.create(
            email='yellow@yellowmail.org',
            fio='Желтов А.А.',
            comment='Бухгалтер',
            user=owner
        )

        c3 = Client.objects.create(
            email='green@greenmail.org',
            fio='Зеленкин А.А.',
            comment='Инженер',
            user=owner,
            is_active=False
        )

        m1 = Message.objects.create(
            subject='Пора сменить шины на зимние!',
            text='Для водителей холода всегда наступают неожиданно, поэтому важно вовремя переобуть автомобиль. Узнайте, как выбрать подходящие для вашего авто шины, чтобы обеспечить надёжное сцепление на зимних дорогах. Подготовьтесь заранее и будьте уверены в своей безопасности!',
            user=owner
        )

        m2 = Message.objects.create(
            subject='Подготовьтесь к Новому году',
            text='Новый год не за горами! Мы предлагаем начать подготовку заранее — тогда праздник точно пройдёт без стресса и суеты. Наполните дом атмосферой волшебства и зимнего чуда с новогодними товарами по низким ценам от Лемана ПРО!',
            user=owner
        )

        mg1 = Mailing.objects.create(
            name='Авто',
            time_start='12:00',
            date_start='2024-11-01',
            period='day',
            message=m1,
            user=owner
        )

        mg2 = Mailing.objects.create(
            name='Ремонт',
            time_start='12:00',
            date_start='2024-11-01',
            period='week',
            message=m2,
            user=owner
        )

        Blog.objects.create(
            title='Аннотации в Looker Studio',
            text='Аннотации – это инструмент, с помощью которого пользователи могут делать заметки, оставлять комментарии к отчетам и графикам.'
        )

        Blog.objects.create(
            title='Создание приложения для API Яндекс.Метрики',
            text='Для использования API Яндекс Метрики вам необходимо создать приложение и пройти авторизацию с помощью OAuth-токена. В этой статье разбирается первая часть подготовительных работ.'
        )

        Blog.objects.create(
            title='Не cookie единым…',
            text='Помимо cookie в браузере пользователя, есть еще несколько мест, где бы мы могли хранить информацию о его поведении. Вот об этих местах, чем они лучше или хуже cookie, как эти знания можно применить на практике, а также о том, что нас может сдерживать мы и поговорим.'
        )

        Blog.objects.create(
            title='Знакомство с Yandex DataLens',
            text='Yandex DataLens (Яндекс ДатаЛенс) – продукт компании Яндекс, относящийся к классу BI-систем. С его помощью можно легко и быстро создавать интерактивные дашборды для разных отделов и задач в компании, подключаться к своим облачным и локальным базам данных, сервисам и обычным файлам, а также назначать каждому сотруднику собственные права доступа с целью совместного принятия управленческих решений на основе данных организации.'
        )
