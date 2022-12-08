from django.contrib import admin
from .models import (
    User, Subject, Quiz, Question, Answer, Student, TakenQuiz, StudentAnswer
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_student', 'is_teacher']
    list_filter = ['is_student', 'is_teacher']
    search_fields = ['username']
    ordering = ['username']
    fieldsets = [
        ['User Information', {'fields': ['username', 'password']}],
        ['Permissions', {'fields': ['is_student', 'is_teacher']}],
    ]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['name']
    fieldsets = [
        ['Subject Information', {'fields': ['name', 'color']}],
    ]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'owner']
    list_filter = ['subject', 'owner']
    search_fields = ['name']
    ordering = ['name']
    fieldsets = [['Quiz Information', {'fields': ['name', 'subject', 'owner']}],
                 ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'quiz']
    list_filter = ['quiz']
    search_fields = ['text']
    ordering = ['text']
    fieldsets = [['Question Information', {'fields': ['text', 'quiz']}],
                 ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'question', 'is_correct']
    list_filter = ['is_correct', 'question']
    search_fields = ['text']
    ordering = ['text']
    fieldsets = [['Answer Information', {'fields': ['text', 'question', 'is_correct']}],
                 ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'score']
    list_filter = ['score']
    search_fields = ['user__username']
    ordering = ['user__username']
    fieldsets = [['Student Information', {'fields': ['user', 'score']}],
                 ]


@admin.register(TakenQuiz)
class TakenQuizAdmin(admin.ModelAdmin):
    list_display = ['student', 'quiz', 'score', 'percentage', 'date']
    list_filter = ['quiz', 'score', 'percentage', 'date']
    search_fields = ['student__user__username']
    ordering = ['student__user__username']
    fieldsets = [['Taken Quiz Information', {'fields': ['student', 'quiz', 'score', 'percentage', 'date']}], ]


@admin.register(StudentAnswer)
class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ['student', 'answer']
    list_filter = ['answer']
    search_fields = ['student__user__username', 'answer__text']
    ordering = ['student__user__username']
    fieldsets = [
        ['Student Answer Information', {'fields': ['student', 'answer']}],
    ]