from django.contrib import admin
from .models import Comment, ProbabilityOfWords,CommentDataSet

admin.site.register(Comment)
admin.site.register(ProbabilityOfWords)
admin.site.register(CommentDataSet)

# Register your models here.
