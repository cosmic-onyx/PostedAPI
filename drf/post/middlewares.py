import functools

from django.core.exceptions import ObjectDoesNotExist

from post.exceptions import ManipulationObjectIsNotUserOwn


def is_user_object_own(func):
    @functools.wraps(func)
    def wrapper(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            raise ObjectDoesNotExist("pk is None")

        obj = self.get_queryset().get(pk=pk)
        if not obj:
            raise ObjectDoesNotExist("select object does not exist in queryset")

        if request.user.id == obj.user.id:
            return func(self, request, *args, **kwargs)

        raise ManipulationObjectIsNotUserOwn("Вы не можете удалять/редактировать это")

    return wrapper