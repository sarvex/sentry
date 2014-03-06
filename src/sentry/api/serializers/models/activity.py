from sentry.api.serializers import Serializer, register, serialize
from sentry.models import Activity


@register(Activity)
class ActivitySerializer(Serializer):
    def serialize(self, obj, request=None):
        d = {
            'id': str(obj.id),
            'user': serialize(obj.user),
            'type': {
                'id': str(obj.type),
                'name': obj.get_type_display(),
            },
            'data': obj.data,
            'dateCreated': obj.datetime,
        }
        return d