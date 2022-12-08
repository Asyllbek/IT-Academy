import hashlib
from collections import (
    namedtuple,
)

from django import template
from django.db.models import (
    Sum,
)

from classroom.models import (
    StudentAnswer,
)

register = template.Library()


@register.simple_tag
def marked_answer(user, opt):
    student_answer_exists = StudentAnswer.objects.filter(student=user.student, answer=opt).exists()

    return (
        'correct' if opt.is_correct else 'wrong'
    ) if student_answer_exists else None


@register.filter
def gravatar_url(username, size=40):
    username_bytes = username.lower().encode('utf-8')

    username_hash = hashlib.md5(username_bytes).hexdigest()

    return f"https://www.gravatar.com/avatar/{username_hash}?s={size}&d=identicon"


@register.filter
def top_subject(taken_quizzes):
    Subject = namedtuple('Subject', ['name', 'score'])

    subjects = taken_quizzes.values('quiz__subject__name') \
        .annotate(score=Sum('score')) \
        .order_by('-score')

    if subjects:
        subject = Subject(subjects[0]['quiz__subject__name'], subjects[0]['score'])
        return f"{subject.name} x {subject.score}"

    return None
