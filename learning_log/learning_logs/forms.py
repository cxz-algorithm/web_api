# -*- coding: UTF-8 -*-
"""
@Project ：web_api 
@File    ：forms.py
@Author  ：ChengXiaozhao
@Date    ：2021/2/16 下午2:32 
@Desc    ：
"""

from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
