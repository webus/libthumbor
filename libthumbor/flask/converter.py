from .views import ThumborImageField

try:
    from flask_admin.contrib.mongoengine.form import CustomModelConverter
    from flask_mongoengine.wtf                import orm

    class BackendModelConverter(CustomModelConverter):
        """
        Translates model field to form widget.
        """
        @orm.converts('ThumborField')
        def conv_ThumborField(self, model, field, kwargs):
            return ThumborImageField(**kwargs)

except ImportError:
    class BackendModelConverter(object):
        pass
