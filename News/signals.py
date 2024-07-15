from django.conf import settings
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from .models import PostCategory


# @receiver(m2m_changed, sender=Post)
# def post_created(instance, created, **kwargs):
#     if not created:
#         return
#
#     emails = User.objects.filter(
#         subscriptions__category=instance.postCategory
#     ).values_list('email', flat=True)
#
#     subject = f'Новый пост в категории {instance.postCategory}'
#
#     text_content = (
#         f'пост: {instance.head}\n'
#         f'Ссылка на пост: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'пост: {instance.head}<br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#         f'Ссылка на пост</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()

def send_notifications(preview, pk, head, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'Link': f'{settings.SITE_URL}/News/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=head,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.head, subscribers)

