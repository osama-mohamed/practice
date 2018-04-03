from rest_framework.serializers import (
    ModelSerializer,
)

from articles.models import Articles


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Articles
        fields = [
            'id',
            'title',
            'body',
        ]

    def create(self, validated_data):
        title = validated_data['title']
        body = validated_data['body']
        article = Articles(
            title=title,
            body=body,
        )
        article.save()
        return validated_data
