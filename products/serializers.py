from .models import Category, Comment, Reply, Product
from users.serializers import UserSerializer

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ReplySerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Reply
        fields = [
            "id",
            "comment",
            "author",
            "content",
            "rate",
            "creation_date",
        ]

    def create(self, validated_data):

        author = validated_data.pop("author")
        replies = Reply.objects.create(author=author, **validated_data)

        return replies

    def update(self, instance, validated_data):

        instance.rate = validated_data.get("rate", instance.rate)
        instance.content = validated_data.get("content", instance.content)
        instance.save()

        return instance


class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "product",
            "author",
            "content",
            "rate",
            "creation_date",
            "replies",
        ]

    def create(self, validated_data):

        author = validated_data.pop("author")
        comment = Comment.objects.create(author=author, **validated_data)

        return comment

    def update(self, instance, validated_data):

        instance.rate = validated_data.get("rate", instance.rate)
        instance.content = validated_data.get("content", instance.content)
        instance.save()

        return instance


class ProductSerializer(serializers.ModelSerializer):
    supplier = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "creation_date",
            "pictures",
            "price",
            "discount",
            "supplier",
            "category",
            "comments",
        ]

    def create(self, validated_data):

        supplier = validated_data.pop("supplier")
        product = Product.objects.create(supplier=supplier, **validated_data)

        return product

    def update(self, instance, validated_data):

        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.price = validated_data.get("price", instance.price)
        instance.discount = validated_data.get("discount", instance.discount)
        instance.supplier = validated_data.get("supplier", instance.supplier)
        instance.save()

        return instance
