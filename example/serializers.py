from rest_framework import serializers
from .models import Poem

class PoemSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Poem
        fields = ['author', 'title', 'type']

    def create(self, validated_data):
        for line in self:
            pass
        pass