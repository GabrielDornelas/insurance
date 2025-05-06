from rest_framework import serializers
from .models import Policy

class PolicySerializer(serializers.ModelSerializer):
    policy_type = serializers.CharField()

    class Meta:
        model = Policy
        fields = ['policy_id', 'customer_name', 'policy_type', 'expiry_date', 'created_at', 'updated_at']
        read_only_fields = ['policy_id', 'created_at', 'updated_at']

    def validate_policy_type(self, value):
        valid_choices = ['auto', 'home', 'life', 'health']
        if value not in valid_choices:
            raise serializers.ValidationError(
                f"Invalid policy type. The options available are: {', '.join(valid_choices)}"
            )
        return value
