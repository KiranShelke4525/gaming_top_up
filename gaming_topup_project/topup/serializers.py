from rest_framework import serializers
from .models import Game, TopUpProduct, TopUpOrder
from django.db.models import Q

class TopUpOrderSerializer(serializers.Serializer):
    gamename = serializers.CharField()
    game_id = serializers.CharField()
    product_name = serializers.CharField()
    product_id = serializers.IntegerField()
    product_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    user_email = serializers.EmailField()
    payment_status = serializers.ChoiceField(choices=['pending', 'success', 'failed'])

    def validate(self, data):
        # Debug print (optional)
        print("DEBUG form data:", data)

        # Try to get the active game (case-insensitive match)
        game = Game.objects.filter(
            Q(name__iexact=data['gamename']),
            Q(game_id__iexact=data['game_id']),
            is_active=True
        ).first()

        if not game:
            raise serializers.ValidationError("Game not found or inactive. Please check 'gamename' and 'game_id'.")

        # Try to get product linked with the given game
        try:
            product = TopUpProduct.objects.get(
                id=data['product_id'],
                name=data['product_name'],
                game=game
            )
        except TopUpProduct.DoesNotExist:
            raise serializers.ValidationError("Product not found or not linked to this game.")

        # Attach validated objects for use in `create()`
        data['game'] = game
        data['product'] = product
        return data

    def create(self, validated_data):
        return TopUpOrder.objects.create(
            user_email=validated_data['user_email'],
            product=validated_data['product'],
            status=validated_data['payment_status']
        )
