from django_filters import FilterSet, ModelChoiceFilter
from .models import Reply, Post


class PostFilter(FilterSet):
    post = ModelChoiceFilter(
        empty_label='Все объявления',
        field_name='post',
        label='Фильтр по обновлениям',
        queryset=Reply.objects.all()
    )

    class Meta:
        model = Reply
        fields = ('post',)

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['post'].queryset = Post.objects.filter(post_author_id=kwargs['request'])
