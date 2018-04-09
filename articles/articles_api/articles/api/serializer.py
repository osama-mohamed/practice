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
            'img',
        ]

    def create(self, validated_data):
        title = validated_data['title']
        body = validated_data['body']
        img = validated_data['img']
        article = Articles(
            title=title,
            body=body,
            img=img,
        )
        article.save()
        return validated_data
