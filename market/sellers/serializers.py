from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from market.sellers.models import Product, Factory, RetailNetwork, PrivateBusinessman


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    product_model = serializers.CharField(required=False)

    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()

    class Meta:
        model = Product
        fields = "__all__"


class FactoryListSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Factory
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Factory
        fields = "__all__"


class FactoryCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        queryset=Product.objects.all(),
        slug_field="title"
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)

    class Meta:
        model = Factory
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "created",
        ]


class RetailNetworkListSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    provider = FactorySerializer(allow_null=True)

    class Meta:
        model = RetailNetwork
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "provider",
            "debt",
            "created",
        ]


class RetailNetworkSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    provider = FactorySerializer(allow_null=True)

    class Meta:
        model = RetailNetwork
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "products",
            "provider",
            "debt",
            "created",
        ]


class RetailNetworkCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Product.objects.all(),
        slug_field='title'
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)
    provider = serializers.PrimaryKeyRelatedField(
        queryset=Factory.objects.all(),
        required=False,
        allow_null=True
    )
    debt = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = RetailNetwork
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "provider",
            "debt",
            "created",
        ]

    def create(self, validated_data):
        provider = Factory.objects.get(id=validated_data.get("provider").id)
        supplier_products = [product.title for product in provider.products.all()]

        with transaction.atomic():
            retailer = RetailNetwork.objects.create(
                title=validated_data.get("title"),
                email=validated_data.get("email"),
                city=validated_data.get("city"),
                provider=provider,
                debt=validated_data.get("debt")
            )

            for product in validated_data.get("products"):
                if product.title in supplier_products:
                    product_obj = Product.objects.get(title=product)
                    retailer.products.add(product_obj)
                    retailer.save()
                else:
                    raise ValidationError(
                        f"У поставщика нет продукта {product.title}"
                    )

        return retailer


class PrivateBusinessmanListSerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Product.objects.all(),
        slug_field='title'
    )
    provider = serializers.CharField(allow_null=True)

    class Meta:
        model = PrivateBusinessman
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "products",
            "provider",
            "debt",
            "created",
        ]


class PrivateBusinessmanCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Product.objects.all(),
        slug_field="title"
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)
    provider = serializers.CharField(required=False)
    debt = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = PrivateBusinessman
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "provider",
            "debt",
            "created",
        ]

    def create(self, validated_data):
        provider = validated_data.pop("provider")

        with transaction.atomic():
            entrepreneur = PrivateBusinessman.objects.create(
                title=validated_data.get("title"),
                email=validated_data.get("email"),
                city=validated_data.get("city"),
                debt=validated_data.get("debt")
            )

            try:
                supplier_object = Factory.objects.filter(title=provider).first() \
                                  or RetailNetwork.objects.get(title=provider)
                entrepreneur.provider = supplier_object
                entrepreneur.save()
            except Factory.DoesNotExist and RetailNetwork.DoesNotExist:
                raise ValidationError(f"Поставщик {provider} не найден")

            supplier_products = [product.title for product in supplier_object.products.all()]

            for product in validated_data.get("products"):
                if product.title in supplier_products:
                    product_obj = Product.objects.get(title=product)
                    entrepreneur.products.add(product_obj)
                    entrepreneur.save()
                else:
                    raise ValidationError(
                        f"У поставщика нет продукта {product.title}"
                    )

        return entrepreneur


class PrivateBusinessmanSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Product.objects.all(),
        slug_field="title"
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)
    provider = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = PrivateBusinessman
        read_only_fields = ["debt"]
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "provider",
            "debt",
            "created",
        ]
